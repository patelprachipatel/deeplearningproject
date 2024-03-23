from setuptools import find_packages,setup

from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    HYPEN_E_DOT="#-e."
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
        

    return requirements

setup(
name="Xray",
version="0.0.1",
author="prachi patel",
author_email="prachi.patel.business@gmail.com",
install_require=get_requirements(r"C:\Users\prach\OneDrive\Desktop\ml_deployment\deep_learning_project\requirements_dev.txt"),
package = find_packages()
)