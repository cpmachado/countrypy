"""
  Setup file for countrypy
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="countrypy",
    version="0.0.0",
    author="Carlos Pinto Machado",
    author_email="cpmachado@protonmai.com",
    description="client for https://restcountries.eu",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cpmachado/countrypy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "countrypy=countrypy.__main__:main",
        ]
    },
    python_requires='>=3.6',
)
