from setuptools import find_packages,setup
from typing import List

HYPEN_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the required packages.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPEN_DOT in requirements:
            requirements.remove(HYPEN_DOT)
    return requirements        

        
setup(
    name = "mlproject",
    version = "0.0.1",
    author = "nishant",
    author_email="nishantrajputec17@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt'),



)