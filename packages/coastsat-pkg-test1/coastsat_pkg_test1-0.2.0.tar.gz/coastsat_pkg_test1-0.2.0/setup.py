from setuptools import setup, find_packages


setup(
    name='coastsat_pkg_test1',
    version='0.2.0',
    license='MIT',
    author="Sharon Fitzpatrick",
    author_email='sharon.fitzpatrick23@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    keywords='test',
    install_requires=[
          'scikit-learn',
          'requests',
          'pytz',
          'scipy',
      ],

)
