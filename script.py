import pandas as pd
import plotly.graph_objs as go

# Step 1: Read Data from Excel
data = pd.read_excel('test_with cell_13.02.24.pcus 1 hour_exported_S0_C1.xlsx')

# Step 2: Data Processing
# Convert non-numeric values to NaN
data_numeric = data.apply(pd.to_numeric, errors='coerce')

# Step 3: Calculate maximum and minimum amplitudes
max_amplitude = data_numeric.max()
min_amplitude = data_numeric.min()

# Step 4: Plotting with Plotly
fig = go.Figure()

for column in data_numeric.columns:
    fig.add_trace(go.Scatter(x=data.index, y=data_numeric[column], mode='lines', name=column))

    # Add annotations for maximum and minimum amplitudes
    max_idx = data_numeric[column].idxmax()
    min_idx = data_numeric[column].idxmin()
    fig.add_annotation(x=max_idx, y=max_amplitude[column], text=f'Max: {max_amplitude[column]:.2f}', showarrow=True, arrowhead=1)
    fig.add_annotation(x=min_idx, y=min_amplitude[column], text=f'Min: {min_amplitude[column]:.2f}', showarrow=True, arrowhead=1)

# Step 5: Customize Plot Layout
fig.update_layout(title='Amplitude vs. Time', xaxis_title='Time', yaxis_title='Amplitude')

# Step 6: Show Plot (Interactive)
fig.show()
