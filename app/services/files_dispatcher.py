import os
import requests
import csv
import json

def dispatch_files(directory_of_files_to_simulate, endpoint_url):
    for file in os.scandir(directory_of_files_to_simulate):
        
        ## Open the idf_file and parse as a string
        with open(file.path, 'r') as simulation_file:
            idf_file_as_string = simulation_file.read()

        # ## Open the epw weather file and parse as a string
        # with open('app/ressources/DNK_SL_Copenhagen-Roskilde.AP.061700_TMYx.epw', 'r') as weather_file:
        #     weather_file_as_string = weather_file.read()

        #input_for_request = json.dumps(idf_file_as_string)

        json_to_send = json.dumps({"idf_file": idf_file_as_string})

        r = requests.post(url = endpoint_url, data = json_to_send)
        
        ##Figure out way to get the data from the response

        result_file = json.loads(r.content)
        csv_file = result_file["result_file"]

        with open(f"app/temp/{file.name}.csv", 'w') as f:
            f.write(csv_file)