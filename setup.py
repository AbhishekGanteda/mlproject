from setuptools import setup,find_packages
from typing import List

HYPHEN_E_DOT="-e ."

def get_requirements(file_path:str)->List[str]:
    requirements=[]

    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[i.replace("\n","") for i in requirements]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="abhishek",
    author_email="rockingabhi2003@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)