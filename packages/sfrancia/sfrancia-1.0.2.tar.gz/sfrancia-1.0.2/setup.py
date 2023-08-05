from distutils.core import setup

setup(name='sfrancia',
      packages=['sfrancia'],
      version='1.0.2',
      description='Shapiro-Francia normality test',
      url='',
      download_url='',
      author='Luiz Paulo Fávero',
      author_email='lpfavero@usp.br',
      keywords=['shapiro', 'francia','normality','test'],
      license='MIT',  # YOUR LICENSE HERE!
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
