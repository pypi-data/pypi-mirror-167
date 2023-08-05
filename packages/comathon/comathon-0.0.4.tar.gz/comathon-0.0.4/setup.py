from setuptools import setup, find_packages

setup(
    name='comathon',
    version='0.0.4',
    license='MIT',
    author="Comathon",
    author_email='Comathon2020@gmail.com',
    description = ("Comathon module for comathon.com website"),
    packages=['src', 'tests'],
    # packages=find_packages('src'),
    # py_modules = ["myfunctions", "simple_addition"],
    # package_dir={'': 'src'},
    url='https://github.com/Comathon/module',
    install_requires=['requests'],
)


