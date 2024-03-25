import sqlite3
from flask import Flask, render_template, request, abort, redirect, url_for

def get_db_connection():
    conn = sqlite3.connect('UdemyNlayerDb.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')


@app.route('/privacy')
def privacy():
  return render_template('privacy.html')


@app.route('/products')
def get_products():
     conn = get_db_connection()
     products = conn.execute('SELECT p.*, c.Name as CategoryName FROM Products p INNER JOIN Categories c WHERE p.CategoryId=c.Id ').fetchall()
     conn.close()
     return render_template('/products/index.html', products=products)

@app.route('/products/<int:id>', methods=('GET',))
def get_product(id):
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM Products WHERE id = ?',
                        (id,)).fetchone()
    conn.close()
    
    if product is None:
        abort(404)
    
    return render_template('/products/edit.html', product=product)
    

@app.route('/products/<int:id>', methods=('POST',))
def edit_product(id):
    
    if request.method == 'POST': 
        
      conn = get_db_connection()
      conn.execute('UPDATE Products SET Name = ?, Stock=?, Price = ? ' 
                   ' WHERE id = ?', 
                   (request.form['txtName'], request.form['txtStock'], request.form['txtPrice'], id))

      conn.commit()
      conn.close()

    return redirect(url_for('get_products'))
   


def index():
  return render_template('index.html')


if __name__ == '__main__' :
    app.run(debug=True)