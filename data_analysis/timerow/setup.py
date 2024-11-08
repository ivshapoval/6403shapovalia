from setuptools import setup, find_packages

setup(
    name='Weather_timerow',
    version='1.0',
    description='Python lab 2',
    author='Ivan Shapoval',
    author_email='iashapoval@yandex.ru',
    url='https://github.com/ivshapoval/6403shapovalia',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'openpyxl',
        'meteostat',
        'numpy'
    ],
    python_requires='>=3.10',
)
