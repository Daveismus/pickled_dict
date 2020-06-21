from distutils.core import setup
import setuptools
from pickled_dict.__init__ import __version__

setup(name='pickled_dict',
      packages=['pickled_dict'],
      version=__version__,
      license='MIT',
      description='Have a persistant Dictionary saved as file',
      author='David Brielbeck',
      author_email='dbrielbeck@gmail.com',
      url='https://github.com/Daveismus/pickled_dict',
      keywords=['pickle', 'dict', 'peristant'],
      setup_requires=['wheel'],
      classifiers=['Development Status :: 3 - Alpha',
                   # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
                   'Intended Audience :: Science/Research',
                   'Topic :: Software Development :: Build Tools',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8', ], )
