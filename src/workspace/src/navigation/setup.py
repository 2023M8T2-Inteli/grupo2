from setuptools import find_packages, setup

package_name = 'navigation'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='amanda',
    maintainer_email='amanda.fontes@sou.inteli.edu.br',
    description='Listener navigation points package',
    license='CC0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'waypoint_listener = navigation.nav_waypoints:main',
        ],
    },
)
