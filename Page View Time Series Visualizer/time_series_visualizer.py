import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=[0])

# Clean data
df = df.loc[(df['value']>=df['value'].quantile(0.025)) & (df['value']<= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(14, 6))
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.plot(df)
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby(df.index.to_period('M')).mean()
    df_bar['year'] = df_bar['value'].index.year
    df_bar['mint'] = df_bar['value'].index.month
    
    piv = df_bar.pivot(columns='mint', values='value', index='year')
    df_bar_piv = pd.DataFrame(
        columns = ['Years', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',  'December']
    )
    df_bar_piv['Years'] = pd.Series(['2016', '2017', '2018', '2019'])
    df_bar_piv.iloc[:,1:] = piv.iloc[:,:]
    
    # Draw bar plot
    
    ax = df_bar_piv.plot(x='Years', kind='bar', stacked=False, figsize=(14,6),
                ylabel = 'Average Page Views'
    )
    fig = ax.get_figure()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    
    df_box.rename(columns={"value": "Page Views", 'year': 'Year', 'month': 'Month'}, inplace=True)
    order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    # Draw box plots (using Seaborn)

    fig, (ax1, ax2) = plt.subplots(figsize=(15,7), ncols=2)
    sns.boxplot(data=df_box, x='Year', y='Page Views', ax=ax1, palette='Set2')
    ax1.set_title('Year-wise Box Plot (Trend)')
    sns.boxplot(data=df_box, x='Month', y='Page Views', ax=ax2, order=order, palette='Set2')
    ax2.set_title('Month-wise Box Plot (Seasonality)')


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
