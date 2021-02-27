# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

import pandas as pd
import os

import test_data as ta

#---------------------------------------------------------------------------------
"""
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,
                assets_folder= os.getcwd(),
                assets_url_path='/',
                external_stylesheets=external_stylesheets)

server = app.server

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
"""
#-----------------------------------------------------------------------------------

file_name = "test_data.pkl"


df, descripcion_dataframe, index_data_null = ta.analisis_serie_tiempo(file_name)


print(df)

fig_serie_tiempo = go.Figure()

fig_serie_tiempo.add_trace(
                    go.Scatter(
                        x=df['Timestamps'], y=df['Values'],
                        name='Values',
                        marker=dict
                                  (
                                    color='rgb(0, 128, 0)'
                                  ),
                              )
                    )

fig_serie_tiempo.add_trace(
                    go.Scatter(
                        x=[df['Timestamps'][index_data_null]], y=[df['Values'][index_data_null]],
                        text=["Dato Adicionado"],
                        textposition="bottom center",
                        mode='markers',
                        name='Values add',                        
                        marker=dict
                                  ( size=20,
                                    color='rgb(128, 0, 0)'
                                  ),
                              )
                    )

fig_serie_tiempo.update_traces(textposition='top center')

fig_serie_tiempo.update_xaxes(rangeslider_visible=True)
fig_serie_tiempo.update_layout(title='Serie de tiempo: test_data',
                        xaxis_title='Timestamps',
                        yaxis_title='Values',
                        plot_bgcolor='white',
                        #grid=True,
                        #showticklabels=True,
                        showlegend=True,
                        legend=dict(x=0, y=1.0),
                        #margin=dict(l=40, r=0, t=40, b=30)
                        )

indices = descripcion_dataframe.index

print(indices)

fig_table_data = go.Figure(data=[go.Table(header=dict(values=['Estadisticos', 'Values']),
                 cells=dict(values=[ indices,descripcion_dataframe['Values']]))
                     ])

#----------------------------------------------

app = dash.Dash()
server = app.server

app.layout = html.Div([
    html.H1('Análisis Serie de Tiempo'),
    dcc.Graph(figure=fig_serie_tiempo),
    html.H3('En la serie de tiempo, punto rojo corresponde al dato adicionado'),
    html.H2('Descripción del dataframe: Serie de Teimpo'),
    dcc.Graph(figure=fig_table_data, style={'height':'110vh', 'width':'100vw'}),

])

print('el servidor está ok !!!')

if __name__ == '__main__':
    app.run_server(debug=True)
    #app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
