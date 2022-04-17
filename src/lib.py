import pkg_resources
from os.path import join, exists
from const import dependency as dp,data_dir_path


installed_packages:list[str] = [i.key for i in pkg_resources.working_set]


def check_libs_installed()->None:
    check = list(filter(lambda x: x not in installed_packages,dp))
    
    if check.__len__() == 0:
        print('All Required Installed')
    else:
        print('{} not installed'.format(check))

def get_file_path(f_name:str)->str:
    abs_path:str = join(data_dir_path,'..\\data',f_name)
    return abs_path if exists(abs_path) else 'None'

def get_processing_folder_path(f_name:str='')->str:
        return join(data_dir_path,'processing',f_name)