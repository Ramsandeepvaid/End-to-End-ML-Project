##This setup.py file will help us to install our ML project or application as a package in any system and even deploy it
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return a list of requirements

    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements



setup(
    name='end-to-end-ML-project',
    version = '0.0.1',
    author='Ram Vaid',
    author_email='ramsandeepvaid@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)