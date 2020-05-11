from setuptools import setup, find_packages

setup(name='ospacial',
      version='0.1',
      description='Solution to Open-Spacial Shokunin Challenge',
      url='https://github.com/safetydave/open-spacial',
      author='David Colls',
      author_email='david dot colls at gmail com',
      license='MIT',
      python_requires='>=3.6.0',
      packages=find_packages("src"),
      package_dir={"": "src"},
      install_requires=['matplotlib', 'networkx', 'numpy', 'pandas', 'scipy'],
      zip_safe=False)
