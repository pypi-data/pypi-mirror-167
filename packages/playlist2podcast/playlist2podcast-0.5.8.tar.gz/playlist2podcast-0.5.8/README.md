# Playlist2Podcast

[![Repo](https://img.shields.io/badge/repo-Codeberg.org-blue)](https://codeberg.org/PyYtTools/Playlist2Podcasts)
[![Downloads](https://pepy.tech/badge/playlist2podcast)](https://pepy.tech/project/playlist2podcast)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked against](https://img.shields.io/badge/Checked-Safety--DB-blue)](https://pyup.io/safety/)
[![Checked with](https://img.shields.io/badge/pip-audit--DB-blue)](https://pypi.org/project/pip-audit/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/playlist2podcast)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/playlist2podcast)
[![CI / Woodpecker](https://ci.codeberg.org/api/badges/PyYtTools/Playlist2Podcasts/status.svg)](https://ci.codeberg.org/PyYtTools/Playlist2Podcasts)


Playlist2Podcast is a command line tool that takes a Youtube playlist and creates a podcast feed from this.


Playlist2Podcast:
1) downloads and converts the videos in one or more playlists to opus audio only files,
2) downloads thumbnails and converts them to JPEG format, and
3) creates a podcast feed with the downloaded videos and thumbnails.

Easiest way to use Playlist2Podcast is to use `pipx` to install it from PyPi. Then you can simply use
`playlist2podcast` on the command line run it.

Playlist2Podcast will ask for all necessary parameters when run for the first time and store them in `config.json`
file in the current directory.

Playlist2Podcast is licences under
the [GNU Affero General Public License v3.0](http://www.gnu.org/licenses/agpl-3.0.html)
