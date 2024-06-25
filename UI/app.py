from flask import Flask, render_template, request
import csv

app = Flask(__name__)

def read_clusters_data(filename):
    clusters = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            clusters.append(row)
    return clusters

@app.route('/')
def index():
    cardType = ["Any", "Gold", "Platinum", "Silver", "Signature"]
    expType = ["Any", "Bills", "Food", "Entertainment", "Grocery", "Fuel", "Travel"]
    gender = ["Any", "Female", "Male"]
    monthName = ["Any", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    dayName = ["Any", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    cityTier = ["Any", "Tier-1", "Tier-2", "Tier-3"]
    
    return render_template('index.html', cardType=cardType, expType=expType, gender=gender, monthName=monthName, dayName=dayName, cityTier=cityTier)

@app.route('/results', methods=['POST'])
def results():
    card_type = request.form.get('cardType', 'Any')
    expense_type = request.form.get('expType', 'Any')
    gender = request.form.get('gender', 'Any')
    month = request.form.get('monthName', 'Any')
    day = request.form.get('dayName', 'Any')
    city_tier = request.form.get('cityTier', 'Any')
    
    # Read clusters data from CSV file
    clusters = read_clusters_data('clusters.csv')
    
    # Filter clusters based on user input
    filtered_clusters = []
    for cluster in clusters:
        if (card_type == "Any" or cluster[0] == card_type) and \
           (expense_type == "Any" or cluster[1] == expense_type) and \
           (gender == "Any" or cluster[2] == gender) and \
           (month == "Any" or cluster[3] == month) and \
           (day == "Any" or cluster[4] == day) and \
           (city_tier == "Any" or cluster[5] == city_tier):
            filtered_clusters.append(", ".join(cluster))
    
    return render_template('results.html', filtered_clusters=filtered_clusters)

if __name__ == '__main__':
    app.run(debug=True)
