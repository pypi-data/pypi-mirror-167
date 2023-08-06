from setuptools import setup, find_packages

setup(name="pyqt_messaging_GB_server_part_GB",
      version="0.0.3",
      description="PyQT GB Server",
      author="Zektornis",
      author_email="shevchenko.logist@mail.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex'],
      scripts=['server/server_run']
      )
