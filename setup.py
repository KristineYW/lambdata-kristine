# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-kristineyw", # the name that you will install via pip
    version="1.1",
    author="Kristine Wang",
    author_email="ywang03@email.com",
    description="Kristine's First VS-Borne Project!",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/KristineYW/lambdata-kristineyw",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)