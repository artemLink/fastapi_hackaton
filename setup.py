from setuptools import setup


setup(
    name='app-hackaton',
    version='0.0.1',
    author='Yoba Team',
    install_requires= [
        'fastapi == 0.70.0',
        'uvicorn == 0.18.3',
        'SQLAlchemy==1.4.26',
        'pytest==6.2.5',
        'requests==2.26.0'
    ],
    scipts =['app/main', 'scripts/create_db.py']
)