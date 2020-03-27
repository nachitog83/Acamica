def detalle():
    '''
    Funciones que tiene la libreria:
        .
        - librerias()
        - porc_null_col()
        - Cat_plot_basic()
        - heat()
        .
    '''

def librerias():
    
    '''
    Funcion para importar librerias.
    Dicha funcion cuenta con las siguientes librerias:
        - pandas as pd
        - numpy as np
        - seaborn as sns
        - matplotlib.pyplot as plt
    Importar las librerias de la siguiente forma:
        - pd, np, sns, plt =  lica.librerias()
    '''
    
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    print('Se importaron las siguientes librerias:')
    print(' - pandas as pd')
    print(' - numpy as np')
    print(' - seaborn as sns')
    print(' - matplotlib.pyplot as plt')

    return pd, np, sns, plt
    
def porc_null_col(pd, df):
    '''
    Funcion para mostrar el porcentaje de nulos que tienen las columnas
    Llamarla de la siguiente forma:
        - lica.porc_null_col(pd, nombre_de_tu_df)
    '''
    na_percents = []
    total = []
    total_columns = []
    columns = []

    for col in df.columns:
        
        total_columns.append(len(df[col]))
        na_percents.append(round((sum(df[col].isna())/df[col].shape[0]*100),2))
        total.append(sum(df[col].isna()))
    
    df_nulls = pd.DataFrame({'columnas': df.columns, 'total_registros_fila': total_columns,'total_columns': total, '%_nulos': na_percents})
    
    df_nulls = df_nulls.sort_values(by=['%_nulos'], ascending=False)
    
    return df_nulls 
    
def Cat_plot_basic(plt, df, colUno, colDos):
    '''
        Función para graficar un catplot simple
        - lica.Cat_plot_basic(plt, nombre_de_tu_df, colUno, colDos)
    '''
    x = df[colUno]
    y = df[colDos]

    fig = plt.figure()
    ax = plt.axes()
    ax.scatter(x,y)
    
import pandas
def heat(plt, sns, pd, df):
    '''
    Funcion para mostrar el porcentaje de nulos que tienen las columnas
    Llamarla de la siguiente forma:
        - lica.heat(plt, sns, pd, nombre_del_df)
    '''
    pd = pandas
    from pandas.api.types import is_numeric_dtype
    
    columns = df.columns
    
    columnas = []
    
    for x in range (0, len(df.columns)):
        if is_numeric_dtype(df[str(df.columns[x])]) == False:
            columnas.append(df.columns[x])
    
    print('Se descartan las siguientes columnas porque son categoricas: ')
    print(' '.join(map(str, columnas)))
    
    corr = df.drop(columns = columnas).corr()
    plt.figure(figsize=(8,8))
    sns.heatmap(corr, cbar = True,  square = True, annot=True, fmt= '.2f',annot_kws={'size': 15},
           xticklabels= df.drop(columns = columnas).columns, 
           yticklabels= df.drop(columns = columnas).columns,
           cmap= 'coolwarm')
    plt.xticks(rotation = 45)
    plt.yticks(rotation = 45)
    plt.show()