from setuptools import setup


setup(name='lazy_pink_pants',
      version='1.0.1',
      description='Log messages into DB and show them in console or create command line menu or sending e-mails or check subscribtion.',
      url='https://github.com/balazs-mark/lazy_pink_pants.git',
      author='Balazs Mark',
      author_email='contact+lazy_pink_pants@mark-balazs.com',
      license='MIT',
      packages=['ConsoleLog', 'DBLog', 'Menu', 'SendMail', 'SubscribeValidator'],
      zip_safe=False)
