from app import app
from flask import request
from app.services import files_stager

@app.route('/')
@app.route('/energyplus_opt_service', methods=['POST'])
def energyplus_opt_service():
    data = request.get_data()
    status_json = files_stager.rule_checker(data)
    return status_json