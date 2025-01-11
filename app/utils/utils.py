import os

def create_file(name, text=''):
    print(f'CREATE {name}')
    file = open(name, 'w')
    file.write(text)
    file.close()

def newdir(name):
    print(f'CREATE DIR {name}')
    os.mkdir(name)

def cd(dir):
    os.chdir(dir)
    print(f'GO TO {os.getcwd()}')