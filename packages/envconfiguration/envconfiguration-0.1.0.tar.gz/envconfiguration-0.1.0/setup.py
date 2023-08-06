from setuptools import setup

setup(
    name='envconfiguration',
    version='0.1.0',
    description='Enviroment configuration',
    url='https://github.com/gpcortes/envconfiguration.git',
    author='Gustavo Côrtes',
    author_email='gpcortes@gmail.com',
    license='BSD 2-clause',
    packages=['envconfiguration'],
    install_requires=[
        'python-dotenv>=0.21.0'
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.7',
    ],
)
