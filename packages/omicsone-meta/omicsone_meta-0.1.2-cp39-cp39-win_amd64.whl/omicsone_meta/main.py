

import argparse
import sys, os, re
from this import d

import numpy as np
import pandas as pd
from tqdm import tqdm

from plugins.meta import Meta


class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)


def main():
    parser = MyParser(description='hzdiff: do differential expression analysis on two groups.')
    parser.add_argument('-i', dest="input_file",
                        help="input meta file (.tsv) ")
    parser.add_argument('-p', dest='option', help='operation')
    # parser.add_argument('-p', dest='param_file', help='parameter file (.param)')
    parser.add_argument('-o', dest='output_dir',help='output directory')

    args = parser.parse_args()

    # check inputs
    if args.input_file is None or (not os.path.exists(args.input_file)):
        print('invalid input file')
        parser.print_help()
        sys.exit(1)
    if args.output_dir is None or (not os.path.exists(args.output_dir)):
        print('invalid output directory')
        parser.print_help()
        sys.exit(1)
    # if args.param_file is None or (not os.path.exists(args.param_file)):
    #     print('invalid parameter file')
    #     parser.print_help()
    #     sys.exit(1)


    meta_path = args.input_file
    option = args.option
    # param_path = args.param_file
    out_dir = args.output_dir

    folder,bn = os.path.split(meta_path)
    bn, ext = os.path.splitext(bn)

    meta = Meta(meta_path)

    if option == "get_tumor_samples":
        output_path = out_dir + os.sep + bn + "-tumors.txt"
        tumors = meta.get_tumor_samples()
        with open(output_path,'w') as f:
            for i in tumors:
                f.write(i + "\n")
            f.close()

    if option == "get_normal_samples":
        output_path = out_dir + os.sep + bn + "-normals.txt"
        normals = meta.get_normal_samples()
        with open(output_path,'w') as f:
            for i in normals:
                f.write(i + "\n")
            f.close()


if __name__ == "__main__":
    main()
