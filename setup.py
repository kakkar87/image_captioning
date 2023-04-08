from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT='-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    this function will return a list of requirements
    '''
    requirements=[]
    with open(file_path) as file_object:
        requirements = file_object.readlines()
        requirements = [line.replace("\n","") for line in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)


setup(
    name='image_captioning',
    version= '0.0.1',
    author= 'Arpit',
    author_email= 'arpitkakkar87@gmail.com',
    packages= find_packages(),
    install_requires= get_requirements('requirements.txt')
)