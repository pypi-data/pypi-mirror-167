from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='ctime',
  version='1.0.0',
  description='ctime is a python library for how long does the function takes for execute completally',
  long_description_content_type='text/markdown',
  long_description=long_description,
  url='',  
  author='mi66mc',
  author_email='miguelmalgarezi@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='time', 
  packages=find_packages(),
  install_requires=[''] 
)