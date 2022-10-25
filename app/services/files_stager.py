from eppy import modeleditor
from eppy.modeleditor import IDF
import shutil


def how_many_files_will_variation_create(list_of_inputs, list_of_objects):

    print(len(list_of_inputs) * len(list_of_objects))



def make_optimisation_from_list_of_components(type_of_object, list_of_objects, all_objects, list_of_inputs, source_file, parameter_to_optimise):

    how_many_files_will_variation_create(list_of_inputs, list_of_objects)

    for _object in list_of_objects:

        for _specific_object in all_objects:
            if _specific_object.Name == _object:

                for input in list_of_inputs:

                    ## Make the copy of the benchmark with appropriate parameter variations in name of file
                    target = f'app/temp/parameter_variation_{type_of_object}_{_specific_object.Name}_{parameter_to_optimise}_{input}.idf'
                    shutil.copyfile(source_file, target)
                    
                    ## Make IDF class hierarchy from previously created file
                    idf_file_to_change = IDF(f'app/temp/parameter_variation_{type_of_object}_{_specific_object.Name}_{parameter_to_optimise}_{input}.idf')
                    list_of_objects = idf_file_to_change.idfobjects[type_of_object]

                    ## Loop through specified objects that has been requested to change
                    for _object in list_of_objects:
                        if _object.Name == _specific_object.Name:
                            _object[parameter_to_optimise] = input
                    
                    ## Save the idf_file after properties have been altered
                    idf_file_to_change.save()



def make_optimisation_on_all_components(type_of_object, all_objects, list_of_inputs, source_file, parameter_to_optimise):

    how_many_files_will_variation_create(list_of_inputs, all_objects)

    for specific_object in all_objects:

        for input in list_of_inputs:
            target = f'app/temp/parameter_variation_{type_of_object}_{specific_object.Name}_{parameter_to_optimise}_{input}.idf'
            shutil.copyfile(source_file, target)
        
            idf_file_to_change = IDF(f'app/temp/parameter_variation_{type_of_object}_{specific_object.Name}_{parameter_to_optimise}_{input}.idf')
            list_of_objects = idf_file_to_change.idfobjects[type_of_object]
            
            for _object in list_of_objects:
                if _object.Name == specific_object.Name:
                    _object[parameter_to_optimise] = input
            
            idf_file_to_change.save()



def files_staging_algorithm(source_file, type_of_object, name_of_object, parameter_to_optimise, list_of_inputs):
    IDF.setiddname("app/ressources/V22-1-0-Energy+.idd")
    idf_benchmark = IDF(source_file)
    
    all_objects = idf_benchmark.idfobjects[type_of_object]

    if type(name_of_object) == list:
        make_optimisation_from_list_of_components(type_of_object, name_of_object, all_objects, list_of_inputs, source_file, parameter_to_optimise)

    ## If the user wants to simulate every object
    elif name_of_object.lower() == "all":
        make_optimisation_on_all_components(type_of_object, all_objects, list_of_inputs, source_file, parameter_to_optimise)

    # If the format is not understood
    else:
        print("Don't understand the input type. Are you sure the object name was spelled correctly?")
                    
            
# For testing without server     
# files_staging_algorithm(idf_benchmark,
#                         idf_file_path, 
#                         'Material', 
#                         ["134370_0.15"], 
#                         'Thickness', 
#                         [0.20, 0.25])


    
