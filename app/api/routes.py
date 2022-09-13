from app import app
from flask import request
from app.services import files_dispatcher, files_stager
import json

@app.route('/')
@app.route('/energyplus_opt_service', methods=['POST'])
def energyplus_opt_service():

    ## Receive json with inputs to optimisation
    data = request.get_data()
    data = json.loads(data)

    source_file = data["source_file"]
    type_of_object = data["type_of_object"]
    name_of_object = data["name_of_object"]
    parameter_to_optimise = data["parameter_to_optimise"]
    list_of_inputs = data["list_of_inputs"]

    ## Stage all the files
    files_stager.files_staging_algorithm(source_file, type_of_object, name_of_object, parameter_to_optimise, list_of_inputs)

    ## Run the files
    files_dispatcher.dispatch_files('app/temp/', 'http://127.0.0.1:3000/run_ep_simulation') 

    ## Save the files locally

    return "results succesfully run"