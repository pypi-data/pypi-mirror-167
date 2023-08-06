from setuptools import setup, find_packages

long_description = ''
with open("README.md") as file:
    long_description = file.read()

setup(
    name='mhpp',
    version='0.3.0',
    description='A median house price prediction project to demonstrate packaging.',
    install_requires=[
        'scipy',
        'numpy',
        'pandas',
        'scikit-learn'
    ],
    long_description = long_description,
    long_description_content_type = "text/markdown",
    extras_require={
        'interactive': ['matplotlib', 'seaborn', 'jupyter']
    },
    entry_points={
        'console_scripts': [
            'fetch-data=mhpp.components.ingest_data:fetch_housing_data',
            'train-test-data=mhpp.components.ingest_data:train_test_data',
            'train=mhpp.components.train:train',
            'evaluate=mhpp.components.score:evaluate'
        ]
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)