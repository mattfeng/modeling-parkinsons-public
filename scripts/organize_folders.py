#!/usr/bin/env python

"""
Description:
    This script flattens the folder structure containing the data to have
    all the NIIs in a single directory.
Date:
    April 28, 2020
Author:
    Matthew Feng, mattfeng@mit.edu
"""

import argparse
import os
import sys
import shutil
from utils import safemakedir

def main(src_dir, out_dir):
    # make output directory
    if not safemakedir(out_dir):
        print(f"[error] The output directory {dirname} already exists.")
        quit()
    
    # walk through source directory
    if not os.path.exists(src_dir):
        print(f"[error] The source directory {src_dir} doesn't exist.")
        quit()
    
    for root, dirs, files in os.walk(src_dir, topdown=False):
        for fname in files:
            fpath = os.path.join(root, fname)
            destpath = os.path.join(out_dir, fname)
            print(f"Moving file {fpath} to {destpath}")
            shutil.move(fpath, destpath)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("src_dir",
        help = "source directory to flatten",
        type = str
        )
    
    parser.add_argument("out_dir",
        help = "output directory to write to",
        type = str
        )

    args = parser.parse_args()
    
    main(args.src_dir, args.out_dir)