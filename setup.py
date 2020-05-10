from setuptools import setup

setup(name='ospacial',
      version='0.1',
      description='Solution to Open-Spacial Shokunin Challenge',
      url='https://github.com/safetydave/open-spacial',
      author='David Colls',
      author_email='david dot colls at gmail com',
      license='MIT',
      packages=['ospacial'],
      python_requires='>=3.6.0',
      install_requires=['matplotlib', 'networkx', 'numpy', 'pandas', 'scipy'],
      zip_safe=False)
