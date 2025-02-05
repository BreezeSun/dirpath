from setuptools import setup, find_packages
setup(
      name='dirpath',
      version='1.0.1',
      author='BreezeSun',
      description='A library for managing directory paths in the python environment.',
      packages=find_packages(),
      long_description=open('README.md','r',encoding='utf-8').read(),
      long_description_content_type="text/markdown",
      license="MIT"
)


