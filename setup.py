from setuptools import setup, find_packages

setup(
    name='BBQ',
    version='0.1.0',
    packages=find_packages(),
    description='Bias benchmark question set',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='yihangw@umich.edu',
    url='https://github.com/HydroXai/BBQ',
    install_requires=[
        # List any package dependencies here
        'numpy',
        'pandas',

    ],
    classifiers=[
        # Additional metadata about your package
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
