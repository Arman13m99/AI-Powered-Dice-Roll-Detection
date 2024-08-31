import numpy as np
import plotly.graph_objects as go
import collections

def initialize_probabilities(mean=7, std_dev=1.5):
    sums = np.arange(2, 13)
    gaussian_probs = np.exp(-0.5 * ((sums - mean) / std_dev) ** 2)
    gaussian_probs /= gaussian_probs.sum()  # Normalize to sum to 1
    return {sum_value: prob for sum_value, prob in zip(sums, gaussian_probs)}

def plot_summed_distribution(summed_roll_cache):
    roll_counts = collections.Counter(summed_roll_cache)
    x = list(range(2, 13))  # Possible dice sums (2 to 12)
    y = [roll_counts[roll] for roll in x]

    fig = go.Figure(data=[go.Bar(x=x, y=y)])
    fig.update_layout(
        title='Dice Roll Distribution',
        xaxis_title='Dice Sum',
        yaxis_title='Frequency',
        xaxis=dict(tickmode='linear', dtick=1),
        width=2400,
        height=800
    )
    fig.show()

def plot_probability_distribution(probabilities):
    x = list(probabilities.keys())
    y = list(probabilities.values())

    fig = go.Figure(data=[go.Bar(x=x, y=y)])
    fig.update_layout(
        title='Real-Time Probability Distribution',
        xaxis_title='Dice Sum',
        yaxis_title='Probability',
        xaxis=dict(tickmode='linear', dtick=1),
        width=2400,
        height=800
    )
    fig.show()
