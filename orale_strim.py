import pandas as pd
import numpy as np
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy.stats import trim_mean, pearsonr
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta


def plotN():  # normalizado
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    x = np.linspace(0, 5, 100)
    fontsize = 10

    fig.add_trace(go.Scatter(name='Example', mode='lines', x=x, y=f(x), line=dict(color='cyan', width=3)),
                  secondary_y=False, )

    fig.update_layout(font=dict(family="sans-serif", size=fontsize, color="black"), template="plotly_white",
                      legend_font_size=14, legend_title_font_size=fontsize)
    fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.1, xanchor="right", x=0.8))
    fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)', 'paper_bgcolor': 'rgba(0,0,0,0)'})

    fig.update_layout(autosize=False, width=450, height=250, margin=dict(l=0, r=0, b=10, t=10, pad=4),
                      yaxis=dict(title='N/PMMoV'))  # ,xaxis=dict(title="Date"))
    fig.update_layout(font_family="Arial", title_font_family="Arial")
    fig.layout.showlegend = True
    return fig


def f(x):
    return x**2

st.sidebar.header('SELECT A LOCATION')
list_cities=['Davis', 'Modesto']
city = st.sidebar.selectbox('', list_cities)

st.sidebar.subheader('Subsewershed')
plot_loc = st.sidebar.checkbox("Emerald Lift Station", value=False)

col1, col2 = st.sidebar.columns([1, 0.51])
smooth = col1.selectbox('Smoothing function', ['Trimmed average', 'Moving average', 'None'], index=1)

if smooth != 'None':
    size_window = col2.selectbox('Size window', [5, 7, 10, 14], index=1)


fig1=plotN()

col1, col2= st.columns(2)
col1.plotly_chart(fig1, use_container_width=True)
