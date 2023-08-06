import argparse
import asyncio
import datetime
import os
import subprocess
import sys

import torf

from . import (__description__, __project_name__, __version__, _btclient,
               _config, _debug, _errors, _location)


def _parse_args(args):
    argparser = argparse.ArgumentParser(
        prog=__project_name__,
        description=__description__,
    )
    argparser.add_argument(
        'TORRENT',
        nargs='+',
        help='Path to torrent file',
    )

    argparser.add_argument(
        '--config-file',
        default=_config.DEFAULT_CONFIG_FILEPATH,
        help='File containing configuration options',
    )

    argparser.add_argument(
        '--location', '-l',
        # TODO: Always use "extend" when Python 3.7 is no longer supported.
        #       https://docs.python.org/3/library/argparse.html#action
        action='extend' if sys.version_info >= (3, 8, 0) else 'append',
        nargs='+' if sys.version_info >= (3, 8, 0) else None,
        default=[],
        help=(
            'Potential download location of existing files in TORRENT '
            '(may be given multiple times)'
        ),
    )
    argparser.add_argument(
        '--locations-file',
        default=_config.DEFAULT_LOCATIONS_FILEPATH,
        help='File containing newline-separated list of download locations',
    )
    argparser.add_argument(
        '--default', '-d',
        help='Default location if no existing files are found',
    )

    argparser.add_argument(
        '--clients-file',
        default=_config.DEFAULT_CLIENTS_FILEPATH,
        help='File containing BitTorrent client connections',
    )
    argparser.add_argument(
        '--client', '-c',
        default=None,
        help='Add TORRENT to CLIENT (CLIENT is a section name in CLIENTS_FILE)',
    )
    argparser.add_argument(
        '--noclient', '-C',
        action='store_true',
        default=None,
        help='Do not add TORRENT to any client, print download location instead',
    )
    start_stop_group = argparser.add_mutually_exclusive_group()
    start_stop_group.add_argument(
        '--start', '-s',
        action='store_true',
        help='Start torrent after adding it to a BitTorrent client',
    )
    start_stop_group.add_argument(
        '--stop', '-S',
        action='store_true',
        help='Stop torrent after adding it to a BitTorrent client',
    )

    argparser.add_argument(
        '--version',
        action='version',
        version=f'{__project_name__} {__version__}',
    )
    argparser.add_argument(
        '--debug',
        nargs='?',
        metavar='FILE',
        help='Write debugging messages to FILE or STDERR if FILE is "-"',
    )

    return argparser.parse_args(args)


def _fatal_error(msg):
    sys.stderr.write(f'{msg}\n')
    sys.exit(1)


def _setup_debugging(args):
    # Debugging
    if args.debug == '-':
        import logging
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    elif args.debug:
        import logging
        logging.basicConfig(filename=args.debug, level=logging.DEBUG)


def _get_config(args):
    # Read main configuration from file
    try:
        return _config.Config(filepath=args.config_file)
    except _errors.ConfigError as e:
        _fatal_error(str(e))


def _get_locations(args):
    # Read locations file
    try:
        locations = _config.Locations(filepath=args.locations_file)
    except _errors.ConfigError as e:
        _fatal_error(str(e))
    else:
        # Prepend arguments from --location to locations from config file
        for location in args.location:
            if location in locations:
                locations.remove(location)
        locations[0:0] = args.location
        if not locations:
            _fatal_error(f'No locations specified. See: {__project_name__} --help')
        return locations


def _get_client_config(args):
    # Read client configurations from file
    try:
        configs = _config.Clients(filepath=args.clients_file)
    except _errors.ConfigError as e:
        _fatal_error(str(e))
    else:
        if args.client is not None:
            try:
                return _update_client_config(args, configs[args.client])
            except KeyError:
                _fatal_error(f'Unknown client: {args.client}')
        elif configs:
            return _update_client_config(args, configs.default)


def _update_client_config(args, config):
    config = config.copy()
    if args.start:
        config['stopped'] = False
    elif args.stop:
        config['stopped'] = True
    return config


def _get_client(args):
    if not args.noclient:
        config = _get_client_config(args)
        if config:
            return _btclient.Client(config)


def _find_location(torrent, args, config):
    location_finder = _location.FindDownloadLocation(
        torrent=torrent,
        locations=_get_locations(args),
        default=args.default,
    )
    try:
        download_location = location_finder.find()

        if config['umask'] is not None:
            _debug('Using special umask: %r', config['umask'])
            umask_orig = os.umask(config['umask'])
        else:
            umask_orig = None

        try:
            location_finder.create_links(download_location)
        finally:
            if umask_orig is not None:
                _debug('Restoring old umask: %r', umask_orig)
                os.umask(umask_orig)

    except _errors.FindError as e:
        _fatal_error(str(e))

    else:
        return download_location


async def _handle_location(location, torrent, client):
    if client:
        response = await client.add_torrent(torrent, location)
        for warning in response.warnings:
            sys.stderr.write(f'{torrent}: WARNING: {warning}\n')
        if response.errors:
            for error in response.errors:
                sys.stderr.write(f'{torrent}: {error}\n')
            return False  # Failure
        return True  # Success
    else:
        sys.stdout.write(f'{location}\n')
        return True  # Success


def _run_shell_commands(cmds, env):
    for cmd in cmds:
        try:
            subprocess.run(
                cmd,
                shell=True,
                check=True,
                env=env,
            )
        except subprocess.CalledProcessError as e:
            _fatal_error(f'Command terminated with exit code {e.returncode}: {cmd}')


def _get_torrent(torrent_path):
    try:
        return torf.Torrent.read(torrent_path)
    except torf.TorfError as e:
        _fatal_error(str(e))


def _get_torrent_target_filepath(torrent, target_path_template, torrent_filename):

    def get_tracker():
        trackers = torrent.trackers.flat
        if trackers:
            return trackers[0].hostname
        else:
            return 'notracker'

    def format_dt(dt, fmt, default):
        if dt:
            return dt.strftime(fmt)
        else:
            return default

    now = datetime.datetime.now()

    try:
        target_path = target_path_template.format(
            current_date=now.strftime('%Y-%m-%d'),
            current_datetime=now.strftime('%Y-%m-%dT%H:%M:%S'),
            current_time=now.strftime('%H:%M:%S'),
            filename=torrent_filename,
            infohash=torrent.infohash,
            name=torrent.name,
            torrent_date=format_dt(torrent.creation_date, '%Y-%m-%d', 'nodate'),
            torrent_datetime=format_dt(torrent.creation_date, '%Y-%m-%dT%H:%M:%S', 'nodatetime'),
            torrent_time=format_dt(torrent.creation_date, '%H:%M:%S', 'notime'),
            tracker=get_tracker(),
        )
    except KeyError as e:
        key = e.args[0]
        _fatal_error(f'Unknown placeholder in {target_path_template}: {key}')
    else:
        if target_path.lower().endswith('.torrent'):
            return target_path
        else:
            return os.path.join(target_path, torrent_filename)


def _copy_torrent(config, torrent_path, torrent):
    target_filepath = _get_torrent_target_filepath(
        torrent,
        config['copy_torrent_to'],
        os.path.basename(torrent_path),
    )
    if target_filepath:
        _debug('Copying %s to %s', torrent_path, target_filepath)
        target_directory = os.path.dirname(os.path.normpath(target_filepath))

        try:
            os.makedirs(target_directory, exist_ok=True)
        except OSError as e:
            msg = e.strerror if e.strerror else str(e)
            _fatal_error(f'Failed to create directory: {target_directory}: {msg}')

        else:
            import shutil
            try:
                shutil.copy(torrent_path, target_filepath)
            except OSError as e:
                msg = e.strerror if e.strerror else str(e)
                _fatal_error(f'Failed to copy {torrent_path}: {msg}')


async def _cli(args):
    args = _parse_args(args)
    _setup_debugging(args)
    config = _get_config(args)
    client = _get_client(args)
    torrents = {
        torrent_path: _get_torrent(torrent_path)
        for torrent_path in args.TORRENT
    }

    for torrent_path in args.TORRENT:
        _copy_torrent(config, torrent_path, torrents[torrent_path])

    exit_code = 0

    for torrent_path in args.TORRENT:
        torrent = torrents[torrent_path]

        _run_shell_commands(config['before_location_search_commands'], env={
            'TOFIPA_TORRENT_FILE': str(torrent_path),
            'TOFIPA_TORRENT_NAME': str(torrent.name),
            'TOFIPA_TORRENT_LOCATION': '',
            'TOFIPA_TORRENT_PATH': '',
        })

        location = _find_location(torrent_path, args, config)

        _run_shell_commands(config['after_location_found_commands'], env={
            'TOFIPA_TORRENT_FILE': str(torrent_path),
            'TOFIPA_TORRENT_NAME': str(torrent.name),
            'TOFIPA_TORRENT_LOCATION': str(location),
            'TOFIPA_TORRENT_PATH': str(os.path.join(location, torrent.name)),
        })

        if not await _handle_location(location, torrent_path, client):
            exit_code = 1
        else:
            _run_shell_commands(config['after_torrent_handled_commands'], env={
                'TOFIPA_TORRENT_FILE': str(torrent_path),
                'TOFIPA_TORRENT_NAME': str(torrent.name),
                'TOFIPA_TORRENT_LOCATION': str(location),
                'TOFIPA_TORRENT_PATH': str(os.path.join(location, torrent.name)),
            })

    return exit_code


def cli():
    try:
        sys.exit(asyncio.run(_cli(sys.argv[1:])))
    except KeyboardInterrupt:
        _fatal_error('Cancelled')
