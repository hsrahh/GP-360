import pandas as pd

# Advanced sample FIFA World Cup data
data = {
    'year': [2018, 2018, 2014, 2014, 2010, 2010, 2006, 2006, 2002, 2002],
    'team': ['France', 'Croatia', 'Germany', 'Argentina', 'Spain', 'Netherlands', 'Italy', 'France', 'Brazil', 'Germany'],
    'opponent': ['Croatia', 'France', 'Argentina', 'Germany', 'Netherlands', 'Spain', 'France', 'Italy', 'Germany', 'Brazil'],
    'goals_scored': [4, 2, 1, 0, 1, 0, 1, 1, 2, 0],
    'goals_conceded': [2, 4, 0, 1, 0, 1, 0, 1, 0, 2],
    'possession': [54, 46, 60, 40, 55, 45, 50, 50, 53, 47],
    'shots_on_target': [6, 4, 7, 3, 6, 4, 5, 5, 8, 2],
    'corners': [7, 3, 8, 2, 5, 3, 4, 6, 5, 4],
    'result': ['win', 'loss', 'win', 'loss', 'win', 'loss', 'win', 'loss', 'win', 'loss']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV file
file_path = 'fifa_world_cup_data_advanced.csv'
df.to_csv(file_path, index=False, encoding='utf-8')

print(f"CSV file saved to: {file_path}")
