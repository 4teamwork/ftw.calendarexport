from setuptools import setup, find_packages

version = open('ftw/calendarexport/version.txt').read().strip()
maintainer = 'Julian Infanger'

setup(name='ftw.calendarexport',
      version=version,
      description="Export function for ftw.calendar (Maintainer: %s)" % maintainer,
      long_description=open("README.txt").read() + "\n" + \
          open("docs/HISTORY.txt").read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='%s, 4teamwork GmbH' % maintainer,
      author_email='mailto:info@4teamwork.ch',
      maintainer=maintainer,
      url='http://psc.4teamwork.ch/',
      license='GPL2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ftw'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'ftw.calendar',
        'plonegov.pdflatex',
        ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
