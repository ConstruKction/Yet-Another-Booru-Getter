
# Yet Another Booru Getter
YABG is a CLI program that downloads images from some of the most famous boorus.

Currently supported boorus:
- Gelbooru
- Danbooru (**no tag limit!**)
- Konachan
- Safebooru
- Lolibooru
- Yande.re

I'll try to support as many boorus as possible in the future. Feel free to create an issue if you want support for a specific booru that's not supported yet.
## Features

- Supports multiple boorus
- Skip already downloaded images based on image md5
- Multiple tag search (both include and exclude)
- Optional metadata logging per image into a txt file (off by default)
- Works with more than two tags at a time for Danbooru without the need for an account
## Usage/Examples

```bash
Booru.py [-h | --help] [-t | --tags TAGS] [-e | --exclude EXCLUDE] [-c | --count COUNT] [-l | --log] [-a | --all] [-s | --sources SOURCES]
```

Halp
```bash
Booru.py -h
```
Get 25 latest items from Gelbooru (max 100):
```bash
Booru.py -c 25 -s gelbooru
```
Refine search by including and excluding tags:
```bash
Booru.py -c 25 -t hatsune_miku,sitting -e nude,looking_at_viewer
```
Just gimme ALL Mikus from everywhere (duplicates will be skipped):
```bash
Booru.py -t hatsune_miku -a -s gelbooru,danbooru,konachan,safebooru,lolibooru,yandere
```
Log metadata per image in a txt file:
```bash
Booru.py -t hatsune_miku -l -s gelbooru
```
## License
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
## Screenshots

<img src="https://raw.githubusercontent.com/ConstruKction/booru_getter/master/screenshots/booru_getter.png" width="600" height="300" />

