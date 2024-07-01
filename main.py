from flask import Flask, render_template
import pymongo 


mongoClient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = mongoClient["AgenciaDeTurismo"]

# col = mydb["PontoTuristico"]

# mydoc = col.find()

# for x in mydoc:
#     print(mydoc)

from pontoTuristico_view import *

app = Flask(__name__)

@app.route('/')
def index():
    mycol = mydb["PontoTuristico"]
    pontosTuristicos = mycol.find()

    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)