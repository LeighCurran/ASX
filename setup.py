from setuptools import setup
from distutils.core import setup
from os import path

setup(
  name = 'asx',
  packages = ['asx'],
  version = '1.0.0',
  license='MIT',
  description = 'Python library to access the ASX API: https://www.asx.com.au/asx/1/share',
  long_description="""ASX is a package to pull data from https://www.asx.com.au/asx/1/share.""",
  long_description_content_type='text/markdown',
  author = 'Leigh Curran',
  author_email = 'ASXPy@outlook.com',
  url = 'https://github.com/leighcurran/ASX',
  keywords = ['ASX', 'API'],
  install_requires=[
          'requests',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)