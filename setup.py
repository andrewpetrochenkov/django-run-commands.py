import setuptools

setuptools.setup(
    name='django-run-commands',
    version='2021.5.18',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
