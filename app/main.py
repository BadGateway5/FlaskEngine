import os
import subprocess

from engine.main import create_engine, newdir
from utils.utils import cd

def main():
    
    name = input("enter project name: ")
    
    questions = {
        'admin': False,
        'auth': False,
    }

    for q in questions.keys():
        ans = int(input(f"use {q} 1 or 0: "))
        if ans:
            questions[q] = True


    cd('..')
    newdir(name)
    cd(name)
    create_engine(questions)

if __name__ == "__main__":
    main()