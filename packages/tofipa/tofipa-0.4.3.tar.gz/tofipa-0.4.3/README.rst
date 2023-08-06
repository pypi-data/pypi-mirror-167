*tofipa* finds files from a torrent beneath a bunch of download locations and
the relevant download location is printed. Optionally, the torrent is added to a
BitTorrent client with the relevant download location.

Matching files are found by name first and, if that fails, by comparing the file
size and then a few piece hashes.

Renamed files are linked to the paths expected by the torrent beneath the
download location of the renamed files.

Hard links are created if possible, symbolic links are used as a fallback.

A default download location is used if not even a single file from the torrent
can be found.

The only output on ``stdout`` is the download location. If the torrent is added
to a BitTorrent client, there is no output. Errors and warnings are printed to
``stderr``.

.. contents::
    :backlinks: none

Algorithm
---------

``TORRENT`` refers to the provided torrent file.

``LOCATION`` is a download directory (the download path without the torrent's
name) provided via ``--location`` and ``~/.config/tofipa/locations``.

1. Find files from ``TORRENT`` in the file system. For each file in ``TORRENT``:

   a) Find a file beneath each ``LOCATION`` with the same size.

   b) Sort multiple size matching files by file name similarity. The file name
      most similar to the one in ``TORRENT`` is processed first.

   c) Hash some pieces to confirm the file content is what ``TORRENT`` expects.

2. If at least one matching file is found, set the download location to the
   ``LOCATION`` of the first matching file.

   If there are no matching files, set the download location to the location
   specified via ``--default`` or the first ``LOCATION``.

3. Make sure every matching file exists beneath the download location with the
   same relative path as in ``TORRENT``. Try to create a hard link and default
   to a symbolic link if source and target are on different file systems.

4. If a client is configured and ``--noclient`` is not given, add ``TORRENT`` to
   the client specified via ``--client`` or the first client in
   ``~/.config/tofipa/clients.ini``.

   If no client is configured or ``--noclient`` is given, print the download
   location to stdout. This is the only output on stdout.

Installation
------------

*tofipa* is on `PyPI <https://pypi.org/project/tofipa/>`_. The recommended
installation method is with `pipx <https://pypa.github.io/pipx/>`_:

.. code-block:: sh

   $ pipx install tofipa

Configuration
-------------

Besides command line options, there are configuration files in
``$XDG_CONFIG_HOME/tofipa/``. If ``$XDG_CONFIG_HOME`` is not set, it defaults to
``~/.config/``.

``~/.config/tofipa/locations``
==============================

``~/.config/tofipa/locations`` is a simple list of download directories. These
are searched for torrent files. There is some support for globbing and
environment variables.

Any directories provided via the ``--location`` argument are searched first in
addition to the directories from ``~/.config/locations``.

Example ``locations``
^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    # Lines that start with "#" and empty lines are ignored.

    # The first download location is the default that is used if no matches are
    # found and --default is not given.
    /downloads/

    # More directories can be listed individually.
    /stuff/various/
    /stuff/more/
    /stuff/other/

    # ... or you can use "*" to include all subdirectories.
    /stuff/*

    # Environment variables can be used as usual. There is no support for fancy
    # expansion stuff like "${FOO:-bar}".
    # NOTE: To keep you sane, unset and empty environment variables are an
    # error case.
    $HOME/downloads

``~/.config/tofipa/clients.ini``
================================

``~/.config/tofipa/clients.ini`` contains all the information that is needed to
add a torrent to a BitTorrent client. Section names are arbitrary strings that
can be passed to ``--client``. If ``--client`` is not given, the first client in
``~/.config/tofipa/clients.ini`` is used.

Comments start with ``#``.

Options
^^^^^^^

.. list-table::

   * - Option
     - Description
     - Valid Values
     - Default

   * - client
     - Name of the BitTorrent client
     - ``deluge``, ``qbittorrent``, ``rtorrent``, ``transmission``
     - Must be provided for every section

   * - url
     - How to connect to ``client``
     - See below
     - See below

   * - username
     - Username for authentication against ``client``
     - Any string
     - Empty

   * - password
     - Password for authentication against ``client``
     - Any string
     - Empty

   * - verify
     - Whether a torrent should be hash checked by the client after it is added
     - true/false, yes/no, on/off, 1/0
     - ``true`` for ``transmission``, ``false`` for other clients

   * - stopped
     - Whether a torrent should be active right away
     - true/false, yes/no, on/off, 1/0
     - ``false``

Client URLs
^^^^^^^^^^^

.. list-table::

   * - Client
     - Format
     - Default

   * - ``deluge``
     - ``[USERNAME:PASSWORD@]HOST[:PORT]``
     - ``localhost:58846``

   * - ``qBittorrent``
     - ``[http[s]://][USERNAME:PASSWORD@]HOST[:PORT]``
     - ``http://localhost:8080``

   * - ``rTorrent``
     - ``[scgi://]HOST[:PORT]`` or
       ``[file://]SOCKET_PATH`` or
       ``http[s]://[USERNAME:PASSWORD@]HOST[:PORT][/PATH]``
     - ``scgi://127.0.0.1:5000``

   * - ``Transmission``
     - ``[http[s]://][USERNAME:PASSWORD@]HOST[:PORT][/PATH]``
     - ``http://localhost:9091/transmission/rpc``

Example ``clients.ini``
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    [foo]
    client = qbittorrent
    url = localhost:5000
    username = hunter1
    password = hunter2

    [bar]
    client = rtorrent
    url = http://localhost:12345
    verify = true

    [baz]
    client = transmission
    stopped = yes

``~/.config/tofipa/config.cfg``
===============================

``~/.config/tofipa/config.cfg`` contains generic configuration options. It's an
INI file without sections, just ``option = value`` pairs.

List values are separated by newline characters with one or more spaces after
it:

.. code-block::

   after_location_found_commands = echo "$TOFIPA_TORRENT_NAME: $TOFIPA_TORRENT_LOCATION"
       chmod u+r "$TOFIPA_TORRENT_PATH"
       ls -l "$TOFIPA_TORRENT_PATH"

Options
^^^^^^^

.. list-table::

   * - Option
     - Description

   * - umask
     - File mode creation mask for created directories, e.g. ``022`` or ``002``
       (see ``man 1 chmod`` or `https://en.wikipedia.org/wiki/umask
       <https://en.wikipedia.org/wiki/umask>`_)

   * - copy_torrent_to
     - Copy ``TORRENT`` to this path template (see `copy_torrent_to Option`_
       below)

   * - before_location_search_commands
     - List of shell commands to run before searching for files in ``TORRENT``

   * - after_location_found_commands
     - List of shell commands to run after the download location of ``TORRENT``
       is found

   * - after_torrent_handled_commands
     - List of shell commands to run after the determined ``LOCATION`` of
       ``TORRENT`` was printed or ``TORRENT`` was added to a client

``copy_torrent_to`` Option
^^^^^^^^^^^^^^^^^^^^^^^^^^

Every ``TORRENT`` is copied to ``copy_torrent_to`` from
``~/.config/tofipa/config.cfg``. If ``copy_torrent_to`` is not set, ``TORRENT``
is not copied. ``copy_torrent_to`` can be a directory or a torrent file. It can
contain placeholders from the table below. Any string enclosed by braces
(e.g. ``{infohash}``) is a placeholder. If you need actual braces in the path, you
need to double them: ``{{infohash}}``

If the path doesn't end with ``.torrent``, it is assumed to be a directory and
the original file name from ``TORRENT`` is appended as the file name.

Example: ``/tmp/tofipa/{current_date}/{tracker}/{infohash}.{name}.{torrent_datetime}.torrent``

.. list-table::

   * - Placeholder
     - Description

   * - filename
     - File name part of ``TORRENT``

   * - name
     - Torrent name of ``TORRENT`` (read from metadata)

   * - infohash
     - Infohash of ``TORRENT``

   * - tracker
     - Name of the first tracker in ``TORRENT`` or ``notracker`` if it doesn't
       have any trackers

   * - current_date
     - Current date in YYYY-MM-DD format

   * - current_time
     - Current time in HH:MM:SS format

   * - current_datetime
     - Current date and time in YYYY-MM-DDTHH:MM:SS format

   * - torrent_date
     - ``TORRENT`` creation date in YYYY-MM-DD format or ``nodate``

   * - torrent_time
     - ``TORRENT`` creation time in HH:MM:SS format or ``notime``

   * - torrent_datetime
     - ``TORRENT`` creation date and time in YYYY-MM-DDTHH:MM:SS format or
       ``nodatetime``

Environment Variables
^^^^^^^^^^^^^^^^^^^^^

The environments of the ``*_commands`` are populated with these variables:

.. list-table::

   * - Variable
     - Description

   * - TOFIPA_TORRENT_FILE
     - Torrent file path as provided (i.e. ``TORRENT``)

   * - TOFIPA_TORRENT_NAME
     - Name of the torrent

   * - TOFIPA_TORRENT_LOCATION
     - Download location of ``TORRENT`` (always empty for
       ``before_location_search_commands``)

   * - TOFIPA_TORRENT_PATH
     - Same as ``$TOFIPA_TORRENT_LOCATION/$TOFIPA_TORRENT_NAME``, but always
       empty for ``before_location_search_commands``
