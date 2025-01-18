from utils.utils import create_file, newdir, cd
from .text import create_db, create_env, create_run, create_blueprint
import venv
import os

def create_engine(names_modules, names_templates):

    os.system("virtualenv venv")
    os.system("venv/bin/pip install Flask")
    os.system("venv/bin/pip install psycopg2-binary")
    os.system("venv/bin/pip install python-dotenv")

    print("CREATE ENGINE")
    
    newdir('app')
    create_file('run.py', create_run)
    create_file('db.py', text=create_db)
    create_file('.env', text=create_env)
    cd('app')
    newdir('templates')
    cd('templates')

    for name in names_templates:
        create_file(name + '.html')

    cd('..')
    create_file('__init__.py')

    for name in names_modules:
        newdir(name)
        cd(name)
        create_file('__init__.py', text=create_blueprint(name))
        create_file(name + '.py')
        cd('..')
        print(f"CREATE DIR - {name}")