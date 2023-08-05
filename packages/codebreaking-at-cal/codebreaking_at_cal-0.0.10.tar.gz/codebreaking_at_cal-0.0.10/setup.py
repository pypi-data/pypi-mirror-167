import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='codebreaking_at_cal',
    version='0.0.10',
    author='Ryan Cottone',
    author_email='rcottone@nvidia.com',
    description='CBC package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/CodebreakingAtCal/codebreaking-package',
    packages=['codebreaking_at_cal'],
    package_data={'': ['*.csv']},
    install_requires=['requests']
)