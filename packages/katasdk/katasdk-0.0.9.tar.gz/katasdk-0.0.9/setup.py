
from setuptools import setup, find_packages
from pkgutil import walk_packages
import katagames_sdk


setup(
    name='katasdk',
    packages = find_packages(include=[
        'katagames_sdk',
        'katagames_sdk.katagames_engine',
        'katagames_sdk.katagames_engine.caps',

        'katagames_sdk.katagames_engine.caps.bioslike',
        'katagames_sdk.katagames_engine.caps.engine_ground',
        'katagames_sdk.katagames_engine.caps.networking',
        'katagames_sdk.katagames_engine.caps.struct',

        'katagames_sdk.katagames_engine.compo',

        'katagames_sdk.katagames_engine.foundation',
        'katagames_sdk.katagames_engine.ifaces',
        'katagames_sdk.katagames_engine.looparts',

        'katagames_sdk.katagames_engine.looparts.ai',
        'katagames_sdk.katagames_engine.looparts.demolib',
        'katagames_sdk.katagames_engine.looparts.gui',
        'katagames_sdk.katagames_engine.looparts.isometric',
        'katagames_sdk.katagames_engine.looparts.polarbear',
        'katagames_sdk.katagames_engine.looparts.tmx',
        ]),
    #entry_points ={
    #    'console_scripts': [
    #    'katasdk = katagames_sdk.katasdk_cmd_line:main'
    #    ]
    #},
    version=katagames_sdk.SDKVER_TAG,  # -- version fournie ici
    include_package_data=True,  # see MANIFEST.in
    description='SDK aimed at creating games for the Kata.games platform',
    author='Gaudia Tech Inc.',
    url='https://github.com/gaudiatech/katagames-glob-repo',
    author_email='thomas@gaudia-tech.com',
    long_description='SDK aimed at creating games for the Kata.games platform, you can find more info on github: user **gaudiatech**',
    license='MIT',
    tests_require=['pytest==4.4.1'],
    install_requires=[
        'pygame>=2.1.2',
        'requests>=2.27.0'
    ],
    test_suite='tests',
)
