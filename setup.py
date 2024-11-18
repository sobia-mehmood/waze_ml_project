from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = 'Waze Machine Learning Project'
VERSION='0.0.1'
DESCRIPTION='This is my machine learning project in modular coding'
AUTHOR_NAME='Sobia Mehmood'
AUTHOR_EMAIL = 'sobia.mehmood.100@gmail.com'

# requirements.txt file open
# read
requirements_file_name = 'requirements.txt'
HYPHEN_E_DOT='-e .'

def get_requirements_list()->List[str]:
    with open(requirements_file_name) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [req.replace("\n","") for req in requirement_list]

        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list

setup(
    name=PROJECT_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    install_requires = get_requirements_list()
)

