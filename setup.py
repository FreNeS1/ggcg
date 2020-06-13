from setuptools import setup, find_packages


with open('README.md') as f:
    readme_text = f.read()

with open('LICENSE.md') as f:
    license_text = f.read()

setup(
    name='ggcg',
    version='0.1.0',
    description='Genetically Generated Computational Graphs',
    long_description=readme_text,
    author='José Antonio Díaz Mata',
    author_email='jose.antonio.diaz.mata@gmail.com',
    url='https://github.com/FreNeS1/ggcg',
    license=license_text,
    packages=find_packages(exclude=('tests', 'docs'))
)