'''Image format converter

Usage: pipenv run python imageconv.py <input> <format>
input   --  Path to inputs. Wildcard supported.
            e.g. C:\\myimages\\*
format  --  Output format
            e.g. jpg
'''

import sys
from os import path

from glob import glob

from PIL import Image

def get_outpath(inpath, fmt):

    base = path.basename(inpath)
    # this looks like foo.jpg

    new_base = base.rsplit('.', 1)[0] + '.' + fmt
    # this looks like foo.png
    # (given fmt==png)

    dirname = path.dirname(inpath)
    # this looks like /bar/baz

    return path.join(dirname, new_base)
    # this looks like /bar/baz/foo.png


def convert(inpath, fmt):
    img = Image.open(inpath)
    img.save(get_outpath(inpath, fmt))


def main():
    try:
        _, path_pattern, fmt = sys.argv
    except ValueError:
        print(__doc__)
        sys.exit(1)

    file_paths = glob(path_pattern)

    for fpath in file_paths:
        convert(fpath, fmt)


if __name__ == '__main__':
    main()
