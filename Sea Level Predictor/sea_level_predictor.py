import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    reg1880 = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    slope1880 = reg1880.slope
    interc1880 = reg1880.intercept
    x1880 = pd.Series(range(1880, 2051))
    y1880 = interc1880 + x1880 * slope1880
    
    ax.plot(x1880.to_numpy(), y1880.to_numpy(), 'r')
    

    # Create second line of best fit
    reg2000 = linregress(x=df['Year'].loc[df['Year']>=2000], y=df['CSIRO Adjusted Sea Level'].loc[df['Year']>=2000])
    slope2000 = reg2000.slope
    interc2000 = reg2000.intercept
    x2000 = pd.Series(range(2000, 2051))
    y2000 = interc2000 + x2000 * slope2000
    
    ax.plot(x2000.to_numpy(), y2000.to_numpy(), 'r')

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()