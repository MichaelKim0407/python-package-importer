from setuptools import setup, find_packages

from python_package_importer import __version__

extra_flake8 = (
    'flake8',
    'flake8-commas',
    'flake8-quotes',
    'flake8-multiline-containers',
)

extra_test = (
    'pytest',
    'pytest-cov',
)

extra_dev = (
    *extra_flake8,
    *extra_test,
)

extra_ci = (
    *extra_flake8,
    *extra_test,
    'coveralls',
)

setup(
    name='python-package-importer',
    version=__version__,
    packages=find_packages(exclude=['tests', 'tests.*']),
    url='https://github.com/MichaelKim0407/python-package-importer',
    license='MIT',
    author='Michael Kim',
    author_email='mkim0407@gmail.com',
    description='Dynamically import all python files in a directory.',

    install_requires=(
        'returns-decorator',
    ),
    extras_require={
        'dev': extra_dev,
        'cached-property': ('cached-property',),
        'ci': extra_ci,
    },
)
