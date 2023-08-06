from setuptools import setup, find_packages


setup(
    name='example_publish_pypi_tutorial56',
    version='0.1',
    license='MIT',
    author="Sharon Fitzpatrick",
    author_email='sharon.fitzpatrick23@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    keywords='example project',
    install_requires=[
          'scikit-learn',
      ],

)
