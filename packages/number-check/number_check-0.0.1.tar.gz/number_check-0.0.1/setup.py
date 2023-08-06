from setuptools import setup,find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='number_check',
  version='0.0.1',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Apurba Khanra',
  author_email='apurbakhanra@yahoo.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['numbers','number','check number'], 
  packages=find_packages(),
  install_requires=[''] 
)