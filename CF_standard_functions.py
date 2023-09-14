# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 13:32:32 2023


@author: ghpetty
"""

import datetime
import os

# For seeing how old a file is when deciding whether to load it
def file_age_in_hours(file_path):
    file_creation_time = os.path.getmtime(file_path)
    current_time = datetime.datetime.now().timestamp()
    age_in_seconds = current_time - file_creation_time
    age_in_hours = age_in_seconds / (60 * 60)
    return age_in_hours