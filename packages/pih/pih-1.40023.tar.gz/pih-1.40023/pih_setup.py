from setuptools import setup

#for facade
#prettytable
#colorama
#protobuf
#grpcio (six)
#pyperclip
#win32com -> pywin32 (!!!)

#MC
#pywhatkit

#for orion
#myssql

#for log
#telegram_send

#for dc2
#docs:
    #mailmerge (pip install docx-mailmerge)
    #xlsxwriter
#ad:
    #pyad
    #pywin32 (!!!)
#transliterate

#for printer (dc2)
#pysnmp

#########################################################################################################
"""
1. python pih_setup.py sdist --dist-dir pih_dist bdist_wheel --dist-dir pih_dist build --build-base pih_build
2. twine upload pih_dist/*
"""

# This call to setup() does all the work
setup(
    name="pih",
    version="1.40023",
    description="PIH library",
    long_description_content_type="text/markdown",
    url="https://pacifichosp.com/",
    author="Nikita Karachentsev",
    author_email="it@pacifichosp.com",
    license="MIT",
    classifiers=[],
    packages=["pih"],
    include_package_data=True,
    install_requires=["prettytable", "colorama", "protobuf", "grpcio"]
)
