from setuptools import setup

setup(
    name='tathum',
    version='0.1.1',
    description='Trajectory Analysis Toolkit for Human Movement',
    url='https://github.com/ActionAttentionLab/tat-hum',
    download_url='https://github.com/ActionAttentionLab/tat-hum/archive/refs/tags/0.1.tar.gz',
    author='Michael Wang, UofT BUMP Lab',
    author_email='michaelwxy.wang@utoronto.ca',
    license='MIT',
    packages=['tathum', ],
    zip_safe=False,
    install_requires=[
        'numpy',
        'pandas',
        'scipy',
        'scikit-spatial',
        'vg',
        'pytransform3d',
        'matplotlib',
        'jupyter',
    ]
)
