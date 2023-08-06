from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='squareapi_py',
    version='0.0.3',
    license='MIT License',
    author='Astro',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='ericksantosyb@gmail.com',
    keywords='square_lib',
    description=u'Uma biblioteca que ultilizar a api da squarecloud',
    packages=['squareapi_py'],
    install_requires=['requests', 'colorama'],)