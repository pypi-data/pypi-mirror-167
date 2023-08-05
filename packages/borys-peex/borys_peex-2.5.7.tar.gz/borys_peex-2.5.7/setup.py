from setuptools import setup

# with open("README.md", 'r') as f:
#     long_description_content_type = f.read()

setup(
        name='borys_peex',
        version='2.5.7',
        description='Incrediable and not reproducible python app!!!111',
        author='borys',
        author_email='borys@deathstar.com',
        license="MIT",
        url="https://long.long.time.ago.com",
        packages=['borys_peex'],
        entry_points={
                'console_scripts': [
                    'borys_ninja=borys_peex.main:main',
                ],
        },
        # long_description_content_type =long_description_content_type 
)