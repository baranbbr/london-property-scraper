from bs4 import BeautifulSoup as bs
import requests
import re
import os
import time

# base url of rightmove
base_url = 'https://www.rightmove.co.uk'

# parameters
bedrooms = 'maxBedrooms=1&minBedrooms=0'
max_price = 'maxPrice=1400'
prop_types = 'propertyTypes=&includeLetAgreed=false&mustHave=&dontShow=houseShare'
# --- location ---
# shepherds bush
# queens park
# notting hill
# west/north west london
# maybe south?
# open to whole of london