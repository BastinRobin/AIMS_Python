import json
from flask import Flask, render_template, request
from sqlalchemy import Column, Integer, String, Text, DateTime,ForeignKey
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Invoice(db.Model):
    '''
    Features table with following model definition
    '''
    __tablename__ = 'invoices'
    id = db.Column(db.Integer(), primary_key=True)
    invoice_date = db.Column(DateTime)
    for_company_name = db.Column(db.String(255), nullable=False)
    for_company_address = db.Column(db.Text(), nullable=False)
    to_company_name = db.Column(db.String(255), nullable=False)
    to_company_address = db.Column(db.Text(), nullable=False)
    items = db.Column(db.Text(), nullable=False)
    tax = db.Column(Integer)
    total = db.Column(db.String(100))


@app.route("/")
def get_home():
    return render_template('index.html')


@app.route("/create", methods=['POST'])
def insert_invoice():

    invoice_date = datetime\
            .strptime(request.form['invoice_date'], '%Y-%m-%d')

    invoice = Invoice(for_company_name=\
        request.form['for_company_name'],\
        for_company_address=request.form['for_company_address'],\
        invoice_date=invoice_date,\
        to_company_address=request.form['to_company_address'],\
        to_company_name=request.form['to_company_name'],\
        items=request.form['items'],\
        tax=request.form['tax'],\
        total=request.form['total']\
        )

    db.session.add(invoice)
    db.session.commit()

    return str(invoice.id)


@app.route('/list', methods=['GET'])
def list_invoices():
    invoices = Invoice.query.all()
    return render_template('list.html', invoices=invoices)


@app.route('/<id>', methods=['GET'])
def show_invoice(id):

    invoice = Invoice.query.get(id)
    return render_template('invoice.html', data=invoice, items=json.loads(invoice.items))











if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=5000)