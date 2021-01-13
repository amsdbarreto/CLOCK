import json
from calc import Angule
from flask import Flask

# from flask_restful import Resource, Api

app = Flask(__name__)


@app.route("/rest/clock/<int:hours>/<int:minute>", methods=["GET"])
def calc(hours=12, minute=0):
    if 1 <= hours <= 24:

        if 0 <= minute <= 59:
            if hours > 12:
                hours = hours - 12

            an = Angule
            _resp = an.clocks(hours, hours, minute)

            return _resp, 200

        else:

            return (json.dumps(
                [
                    {"Status": 400,
                     "Menssagem": 'Minuto inválido ( >59 )',
                     "Como resolver": 'Valor entre (1-59)'
                     }
                ])), 400
    else:

        return (json.dumps(
            [
                {"Status": 400,
                 "Menssagem": 'Minuto inválido ( >24 )',
                 "Como resolver": 'Valor entre (1-24)'
                 }])), 400


@app.route("/rest/clock/<int:hours>", methods=["GET"])
def calc2(hours=0, minute=0):
    if 12 < hours <= 24:
        hours = hours - 12
    if hours > 24:
        _resp = json.dumps(
            [
                {"Status": 400,
                 "Menssagem": 'Minuto inválido ( >24 )',
                 "Como resolver": 'Valor entre (1-24)'
                 }
            ])
    else:
        an = Angule
        _resp = an.clocks(Angule, hours, minute)
    return _resp


app.run(port=8080)
