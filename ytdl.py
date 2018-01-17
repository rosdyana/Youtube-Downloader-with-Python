from __future__ import unicode_literals
import youtube_dl
import os
# import subprocess
import re
import argparse
import ffmpy


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
    parser.add_argument('-i', '--input', nargs='+',
                        help='youtube id', required=True)
    parser.add_argument('-q', '--quality',
                        help='quality level', default='worst')
    parser.add_argument('-f', '--format',
                        help='a format output', default='mpg')
    parser.add_argument('-c', '--convert',
                        help='force convert', default=True)
    args = parser.parse_args()
    ytdl(args.input, args.quality, args.format, args.convert)


def ytdl(_input, _quality, _format,_convert):
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

    if _convert:
        sourcedir = os.getcwd()

        if not os.path.exists("{}/videos".format(sourcedir)):
            os.makedirs("{}/videos".format(sourcedir))
        filext = ""
        if _quality == 'worst':
            filext = "3gp"
        if _quality == 'best':
            filext = "mp4"
        for file in os.listdir(sourcedir):
            if file.endswith(".{}".format(filext)):
                filename = file.split('.')
                length = len(filename)
                ekst = filename[length - 1]
                newname = ""
                for i in range(0, length - 1):
                    filename[i] = re.sub(r'[^\w\s]', '', filename[i])
                    filename[i] = re.sub(r"\s+", '-', filename[i])
                    newname += filename[i]
                os.rename("{}/{}".format(sourcedir, file),
                          "{}/{}.{}".format(sourcedir, newname, ekst))
                print("now converting . . .")
                inputFile = "{}/{}.{}".format(sourcedir, newname, ekst)
                outputFile = "{}/{}.{}".format(sourcedir, newname, _format)
                # subprocess.call(["ffmpeg", "-i", inputFile, outputFile])
                ff = ffmpy.FFmpeg(inputs={inputFile: None},
                                  outputs={outputFile: '-c:a copy'})
                ff.run()
                # os.remove(inputFile)
                os.rename(outputFile, "{}/videos/{}".format(sourcedir, outputFile))
                print("done")


if __name__ == '__main__':
    main()
