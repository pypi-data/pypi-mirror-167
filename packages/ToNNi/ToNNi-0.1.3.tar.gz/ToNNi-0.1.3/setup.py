from setuptools import setup, find_packages


setup(
    name='ToNNi',
    version='0.1.3',
    license='MIT',
    author="Antonio Kezele",
    author_email='akezele35@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://gitlab.com/big-projects1/tonni-pip',
    keywords='neural network',
    install_requires=[
          'numpy',
      ],

)