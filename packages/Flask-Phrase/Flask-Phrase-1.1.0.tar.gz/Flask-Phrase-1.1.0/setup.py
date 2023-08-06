"""
Flask-Phrase
------------

Connect your Flask apps to Phrase, the powerful in-context-translation solution.

"""

from setuptools import setup

setup(
    name='Flask-Phrase',
    version='1.1.0',
    url='http://github.com/phrase/Flask-Phrase',
    license='MIT',
    author='Dynport GmbH',
    author_email='tobias.schwab@phrase.com',
    description='Connect your Flask apps to Phrase, the powerful in-context-translation solution.',
    packages=['flask_phrase'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask-Babel'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Software Development :: Localization'
    ]
)
