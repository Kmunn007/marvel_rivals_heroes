import pandas as pd
import numpy as np

# Load the data
df = pd.read_csv("marvel_rivals_hot_list_season_6.csv")

# Convert Percents into Decimals
df['Pick Rate'] = df['Pick Rate (%)']/100
df['Win Rate'] = df['Win Rate (%)']/100

# Standardize the data
mean_role = df.groupby('Role')['Pick Rate'].mean()

df['role_mean_pick'] = (
    df.groupby('Role')['Pick Rate']
    .transform('mean')
)

df['pick_norm'] = df['Pick Rate'] / df['role_mean_pick']
df['pick_z'] = df.groupby('Role')['Pick Rate'].transform(
    lambda x: (x-x.mean())/x.std()
)
df['win_z'] = df.groupby('Role')['Win Rate'].transform(
    lambda x: (x-x.mean())/x.std()
)

#Calculate hero scores
pick_weight = 0.6
win_weight = 0.4

df['hero_score'] = (
    pick_weight * df['pick_z'] +
    win_weight  * df['win_z']
)

#Clean up columns for standardized sheet
columns_to_keep = [
    'Hero Name',
    'Role',
    'Rank',
    'Pick Rate',
    'Win Rate',
    'pick_norm',
    'pick_z',
    'win_z',
    'hero_score'
]

df_standardized = df[columns_to_keep].copy()
df_standardized.to_csv("marvel_rivals_standardized.csv", index = False)

#Create a tier list based on hero scores
def assign_tier(score):
    if score >= 1.0:
        return 'S'
    elif score >= 0.3:
        return 'A'
    elif score >= -0.3:
        return 'B'
    elif score >= -1.0:
        return 'C'
    else:
        return 'D'

df_standardized['tier'] = df_standardized['hero_score'].apply(assign_tier)

#Clean up and create tier list sheet
final_columns = [
    'Hero Name',
    'Role',
    'Rank',
    'Pick Rate',
    'Win Rate',
    'hero_score',
    'tier'
]

df_ranked = df_standardized.copy()
df_ranked[final_columns].to_csv('marvel_rivals_tier_list.csv', index = False)

