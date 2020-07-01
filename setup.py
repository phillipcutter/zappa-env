from distutils.core import setup
setup(
    name='zappa-env',         # How you named your package folder (MyLib)
    packages=['zappa-env'],   # Chose the same as "name"
    version='0.22',      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='Run Zappa commands with Python virtual environments',
    author='Phillip Cutter',                   # Type in your name
    author_email='mrfleap@gmail.com',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/mrfleap/zappa-env',
    # I explain this later on
    download_url='https://github.com/mrfleap/zappa-env/archive/0.22.tar.gz',
    # Keywords that define your package best
    keywords=['zappa', 'virtualenv', 'env', 'virtualenvironment'],
    install_requires=[            # I get to this in a second
        'zappa',
    ],
    entry_points={
        'console_scripts': [
            'zappa-env=zappa-env.zappa-env:main',
        ],
    },
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 4 - Beta',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
