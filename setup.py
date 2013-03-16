from setuptools import setup, find_packages

setup(name='git-continuous-buildpackage',
      description="Git buildpackage for jenkins",
      long_description="Builds and releases new packages with jenkins",
      version="0.0.1",
      url='',
      author="Arthur Gautier",
      author_email="aga@zenexity.com",
      packages = find_packages(),
      license = "2-clauses BSD",
      classifiers = ['Topic :: System :: Systems Administration'],
      install_requires = [
        'argparse',
        'GitPython',
        'PyYAML'
      ],
      entry_points={ 'console_scripts': [
        'gbc = gbc.cli:main'
      ]}
      )

