from setuptools import find_packages, setup

# Read the long description from the README file
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# Metadata
__version__ = "0.0.1"
URI = 'https://github.com'
GITHUB_USERNAME = 'Srinath991'
REPO = 'kidney-disease-clssification-app'
AUTHOR = 'Srinath V'
SRC_REPO = 'kidneyDiseaseNet'
AUTHOR_EMAIL = 'srinathvsrinatv863@gmail.com'
DESCRIPTION = "Python package designed for building and training Convolutional Neural Networks (CNNs) to classify kidney diseases"
CONTENT_TYPE = 'text/markdown'

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type=CONTENT_TYPE,
    url=f"{URI}/{GITHUB_USERNAME}/{REPO}",
    project_urls={
        'Bug Tracker': f"{URI}/{GITHUB_USERNAME}/{REPO}/issues"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
  
)
