from setuptools import setup

# readme description
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(    
    # each of these parameters is essentially a line of configuration that you are giving to pip
    # to tell it how to install your package

    name="flask-dt", # name is what you pip install. In this case: pip install flask-dt
    #                  it doesn't have to be the name of the python code that people will import

    version="0.0.1.1", # 0.0.x version numbers imply that it is unstable
    #             there is a good chance that the first few times you upload the package to pypi
    #             there might be a packaging mistake

    description="Display Tables", # usually a one-liner

    py_modules=["flask_dt"],  # this is a list of the actual python code modules
    #                           this is the code that we want to distribute
    #                           this is what people import now, not what they pip install

    package_dir={'': 'src'}, # all what this line is doing is telling setuptools our code is in 
    #                          the src directory

    # classifiers
    classifiers=[
        "Programming Language :: Python :: 3", 
        "Programming Language :: Python :: 3.6", 
        "Programming Language :: Python :: 3.7", 
        "Programming Language :: Python :: 3.8", 
        "Programming Language :: Python :: 3.9", 
        "License :: OSI Approved :: MIT License", 
        "Operating System :: OS Independent", 
        "Development Status :: 4 - Beta", 
        "Framework :: Flask", 
        "Intended Audience :: Developers", 
        "Intended Audience :: Education", 
        "Natural Language :: English", 

    ], 

    # readme
    long_description=long_description, 
    long_description_content_type="text/markdown", 

    # dependencies
    install_requires=[
        "SQLAlchemy <= 1.3.23", 
        "Flask <= 2.0.1", 
        "Flask-SQLAlchemy ~=2.4.4", 
    ], 

    # pytest
    extras_require={

        "dev":[
            "pytest>=3.7", 
            "check-manifest>=0.46", 
            "twine>=3.4.2", 
        ], 

    }, 

    # maintainer info
    url="https://github.com/GreatDt1/flaskdt", 
    author="Donatus", 
    author_email="flaskdt@gmail.com", 
)