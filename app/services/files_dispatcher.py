import os
import requests
import csv

def dispatch_files(directory_of_files_to_simulate, endpoint_url):
    for file in os.scandir(directory_of_files_to_simulate):
        r = requests.post(url = endpoint_url, data = open(file.path, "rb"))

        with open(f"app/temp/results_{file.name}.csv", "w") as file:
            csv.writer(r)