from setuptools import setup
from route_helper import VERSION

setup(
    name="route-helper",
    version=VERSION,
    packages=["route_helper"],
    include_package_data=True,
    description="Help find routes avoiding Switzerland using Google Maps API",
    author="Maks Blazhko",
    namespace_packages=['route_helper'],
    author_email="maksym.blazhko.pydev@gmail.com",
    url="https://github.com/mblazhko/route-helper",
    install_requires=["googlemaps>=4.10.0"],
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: MIT',
    ],
    license="MIT",
    keywords="google maps route",
)
