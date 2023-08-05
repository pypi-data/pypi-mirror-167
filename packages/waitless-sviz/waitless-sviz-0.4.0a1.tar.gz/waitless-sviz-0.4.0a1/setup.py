import sys
# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system.
sys.path.pop(0)
from setuptools import setup, find_packages

setup(
    name='waitless-sviz',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data = {"waitless_sviz_mdol-ideas": [	'waitless_sviz_mdol-ideas.lib/*',
    							'waitless_sviz_mdol-ideas.res/*',
    							'waitless_sviz_mdol-ideas.tmp']},
    version='0.4.0a1',
    description='MicroPython app to monitorize time arrivals of each bus stop in Madrid Region',
    long_description='This library lets you communicate with an Aosong AM2320 temperature and humidity sensor over I2C.',
    keywords='bus arrivals madrid micropython',
    url='https://github.com/modl-ideas/WAITLESS_SVIZ',
    author='Miguel Palomino Civantos',
    author_email='miguelpalominocivantos@gmail.com',
    maintainer='Miguel Palomino Civantos',
    maintainer_email='miguelpalominocivantos@gmail.com',
    license='MIT',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: Implementation :: MicroPython',
        'License :: OSI Approved :: MIT License',
    ],
    include_package_data = True, 
    	install_requires = [],	
	platforms = "any",
    #cmdclass={'sdist': sdist_upip.sdist}
)
