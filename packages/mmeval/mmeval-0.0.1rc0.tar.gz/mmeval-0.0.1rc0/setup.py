from setuptools import find_packages, setup  # type: ignore


def readme():
    with open('README.md', encoding='utf-8') as f:
        content = f.read()
    return content


version_file = 'mmeval/version.py'


def get_version():
    with open(version_file, 'r') as f:
        exec(compile(f.read(), version_file, 'exec'))
    return locals()['__version__']


setup(
    name='mmeval',
    version=get_version(),
    description='Metrics of computer vision',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/open-mmlab/mmeval',
    author='MMEval Authors',
    author_email='openmmlab@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=[],
)
