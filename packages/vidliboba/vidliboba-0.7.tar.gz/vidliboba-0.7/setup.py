from setuptools import setup, find_packages


setup(
    name='vidliboba',
    version='0.7',
    license='MIT',
    author="Nikolay Igotin",
    author_email='poqdev@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/pomoq-dev/video-clipping',
    keywords='video images audio tools',
    install_requires=[
        'moviepy',
        'tqdm~=4.64.0',
        'ffmpeg-python',
        'yt-dlp',
        'pydub',
        'soundfile',
        'pysndfx',
        'pyaudioconvert'
      ],

)