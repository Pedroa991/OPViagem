import pandas as pd
import numpy as np
from tkinter import filedialog
import tkinter

global version
version = 'V1.0'

def main():

    print('Cargill OPViagem ', version)
    root = tkinter.Tk()

    pathLogOP = filedialog.askopenfilename(title='Selecione o arquivo LogOP',
                                filetypes= [("Excel files","*.xlsx")])
    pathBD = filedialog.askopenfilename(title='Selecione o arquivo Log de motores',
                            filetypes= [("Excel files","*.csv")])
    df_BD = pd.read_csv(pathBD, low_memory=False)
    df_LogOP = pd.read_excel(pathLogOP, sheet_name='Operação')

    df_BD['Timestamp'] = pd.to_datetime(df_BD['Timestamp'])
    df_LogOP['Chegada'] = pd.to_datetime(df_LogOP['Chegada'])
    df_LogOP['Partida'] = pd.to_datetime(df_LogOP['Partida'])

    DestinoAnt = ''
    DataChegadaAnt = ''
    for LinhaOP in df_LogOP.index:
        
        DataPartida = df_LogOP.loc[LinhaOP, 'Partida']
        DataChegada = df_LogOP.loc[LinhaOP, 'Chegada']
        Site = df_LogOP.loc[LinhaOP, 'Site']
        Destino = df_LogOP.loc[LinhaOP, 'Destino']

        df_BD.loc[((df_BD['Timestamp']>= DataPartida) & (df_BD['Timestamp']<= DataChegada) & 
                   (df_BD['Site'] == Site)), 'Modo de Operação'] = Destino

        if DestinoAnt == 'Miritituba':
            df_BD.loc[((df_BD['Timestamp'] >= DataPartida) & (df_BD['Timestamp'] <= DataChegada) & 
                       (df_BD['Site'] == Site)), 'Modo de Operação'] = 'Manobra'
        

        DestinoAnt = Destino
        DataChegadaAnt = DataChegada


if  __name__ == '__main__':
    main()
