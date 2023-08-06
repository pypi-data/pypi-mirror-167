from setuptools import setup

setup(
    name='sotest_utils',
    version='0.0.3',
    packages=['sotest_utils'],
    install_requires=['python-consul', 'boto3', 'allure-pytest>=2.9.45']
)
