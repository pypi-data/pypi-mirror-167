import setuptools


setuptools.setup(
	name='ICityTool',
	version='0.1.1',
	description='',
	packages=setuptools.find_packages(),
	install_requaires=['pandas>=1.3.4', 'numpy>=1.21.3', 'sklearn>=0.0'],
	include_package_data=True,
)