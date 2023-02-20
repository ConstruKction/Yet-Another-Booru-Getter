# Yet Another Booru Getter

YABG is a CLI program that downloads images from some of the most famous boorus.

Currently supported boorus:

- Gelbooru
- Danbooru
- Konachan
- Safebooru
- Lolibooru
- Yande.re
- Zerochan (not recommended to combine with others)
- ATF

I'll try to support as many boorus as possible in the future. Feel free to create an issue if you want support for a
specific booru that's not supported yet.

**DISCLAIMER:** Although it is possible to tell the program to download specified tags from all possible imageboards,
it's
not always going to yield ideal results due to some differences in how certain imageboards handle tags (e.g. $artist_(artist) vs $artist) etc. Also please note that some imageboards are slower than others. For example, Gelbooru is crazy
fast, but Zerochan enforces a sleeptime, while ATF or Yande.re are just plain slow.

## Features

- Supports multiple boorus
- Skip already downloaded images based on image md5
- Multiple tag search (both include and exclude)
- Optional metadata logging per image into a txt file (off by default)
- Works with more than two tags at a time for Danbooru without the need for an account. Note however that the operation
  is much slower when querying more than two tags at a time due to Danbooru API limitations (must complete query within
  3s or else timeout, so the downloader has to retry quite often).
- Can use user account for Zerochan. You need to fill out your z_id and z_hash in zerochan.json. You can find them in
  your Zerochan cookies.
- NSFW / SFW-only modes.

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
Booru.py -t hatsune_miku -a -s gelbooru,danbooru,konachan,safebooru,lolibooru,yandere,zerochan,atf
```

Log metadata per image in a txt file:

```bash
Booru.py -t hatsune_miku -l -s gelbooru
```

## License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

## Screenshots

<img src="https://raw.githubusercontent.com/ConstruKction/booru_getter/master/screenshots/booru_getter.png"/>

