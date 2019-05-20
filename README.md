[![Build Status](https://travis-ci.com/nimamahmoudi/nima_cast.svg?token=J1fG4B1WmwjMJ3ZExa6D&branch=master)](https://travis-ci.com/nimamahmoudi/nima_cast)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI version nima-cast](https://badge.fury.io/py/nima-cast.svg)](https://pypi.python.org/pypi/nima-cast/)
[![PyPI license](https://img.shields.io/pypi/l/nima-cast.svg)](https://pypi.python.org/pypi/nima-cast/)
[![PyPI format](https://img.shields.io/pypi/format/nima-cast.svg)](https://pypi.python.org/pypi/nima-cast/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/nima-cast.svg)](https://pypi.python.org/pypi/nima-cast/)
[![PyPI status](https://img.shields.io/pypi/status/nima-cast.svg)](https://pypi.python.org/pypi/nima-cast/)
![PyPI - License](https://img.shields.io/pypi/l/nima-cast.svg)
![GitHub](https://img.shields.io/github/license/nimamahmoudi/nima_cast.svg)
![Libraries.io dependency status for latest release](https://img.shields.io/librariesio/release/pypi/nima-cast.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/nima-cast.svg)
![GitHub issues](https://img.shields.io/github/issues/nimamahmoudi/nima_cast.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/nimamahmoudi/nima_cast.svg)





# nima_cast CLI

# Usage

```bash
$ nima_cast
Welcome! Type ? to list commands. options: --no-minio and --show-debug

(nima.cast) select
INFO:pychromecast:Querying device status
INFO:pychromecast:Querying device status
[0] - Bedroom speaker
[1] - Living Room TV
Please choose an index: 1

(nima.cast) list
[ 0]-   example_video.mp4

(nima.cast) play 0
INFO:pychromecast.controllers:Receiver:Launching app CC1AD845

(nima.cast) pause

(nima.cast) goto 0:10:0

(nima.cast) pause

(nima.cast) stop

(nima.cast) quit
INFO:pychromecast:Quiting current app
INFO:pychromecast.controllers:Receiver:Stopping current app 'CC1AD845'

(nima.cast) exit
```

# Commands

You can get a list of commands by enterring `?`:

```bash
(nima.cast) ?

Documented commands (type help <topic>):
========================================
EOF     exit  help  play  search  select  stream
device  goto  list  quit  seek    stop

Undocumented commands:
======================
pause  resume

```

Look at the documentation for each of them by entering `help CMD`:

```bash
(nima.cast) help play
play [num] starts playing the file specified by the number in results of list
```

# Installation

Install using pip:
```bash
$ pip install nima_cast
```

Upgrading:
```bash
pip install nima_cast --upgrade
```

# Minio Configuration

On windows: 

```bash
set ACCESS_KEY=XXXXXXXXXXXXXXXXX
set SECRET_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
set MINIO_SERVER=YOUR_MINIO_SERVER:9000
```

On ubuntu:

```bash
export ACCESS_KEY=XXXXXXXXXXXXXXXXX
export SECRET_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
export MINIO_SERVER=YOUR_MINIO_SERVER:9000
```

# Running the app

```bash
$ nima_cast
```

# Options

- use `--no-minio` for streaming purposes (no need to connect to minio).
- use `--show-debug` to see debug messages from the cast.

# Publishing

Install dependencies:
```bash
pip install twine
```

Update the version in `nima_cast/__init__.py`, create a source distribution and upload them:
```bash
nano nima_cast/__init__.py
python setup.py sdist
twine upload dist/*
```

Add travis info:

```bash
travis encrypt your-password-here --add deploy.password
```