import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file

    df = pd.read_csv('epa-sea-level.csv', index_col=0)

    fig, ax = plt.subplots(figsize=(10, 8))

    # Create scatter plot

    ax.scatter(
        x = df.index,
        y = df['CSIRO Adjusted Sea Level'],
        label = 'CSIRO Adjusted Sea Level'
    )

    # Create first line of best fit

    years_1880_2050 = pd.Series([year for year in range(df.index.min(), 2050 + 1)], dtype='float')

    slope1, intercept1, _, _, _ = linregress(
        x = df.index,
        y = df['CSIRO Adjusted Sea Level']
    )

    ax.plot(
        years_1880_2050,
        slope1 * years_1880_2050 + intercept1,
        color = 'red',
        label = 'First best fit line'
    )

    # Create second line of best fit

    years_2000_2050 = years_1880_2050[years_1880_2050 >= 2000]

    slope2, intercept2, _, _, _ = linregress(
        x = df[df.index >= 2000].index,
        y = df[df.index >= 2000]['CSIRO Adjusted Sea Level']
    )

    ax.plot(
        years_2000_2050,
        slope2 * years_2000_2050 + intercept2,
        color = 'orange',
        label = 'Second best fit line'
    )

    # Add labels and title

    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    plt.margins(0.1)

    ax.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()