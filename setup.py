from setuptools import setup

setup(
    name='PyVetmanagerApi',
    version='0.1',
    packages=['tests', 'vetmanager'],
    url='git@github.com:otis22/PyVetmanagerApi.git',
    license='MIT',
    author='otis',
    author_email='vromanichev24@gmail.com',
    description='Vetmanager Api for Python',
    install_requires = ["requests"]
)
