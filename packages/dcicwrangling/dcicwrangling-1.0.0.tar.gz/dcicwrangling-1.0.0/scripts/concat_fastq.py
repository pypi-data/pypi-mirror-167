#!/usr/bin/env python3
'''
read gzip fastqs - add shared id for header of each file and output as single concatenated fastq
'''
import os
import sys
import gzip
import argparse
from functions import script_utils as scu


def get_args(args):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument('directory',
                        help="The directory from which to read the files - use . for current dir")
    args = parser.parse_args()
    return args


# def process(lines=None):
#     ks = ['name', 'sequence', 'optional', 'quality']
#     return {k: v for k, v in zip(ks, lines)}


def get_fastq_files_from_dir(dirname):
    fastqs = []
    with os.scandir(dirname) as entries:
        for entry in entries:
            if entry.is_file():
                if entry.name.endswith('fastq.gz'):
                    fastqs.append(entry)
    return(fastqs)


def main():  # pragma: no cover
    # initial set up
    args = get_args(sys.argv[1:])
    dname = args.directory
    if not dname.endswith('/'):
        dname = dname + '/'
    fastqs = get_fastq_files_from_dir(dname)

    outfile = dname + 'concat_file.fastq'
    with open(outfile, 'w') as of:
        profileno = 0
        for f in fastqs:
            profileno += 1
            prof_id = ' NP:{:05d}'.format(profileno)
            fpath = dname + f.name
            with gzip.open(fpath, 'r') as fq:
                n = 0
                for line in fq:
                    line = line.decode('utf-8')
                    if n == 0:
                        line = line.rstrip() + prof_id + '\n'
                    of.write(line)
                    n += 1
                    if n == 4:
                        n = 0


if __name__ == '__main__':
    main()
