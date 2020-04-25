from setuptools import setup

setup(
    name='PyVetmanagerApi',
    version='0.1.1',
    long_description=open('README.rst').read(),
    packages=['tests', 'vetmanager'],
    url='https://github.com/otis22/PyVetmanagerApi',
    license='MIT',
    author='otis',
    author_email='vromanichev24@gmail.com',
    descriptions='Vetmanager Api for Python',
    install_requires=["requests"]
)
