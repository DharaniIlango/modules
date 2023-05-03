from setuptools import setup

setup(
    name='my_package',
    version='0.1',
    packages=['my_package'],
    install_requires=[
        'numpy=>1.22.4',
        'scikit-learn>=1.2.2',
        'pandas=>1.4.4'
    ],
    description='My package description',
    author='My Name',
    author_email='dharaniilango1209@gmail.com',
    url='https://github.com/DharaniIlango/modules',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)