# Youtube Downloader with Python

## Description
This source just for trouble-solving issue in my daily live. Currently, my video player in car only can read mpeg1video format, So I need to convert the video format to mpg, since youtube-dl is not support for mpeg format (https://github.com/rg3/youtube-dl#format-selection), I decide to write this.

## Requirement
```bash
pip install -r requirements.txt
```
## Usage
```bash
usage: ytdl.py [-h] -i INPUT [INPUT ...] [-1 QUALITY] [-f FORMAT]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT [INPUT ...], --input INPUT [INPUT ...]
                        a csv file of stock data (default: None)
  -1 QUALITY, --quality QUALITY
                        quality level (default: worst)
  -f FORMAT, --format FORMAT
                        a format output (default: mpg)

```

## Credit
thanks to :
- youtube-dl (https://github.com/rg3/youtube-dl)
- ffmpy (https://github.com/Ch00k/ffmpy)

