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

# Step 4: Create traces for max and min amplitudes
max_trace = go.Scatter(x=data.index, y=max_amplitude, mode='lines', name='Max Amplitude', line=dict(color='red'))
min_trace = go.Scatter(x=data.index, y=min_amplitude, mode='lines', name='Min Amplitude', line=dict(color='blue'))

# Step 5: Plotting with Plotly
fig = go.Figure([max_trace, min_trace])

# Step 6: Customize Plot Layout
fig.update_layout(title='Amplitude vs. Sample Data', xaxis_title='Sample Data', yaxis_title='Amplitude')

# Step 7: Show Plot (Interactive)
fig.show()
