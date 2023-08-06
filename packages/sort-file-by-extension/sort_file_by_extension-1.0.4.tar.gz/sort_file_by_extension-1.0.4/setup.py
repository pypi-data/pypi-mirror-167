from importlib.metadata import entry_points
from setuptools import setup, find_namespace_packages

setup(name='sort_file_by_extension',
      version='1.0.4',
      description='Scrtip sort file by extension',
      url='https://github.com/gorandalex/Python-home-work',
      author='Andrii Horobets',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points = {'console_scripts': ['clean-folder = sort:main']})