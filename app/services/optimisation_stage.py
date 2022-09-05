import json
import numpy as np
from eppy import modeleditor
from eppy.modeleditor import IDF
import shutil


idf_file_path = "app/ressources/benchmark.idf"
IDF.setiddname("app/ressources/V9-6-0-Energy+.idd")
idf_benchmark = IDF(idf_file_path)


def idf_object_looper(idf_file, idf_file_path, type_of_object, name_of_object, parameter_to_optimise, list_of_inputs):
    list_of_objects_in_type = idf_file.idfobjects[type_of_object]
    current_number = 0

    make_copies_of_benchmark(idf_file_path, list_of_inputs)

    for _object in list_of_objects_in_type:
        object_name = _object.Name

        if object_name == name_of_object:
            object_name = "Hello"
            
            make_files_to_stage(idf_file, _object, parameter_to_optimise, list_of_inputs)
        
        current_number += 1


def make_copies_of_benchmark(source_file, list_of_inputs):
    
    for i in range(len(list_of_inputs)):
        target = f'app/temp/parameter_variation{i}.idf'
        shutil.copyfile(source_file, target)


def make_files_to_stage(idf_file, _object, parameter_to_optimise, list_of_inputs, current_number):
    pass



idf_object_looper(idf_benchmark, idf_file_path, 'Material', '134370_0.15', 'Thickness', [0.20, 0.25, 0.30])





# def optimisation_stage(json_file, lower_range, upper_range, step):
#     data = json.load(json_file)

#     window_gvalue_optimisation(data)


# def input_variables_as_list(original_value, stop, range_variable, stepwidth):
#     list_for_variables = []
#     start = original_value - range_variable / 2

#     for i in np.arange(start,stop,stepwidth):
#         list_for_variables.append(round(i,3))

#     return list_for_variables


# def window_gvalue_optimisation(data):
#     list_of_input_dicts = []

#     materials = data["Materials"][0].copy()
#     window_materials = materials["WindowMaterials"]

#     for window_material in window_materials:
#         window_material_SHGC = list(window_material.values())[0]["Solar_Heat_Gain_Coefficient"]

#         list_for_variables = input_variables_as_list(window_material_SHGC, 0.9, 0.4, 0.05)
#         # Next part is to create the dict that goes into the list of different simulations
#         window_material[""]

    
# optimisation_stage(json_file, 0.6, 0.8, 0.1)