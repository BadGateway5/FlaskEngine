import os

def create_file(name, text=''):
    print(f'CREATE {name}')
    with open(name, 'w+') as file:
        file.write(text)

def newdir(name):
    print(f'CREATE DIR {name}')
    os.mkdir(name)

def cd(dir):
    os.chdir(dir)
    print(f'GO TO {os.getcwd()}')