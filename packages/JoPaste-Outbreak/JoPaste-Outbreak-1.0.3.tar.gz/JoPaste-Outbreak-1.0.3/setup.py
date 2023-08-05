from setuptools import setup, find_packages

VERSION = '1.0.3'
DESCRIPTION = 'Simulating covid outbreak'
LONG_DESCRIPTION = 'A package that supplys the classes to simulate a covid out break based on events'

# Setting up
setup(
    name="JoPaste-Outbreak",
    version=VERSION,
    author="JoshuaPaste (Joshua Payte)",
    author_email="Joshua@peerlogic.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'covid', 'siulate', 'outbreak', 'plague', 'covid  outbreak'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)