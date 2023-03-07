from setuptools import find_packages, setup
HYPEN_E_DOT = '-e .'
def get_requirements(filepath:str):
    '''
    This function will return the list of requirements
    '''
    requiremtns = []
    with open(filepath) as file:
        requiremtns = file.readlines()
        requiremtns = [req.replace("\n", "") for req in requiremtns]

    if HYPEN_E_DOT in requiremtns:
        requiremtns.remove(HYPEN_E_DOT)
    
    return requiremtns


setup(
    name="MLProject",
    version="0.0.1",
    author="Sarath",
    author_email="sarathperingayisuresh@gmail.com",
    packages=find_packages(),
    install_reqires = get_requirements("requirements.txt")
)