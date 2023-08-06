from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='cal_fibonacci',
  version='0.0.1',
  description='A very basic fibonacci calculator',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Siddhesh Sagar',
  author_email='siddheshsagar3182001@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='fibonacci', 
  packages=find_packages(),
  install_requires=[''] 
)