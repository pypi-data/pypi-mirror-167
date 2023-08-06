from setuptools import setup

setup(
    name='sunnyday-ferroni',
    packages=['sunnyday-ferroni'],
    version='2.0.0',
    license='MIT',
    description='Weather forecast data',
    author='Eduardo Ferroni',
    author_email='edu_ferroni@hotmail.com',
    keywords=['weather', 'forecast', 'openweather'],
    install_requires=[
        'requests',
    ]
)