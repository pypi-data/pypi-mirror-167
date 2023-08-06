from setuptools import setup, find_packages


setup(
    name='quanario',
    version='1.0.46',
    author='Stepan-Coder',
    author_email='stepan.borodin2016@bk.ru',
    description='Module for creating VK bots...',
    long_description="Some decription",
    # long_description_content_type='text/markdown',
    url='https://github.com/Stepan-coder/Quanario_VK',
    download_url='https://github.com/Stepan-coder/Quanario_VK/archive/v1.0.46.zip',
    license='CC-BY-NC',
    packages=['quanario'],
    install_requires=['vk-api', 'asyncio', 'ffmpeg', 'pydub', 'prettytable', 'urllib3'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    # python_requires='>=3.5',
)