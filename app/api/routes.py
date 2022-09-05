from app import app
from flask import request
from app.services import optimisation_stage

@app.route('/')
@app.route('/energyplus_opt_service', methods=['POST'])
def energyplus_opt_service():
    data = request.get_data()
    status_json = optimisation_stage.rule_checker(data)
    return status_json