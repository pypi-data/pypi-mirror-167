from setuptools import setup, find_packages


setup(
    name='exprnames',
    version='0.1',
    license='MIT',
    author="Mudit Verma",
    author_email='muditverma@asu.edu',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='http://famishedrover.github.io',
    keywords='Machine Learning',
    install_requires=[],
)