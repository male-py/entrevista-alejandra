import numpy as np
import pandas as pd
from datetime import datetime
from datetime import timedelta

__all__ = ['analisis_serie_tiempo']


def analisis_serie_tiempo(file_name):

    """
    esto es para leer el archivo que se llama: "test_data.pkl"
    """
    df_serie_tiempo = pd.read_pickle(file_name)

    """
    imprimir por pantalla la variable df_serie_tiempo. En este caso, df_serie_tiempo es un dataframe 
    con los datos del archivo "test_data.pkl"
    """
    print(df_serie_tiempo)
    
    descripcion_dataframe = df_serie_tiempo.describe()

    print(descripcion_dataframe)

    numero_1 = "1."

    TITULO_ANALISIS = "INFORME DE HALLAZGOS"
    NOMBRE_DE_ANALISIS = "{} Descripción estadistica del DataFrame".format(numero_1)
    print('\n') # equivalente a dar un ENTER
    print(TITULO_ANALISIS)
    print('\n') # equivalente a dar un ENTER
    print(NOMBRE_DE_ANALISIS)
    print(descripcion_dataframe)

    missing_values_count = df_serie_tiempo.isnull().sum()

    #https://es.stackoverflow.com/questions/279443/c%C3%B3mo-calcular-el-recuento-de-datos-faltantes-para-columnas

    for name, miss_vals in missing_values_count.items():
        print("La columna {0} tiene {1} datos faltantes".format(name, miss_vals))

    df_null_data = df_serie_tiempo[df_serie_tiempo.isnull().any(axis=1)]

    #este paso asume que se tiene un solo dato null
    index_anterior = df_null_data.index[0] - 1
    index_data_null = df_null_data.index[0]
    index_posterior = df_null_data.index[0] + 1
    print(index_anterior, index_data_null, index_posterior)

    #https://www.it-swarm-es.com/es/python/python-pandas-devuelve-solo-aquellas-filas-que-tienen-valores-faltantes/1053644035/

    df_serie_tiempo_seccion_null = df_serie_tiempo.iloc[index_anterior:index_posterior+1]
    print(df_serie_tiempo_seccion_null)

    fecha_faltante = df_serie_tiempo['Timestamps'][index_posterior] - timedelta(minutes=1)
    print(fecha_faltante)

    df_serie_tiempo['Timestamps'].iloc[index_data_null] = fecha_faltante

    print(df_serie_tiempo.iloc[index_anterior:index_posterior])

    return df_serie_tiempo, descripcion_dataframe, index_data_null

def main():
    """
    definir una variable como file_name y a esta varible se le ASIGNA (=) el valor
    de un STRING "test_data.pkl"
    """
    file_name = "test_data.pkl"
    df, descripcion_dataframe, index_data_null = ta.analisis_serie_tiempo(file_name)
    
if __name__ == '__main__':
    main()