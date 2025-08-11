import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import seaborn as sns
df = pd.read_csv(r"C:/users/alire/downloads/compressed/archive/medical_examination.csv", sep = ',')
df['overweight'] = (df['weight']/((df['height']/100)**2)).apply(lambda x:1 if x>25 else 0)
df['cholesterol'] = df['cholesterol'].apply(lambda x:0 if x==1 else 1)
df['gluc'] = df['gluc'].apply(lambda x:0 if x==1 else 1)
def draw_cat_plot():
    df_cat = pd.melt(df,id_vars= ["cardio"], value_vars = ['cholesterol','gluc','smoke','alco','active','overweight'])
    df_cat['total'] = 1
    df_cat = df_cat.groupby(['cardio','variable','value'], as_index = False).count()
    print(df_cat)
    fig = sns.catplot(x = "variable", y = "total", data = df_cat, hue = "value", kind = "bar", col = "cardio").fig
    fig.savefig('catplot.png')
    return fig 
def draw_heat_map():
    df_heatmap = df[
    (df['ap_lo']<= df['ap_hi'])&
    (df['height']>= df['height'].quantile(0.025))&
    (df['height']<= df['height'].quantile(0.975))&
    (df['weight']>= df['weight'].quantile(0.025))&
    (df['weight']<= df['weight'].quantile(0.975))
    ]
    corr = df_heatmap.corr(method = "pearson",)
    mask = np.triu(corr)
    fig,ax = plt.subplots(figsize = (12,12))
    sns.heatmap(corr, linewidths = 1, annot = True, square = True, mask = mask, fmt = ".1f", center = 0.08, cbar_kws = {"shrink": 0.5})
    print(df_heatmap)
    print(corr)
    fig.savefig('heatmap.png')
    return fig 