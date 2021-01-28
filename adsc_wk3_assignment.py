# Applied Data Science Capstone Week 3 Assignment
import pandas as pd
import numpy as np
import json
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
import requests
from pandas.io.json import json_normalize
import matplotlib.cm as cm
import matplotlib.colors as colors
from sklearn.cluster import KMeans
import folium
import geocoder

print("Libraries successfully imported!")

url = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'
df = pd.read_html(url, header=0)[0]
df.rename(columns={'Postal Code': 'PostalCode',
                   'Neighbourhood' : 'Neighborhood'}, inplace=True)

# Drops all rows with empty values and resets the index
df = df[df.Borough != 'Not assigned']
df.reset_index(drop=True, inplace=True)

# Get coordinates
lat_lng_coords = None

while(lat_lng_coords is None):
    g = geocoder.google('{}, Toronto, Ontario'.format('PostalCode'))
    lat_lng_coords = g.latlng
    
latitude = lat_lng_coords[0]
longitude = lat_lng_coords[1]