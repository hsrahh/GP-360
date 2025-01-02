from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Load data
data_file_path = os.path.join('data', 'fifa_data3.csv')
if os.path.exists(data_file_path):
    data = pd.read_csv(data_file_path)
else:
    raise FileNotFoundError(f"File not found: {data_file_path}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/team_data', methods=['POST'])
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
        matches_won = int(team_data[team_data['outcome'] == 1].shape[0])  # Convert to native int
        total_goals = int(team_data['goals'].sum())  # Convert to native int

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
