import tkinter as tk
import webbrowser

# Create the main window
a = tk.Tk()
a.title("Enquiry")

# Create the label and entry for the course
label = tk.Label(a, text="Course:", font=("Times New Roman", 20))
entry = tk.Entry(a, font=("Times New Roman", 20))

# Create the label, variable, options, and dropdown menu for the information source
s_label = tk.Label(a, text="Where did you hear about us?", font=("Times New Roman", 20))
s_var = tk.StringVar(a)
s_options = ["YouTube", "Reddit"]
s_dropdown = tk.OptionMenu(a, s_var, *s_options)
s_dropdown.config(font=("Times New Roman", 20))  # Set font size for dropdown menu

# Function to handle form submission
def form():
    # Get the input values
    course = entry.get()
    source = s_var.get()

    # Define the base URLs based on the selected source
    if source == "YouTube":
        base_url = "https://www.youtube.com/results?search_query="
    elif source == "Reddit":
        base_url = "https://www.reddit.com/search/?q="
    
        
# Construct the search query URL
    query = course.replace(" ", "+")
    url = base_url + query

# Open the URL in the default web browser
    webbrowser.open(url)

# Create the button for form submission
button = tk.Button(a, text="Search", command=form, font=("Times New Roman", 20))


# Grid layout for the widgets
label.grid(row=0, column=0)
entry.grid(row=0, column=1)
s_label.grid(row=1, column=0)
s_dropdown.grid(row=1, column=1)
button.grid(row=2, column=0, columnspan=2)

# Start the main event loop
a.mainloop()
