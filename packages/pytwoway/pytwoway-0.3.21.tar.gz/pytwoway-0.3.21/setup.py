import setuptools

with open('README.rst', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pytwoway',
    version='0.3.21',
    author='Thibaut Lamadon',
    author_email='thibaut.lamadon@gmail.com',
    description='Estimate two way fixed effect labor models',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/tlamadon/pytwoway',
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'numba',
        'paramsdict>=0.0.3',
        'bipartitepandas>=1.1.3',
        'scipy',
        'statsmodels',
        'pyamg',
        'qpsolvers',
        'quadprog',
        'ConfigArgParse',
        'matplotlib',
        'tqdm'
      ],
    entry_points = {
        'console_scripts': ['pytw=pytwoway.command_line:main'],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
