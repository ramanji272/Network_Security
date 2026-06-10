from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements.

    """
    requirement_list:List[str] = []
    try:
        with open("requirements.txt", 'r') as file:
            # Read lines from the file
            lines = file.readlines()

            ## Process each line
            for line in lines:
                requirement = line.strip()

                ## ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    
    except FileNotFoundError:
        print('requirements.txt file not found')
    
    return requirement_list

print(get_requirements())

setup(
    name = "Network Security",
    version = "0.0.1",
    author = "Ramanjaneyulu",
    author_email = "ramanjaneyulumangira@gmail.com",
    packages = find_packages(),
    

)