from setuptools import setup


# specify requirements of your package here
REQUIREMENTS = []

# some more details
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Internet',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.10',
    ]

# calling the setup function 
setup(name='colubrid-helpers',
      version='1.0.19',
      description='Colubrid libraries',
      url='https://github.com/rhonalejandro/Colubrid-Framework',
      author='Rhonald Alejandro Brito Querales',
      author_email='rhonalejandro@gmail.com',
      license='MIT',
      packages=["src"],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='colubrid-helpers',
      entry_points = {
        "console_scripts": [
            "my_project = src.__main__:main"
        ]
    }
      )