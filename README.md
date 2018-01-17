# Youtube Downloader with Python

## Description
This source just for trouble-solving issue in my daily live. Currently, my video player in car only can read mpeg1video format, So I need to convert the video format to mpg, since youtube-dl is not support for mpeg format (https://github.com/rg3/youtube-dl#format-selection), I decide to write this.

## Requirement
```bash
pip install -r requirements.txt
```
## Usage
```bash
usage: ytdl.py [-h] -i INPUT [INPUT ...] [-q QUALITY] [-f FORMAT] [-c CONVERT]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT [INPUT ...], --input INPUT [INPUT ...]
                        youtube id (default: None)
  -q QUALITY, --quality QUALITY
                        quality level (default: worst)
  -f FORMAT, --format FORMAT
                        a format output (default: mpg)
  -c CONVERT, --convert CONVERT
                        force convert (default: True)


```

## Credit
thanks to youtube-dl (https://github.com/rg3/youtube-dl)
