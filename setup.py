from setuptools import setup, find_packages

about = {}
with open("geofound/__about__.py") as fp:
    exec(fp.read(), about)

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(name='geofound',
      version=about['__version__'],
      description='A package to assess the bearing capacity and settlement of geofound',
      long_description=readme + '\n\n',
      url='https://github.com/eng-tools/geofound',
      author='Maxim Millen',
      author_email='mmi46@uclive.ac.nz',
      keywords='geotechnical engineering foundations settlement',
      license='MIT',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
      ],
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      install_requires=['sfsimodels>=0.9.12'],
      # List additional groups of dependencies here (e.g. development
      # dependencies). You can install these using the following syntax,
      # for example:
      # $ pip install -e .[dev,test]
      extras_require={
          'test': ['pytest'],
      },
      python_requires='>=3',
      package_data={'': ['LICENSE']},
      include_package_data=True,
      zip_safe=False)


# From python packaging guides
# versioning is a 3-part MAJOR.MINOR.MAINTENANCE numbering scheme,
# where the project author increments:

# MAJOR version when they make incompatible API changes,
# MINOR version when they add functionality in a backwards-compatible manner, and
# MAINTENANCE version when they make backwards-compatible bug fixes.
