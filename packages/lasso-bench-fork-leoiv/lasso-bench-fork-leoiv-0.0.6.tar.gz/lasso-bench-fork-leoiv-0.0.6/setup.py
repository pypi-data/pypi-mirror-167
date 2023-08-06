from setuptools import setup


setup(
      name='lasso-bench-fork-leoiv',
      version="0.0.6",
      packages=['LassoBench'],
      install_requires=[
          'sparse-ho-fork-leoiv==0.1.dev0',
          'celer',
          'pyDOE',
          'libsvmdata',
          'ax-platform',
          'matplotlib>=2.0.0',
          'numpy>=1.12',
          'scipy>=0.18.0',
          'scikit-learn>=0.21',
          'seaborn>=0.7',
          'GPy>=1.9.2',
          'pyDOE>=0.3.8'],
      )
