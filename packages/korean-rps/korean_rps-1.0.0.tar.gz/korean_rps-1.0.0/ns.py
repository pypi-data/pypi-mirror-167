import setuptools
from korean_rps import __version__
#python ns.py sdist bdist_wheel
#python -m twine upload dist/*


setuptools.setup(
    name="korean_rps",
    version=__version__,
    license="MIT",
    author="VoidAsMad",
    author_email="voidasmad@gmail.com",
    description="가위바위보 라이브러리",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)