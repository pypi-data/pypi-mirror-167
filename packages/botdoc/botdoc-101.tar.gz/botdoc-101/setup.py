# This file is placed in the Public Domain.


import os


from setuptools import setup


def read():
    return open("README.rst", "r").read()


def uploadlist(dir):
    upl = []
    for file in os.listdir(dir):
        if not file or file.startswith('.'):
            continue
        d = dir + os.sep + file
        if os.path.isdir(d):   
            upl.extend(uploadlist(d))
        else:
            if file.endswith(".pyc") or file.startswith("__pycache"):
                continue
            upl.append(d)
    return upl


setup(
    name="botdoc",
    version="101",
    url="https://github.com/bthate/botdoc",
    author="Bart Thate",
    author_email="bthate67@gmail.com",
    description="The Python3 bot Namespace",
    install_requires=["oplib", "runlib", "botlib", "botd"],
    long_description=read(),
    long_description_content_type="text/x-rst",
    license="Public Domain",
    packages=["botdoc"],
    include_package_data=True,
    data_files=[
                ("share/doc/botdoc", uploadlist("docs")),
                ("share/doc/botdoc/_static", uploadlist("docs/_static")),
                ("share/doc/botdoc/_templates", uploadlist("docs/_templates")),
               ],
    scripts=["bin/botrtfd"],
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: Public Domain",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Topic :: Utilities",
    ],
)
