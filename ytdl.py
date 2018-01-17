from __future__ import unicode_literals
import youtube_dl
import os
import subprocess
import re
import argparse


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading')


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--input',nargs='+',
                        help='a csv file of stock data', required=True)
    parser.add_argument('-1', '--quality',
                        help='quality level', default='worst')
    parser.add_argument('-f', '--format',
                        help='a format output', default='mpg')
    args = parser.parse_args()
    ytdl(args.input, args.quality, args.format)


def ytdl(_input,_quality,_format):
    ydl_opts = {
        'format': _quality,
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
        'outtmpl': '%(title)s.%(ext)s',
    }

    # put the video link on this list
    video_list = list()
    for i in _input:
        video_list.append("https://www.youtube.com/watch?v={}".format(i))
    print(video_list)

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(video_list)

    sourcedir = os.getcwd()

    for file in os.listdir(sourcedir):
        if file.endswith(".3gp"):
            filename = file.split('.')
            length = len(filename)
            ekst = filename[length-1]
            newname = ""
            for i in range(0, length - 1):
                filename[i] = re.sub(r'[^\w\s]', '', filename[i])
                filename[i] = re.sub(r"\s+", '-', filename[i])
                newname += filename[i]
            os.rename("{}/{}".format(sourcedir, file),
                      "{}/{}.{}".format(sourcedir, newname, ekst))
            print("now converting . . .")
            subprocess.call(["ffmpeg", "-i", sourcedir + "/" +
                             newname + ".{}".format(ekst), sourcedir + "/" + newname + ".{}".format(_format)])
            os.remove("{}/{}.{}".format(sourcedir, newname, ekst))
            print("done")


if __name__ == '__main__':
    main()
