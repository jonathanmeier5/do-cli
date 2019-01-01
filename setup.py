
from setuptools import setup, find_packages

setup(
    name='do-cli',
    license='MIT',
    description='CLI for working with digital ocean',
    install_requires=[
        'python-digitalocean',
        ],
    author='Jonathan Meier',
    author_email='jonathan.w.meier@gmail.com',
    url='https://github.com/jonathanmeier5/do-cli',
    version='0.0.0',
    package_dir={'': 'src'},
    packages=['docli'],
    entry_points={
        'console_scripts': [
            'do-create = docli.console_scripts:create',
            'do-destroy = docli.console_scripts:destroy',
            'do-list = docli.console_scripts:list',
        ],
    },
)
