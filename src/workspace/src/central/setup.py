from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'central'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'resource'), glob('resource/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='antonio',
    maintainer_email='antonio.cavalcante@sou.inteli.edu.br',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "chatbot= central.chatbot:main",
            "input_node= central.input_node:main",
            "llm= central.llm:main",
            "telegram= central.telegram_api:main",
        ],
    },
)
