import pandas as pd
import numpy as np
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy.stats import trim_mean, pearsonr, gamma
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta
st.set_page_config(layout="wide", initial_sidebar_state="auto", page_title=None, page_icon=None)

fontsize=14
def plotgamma(xmin, xmax, alpha,beta):  # normalizado
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    xpri = np.linspace(xmin, xmax, 400)
    fig.add_trace(go.Scatter(name='Example', mode='lines', x=xpri, y=gamma.pdf(xpri, alpha, scale=1 / beta), line=dict(color='black', width=3)),
                  secondary_y=False, )

    fig.update_layout(font=dict(family="sans-serif", size=fontsize, color="black"), template="plotly_white",
                      legend_font_size=14, legend_title_font_size=fontsize)
    fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.1, xanchor="right", x=0.8))
    fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)', 'paper_bgcolor': 'rgba(0,0,0,0)'})

    fig.update_layout(autosize=False, width=450, height=250, margin=dict(l=0, r=0, b=10, t=10, pad=4),
                      yaxis=dict(title='f(x)'))  # ,xaxis=dict(title="Date"))
    fig.update_layout(font_family="Arial", title_font_family="Arial")
    fig.layout.showlegend = True
    return fig

distributions={'Gamma': r'f(x,\alpha,\beta)=\frac{\beta^\alpha x^{\alpha-1}e^{-\beta x}}{\Gamma(\alpha)}',
               'Beta': r'f(x,a,b)=\frac{\Gamma(a+b) x^{a-1}(1-x)^{b-1}}{\Gamma(a)\Gamma(b)}'}
st.sidebar.header('SELECT A DISTRIBUTION')
list_distri=['Gamma', 'Beta', 'Normal', 'Poisson']
city = st.sidebar.selectbox('', list_distri)

st.header(city + ' distribution')
st.write('The probability density function')
st.write('gama: pyhton scale=1/beta')

#st.latex(r'f(x,\alpha,\beta)=\frac{\beta^\alpha x^{\alpha-1}e^{-\beta x}}{\Gamma(\alpha)}')
st.latex(distributions[city])
#st.sidebar.subheader('Subsewershed')
#plot_loc = st.sidebar.checkbox("Emerald Lift Station", value=False)

col1, col2 = st.columns([1, 0.3])
#smooth = col1.selectbox('Smoothing function', ['Trimmed average', 'Moving average', 'None'], index=1)

#if smooth != 'None':
#    size_window = col2.selectbox('Size window', [5, 7, 10, 14], index=1)

xmin, xmax = col1.slider('X', min_value=0, max_value=100, value=(0, 50))

#alpha = col2.slider('alpha', min_value=0, max_value=100, value=20)
col2.write('Parameters')
if city=='Gamma':
    alpha = col2.number_input('alpha', min_value=0.00000000, value=1.00000000, step=0.00000001, format="%f")
    beta = col2.number_input('beta', min_value=0.00000000, value=1.00000000, step=0.00000001, format="%f")
    fig1 = plotgamma(xmin, xmax, alpha, beta)
elif city=='Beta':
    a = col2.number_input('a', min_value=0.00000000, value=1.00000000, step=0.00000001, format="%f")
    b = col2.number_input('b', min_value=0.00000000, value=1.00000000, step=0.00000001, format="%f")
    fig1 = plotgamma(xmin, xmax, a, b)

col1.plotly_chart(fig1, use_container_width=True)
