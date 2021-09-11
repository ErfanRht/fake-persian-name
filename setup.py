from distutils.core import setup
setup(
  name = 'fake_persian_name',
  packages = ['fake_persian_name'],
  version = '1.1.3',
  license='MIT',
  description = 'A small Python library to generate fake Persian name.',
  long_description="https://github.com/ErfanRht/fake_persian_name/blob/master/README.md",
  long_description_content_type='text/markdown',
  author = 'Erfan Rahmati',
  author_email = 'ErfanRht2005@gmail.com',
  url = 'https://github.com/ErfanRht/fake-persian-name',
  download_url = 'https://github.com/ErfanRht/fake_persian_name/blob/master/dist/fake_persian_name-1.1.3.tar.gz',
  keywords = ['fake', 'persian', 'name', 'persian name', 'fake name'],
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
  install_requires= [
    "requests"
  ],
  project_urls={
        'Documentation': 'https://requests.readthedocs.io',
        'Source': 'https://pypi.org/project/fake_persian_name/',
    },
  include_package_data=True,
)