from setuptools import find_packages,setup

from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    HYPEN_E_DOT="#-e."
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT or '' in requirements:
            requirements.remove(HYPEN_E_DOT)
            requirements.remove('')
        
    return requirements


setup(
name="Xray",
version="0..0.1",
author="prachi patel",
author_email="prachi.patel.business",
install_require=get_requirements(),
package = find_packages()
)