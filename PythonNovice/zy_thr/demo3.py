# -*- coding: utf-8 -*-
__author__ = 'yuan'

# import fileinput,random
# fortunes=list(fileinput.input())
# print(random.choice(fortunes))

import sys,shelve
# s=shelve.open('test.dat')
# s['x']=['a','b','c']
# temp=s['x']
# temp.append('d')
# s['x']=temp
# print(s['x'])

# error
def store_person(db):
    pid=input('Enter unique ID number:')
    person={}
    person['name']=input('Enter name:')
    person['age']=input('Enter age:')
    person['phone']=input('Enter phone number:')
    db[pid]=person
def lookup_person(db):
    pid=input('Enter ID number:')
    field=input('What would you like to know?(name,age,phone)')
    field=field.strip().lower()
    print(field.capitalize()+':',db[pid][field])
def print_help():
    print('The available commands are:')
    print('store:Stores information about a person')
    print('lookup:Looks up a person from ID number')
    print('quit:Save changes and exit')
    print('?:Prints this message')
def enter_command():
    cmd=input('Enter command(? for help):')
    cmd=cmd.strip().lower()
    return cmd
def main():
    database=shelve.open('tet.dat')
    try:
        while True:
            cmd=enter_command()
            if cmd=='store':
                store_person(database)
            elif cmd=='lookup':
                lookup_person(database)
            elif cmd=='?':
                print_help()
            elif cmd=='quit':
                return
    finally:
        database.close()
if __name__ == '__main__':
    main()