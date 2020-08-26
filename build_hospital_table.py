# Building a complete list of chargemaster source locations for every hospital across the USA
# 08-26-2020 Brad Egan

import requests
from pandas import read_csv
from numpy import nan

class Hospital_Table:
    def __init__(self, url):
        self.url = url
        self.df = self.get_all_hospitals()

    def get_all_hospitals(self):
        response = requests.get(self.url)
        data_file = response.json().get('url')
        return read_csv(data_file)
    
    def add_cols(self, col_list):
        for col in col_list:
            self.df[col] = nan

    def write_csv(self, name):
        self.df.to_csv(name, index=False)
        return "Successfully Created Full Hospital Table"

# Gather list of all hospitals across USA from Data.gov
full_hospital_table = Hospital_Table('https://opendata.arcgis.com/datasets/6ac5e325468c4cb9b905f1728d6fbf0f_0.csv?outSR=%7B%22latestWkid%22%3A3857%2C%22wkid%22%3A102100%7D&url_only=true')
full_hospital_table.add_cols(['CHARGEMASTER LINK PAGE', 'CHARGEMASTER SOURCE FILE', 'DRG SOURCE FILE'])
full_hospital_table.write_csv('Hospital_Chargemasters.csv')



