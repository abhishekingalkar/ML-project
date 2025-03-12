## building our application as a package itself 
from setuptools import find_packages,setup #this will automatically find all the packages in entire ML aplication ,from directory that we havr created 
from typing import List

HYPEN_E_DOT ='-e .'
def get_requirements(file_path:str)->List[str]:
    
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path)as file_obj:
        requirements= file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
            
#metadata information about the entire project 
setup(
name = 'mlproject',
version='0.0.1',
author= 'Abhishek',
packages=find_packages(),
install_requires =get_requirements('requirements.txt')

)