from setuptools import setup, find_packages

setup(name='lasso-bench-fork-leoiv',
      version="0.0.5",
      packages=find_packages(),
      install_requires=[
          'sparse-ho-fork-leoiv==0.1.dev0',
          'celer',
          'pyDOE',
          'libsvmdata',
          'matplotlib>=2.0.0',
          'numpy>=1.12',
          'scipy>=0.18.0',
          'scikit-learn>=0.21',
          'seaborn>=0.7'],
      )
