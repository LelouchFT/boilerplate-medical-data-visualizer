import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = df.apply(lambda row :  1 if (row['weight']/(pow(row['height']/100 , 2))) > 25 else 0,axis = 1)

# 3
df['cholesterol'] = df['cholesterol'].apply(lambda x : 1 if x >1 else 0)
df['gluc'] = df['gluc'].apply(lambda x : 1 if x >1 else 0)

# 4

def draw_cat_plot():
    # 5
    df_cat  = pd.melt(df,id_vars= ['cardio'],value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'],var_name= 'variable',value_name ='value')
    
    
    
    
    # 6
    df_cat = df_cat.groupby(['cardio','variable','value']).size().reset_index(name='total')
    

    # 7



    # 8
    fig = sns.catplot(data= df_cat,x='variable',y='total',kind='bar',col ='cardio',hue ='value').fig


    # 9
    fig.savefig('catplot.png')
    plt.show()
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
    	(df['height'] >= df['height'].quantile(0.025)) &
  	  (df['height'] <= df['height'].quantile(0.975)) &
  	  (df['ap_lo'] <=df['ap_hi']) &
	    (df['weight'] >= df['weight'].quantile(0.025)) &
  	  (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr,dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(15, 15))

    # 15
    sns.heatmap(
    	corr,
    #	square = True,
    	#center = 0,
    	mask = mask,
    	annot= True,
    	fmt =".1f",
    #	cbar_kws={"shrink": 0.4}
    )
    plt.show()
   



    # 16
    fig.savefig('heatmap.png')
    return fig
    
draw_heat_map()
