import os

def create_file(name):
    print(f'CREATE {name}')
    return open(name, 'w')

def newdir(name):
    print(f'CREATE DIR {name}')
    os.mkdir(name)

def cd(dir):
    os.chdir(dir)