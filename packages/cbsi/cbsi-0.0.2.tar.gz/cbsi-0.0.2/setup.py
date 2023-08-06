from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='cbsi',
  version='0.0.2',
  description='Choice based sensor independent Library',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/abhinav-alangadan/CBSI',  
  author='Abhinav A',
  author_email='abhinava.iirs.isro@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='cbsi, ndvi', 
  packages=find_packages(),
  install_requires=['numpy'] 
)
