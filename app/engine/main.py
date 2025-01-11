from utils.utils import create_file, newdir, cd

def create_engine(questions):

    # тут еще надо установить виртуальное окружение
    print("CREATE ENGINE")
    newdir('app')
    create_file('run.py')
    create_file('db.py')
    create_file('.env')
    cd('app')
    newdir('templates')
    create_file('__init__.py')

    for name, ans in questions.items():
        if ans:
            newdir(name)
            cd(name)
            create_file('__init__.py')
            create_file(name + '.py')
            cd('..')
            print(f"CREATE DIR - {name}")
    