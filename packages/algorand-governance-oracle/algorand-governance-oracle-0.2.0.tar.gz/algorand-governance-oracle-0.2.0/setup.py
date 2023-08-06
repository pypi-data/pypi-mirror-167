import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as requirements_txt:
    requirements = requirements_txt.read().strip().splitlines()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='algorand-governance-oracle',
    version='0.2.0',
    packages=['algorand_governance_oracle'],
    include_package_data=True,
    license='MIT',
    license_files=['LICENSE'],
    description='Statistics related with the current governance period.',
    long_description=README,
    long_description_content_type="text/markdown",
    author='hipo',
    author_email='pypi@hipolabs.com',
    url='https://github.com/Hipo/algorand-governance-oracle',
    python_requires=">=3.7",
    install_requires=requirements,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
