#!/usr/bin/env python
from fastai.vision.data import ImageImageList
import nilearn.image as nim

def load_nifti_img(fn):
    image = nim.load_img(str(fn)).get_fdata().squeeze()

    return image