from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

#inventory app config
appinventory = Flask(__name__)
CORS(appinventory)

appinventory.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///inventory.db"
appinventory.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

inventorydb = SQLAlchemy(appinventory)

#customer app config
appcustomer = Flask(__name__)
CORS(appcustomer)
appcustomer.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///customers.db"
appcustomer.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

custdb = SQLAlchemy(appcustomer)

#vendor app config
appvend = Flask(__name__)
CORS(appvend)

appvend.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///vendors.db"
appvend.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

venddb = SQLAlchemy(appvend)

#invoice app config
appinvoice = Flask(__name__)
CORS(appinvoice)

appinvoice.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///invoices.db"
appinvoice.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

invoicedb = SQLAlchemy(appinvoice)