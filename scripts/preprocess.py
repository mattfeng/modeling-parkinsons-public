#!/usr/bin/env python

"""
Description:
    A variety of preprocessing functions for analyzing
    PPMI (MRI images, specifically) dataset.
"""

import argparse
import nibabel as nib
import os
import imageio
import numpy as np
from torchvision import transforms
from utils import safemakedir
from ppmi import *
from pathlib import Path

def extract_center_image(data):
    data = data.squeeze()
    width, height, depth = data.shape
    midpoint = depth // 2

    return data[:, :, midpoint]

def extract_center_control(args):
    indir = args.indir
    outdir = args.outdir

    if not safemakedir(outdir):
        print(f"[error] Output directory {outdir} already exists.")
        quit()

    if not os.path.isdir(indir):
        print(f"[error] Input directory {indir} is not a directory (or does not exist).")
        quit()

    infiles = Path(indir).glob("*.nii")

def extract_center_routine(args):
    indir = args.indir   # input directory
    outdir = args.outdir # output directory

    if not safemakedir(outdir):
        print(f"[error] Output directory {outdir} already exists.")
        quit()

    if not os.path.isdir(indir):
        print(f"[error] Input directory {indir} is not a directory (or does not exist).")
        quit()

    infiles = Path(indir).glob("*.nii")
    for fpath in infiles:
        pid, iid = get_pid_iid_from_fname(fpath.name)
        try:
            img = nib.load(fpath)
            center_img_data = extract_center_image(img.get_fdata())
        except:
            print(f"[error] Bad image: {fpath}")
            continue
        min_, max_ = center_img_data.min(), center_img_data.max()
        
        center_img_data = ((center_img_data - min_) / (max_ - min_)) * 255
        out_fname = f"{pid}_{iid}.png"
        out_fpath = f"{outdir}/{out_fname}"

        imageio.imwrite(out_fpath, center_img_data)

        print(f"Writing output image to {out_fpath}.")

def main(action, args):
    if action == "xcenter":
        extract_center_routine(args)

    print("[info] Done.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("action",
        help = "preprocessing routing to run",
        type = str)
    parser.add_argument("indir",
        help = "input directory",
        type = str)
    parser.add_argument("outdir",
        help = "output directory",
        type = str)

    args = parser.parse_args()

    main(args.action, args)