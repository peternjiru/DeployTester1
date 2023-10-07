#!/usr/bin/env python3

# Local imports
from app import app
from models import Program
from config import db

if __name__ == '__main__':

    with app.app_context():

        print('Deleting existing programs...')
        Program.query.delete()

        print('Creating program objects...')
        after1 = Program(name='happy toto inc', grade='ms')
        after2 = Program(name='hebrew classes', grade='7')
        after3 = Program(name='smiles academy', grade='1')
        after4 = Program(name='nutrition class', grade='3')


        print('Adding program objects to transaction...')
        db.session.add_all([after1, after2, after3, after4])

        print('Committing transaction...')
        db.session.commit()

        print('Complete.')