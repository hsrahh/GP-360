from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Create FIFA World Cup data and save it to a CSV file
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

# Save the data to a CSV file
file_path = 'fifa_world_cup_data_advanced.csv'
df = pd.DataFrame(data)
df.to_csv(file_path, index=False, encoding='utf-8')
print(f"CSV file saved to: {file_path}")

# Load the data from the CSV file
if os.path.exists(file_path):
    data = pd.read_csv(file_path)
else:
    raise FileNotFoundError(f"File not found: {file_path}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/team_data', methods=['POST'])
def team_data():
    try:
        # Parse JSON request
        team = request.json.get('team', None)
        if not team:
            return jsonify({'error': 'Team not provided'}), 400

        # Filter data for the team
        team_data = data[data['team'] == team]
        if team_data.empty:
            return jsonify({'error': 'Team not found'}), 404

        # Calculate metrics
        matches_played = int(team_data.shape[0])  # Convert to native int
        years_played = team_data['year'].unique().tolist()  # Convert to list
        matches_won = int(team_data[team_data['result'] == 'win'].shape[0])  # Convert to native int
        total_goals = int(team_data['goals_scored'].sum())  # Convert to native int

        # Return JSON response
        return jsonify({
            'team': team,
            'matches_played': matches_played,
            'years_played': years_played,
            'matches_won': matches_won,
            'total_goals': total_goals
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
