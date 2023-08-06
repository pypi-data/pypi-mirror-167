from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='ts_mail_sender',
  version='0.0.1',
  description='A package to send emails and attachments',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/edwardtsatsu/email_lib',  
  author='Akorlie Edward Tsatsu',
  author_email='edwardakorlie73@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='email', 
  packages=find_packages(),
  install_requires=['sendgrid'] 
)