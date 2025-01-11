import os
import subprocess

from engine.main import create_engine, newdir
from utils.utils import cd

def main():
    
    name = input("enter project name: ")
    
    amount_modules = int(input("amount modules: "))
    amount_templates = int(input("amount html templates: "))


    names_modules = []
    names_templates = []

    for _ in range(amount_modules):
        names_modules.append(input("enter name module: "))

    for _ in range(amount_templates):
        names_templates.append(input('enter name html template: '))


    cd('..')
    cd('..')
    newdir(name)
    cd(name)
    create_engine(names_modules, names_templates)

if __name__ == "__main__":
    main()