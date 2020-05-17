#!/usr/bin/env python

"""
Description:
    PPMI dataset related functions and values.
Author:
    Matthew Feng
Date:
    April 28, 2020
"""

import nibabel as nib
import glob
import os

PPMI_META_RENAME_DICT = {
    "Image Data ID": "iid",
    "Subject": "pid",
    "Group": "group",
    "Age": "age",
    "Visit": "visit",
    "Modality": "modality",
    "Description": "desc",
    "Type": "type",
    "Acq Date": "acq_date",
    "Format": "fmt",
    "Downloaded": "downloaded",
    "Sex": "sex"
}

def get_fname_from_iid(iid, data_dir, ext="nii", debug=False):
    """Returns the filename given the image ID."""
    files = glob.glob(os.path.join(data_dir, f"*_I{iid}*.{ext}"))
    if len(files) == 0:
        raise Exception(f"Did not find any filenames in `{data_dir}` with image id `{iid}`.")
    if len(files) > 1:
        raise Exception(f"Got more than one file associated with image id `{iid}`.")
    if debug:
        print(f"Retrieved file: {files[0]}")
    return files[0]

def get_fnames_from_pid(pid, data_dir):
    """Retrieves the files that are relevant to a specific patient ID."""
    pass

def get_img_from_iid(iid, data_dir, ext="nii"):
    fname = get_fname_from_iid(iid, data_dir, ext)
    return nib.load(fname)

def get_pid_iid_from_fname(fname_orig):
    """Retrieves the patient ID and image ID from the filename."""
    fname, ext = os.path.splitext(fname_orig)
    fname_split = fname.split("_")
    patient_id = int(fname_split[1])
    image_id = int(fname_split[-1].strip("I"))

    return patient_id, image_id

def get_img_info_from_iid(df, iid):
    """Gets the dataframe with the related information given an iid."""
    return df[df["iid"] == iid].to_dict("records")[0]

