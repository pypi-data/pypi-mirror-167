from setuptools import find_packages, setup
setup(
    name='kp_compression',
    packages=find_packages(include=['kp_compression']),
    version='0.1.0',
    description='Library to compress LSTM layers',
    author='Suyash Saxena and Varun Singh Negi',
    license='IITD',
    install_requires=['numpy','pytorch'],
    zip_save='true'
)
