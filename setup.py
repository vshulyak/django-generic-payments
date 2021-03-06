from setuptools import setup, find_packages
 
setup(
    name='django-generic-payments',
    version='0.0.1',
    description='Generic payments app',
    author='Vladimir Shulyak',
    author_email='vladimir@shulyak.net',
    url='http://shulyak.net/',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['django-annoying>=0.7.4']
)
