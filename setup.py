from setuptools import find_packages, setup


def read_description():
    with open('README.md') as file:
        return file.read()


if __name__ == '__main__':
    setup(
        name="mpire",
        version='1.0.0',
        author="Sybren Jansen (Target Holding)",
        author_email="sybren.jansen@target-holding.nl",
        description="A Python package for multiprocessing, but faster than multiprocessing",
        long_description=read_description(),
        packages=find_packages(),
        scripts=['bin/mpire-dashboard'],
        install_requires=["numpy", "tqdm"],
        include_package_data=True,
        extras_require={
            'dashboard': ['flask'],
            'docs': ['sphinx', 'sphinx-rtd-theme', 'sphinx-autodoc-typehints', 'sphinxcontrib-images'],
            'dill': ['multiprocess']
        },
        test_suite='tests'
    )
