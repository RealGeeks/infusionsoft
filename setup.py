from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name="infusionsoft",
    version='0.2.0',
    description="A client library for the InfusionSoft API",
    url='https://github.com/realgeeks/infusionsoft',
    author='Kevin McCarthy',
    author_email='me@kevinmccarthy.org',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='infusionsoft client api',
    packages=find_packages(),
    install_requires = ['requests']
)
