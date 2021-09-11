from setuptools import setup

with open('./README.md', 'r') as f:
    long_description = f.read()

setup(
  name='fake-persian-name',
  packages=['fake_persian_name'],
  version='1.2.0',
  license='MIT',
  description='A small Python library to generate fake Persian name.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author='Erfan Rahmati',
  author_email='ErfanRht2005@gmail.com',
  url='https://github.com/ErfanRht/fake-persian-name',
  download_url='https://github.com/ErfanRht/fake-persian-name/blob/master/dist/fake-persian-name-1.2.0.tar.gz',
  keywords=['fake', 'persian', 'name', 'persian name', 'fake name', 'fake persian name'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
  install_requires=[
    "requests"
  ],
  project_urls={
        'HomePage': 'https://pypi.org/project/fake-persian-name/',
        'Documentation': 'https://pypi.org/project/fake-persian-name/',
        'Source': 'https://github.com/ErfanRht/fake-persian-name/',
    },
  include_package_data=True,
)