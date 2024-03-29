import pandas as pd
import numpy as np

global version
version = 'V1.4'

def main(pathBD, pathLogOP):

    print('Cargill OPViagem ', version)
    
    df_BD = pd.read_csv(pathBD, low_memory=False)
    df_LogOP = pd.read_excel(pathLogOP, sheet_name='Operação')

    df_BD['Timestamp'] = pd.to_datetime(df_BD['Timestamp'])
    df_LogOP['Chegada'] = pd.to_datetime(df_LogOP['Chegada'])
    df_LogOP['Partida'] = pd.to_datetime(df_LogOP['Partida'])

    df_LogOP.sort_values(by=['Site', 'Partida'], ascending = True, inplace = True, ignore_index=True)

    DestinoAnt = ''
    DataChegadaAnt = ''
    SiteAnt = ''
    for LinhaOP in df_LogOP.index: # Equivalente à isso -> range(len(df_LogOP))
        
        DataPartida = df_LogOP.loc[LinhaOP, 'Partida']
        DataChegada = df_LogOP.loc[LinhaOP, 'Chegada']
        Site = df_LogOP.loc[LinhaOP, 'Site']
        Destino = df_LogOP.loc[LinhaOP, 'Destino']

        df_BD.loc[((df_BD['Timestamp']>= DataPartida) & (df_BD['Timestamp']<= DataChegada) & 
                   (df_BD['Site'] == Site)), 'Modo_de_Operação'] = Destino
        
        if Destino == 'Santarem':
            df_BD.loc[((df_BD['Timestamp']>= DataPartida) & (df_BD['Timestamp']<= DataChegada) & 
                   (df_BD['Site'] == Site)), 'IDViagem'] = 'STM - '+ str(DataPartida)
        elif Destino == 'Miritituba':
            df_BD.loc[((df_BD['Timestamp']>= DataPartida) & (df_BD['Timestamp']<= DataChegada) & 
                   (df_BD['Site'] == Site)), 'IDViagem'] = 'MTB - ' + str(DataPartida)

        if DestinoAnt == 'Miritituba' and SiteAnt == Site:
            df_BD.loc[((df_BD['Timestamp'] >= DataChegadaAnt) & (df_BD['Timestamp'] <= DataPartida) & 
                       (df_BD['Site'] == Site)), 'Modo_de_Operação'] = 'Manobra'
            
            df_BD.loc[((df_BD['Timestamp'] >= DataChegadaAnt) & (df_BD['Timestamp'] <= DataPartida) & 
                       (df_BD['Site'] == Site)), 'IDViagem'] = 'MNB - ' + str(DataChegadaAnt)
        

        DestinoAnt = Destino
        DataChegadaAnt = DataChegada
        SiteAnt = Site
    

    df_BD.to_csv(pathBD, index=False, encoding='utf-8-sig')
    
    return True


if  __name__ == '__main__':
    print('Execute através da GUI!!!')
