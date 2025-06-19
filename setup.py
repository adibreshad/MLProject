from setuptools import find_packages, setup
from typing import List
HYPHEN_E_DASH = '-e .'
def get_requirements(file_path:str) -> list:
    """
    This function reads a requirements file and returns a list of packages.
    It removes any comments or empty lines.
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n"," ") for req in requirements]
    
        if HYPHEN_E_DASH in requirements:
            requirements.remove(HYPHEN_E_DASH)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='ReshadAdib',
    author_email="adibahmadreshad@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)