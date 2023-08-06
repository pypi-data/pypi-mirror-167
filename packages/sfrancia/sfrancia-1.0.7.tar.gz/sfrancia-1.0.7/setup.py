from distutils.core import setup

try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()


setup(name='sfrancia',

      packages=['sfrancia'],

      version='1.0.7',

      description=""" Shapiro-Francia normality test """,

      long_description_content_type="text/markdown",

      long_description=long_description,
      
      author='Luiz Paulo Fávero',     
      author_email='lpfavero@usp.br',
      keywords=[],
      install_requires=['numpy', 'scipy'],  # YOUR DEPENDENCIES HERE
      classifiers=[
          # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools',
          'License :: OSI Approved :: MIT License',  # Your License Here
          # List Python versions that you support Here
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
      ],
      )
