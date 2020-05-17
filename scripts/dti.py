#!/usr/bin/env python

"""
Description:
    Functions and constants related to DTI imaging.
Author:
    Matthew Feng, mattfeng@mit.edu
Initial Date:
    May 4, 2020
"""

import pandas as pd
import glob
import os
from collections import namedtuple

DTI_RENAME_DICT = {
    "Image Data ID": "iid", # image id
    "Subject": "pid",       # patient id
    "Group": "group",
    "Sex": "sex",
    "Age": "age",
    "Visit": "visit",
    "Modality": "modality",
    "Description": "desc",
    "Type": "type",
    "Acq Date": "acq_date",
    "Format": "fmt",
    "Downloaded": "dl"
}

# annoyingly, the metadata returned by the search results
# differs from the metadata available during image download.
DTI_SEARCH_RENAME_DICT = {
    "Subject ID": "pid",
    "Project": "project",
    "Research Group": "group",
    "Sex": "sex",
    "Weight": "weight",
    "Visit": "visit_type",
    "Archive Date": "archive_date",
    "Study Date": "study_date",
    "Age": "age",
    "Modality": "modality",
    "Description": "desc",
    "Imaging Protocol": "imaging_protocol",
    "Image ID": "iid"
}

ImgInfo = namedtuple("ImgInfo", "fpath, fname, pid, iid, idx")

def prep_search_df(df):
    df = df.rename(columns=DTI_SEARCH_RENAME_DICT)
    df = df.astype({"archive_date": "datetime64[ns]"})
    df = df.astype({"study_date": "datetime64[ns]"})
    return df

def prep_meta_df(df):
    df = df.rename(columns=DTI_RENAME_DICT)
    df = df.astype({"acq_date": "datetime64[ns]"})
    try:
        df = df.drop(columns="dl")
    except:
        print("Not dropping non-existent column `dl`")
    return df


def get_iminf_from_fpath(fpath):
    """Parses image information from the file path.
    """
    basename = os.path.basename(fpath)
    fname, fext = os.path.splitext(basename)
    info = fname.split("_")
    src = info[0]
    pid = src + info[1]
    iid = int(info[-1].strip("I"))
    idx = int(info[-3])
    return ImgInfo(fpath, fname, pid, iid, idx)

def get_all_imgs_from_iid(src_path, iid):
    """Gets all the nifti images from `src_path`
       that correspond to the image ID `iid`.
    """
    selector = f"{src_path}/*_I{iid}.nii"
    print(f"Selecting items using selector: {selector}")
    all_files = glob.glob(selector)

    return [get_iminf_from_fpath(f) for f in all_files]