# -*- coding: utf-8 -*-
import pandas as pd
import holidays # type: ignore
from pathlib import Path

dir_path = Path(__file__).parent
MESES = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
dicionario_meses = dict(zip(range(1, 13), MESES))

dicionario_dias = {"Sunday": "Domingo", "Monday": "Segunda", "Tuesday": "Terça", "Wednesday": "Quarta", "Thursday": "Quinta", "Friday": "Sexta", "Saturday": "Sábado"}

def converte_para_feriado(data):
    data_formatada = pd.to_datetime(data, format='%d/%m/%Y')
    br_holidays = holidays.Brazil(years=data_formatada.year)

    if data_formatada in br_holidays:
        nome_do_feriado = br_holidays.get(data_formatada)
        return f"Feriado ({nome_do_feriado})"
    else:
        return dicionario_dias.get(data_formatada.strftime('%A'), "ERRO NA FUNÇÃO converte_para_feriado")

def datas_do_periodo(data_inicial, data_final):

    # Formatando as datas para pd_datetime
    data_inicial = pd.to_datetime(data_inicial, format='%d/%m/%Y')
    data_final = pd.to_datetime(data_final, format='%d/%m/%Y')

    # Cria a série de datas
    datas = pd.date_range(data_inicial, data_final)

    # Cria um dataframe com duas colunas, uma para datas e outra para os dias da semana.
    df = pd.DataFrame({"Data": datas, "Dia da semana": datas})

    # Formatando as colunas
    df['Data'] = datas.strftime('%d/%m/%Y')
    df['Dia da semana'] = datas.map(converte_para_feriado).astype(str)

    return df

df = datas_do_periodo("20/05/2024", "05/10/2024")
file_path = dir_path.joinpath(f'calendario.xlsx')
df.to_excel(file_path, index=False)
