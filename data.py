from datetime import date


class Data:
    def __init__(self, dia, mes, ano):
        teste = date(ano, mes, dia)
        print( teste.strftime('%d/%m/%y'))
