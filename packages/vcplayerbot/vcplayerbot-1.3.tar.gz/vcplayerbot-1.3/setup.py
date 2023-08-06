import pathlib

from setuptools import find_packages, setup

CWD = pathlib.Path(__file__).parent

README = (CWD / "README.md").read_text()

setup(
    name='vcplayerbot',
    version='1.3',
    packages=find_packages(),
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/gautam1834',
    license='GPL3.0',
    author='https://github.com/gautam1834',
    author_email='gautam@gautam1834.gq',
    include_package_data=True,
    description='VC Player Bot',
    platforms="any",
    install_requires=[
        'aiofiles',
        'aiohttp',
        'asyncio',
        'dnspython',
        'ffmpeg-python',
        'gitpython',
        'hachoir',
        'heroku3',
        'lyricsgenius',
        'motor',
        'pillow',
        'psutil',
        'py-tgcalls==0.8.6',
        'pykeyboard',
        'pyrogram==1.4.16',
        'python-dotenv',
        'pyyaml==5.3.1',
        'requests',
        'speedtest-cli',
        'spotipy',
        'tgcrypto',
        'youtube-search',
        'youtube-search-python',
        'yt-dlp'

    ],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 5 - Production/Stable"
    ],
    python_requires=">=3.10",
)
