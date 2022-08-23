from dbconnection import *
from flask import Flask , request , g ,redirect ,url_for
import json
import sqlite3 as sql
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Pratham07@localhost/postgres'
db=SQLAlchemy(app)


# addbook = http://127.0.0.1:5000/add_book?id=13&bookname='the alchemist'&auther='paulo cohelo'
# update = http://127.0.0.1:5000/update?id=13&bookname=the alchemist&auther=nikhil tayade
# edit = 

#pg = PostgresConnector()
#session = pg.get_conn()

class Book(db.Model):
  __tablename__='books'
  id       = db.Column(db.Integer,primary_key=True)
  bookname = db.Column(db.String(40))
  auther   = db.Column(db.String(40))

  def __init__(self,id,bookname,auther):
    self.id       = id
    self.bookname = bookname
    self.auther   = auther

@app.route('/add_book')
def add_book():
    print('----->>>>',request.method)
    id       = request.args.get('id')
    bookname = request.args.get('bookname')
    auther   = request.args.get('auther')
    book     =  Book(id,bookname,auther)
    db.session.add(book)
    db.session.commit()
    return redirect(url_for("get_all_books"))

@app.route('/update')
def get_update_books():
    id       = request.args.get('id')
    bookname = request.args.get('bookname')
    auther   = request.args.get('auther')
    db.session.execute(f"UPDATE books set bookname= '{bookname}', auther = '{auther}' where id = '{id}' ")
    db.session.commit()
    db.session.close()
    return redirect(url_for("get_all_books"))
    
@app.route('/delete')
def delete_book_name():
    id = request.args.get('id')
    db.session.execute(f"DELETE from books where id = '{id}' ")
    db.session.commit()
    db.session.close()
    return redirect(url_for("get_all_books"))

@app.route('/fetch',methods= ['GET'])
def get_all_books():
    books_name = db.session.execute('SELECT * FROM books')
    books_name = books_name.fetchall()
    db.session.close()
    results = [tuple(row) for row in books_name]
    return json.dumps(results)

if __name__ == '__main__':
   app.run(debug=True)




