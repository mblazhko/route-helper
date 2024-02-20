from setuptools import setup, find_packages


setup(
    name="route-helper",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    package_dir={'route_helper': 'helper'},
    description="Help find routes avoiding Switzerland using Google Maps API",
    author="Maks Blazhko",
    author_email="maksym.blazhko.pydev@gmail.com",
    url="https://github.com/mblazhko/route-helper",
    install_requires=("googlemaps>=4.10.0",),
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
