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
    long_description_content_type='text/markdown',

    install_requires=(
        'returns-decorator',
    ),
    extras_require={
        'dev': extra_dev,
        'cached-property': ('cached-property',),
        'ci': extra_ci,
    },

    classifiers=[
        'Intended Audience :: Developers',

        'Development Status :: 5 - Production/Stable',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',

        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
