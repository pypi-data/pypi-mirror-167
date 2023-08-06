from setuptools import setup

setup(name='personal_lib',
      version='1.0.8',
      description="a personal library",
      long_description = "a personal library",
      packages=['personal_lib', 'personal_lib/utils'],
      package_data={'': ['*.txt']},
      install_requires=['pandas>=1.1.4', 'yagmail>=0.14.261', 'paramiko>=2.7.2', 'pymysql>=1.0.2'],
      python_requires='>=3.7',
      )
