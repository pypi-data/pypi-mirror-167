from setuptools import setup

setup(
      # name='rbf_otp',
      # version='0.1.1',
      description='Get OTP 6 digits from OTP',
      url='https://argon.ceti.etat-ge.ch/gitlab/performancetests/robotframework/rbf-otp',
      author='Pedro Lopez Perez',
      maintainer='Pedro Lopez Perez',
      author_email='pedro.lopez-perez@etat.ge.ch',
      keywords='OTP, TOTP',
      license='MIT',
      packages=['rbf_otp'],
      install_requires=[
          "pyotp=='2.6.0'",
      ],
      package_dir={'': 'src'},
      zip_safe=False
      )
