import json
import mysql
from flask import Flask, Response
import mariadb

from PythonModule8 import cursor

connection = mariadb.connect(
    user="root",
    password="Shalala",
    host="127.0.0.1",
    port=3306,
    database="flight_game",
)
app = Flask(__name__)


@app.route('/airport/<code>')
def airport_information_fro_code(code):
    try:
        sql = "SELECT name, municipality FROM airport"
        sql += "WHERE airport.ident = '" + code + "'"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        if cursor.rowncount > 0:
            name = result[0]
            location = result[1]
            response = {
                "ICAO": code,
                "Name": name,
                "Location": location,
            }
        else:
            response = {}

        return response
    except ValueError:
        print(ValueError)
        response = {
            "message": "Invalid number as addend",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response


@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
