import json
import numpy as np
from eppy import modeleditor
from eppy.modeleditor import IDF
import shutil


idf_file_path = "app/ressources/benchmark.idf"
IDF.setiddname("app/ressources/V9-6-0-Energy+.idd")
idf_benchmark = IDF(idf_file_path)

def make_copy_of_idf_files():
    pass

def files_staging_algorithm(idf_benchmark,
                            source_file, 
                            type_of_object, 
                            name_of_object, 
                            parameter_to_optimise,
                            list_of_inputs):
    
    if name_of_object.lower() == "all":
        all_objects = idf_benchmark.idfobjects[type_of_object]

        for specific_object in all_objects:
            for input in list_of_inputs:
                target = f'app/temp/parameter_variation_{type_of_object}_{specific_object.Name}_{parameter_to_optimise}_{input}.idf'
                shutil.copyfile(source_file, target)
            
            idf_file_to_change = IDF(f'app/temp/parameter_variation_{type_of_object}_{specific_object.Name}_{parameter_to_optimise}_{input}.idf')
            list_of_objects = idf_file_to_change.idfobjects[type_of_object]

            for _object in list_of_objects:
                    _object.Thickness = input
                    idf_file_to_change.save()

    else:
        for input in list_of_inputs:
            # First create a copy idf file that can be run
            target = f'app/temp/parameter_variation_{type_of_object}_{name_of_object}_{parameter_to_optimise}_{input}.idf'
            shutil.copyfile(source_file, target)

            idf_file_to_change = IDF(f'app/temp/parameter_variation_{type_of_object}_{name_of_object}_{parameter_to_optimise}_{input}.idf')

            list_of_objects = idf_file_to_change.idfobjects[type_of_object]

            for _object in list_of_objects:
                if _object.Name == name_of_object:
                    _object.Thickness = input
                    idf_file_to_change.save()
                    
            
        
files_staging_algorithm(idf_benchmark,
                        idf_file_path, 
                        'Material', 
                        '134376_0.025', 
                        'Thickness', 
                        [0.20, 0.25])

def make_files_to_stage(idf_file, _object, parameter_to_optimise, list_of_inputs, current_number):
    pass
