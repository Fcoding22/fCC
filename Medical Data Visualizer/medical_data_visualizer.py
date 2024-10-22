import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = df['overweight'] = df['weight']/(df['height']/100)**2 < 25

# 3
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1).astype('category')
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1).astype('category')

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars = ['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])


    # 6
    #df_cat = None
    

    # 7
    fig = sns.catplot(data=df_cat, kind="count",  x="variable", hue="value", col="cardio")
    fig.set_axis_labels("variable", "total")


    # 8
    fig = fig.figure


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(corr)



    # 14
    fig, ax = plt.subplots(figsize=(10, 10))

    # 15
    fig = sns.heatmap(data=corr, mask=mask, annot = round(corr,1))
    fig = fig.figure


    # 16
    fig.savefig('heatmap.png')
    return fig
