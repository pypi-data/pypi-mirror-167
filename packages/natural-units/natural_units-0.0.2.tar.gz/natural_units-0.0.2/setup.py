import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="natural_units",
    setup_requires=['setuptools-git-versioning'],
    author="APN",
    author_email="APN-Pucky@no-reply.github.com",
    description="uncertainty quantification for numerical computations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/APN-Pucky/numcertainties",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "scipy"
    ],
    extras_require={
        'dev': [
            "uncertainties",
            "build",
            "pytest",
            "pytest-cov",
            "pytest-profiling",
            "pytest-line-profiler-apn>=0.1.3",
            "jupyterlab",
            "pandas",
            "ipython",
        ],
        'docs': [
            "jupyter-sphinx",
            "sphinx_math_dollar",
            "pandoc",
            "sphinx",
            "nbsphinx",
            "sphinx_rtd_theme",
            "numpydoc",
            "sphinx-autobuild",
        ]
    },
    version_config={
        "template": "{tag}",
        "dev_template": "{tag}.{ccount}",
        "dirty_template": "{tag}.{ccount}+dirty",
        "starting_version": "0.0.0",
        "version_callback": None,
        "version_file": None,
        "count_commits_from_version_file": False
    },
    python_requires='>=3.6',
)
