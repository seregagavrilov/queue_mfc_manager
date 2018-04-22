from setuptools import setup, find_packages


setup(
    name='queue_mfc_manager',
    description='Simple queue manager for me and you!',
    author='Sergey Gavrilov',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    author_email='sergeigavrilov123@gmail.com',
    py_modules=['workers'],
    license='MIT',
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        workers=queue_mfc_manager.workers.workers:start_workers
    ''',
)