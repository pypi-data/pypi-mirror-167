from setuptools import find_namespace_packages, setup
setup(
    name = 'actelink-computation',
    packages=find_namespace_packages(include=['actelink*']),
    license='LICENSE.txt',
    long_description_content_type="text/markdown",
    long_description="",
    install_requires=['requests', 'flask', 'flask_restx', 'coloredlogs', 'python-dotenv', 'gunicorn'],
)