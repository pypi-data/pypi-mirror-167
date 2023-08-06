from setuptools import (
    find_packages,
    setup,
)

setup(
    name='sms_tool',
    version='0.0.1',
    description='sms sdk',
    classifiers=[],
    keywords='sms sdk',
    author='zgl',
    author_email='',
    url='',
    license='MIT',
    packages=find_packages(exclude=[]),
    package_data={'': ['*.*']},
    include_package_data=True,
    install_requires=[
        'colorama~=0.4.4',
        'requests~=2.28.1'
    ],
    long_description='sms sdk by python'
)
