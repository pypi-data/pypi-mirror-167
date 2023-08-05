from setuptools import setup, find_packages


setup(
    name='input-parser',
    description = "Argparse for input(): enables easy validation of user inputs",
    version='0.1.0',
    license='MIT',
    author="Jolon Behrent",
    author_email='',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    keywords='input, parser, arguments, stdin',
    install_requires=[
      ],
)

