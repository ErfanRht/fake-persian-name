from distutils.core import setup
setup(
  name = 'fake_persian_name',
  packages = ['fake_persian_name'],
  version = '1.0.0',
  license='MIT',
  description = 'A package to generate fake persian name',
  author = 'Erfan Rahmati',
  author_email = 'ErfanRht2005@gmail.com',
  url = 'https://github.com/ErfanRht/fake-persian-name',
  download_url = 'https://github.com/ErfanRht/fake-persian-name/archive/v_01.tar.gz',
  keywords = ['fake', 'persian', 'name', 'persian name', 'fake name'],
  install_requires=[
          'random',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)