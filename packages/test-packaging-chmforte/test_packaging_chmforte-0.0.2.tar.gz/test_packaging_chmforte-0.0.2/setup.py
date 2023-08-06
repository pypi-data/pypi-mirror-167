from setuptools import setup, find_packages

VERSION = '0.0.2' 
DESCRIPTION = 'My first Python package'
LONG_DESCRIPTION = 'My first Python package with a slightly longer description'

# Setting up
setup(
        name="test_packaging_chmforte", 
        version=VERSION,
        author="Christopher M. Forte",
        author_email="christopher.forte1@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],        
        keywords=['python', 'first package'],
        classifiers= []
)
