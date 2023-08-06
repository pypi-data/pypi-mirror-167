from setuptools import setup, find_packages

setup(
      name='yeref',
      version='0.0.1',
      description='desc-f',
      author='john smith',
      py_modules=['yeref'],
      packages=find_packages(),
      scripts=['yeref.py']
)

# from distutils.core import setup
# from setuptools import setup, find_packages
# setup(
#       name='yeref',
#       version='0.0.1',
#       description='desc-f',
#       author='john smith',
#       py_modules=['yeref'],
#       packages=find_packages(),
#       scripts=['yeref.py']
# )
#
# python setup.py sdist
# python setup.py install
# python setup.py develop
# python setup.py bdist_wheel
#
# twine upload --repository-url https://upload.pypl.org/legacy dist/*
# +pswd