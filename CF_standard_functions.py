# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 13:32:32 2023


@author: ghpetty
"""

import datetime
import os
import requests,time 
import numpy as np
import pandas as pd
import re

# For seeing how old a file is when deciding whether to load it
def file_age_in_hours(file_path):
    file_creation_time = os.path.getmtime(file_path)
    current_time = datetime.datetime.now().timestamp()
    age_in_seconds = current_time - file_creation_time
    age_in_hours = age_in_seconds / (60 * 60)
    return age_in_hours

# Load bulk data from Scryfall
def data_from_scryfall():
    sf_bulk_url = "https://api.scryfall.com/bulk-data"
    time.sleep(0.5)
    sf_response = requests.get(sf_bulk_url).json()
    download_dict = [d for d in sf_response['data'] if d['type'] == 'default_cards'][0]
    data_size = np.round(download_dict['size'] / 1e6,1)
    print(f"Downloading {data_size} MB of card data...")
    card_data_raw = requests.get(download_dict['download_uri']).json()
    print("Download complete!")
    data = pd.DataFrame(card_data_raw)
    data.drop(data.index[data['set_type'] == 'funny'],inplace=True)
    data.drop(data.index[data['lang']!='en'],inplace=True)
    data.drop(data.index[data['flavor_text'].isnull()],inplace=True)
    data['flavor_text'] = data.flavor_text.apply(lambda x : x.lower())
    data.drop_duplicates(subset ='flavor_text',inplace=True)
    nCards = data.shape[0]
    print(f"{nCards} cards with unique flavor text in data set")
    return data

# Trim data set to monocolor cards and label by color 
def parse_monocolor_cards(data):
    for c in ['W','U','B','R','G']:
        tf = data.colors.apply(lambda x : np.shape(x) != (0,) and np.any(np.isin(x,c)))
        data['is_'+c] = tf
        
    data['is_monocolor'] = np.sum(data.loc[:][['is_W','is_U','is_B','is_R','is_G']],axis=1) == 1
    data_monocolor = data.loc[data.is_monocolor][['name','colors','flavor_text']].copy()
    data_monocolor['colors'] = data_monocolor.colors.apply(lambda x: ''.join(x)) # Convert from list to string
    data_monocolor['colors'] = pd.Categorical(data_monocolor['colors'],ordered=True)
    data_monocolor['colors'] = data_monocolor['colors'].cat.reorder_categories(['W','U','B','R','G'])
    data_monocolor.sort_values('colors',ascending=True,inplace=True)
    return data_monocolor

# Remove special characters from a string, keeping spaces intact (but not newlines). Regular expressions!
def remove_special_characters(input_string):
    # Regular expression to keep whitespace and remove all special characters
    pattern = r'[^a-zA-Z0-9\s]'
    # Substitute special characters with an empty string
    result_string = re.sub(pattern, '', input_string)
    # Substitute newlines with spaces
    result_string = re.sub(r'\n',' ',result_string)
    return result_string
