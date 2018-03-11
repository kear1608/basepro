import pandas as pd
import numpy as np
import plotly as py
import plotly.graph_objs as go



# Import data from csv
df = pd.read_csv('/home/eh/Documents/Base de Programmation/Rapport Tri Rapide/QuickSort_*10.csv')
df.head()

trace1 = go.Scatter(
                    x=df['n'], y=df['time'], # Data
                    mode='lines', name='QS_AVG' # Additional options
                   )

trace2 = go.Scatter(
                    x=df['n'], y=df['time(wc)'], # Data
                    mode='lines', name='QS_WC' # Additional options
                   )


layout = go.Layout(title='Quick Sort Facteur 10',
                   plot_bgcolor='rgb(230, 230,230)')

fig = go.Figure(data=[trace1, trace2], layout=layout)

# Plot data in the notebook

py.offline.plot(fig, filename='basic-line')
