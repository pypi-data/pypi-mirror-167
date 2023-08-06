from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install

#region Custom command

class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        develop.run(self)
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION

#endregion

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
      version='1.0.8',
      description='Colubrid libraries',
      url='https://github.com/rhonalejandro/Colubrid-Framework',
      author='Rhonald Alejandro Brito Querales',
      author_email='rhonalejandro@gmail.com',
      license='MIT',
      packages=[],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='colubrid-helpers',
      cmdclass = {
        'console_scripts': PostDevelopCommand
    }
      )