# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="joshuatree", 
    version="1.0",
    author="joshua piche",
    author_email="jpiche92@gmail.com",
    description="Learning Experience",
    #long_description=long_description,
    #long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/jpiche0720/lambdata-jpiche",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)