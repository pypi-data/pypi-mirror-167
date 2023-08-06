from setuptools import *

LONG_DESC = """
This is pytorch lightning helper
"""

setup(name='pytorch-lightning-helper',
	  version='0.0.4',
	  description='Pytorch lightning helper',
	  long_description=LONG_DESC,
	  author='Sang Ki Kwon',
	  url='https://github.com/automatethem/pytorch-lightning-helper',
	  #install_requires=['pytorch-lightning', 'torchsummaryX'],
	  install_requires=[],
	  author_email='automatethem@gmail.com',
	  license='MIT',
	  packages=find_packages(),
	  zip_safe=False)
