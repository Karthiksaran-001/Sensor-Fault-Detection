from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str] = []

    with open("requirements.txt" , "r") as f:
        r = list(f.readlines())
        for i in r:
            i = i.replace("\n" , "")
            requirement_list.append(i)

    return requirement_list

setup(
    name="sensor",
    version="0.0.1",
    author="Karthik",
    author_email="mailmekarthik001@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),#["pymongo==4.2.0"],
)

