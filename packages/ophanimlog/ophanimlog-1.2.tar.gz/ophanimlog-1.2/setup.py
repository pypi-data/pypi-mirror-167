from setuptools import setup, find_packages


setup(
    name='ophanimlog',
    version='1.2',
    license='GNU V3',
    author="Alex Acciarri",
    author_email='accia.ale@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/ImAccia/easylog',
    keywords='Log Logging Logger Py Python Easy Simple',
    install_requires=[
          'colorama',
      ],

)