from setuptools import setup,find_packages
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='ramesh',
  version='0.1.1',
  description='A helper module with greatest power ',
  long_description=open('README.txt').read(),
  url='',  
  author='Ramesh',
  author_email='rr188351@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='tkinter', 
  packages=find_packages(),
  install_requires=[''] 
)
