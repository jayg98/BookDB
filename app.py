from models import (Base, session, 
                    Book, engine)

# import models
# main menu - add, search, analysis, exit, view
# add books to DB
# edit books
# delte books
# search books
# data cleaning
# loop runs program

if __name__ == '__main__':
    Base.metadata.create_all(engine)