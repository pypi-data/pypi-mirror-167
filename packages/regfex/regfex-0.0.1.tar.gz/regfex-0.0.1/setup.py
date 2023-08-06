from setuptools import setup
import io


with io.open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(name='regfex', 
    author='WoidZero',
    version='0.0.1', 
    url='https://github.com/woidzero/regfex',
    description='Python module for get regular expressions from .re files.', 
    packages=['regfex'], 
    author_email='contact@woidzero.xyz', 
    long_description=long_description,
    long_description_content_type='text/markdown',
    zip_safe=False)