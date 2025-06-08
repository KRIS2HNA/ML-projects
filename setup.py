from setuptools import find_packages, setup
from typing import List
# This is the setup file for a Python package.
# It defines the package metadata and dependencies.
HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    """
    This function reads a requirements file and returns a list of dependencies.
    
    :param file_path: Path to the requirements file
    :return: List of dependencies
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements
setup(
    name='ML projects',
    version='0.1',
    author='Krishna',
    author_email='krishnavamsimummidivarapu@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    
    
)