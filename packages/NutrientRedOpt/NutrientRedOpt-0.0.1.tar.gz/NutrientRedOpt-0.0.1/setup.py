from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name = 'NutrientRedOpt',
    version='0.0.1',
    description='Finds the optimal placement of BMPs and Technologies in a network in order to reduce the nutrient loadings at the lake',
    Long_description = open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Ashim Khanal, Hanieh Rastegar',
    author_email = 'ashimkhanal18@gmail.com, hanieh.rastegar.m@gmail.com',
    license = 'MIT',
    classifiers=classifiers,
    keywords='Optimization, Environment, Best Management Practices, Technologies, Nutrient Load Reduction, environemnt protection',
    packages=find_packages(),
    install_requires=['']
)

