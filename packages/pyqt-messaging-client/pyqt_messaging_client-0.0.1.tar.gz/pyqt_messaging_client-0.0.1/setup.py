from setuptools import setup, find_packages

setup(name="pyqt_messaging_client",
      version="0.0.1",
      description="PyQT GB Client",
      author="Zektornis",
      author_email="shevchenko.logist@mail.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
