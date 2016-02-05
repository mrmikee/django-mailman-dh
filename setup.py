from distutils.core import setup

setup(
    name = 'django-mailman-dh',
    version = '0.1',
    packages = ['django_mailman_dh',],
    platforms = ['any'],
    license = 'GNU LGPL v2.1',
    author = 'Bernd Schlapsi',
    author_email = 'brot@gmx.info',
    author = 'Michael Cone',
    author_email = 'mrmikee@juno.com',
    description = 'Interface to Mailman Web-API hosted by DreamHost',
    long_description = open('README').read(),
    url = '',
)
