from setuptools import setup, find_packages
setup(
    name='dl_common',
    version='0.0.2',
    license='MIT',
    author="Zaheer ud Din Faiz",
    author_email='zaheer@datalogz.io',
    packages=find_packages(exclude=["tests*"]),
)