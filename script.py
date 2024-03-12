import pandas as pd
import plotly.graph_objs as go

def get_alphabet_labels(n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    labels = []
    for i in range(n):
        q, r = divmod(i, len(alphabet))
        label = alphabet[r]
        while q > 0:
            q, r = divmod(q - 1, len(alphabet))
            label = alphabet[r] + label
        labels.append(label)
    return labels

data = pd.read_excel('test_with cell_13.02.24.pcus 1 hour_exported_S0_C1.xlsx')

data_numeric = data.apply(pd.to_numeric, errors='coerce')

max_amplitude = data_numeric.max()
min_amplitude = data_numeric.min()
mean_amplitude = data_numeric.mean()

max_trace = go.Scatter(x=data.index, y=max_amplitude, mode='lines', name='Max Amplitude', line=dict(color='red'))
min_trace = go.Scatter(x=data.index, y=min_amplitude, mode='lines', name='Min Amplitude', line=dict(color='blue'))
mean_trace = go.Scatter(x=data.index, y=mean_amplitude, mode='lines', name='Mean Amplitude', line=dict(color='green'))

max_marker = go.Scatter(x=[max_amplitude.idxmax()], y=[max_amplitude.max()], mode='markers', name='Max Value', marker=dict(color='red', size=10))
min_marker = go.Scatter(x=[min_amplitude.idxmin()], y=[min_amplitude.min()], mode='markers', name='Min Value', marker=dict(color='blue', size=10))
mean_marker = go.Scatter(x=[mean_amplitude.idxmin()], y=[mean_amplitude.min()], mode='markers', name='Mean Value', marker=dict(color='green', size=10))

fig = go.Figure([max_trace, min_trace, mean_trace, max_marker, min_marker, mean_marker])

fig.update_layout(title='Amplitude vs. Sample Data', xaxis_title='Sample Data', yaxis_title='Amplitude')

alphabet_labels = get_alphabet_labels(len(data.index))
fig.update_xaxes(tickvals=data.index, ticktext=alphabet_labels)

fig.show()
