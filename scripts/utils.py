#!/usr/bin/env python

"""
Description:
    Contains general utility functions.
Author:
    Matthew Feng, mattfeng@mit.edu
Date:
    May 4, 2020
"""

import os

def safemakedir(dirname):
    if os.path.exists(dirname):
        return False

    os.makedirs(dirname)
    return True

def has_duplicates(lst):
    """Performs a rudimentary check to see if a list has duplicate elements
    """
    return len(set(lst)) == len(lst)