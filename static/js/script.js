document.getElementById('team-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const team = document.getElementById('team').value;

    fetch('/team_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ team: team })
    })
    .then(response => response.json())
    .then(data => {
        const teamDataDiv = document.getElementById('team-data');
        if (data.error) {
            teamDataDiv.innerHTML = `Error: ${data.error}`;
        } else {
            teamDataDiv.innerHTML = `
                <p><strong>Team:</strong> ${data.team}</p>
                <p><strong>Matches Played:</strong> ${data.matches_played}</p>
                <p><strong>Years Played:</strong> ${data.years_played.join(', ')}</p>
                <p><strong>Matches Won:</strong> ${data.matches_won}</p>
                <p><strong>Total Goals:</strong> ${data.total_goals}</p>
            `;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('team-data').innerHTML = `Error fetching team data.`;
    });
});
