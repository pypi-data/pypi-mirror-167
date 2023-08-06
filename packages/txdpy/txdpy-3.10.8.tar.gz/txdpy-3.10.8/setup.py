from distutils.core import  setup

packages = ['txdpy']# 唯一的包名

setup(name='txdpy',
    version='3.10.8',
    author='唐旭东',
    packages=packages,
    package_dir={'requests': 'requests'},)