import os
import setuptools

def requirements():
    with open(os.path.join(os.path.dirname(__file__), 'requirements.txt'), encoding='utf-8') as f:
        return f.read().splitlines()

setuptools.setup(
	name='pytorch-lightning-helper',
	version='0.0.6',
	description='Pytorch lightning helper',
	long_description=open('README.md').read(),
	author='Sang Ki Kwon',
	url='https://github.com/automatethem/pytorch-lightning-helper',
	install_requires=requirements(),
	author_email='automatethem@gmail.com',
	license='MIT',
	packages=setuptools.find_packages(),
	zip_safe=False
)
