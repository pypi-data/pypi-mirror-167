from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='DMLABBasicCal',
  version='0.0.5',
  description='A very basic function that used python wrapped C++ calculators (ADD and SUB)',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Ayush Kanyal',
  author_email='kanyal.lavi@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='calculator',
  include_package_data=True, 
  packages=find_packages(),
  install_requires=[''] 
)