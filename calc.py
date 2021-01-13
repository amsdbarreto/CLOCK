import datetime
import json
from math import floor
from dtbase import Conexao


class Angule:

    def clocks(self, w_hour, w_min):
        print("HORA .... : {}".format(w_hour))
        print("MINUTE .. : {}".format(w_min))
        columns = 'angle'
        results = []

        rs = None
        wdata = None
        con = Conexao('localhost', 'clock', 'postgres', '1234')

        # con = psycopg2.connect(host='localhost', database='clock', user='postgres', password='')
        # cur = con.cursor()
        wdata = datetime.datetime.now()
        sql = "select  json_build_object('angle',angle) as angulo_relogio from clock_angle where hour={} and minute={}"

        rs = con.consultar(sql.format(w_hour, w_min))


        if len(rs) == 0:

            # calc_ang = self.calc_Angle(w_hour,w_min)
            # calculo do angulo

            calc_h = 60 * w_hour
            calc_m = 11 * w_min
            calc_ang = floor(abs(calc_m - calc_h) / 2)

            sql = "insert into clock_angle values (default,{},{},{},'{}')"
            if con.manipular(sql.format(w_hour, w_min, calc_ang, wdata.strftime("%d/%m/%Y"))):
                dicts = {"angle": calc_ang}

                # results.append(dict(zip(columns, list(str(calc_ang)))))  # devolve o json do Angulo
                _resp = json.dumps(dicts)
            else:
                _resp = json.dumps(
                    [
                        {"Status": 400,
                         "Menssagem": 'Falha na Inclusão',
                         "Como resolver": 'Procure o Administrador'
                         }
                    ])
        else:
            _resp = json.dumps(rs[0][0])
            _x = json.loads(_resp)
            # Incluir a requisição
            sql = "insert into clock_angle values (default,{},{},{},'{}')"
            print(sql.format(w_hour, w_min, _x['angle'], wdata.strftime("%x")))
            if not con.manipular(sql.format(w_hour, w_min, _x['angle'], wdata.strftime("%d/%m/%Y"))):
                _resp = json.dumps(
                    [
                        {"Status": 400,
                         "Menssagem": 'Falha na Inclusão',
                         "Como resolver": 'Procure o Administrador'
                         }
                    ])
        con.fechar()

        return _resp  # json.dumps(results)
