from setuptools import setup, find_packages

setup(
    # this will be the package name you will see, e.g. the output of 'conda list' in anaconda prompt
    name='datadog-ariadne-graphql-server',
    description='Includes the GraphQL operation name in the datadog APM resource name if one is present.',
    # some version number you may wish to add - increment this after every update
    version='1.0',
    author="Butch Marshall",
    author_email="butch.a.marshall@gmail.com",
    # Use one of the below approach to define package and/or module names:

    # if there are only handful of modules placed in root directory, and no packages/directories exist then can use below syntax
    #     packages=[''], #have to import modules directly in code after installing this wheel, like import mod2 (respective file name in this case is mod2.py) - no direct use of distribution name while importing

    # can list down each package names - no need to keep __init__.py under packages / directories
    #     packages=['<list of name of packages>'], #importing is like: from package1 import mod2, or import package1.mod2 as m2

    # this approach automatically finds out all directories (packages) - those must contain a file named __init__.py (can be empty)
    packages=find_packages(),
    install_requires=[
        'ddtrace>=1.3.2',
        'ariadne~=0.15.0',
    ],
    requires_python=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="BSD",
)