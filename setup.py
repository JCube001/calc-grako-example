from contextlib import contextmanager
from setuptools import setup
from setuptools.command.build_py import build_py
import os
import subprocess

@contextmanager
def cd(target):
    cwd = os.getcwd()
    try:
        os.chdir(target)
        yield
    finally:
        os.chdir(cwd)


class BuildPyCommand(build_py):

    def run(self):
        if not self.dry_run:
            with cd('calc'):
                subprocess.call('grako -o calc.py calc.ebnf')
        return super().run()


with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='calc',
    version='1.0.0',
    description='An example calculator application showing how to use Grako',
    long_description=long_description,
    url='https://github.com/JCube001/calc-grako-example',
    author='Jacob McGladdery',
    author_email='jacobm117@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Code Generators'
    ],
    keywords='calculator grako infix example',
    packages=['calc'],
    install_requires=[
        'grako>=3.9.1'
    ],
    entry_points={
        # Note that all entry points must be callable objects
        'console_scripts': [
            'calc=calc.__main__:main'
        ]
    },
    cmdclass={
        'build_py': BuildPyCommand
    }
)
