from setuptools import setup, find_packages

NAME = 'ggcg'
VERSION = '0.1.0'
DESCRIPTION = 'Genetically Generated Computational Graphs'
AUTHOR = 'José Antonio Díaz Mata'
EMAIL = 'jose.antonio.diaz.mata@gmail.com'
URL = 'https://github.com/FreNeS1/ggcg'
PYTHON_REQUIRES = '>=3.5, <4'

with open('README.md') as f:
    readme_text = f.read()

with open('LICENSE.md') as f:
    license_text = f.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=readme_text,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    license=license_text,
    packages=find_packages(exclude=('tests', 'docs')),
    python_requires=PYTHON_REQUIRES,
)
