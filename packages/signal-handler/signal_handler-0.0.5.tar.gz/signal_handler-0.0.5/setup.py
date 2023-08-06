from setuptools import setup

setup(
    name='signal_handler',
    version='0.0.5',
    packages=['signal_handler'],
    readme="README.md",
    url='https://github.com/oleglpts/signal_handler',
    license='MIT',
    author='Oleg Lupats',
    author_email='oleglupats@gmail.com',
    description='Handling system signals and taking actions on application termination',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)
