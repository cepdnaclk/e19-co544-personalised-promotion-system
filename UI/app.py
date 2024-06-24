import tkinter as tk
from tkinter import ttk
import csv

def read_clusters_data(filename):
    clusters = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            clusters.append(row)
    return clusters

def update_output():
    # Get selected values from all dropdowns
    card_type = cardTypeDropDown.get()
    expense_type = expTypeDropDown.get()
    gender = genderDropDown.get()
    month = monthNameDropDown.get()
    day = dayNameDropDown.get()
    city_tier = cityTierDropDown.get()
    
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
    
    # Prepare output text
    output_entry.delete(1.0, tk.END)  # Clear previous content
    output_entry.insert(tk.END, "\n".join(filtered_clusters))

# Create main tkinter window
root = tk.Tk()
root.title("Promotions Predictor")

root.geometry("700x400")

# Define variables for dropdown selections
cardType = ["Any", "Gold", "Platinum", "Silver", "Signature"]
expType = ["Any", "Bills", "Food", "Entertainment", "Grocery", "Fuel", "Travel"]
gender = ["Any", "Female", "Male"]
monthName = ["Any", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
dayName = ["Any", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
cityTier = ["Any", "Tier-1", "Tier-2", "Tier-3"]

dropdown_style = ttk.Style()
dropdown_style.configure('Dropdown.TCombobox', width=20, font=('Helvetica', 12))

# Create dropdowns
cardTypeDropDown = ttk.Combobox(root, values=cardType, state="readonly")
expTypeDropDown = ttk.Combobox(root, values=expType, state="readonly")
genderDropDown = ttk.Combobox(root, values=gender, state="readonly")
monthNameDropDown = ttk.Combobox(root, values=monthName, state="readonly")
dayNameDropDown = ttk.Combobox(root, values=dayName, state="readonly")
cityTierDropDown = ttk.Combobox(root, values=cityTier, state="readonly")

# Position dropdowns in the window
cardTypeDropDown.grid(row=0, column=1, padx=10, pady=5)
expTypeDropDown.grid(row=1, column=1, padx=10, pady=5)
genderDropDown.grid(row=2, column=1, padx=10, pady=5)
monthNameDropDown.grid(row=3, column=1, padx=10, pady=5)
dayNameDropDown.grid(row=4, column=1, padx=10, pady=5)
cityTierDropDown.grid(row=5, column=1, padx=10, pady=5)

# Create labels for dropdowns
label1 = tk.Label(root, text="Card Type:")
label2 = tk.Label(root, text="Expense Type:")
label3 = tk.Label(root, text="Gender:")
label4 = tk.Label(root, text="Month:")
label5 = tk.Label(root, text="Day:")
label6 = tk.Label(root, text="City Tier:")

# Position labels in the window
label1.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
label2.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
label3.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
label4.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
label5.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
label6.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)

# Create output text area
output_label = tk.Label(root, text="Promotion:")
output_label.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
output_entry = tk.Text(root, height=10, width=100, wrap=tk.WORD)
output_entry.grid(row=6, column=1, columnspan=2, padx=10, pady=5)

# Create button to update output
update_button = tk.Button(root, text="Check", command=update_output)
update_button.grid(row=7, columnspan=3, pady=10)

# Run the tkinter main loop
root.mainloop()
