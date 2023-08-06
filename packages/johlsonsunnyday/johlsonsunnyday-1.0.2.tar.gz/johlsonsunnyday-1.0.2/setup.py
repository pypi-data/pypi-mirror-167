from setuptools import setup
setup(
    name='johlsonsunnyday',            #* Your package will have this name. Search on pypi if available.
    packages = ['johlsonsunnyday'],    #* Name the package again. List subpackages also if you have them.
    version = '1.0.2',          #* To be increased every time you change your library
    license = 'MIT',              # Type of license. More here: https://help.github.com/articles/licensing-a-repository
    description = 'Weather forecast data',      # Short description of your library
    author = 'Jonas Ohlson',                    # Your name
    author_email = 'jonas_ohlson@yahoo.se',     # Your email
    url = 'https://example.com',                 # Homepage of your library (e.g. github or your website)
    keywords = ['weather', 'forecast', 'openweather'],  #Keywords users can search on pypi.org
    install_requires=[                          # Other 3rd party libs that pip needs to install
        'requests'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',      # Choose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current status
        'Intended Audience :: Developers',      # Who is the audience for your library?
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Type a license again
        'Programming Language :: Python :: 3.5',    # Python versions your library supports. Try by installing multiple versions of Python
        'Programming Language :: Python :: 3.6',    # and importing your library into each of them.
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ]
)
