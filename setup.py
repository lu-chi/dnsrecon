from setuptools import setup                                                                                       

setup(
  name='dnsrecon',
  version='0.1',
  long_description=__doc__,
  include_package_data=True,
  zip_safe=False,
  install_requires=[
    'dnspython',
    'netaddr'
  ],
)
