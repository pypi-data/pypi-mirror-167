from setuptools import setup, find_packages

VERSION = '0.0.8'
DESCRIPTION = 'Wrapper for PRAW scripts built over the years by the community and mods'

# Setting up
setup(
    name="prawscripts",
    version=VERSION,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['praw'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ]
)
