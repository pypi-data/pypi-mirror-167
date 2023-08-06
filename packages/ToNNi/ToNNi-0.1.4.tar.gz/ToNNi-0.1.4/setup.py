from setuptools import setup, find_packages


setup(
    name='ToNNi',
    version='0.1.4',
    license='MIT',
    author="Antonio Kezele",
    author_email='akezele35@gmail.com',
    packages=find_packages('tonni'),
    package_dir={'': 'tonni'},
    url='https://gitlab.com/big-projects1/tonni-pip',
    keywords='neural network',
    install_requires=[
          'numpy',
      ],

)