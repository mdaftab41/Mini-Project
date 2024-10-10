# import tkinter as tk
# from tkinter import filedialog, messagebox
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# # Global variable for the dataset
# dataset = None

# def load_dataset():
#     global dataset
#     filepath = filedialog.askopenfilename(title="Select a CSV file", filetypes=(("CSV files", "*.csv"),))
#     if filepath:
#         try:
#             dataset = pd.read_csv(filepath)
#             messagebox.showinfo("Success", "Dataset loaded successfully!")
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to load dataset: {e}")

# def show_state_vs_crime():
#     try:
#         df_sum_by_state = dataset.groupby('STATE/UT')['TOTAL IPC CRIMES'].sum().reset_index()
#         states = df_sum_by_state['STATE/UT']
#         total_crime = df_sum_by_state['TOTAL IPC CRIMES']
        
#         fig, ax = plt.subplots()
#         ax.bar(states, total_crime)
#         plt.xticks(rotation=90, ha='right')
#         plt.title('State vs Total Crime Over 10 Years')
#         plt.xlabel('State/UT')
#         plt.ylabel('Total IPC Crimes')
#         plt.tight_layout()
#         plt.show()
#     except Exception as e:
#         messagebox.showerror("Error", f"Failed to plot data: {e}")

# def show_crime_type_vs_rate():
#     try:
#         sum_column = dataset.sum(axis=0)
#         crime_rates = sum_column[2:30]
#         crimes = dataset.columns.values[2:30]

#         fig, ax = plt.subplots()
#         ax.bar(crimes, crime_rates)
#         plt.xticks(rotation=90, ha='right')
#         plt.title('Type of Crime vs Rate of Crime')
#         plt.xlabel('Crime Type')
#         plt.ylabel('Total Occurrences')
#         plt.tight_layout()
#         plt.show()
#     except Exception as e:
#         messagebox.showerror("Error", f"Failed to generate crime rate graph: {e}")

# def show_crime_rate_pie_chart():
#     try:
#         df_sum_by_state = dataset.groupby('STATE/UT')['TOTAL IPC CRIMES'].sum().reset_index()
#         states = df_sum_by_state['STATE/UT']
#         total_crime = df_sum_by_state['TOTAL IPC CRIMES']

#         colors = plt.cm.tab20.colors  # Use a colormap for more colors
#         plt.figure(figsize=(8,8))
#         plt.pie(total_crime, labels=states, colors=colors, autopct='%1.1f%%', startangle=140)
#         plt.title('Pie Chart of Crime Rate per State')
#         plt.axis('equal')
#         plt.tight_layout()
#         plt.show()
#     except Exception as e:
#         messagebox.showerror("Error", f"Failed to generate pie chart: {e}")

# def show_state_safety_classification():
#     try:
#         # Assuming y_kmeans is available from previous clustering
#         from sklearn.cluster import KMeans

#         # Prepare data for clustering
#         total_crime_by_state = dataset.groupby('STATE/UT')['TOTAL IPC CRIMES'].sum().reset_index()
#         crime_data = total_crime_by_state['TOTAL IPC CRIMES'].values.reshape(-1,1)

#         # Perform KMeans clustering
#         kmeans = KMeans(n_clusters=2, random_state=42)
#         y_kmeans = kmeans.fit_predict(crime_data)

#         # Add classification to the dataframe
#         total_crime_by_state['Safety Classification'] = y_kmeans

#         # Plotting the classification
#         fig, ax = plt.subplots()
#         bars = ax.bar(total_crime_by_state['STATE/UT'], total_crime_by_state['Safety Classification'])
#         plt.xticks(rotation=90, ha='right')
#         plt.title('State Safety Classification (0: Safe, 1: Unsafe)')
#         plt.xlabel('State/UT')
#         plt.ylabel('Classification')
#         plt.tight_layout()
#         plt.show()
#     except Exception as e:
#         messagebox.showerror("Error", f"Failed to classify states: {e}")

# def show_crime_trend_per_state():
#     try:
#         # Get list of unique states
#         states = dataset['STATE/UT'].unique()
#         years = sorted(dataset['YEAR'].unique())

#         for state in states:
#             state_data = dataset[dataset['STATE/UT'] == state]
#             total_crime_per_year = state_data.groupby('YEAR')['TOTAL IPC CRIMES'].sum()

#             plt.figure()
#             plt.plot(years, [total_crime_per_year.get(year, 0) for year in years], marker='o')
#             plt.title(f'Total IPC Crimes Over Years in {state}')
#             plt.xlabel('Year')
#             plt.ylabel('Total IPC Crimes')
#             plt.xticks(years, rotation=45)
#             plt.tight_layout()
#             plt.show()
#     except Exception as e:
#         messagebox.showerror("Error", f"Failed to plot crime trends: {e}")

# # Tkinter GUI window setup
#  # Tkinter GUI window setup
# root = tk.Tk()
# root.title("Crime Analysis Tool")

# # Variable to keep track of fullscreen status
# is_fullscreen = True

# # Function to toggle fullscreen
# def toggle_fullscreen(event=None):
#     global is_fullscreen
#     is_fullscreen = not is_fullscreen  # Toggle the boolean flag
#     root.attributes('-fullscreen', is_fullscreen)

# # Function to exit fullscreen (with the Esc key)
# def exit_fullscreen(event=None):
#     global is_fullscreen
#     is_fullscreen = False
#     root.attributes('-fullscreen', False)

# # Make the window fullscreen initially
# root.attributes('-fullscreen', True)

# # Bind the Esc key to exit fullscreen
# root.bind("<Escape>", exit_fullscreen)

# # Create a Frame to hold the buttons and align them horizontally
# button_frame = tk.Frame(root)
# button_frame.pack(side='top', fill='x', pady=10)  # Align at the top, full width

# # Adding Buttons in a single line (like a navigation bar)
# load_button = tk.Button(button_frame, text="Load Dataset", command=load_dataset)
# load_button.pack(side='left', padx=5)

# plot_button = tk.Button(button_frame, text="State vs Total Crime", command=show_state_vs_crime)
# plot_button.pack(side='left', padx=5)

# crime_type_button = tk.Button(button_frame, text="Crime Type vs Rate", command=show_crime_type_vs_rate)
# crime_type_button.pack(side='left', padx=5)

# pie_chart_button = tk.Button(button_frame, text="Pie Chart of Crime Rate", command=show_crime_rate_pie_chart)
# pie_chart_button.pack(side='left', padx=5)

# classification_button = tk.Button(button_frame, text="State Safety Classification", command=show_state_safety_classification)
# classification_button.pack(side='left', padx=5)

# trend_button = tk.Button(button_frame, text="Crime Trend per State", command=show_crime_trend_per_state)
# trend_button.pack(side='left', padx=5)

# # Add a button to toggle fullscreen
# toggle_button = tk.Button(button_frame, text="Toggle Fullscreen", command=toggle_fullscreen)
# toggle_button.pack(side='left', padx=5)

# root.mainloop()




















# import tkinter as tk
# from tkinter import filedialog, messagebox
# from PIL import Image, ImageTk  # Importing Pillow for image handling
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import requests
# from io import BytesIO
# from sklearn.cluster import KMeans

# # Global variable for the dataset and for active button
# dataset = None
# active_button = None  # To track the currently active button

# # Function to load the image
# def load_criminal_image(image_path):
#     try:
#         # Load and resize the image
#         img = Image.open(image_path)
#         img = img.resize((200, 200), Image.LANCZOS)  # Resize image to fit the label
#         img = ImageTk.PhotoImage(img)
        
#         # Create a label to display the image
#         img_label = tk.Label(root, image=img)
#         img_label.image = img  # Keep a reference to avoid garbage collection
#         img_label.pack(pady=10)  # Add some padding around the image
#     except Exception as e:
#         messagebox.showerror("Error", f"Failed to load image: {e}")

# def load_dataset():
#     global dataset
#     filepath = filedialog.askopenfilename(title="Select a CSV file", filetypes=(("CSV files", "*.csv"),))
#     if filepath:
#         try:
#             dataset = pd.read_csv(filepath)
#             messagebox.showinfo("Success", "Dataset loaded successfully!")
#             load_criminal_image("criminal.png")  # Load the criminal image after dataset is loaded
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to load dataset: {e}")
#     set_active_button(load_button)

# def show_state_vs_crime():
#     try:
#         df_sum_by_state = dataset.groupby('STATE/UT')['TOTAL IPC CRIMES'].sum().reset_index()
#         states = df_sum_by_state['STATE/UT']
#         total_crime = df_sum_by_state['TOTAL IPC CRIMES']
        
#         fig, ax = plt.subplots()
#         ax.bar(states, total_crime)
#         plt.xticks(rotation=90, ha='right')
#         plt.title('State vs Total Crime Over 10 Years')
#         plt.xlabel('State/UT')
#         plt.ylabel('Total IPC Crimes')
#         plt.tight_layout()
#         plt.show()
#     except Exception as e:
#         messagebox.showerror("Error", f"Failed to plot data: {e}")
#     set_active_button(plot_button)

# def show_crime_type_vs_rate():
#     try:
#         sum_column = dataset.sum(axis=0)
#         crime_rates = sum_column[2:30]
#         crimes = dataset.columns.values[2:30]

#         fig, ax = plt.subplots()
#         ax.bar(crimes, crime_rates)
#         plt.xticks(rotation=90, ha='right')
#         plt.title('Type of Crime vs Rate of Crime')
#         plt.xlabel('Crime Type')
#         plt.ylabel('Total Occurrences')
#         plt.tight_layout()
#         plt.show()
#     except Exception as e:
#         messagebox.showerror("Error", f"Failed to generate crime rate graph: {e}")
#     set_active_button(crime_type_button)

# def show_crime_rate_pie_chart():
#     try:
#         df_sum_by_state = dataset.groupby('STATE/UT')['TOTAL IPC CRIMES'].sum().reset_index()
#         states = df_sum_by_state['STATE/UT']
#         total_crime = df_sum_by_state['TOTAL IPC CRIMES']

#         colors = plt.cm.tab20.colors  # Use a colormap for more colors
#         plt.figure(figsize=(8,8))
#         plt.pie(total_crime, labels=states, colors=colors, autopct='%1.1f%%', startangle=140)
#         plt.title('Pie Chart of Crime Rate per State')
#         plt.axis('equal')
#         plt.tight_layout()
#         plt.show()
#     except Exception as e:
#         messagebox.showerror("Error", f"Failed to generate pie chart: {e}")
#     set_active_button(pie_chart_button)

# def show_state_safety_classification():
#     try:
#         total_crime_by_state = dataset.groupby('STATE/UT')['TOTAL IPC CRIMES'].sum().reset_index()
#         crime_data = total_crime_by_state['TOTAL IPC CRIMES'].values.reshape(-1,1)
#         kmeans = KMeans(n_clusters=2, random_state=42)
#         y_kmeans = kmeans.fit_predict(crime_data)
#         total_crime_by_state['Safety Classification'] = y_kmeans
#         fig, ax = plt.subplots()
#         ax.bar(total_crime_by_state['STATE/UT'], total_crime_by_state['Safety Classification'])
#         plt.xticks(rotation=90, ha='right')
#         plt.title('State Safety Classification (0: Safe, 1: Unsafe)')
#         plt.xlabel('State/UT')
#         plt.ylabel('Classification')
#         plt.tight_layout()
#         plt.show()
#     except Exception as e:
#         messagebox.showerror("Error", f"Failed to classify states: {e}")
#     set_active_button(classification_button)

# def show_crime_trend_per_state():
#     try:
#         states = dataset['STATE/UT'].unique()
#         years = sorted(dataset['YEAR'].unique())

#         for state in states:
#             state_data = dataset[dataset['STATE/UT'] == state]
#             total_crime_per_year = state_data.groupby('YEAR')['TOTAL IPC CRIMES'].sum()

#             plt.figure()
#             plt.plot(years, [total_crime_per_year.get(year, 0) for year in years], marker='o')
#             plt.title(f'Total IPC Crimes Over Years in {state}')
#             plt.xlabel('Year')
#             plt.ylabel('Total IPC Crimes')
#             plt.xticks(years, rotation=45)
#             plt.tight_layout()
#             plt.show()
#     except Exception as e:
#         messagebox.showerror("Error", f"Failed to plot crime trends: {e}")
#     set_active_button(trend_button)

# # Function to set active button and change its color
# def set_active_button(button):
#     global active_button
#     if active_button:
#         active_button.config(bg="SystemButtonFace")  # Reset previous button to default color
#     button.config(bg="red")  # Set new active button color to red
#     active_button = button  # Update active button

# # Tkinter GUI window setup
# root = tk.Tk()
# root.title("Crime Analysis Tool")

# # Variable to keep track of fullscreen status
# is_fullscreen = True

# # Function to toggle fullscreen
# def toggle_fullscreen(event=None):
#     global is_fullscreen
#     is_fullscreen = not is_fullscreen  # Toggle the boolean flag
#     root.attributes('-fullscreen', is_fullscreen)

# # Function to exit fullscreen (with the Esc key)
# def exit_fullscreen(event=None):
#     global is_fullscreen
#     is_fullscreen = False
#     root.attributes('-fullscreen', False)

# # Make the window fullscreen initially
# root.attributes('-fullscreen', True)

# # Bind the Esc key to exit fullscreen
# root.bind("<Escape>", exit_fullscreen)

# # Create a Canvas to hold the background image
# canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())  # Full screen size
# canvas.pack(fill="both", expand=True)

# # Load the background image from an online URL
# image_url = "https://cdn.pixabay.com/photo/2018/03/15/09/11/zurich-cantonal-police-3227506_1280.jpg"  # Replace with your online image URL
# try:
#     response = requests.get(image_url)
#     response.raise_for_status()  # Check for HTTP errors
#     bg_image = Image.open(BytesIO(response.content))  # Open the image from the response
#     bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)  # Resize to fit canvas
#     bg_image = ImageTk.PhotoImage(bg_image)

#     # Create a background image on the canvas
#     canvas.create_image(0, 0, image=bg_image, anchor="nw")
# except Exception as e:
#     messagebox.showerror("Error", f"Failed to load background image: {e}")

# # Create a Frame to hold the buttons and align them horizontally
# button_frame = tk.Frame(canvas)
# button_frame.place(relx=0.5, rely=0.01, anchor='n')  # Position the button frame at the top center

# # Adding Buttons in a single line (like a navigation bar)
# load_button = tk.Button(button_frame, text="Load Dataset", command=load_dataset)
# load_button.pack(side='left', padx=5)

# plot_button = tk.Button(button_frame, text="State vs Total Crime", command=show_state_vs_crime)
# plot_button.pack(side='left', padx=5)

# crime_type_button = tk.Button(button_frame, text="Crime Type vs Rate", command=show_crime_type_vs_rate)
# crime_type_button.pack(side='left', padx=5)

# pie_chart_button = tk.Button(button_frame, text="Pie Chart of Crime Rate", command=show_crime_rate_pie_chart)
# pie_chart_button.pack(side='left', padx=5)

# classification_button = tk.Button(button_frame, text="State Safety Classification", command=show_state_safety_classification)
# classification_button.pack(side='left', padx=5)

# trend_button = tk.Button(button_frame, text="Crime Trend per State", command=show_crime_trend_per_state)
# trend_button.pack(side='left', padx=5)

# # Add a button to toggle fullscreen
# toggle_button = tk.Button(button_frame, text="Toggle Fullscreen", command=toggle_fullscreen)
# toggle_button.pack(side='left', padx=5)

# root.mainloop()


 
# import tkinter as tk
# from tkinter import filedialog, messagebox
# from PIL import Image, ImageTk  # Importing Pillow for image handling
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import requests
# from io import BytesIO
# from sklearn.cluster import KMeans

# # Global variable for the dataset and for active button
# dataset = None
# active_button = None  # To track the currently active button

# # Tkinter GUI window setup
# root = tk.Tk()
# root.title("Crime Analysis Tool")

# # Variable to keep track of fullscreen status
# is_fullscreen = True

# # Function to toggle fullscreen
# def toggle_fullscreen(event=None):
#     global is_fullscreen
#     is_fullscreen = not is_fullscreen  # Toggle the boolean flag
#     root.attributes('-fullscreen', is_fullscreen)

# # Function to exit fullscreen (with the Esc key)
# def exit_fullscreen(event=None):
#     global is_fullscreen
#     is_fullscreen = False
#     root.attributes('-fullscreen', False)

# # Make the window fullscreen initially
# root.attributes('-fullscreen', True)

# # Bind the Esc key to exit fullscreen
# root.bind("<Escape>", exit_fullscreen)

# # Create a Canvas to hold the background image
# canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())  # Full screen size
# canvas.pack(fill="both", expand=True)

# # Load the background image from an online URL
# def load_background_image():
#     image_url = "https://cdn.pixabay.com/photo/2018/03/15/09/11/zurich-cantonal-police-3227506_1280.jpg"  # Replace with your online image URL
#     try:
#         response = requests.get(image_url)
#         response.raise_for_status()  # Check for HTTP errors
#         bg_image = Image.open(BytesIO(response.content))  # Open the image from the response
#         bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)  # Resize to fit canvas
#         bg_image = ImageTk.PhotoImage(bg_image)

#         # Create a background image on the canvas
#         canvas.create_image(0, 0, image=bg_image, anchor="nw")
#         return bg_image  # Return the image to keep a reference
#     except Exception as e:
#         messagebox.showerror("Error", f"Failed to load background image: {e}")

# # Create a Frame to hold the buttons and align them horizontally
# def create_button_frame():
#     button_frame = tk.Frame(canvas, bg='')  # Set the background to empty for transparency
#     button_frame.place(relx=0.5, rely=0.01, anchor='n')  # Position the button frame at the top center

#     # Adding Buttons in a single line (like a navigation bar)
#     load_button = tk.Button(button_frame, text="Load Dataset", command=load_dataset, bg='black', fg='white', height=2)
#     load_button.pack(side='left', padx=(0, 10))  # Set padding for left button

#     plot_button = tk.Button(button_frame, text="State vs Total Crime", command=show_state_vs_crime, bg='black', fg='white', height=2)
#     plot_button.pack(side='left', padx=10)

#     crime_type_button = tk.Button(button_frame, text="Crime Type vs Rate", command=show_crime_type_vs_rate, bg='black', fg='white', height=2)
#     crime_type_button.pack(side='left', padx=10)

#     pie_chart_button = tk.Button(button_frame, text="Pie Chart of Crime Rate", command=show_crime_rate_pie_chart, bg='black', fg='white', height=2)
#     pie_chart_button.pack(side='left', padx=10)

#     classification_button = tk.Button(button_frame, text="State Safety Classification", command=show_state_safety_classification, bg='black', fg='white', height=2)
#     classification_button.pack(side='left', padx=10)

#     trend_button = tk.Button(button_frame, text="Crime Trend per State", command=show_crime_trend_per_state, bg='black', fg='white', height=2)
#     trend_button.pack(side='left', padx=10)

#     # Add a button to toggle fullscreen
#     toggle_button = tk.Button(button_frame, text="Toggle Fullscreen", command=toggle_fullscreen, bg='black', fg='white', height=2)
#     toggle_button.pack(side='left', padx=(10, 0))  # Set padding for the toggle button

# # Function to load the image
# def load_criminal_image(image_path):
#     try:
#         # Load and resize the image
#         img = Image.open(image_path)
#         img = img.resize((200, 200), Image.LANCZOS)  # Resize image to fit the label
#         img = ImageTk.PhotoImage(img)
        
#         # Create a label to display the image
#         img_label = tk.Label(root, image=img)
#         img_label.image = img  # Keep a reference to avoid garbage collection
#         img_label.pack(pady=10)  # Add some padding around the image
#     except Exception as e:
#         messagebox.showerror("Error", f"Failed to load image: {e}")

# def load_dataset():
#     global dataset
#     filepath = filedialog.askopenfilename(title="Select a CSV file", filetypes=(("CSV files", "*.csv"),))
#     if filepath:
#         try:
#             dataset = pd.read_csv(filepath)
#             messagebox.showinfo("Success", "Dataset loaded successfully!")
#             load_criminal_image("criminal.png")  # Load the criminal image after dataset is loaded
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to load dataset: {e}")

# def show_state_vs_crime():
#     try:
#         df_sum_by_state = dataset.groupby('STATE/UT')['TOTAL IPC CRIMES'].sum().reset_index()
#         states = df_sum_by_state['STATE/UT']
#         total_crime = df_sum_by_state['TOTAL IPC CRIMES']
        
#         fig, ax = plt.subplots()
#         ax.bar(states, total_crime)
#         plt.xticks(rotation=90, ha='right')
#         plt.title('State vs Total Crime Over 10 Years')
#         plt.xlabel('State/UT')
#         plt.ylabel('Total IPC Crimes')
#         plt.tight_layout()
#         plt.show()
#     except Exception as e:
#         messagebox.showerror("Error", f"Failed to plot data: {e}")

# def show_crime_type_vs_rate():
#     try:
#         sum_column = dataset.sum(axis=0)
#         crime_rates = sum_column[2:30]
#         crimes = dataset.columns.values[2:30]

#         fig, ax = plt.subplots()
#         ax.bar(crimes, crime_rates)
#         plt.xticks(rotation=90, ha='right')
#         plt.title('Type of Crime vs Rate of Crime')
#         plt.xlabel('Crime Type')
#         plt.ylabel('Total Occurrences')
#         plt.tight_layout()
#         plt.show()
#     except Exception as e:
#         messagebox.showerror("Error", f"Failed to generate crime rate graph: {e}")

# def show_crime_rate_pie_chart():
#     try:
#         df_sum_by_state = dataset.groupby('STATE/UT')['TOTAL IPC CRIMES'].sum().reset_index()
#         states = df_sum_by_state['STATE/UT']
#         total_crime = df_sum_by_state['TOTAL IPC CRIMES']

#         colors = plt.cm.tab20.colors  # Use a colormap for more colors
#         plt.figure(figsize=(8,8))
#         plt.pie(total_crime, labels=states, colors=colors, autopct='%1.1f%%', startangle=140)
#         plt.title('Pie Chart of Crime Rate per State')
#         plt.axis('equal')
#         plt.tight_layout()
#         plt.show()
#     except Exception as e:
#         messagebox.showerror("Error", f"Failed to generate pie chart: {e}")

# def show_state_safety_classification():
#     try:
#         total_crime_by_state = dataset.groupby('STATE/UT')['TOTAL IPC CRIMES'].sum().reset_index()
#         crime_data = total_crime_by_state['TOTAL IPC CRIMES'].values.reshape(-1,1)
#         kmeans = KMeans(n_clusters=2, random_state=42)
#         y_kmeans = kmeans.fit_predict(crime_data)
#         total_crime_by_state['Safety Classification'] = y_kmeans
#         fig, ax = plt.subplots()
#         ax.bar(total_crime_by_state['STATE/UT'], total_crime_by_state['Safety Classification'])
#         plt.xticks(rotation=90, ha='right')
#         plt.title('State Safety Classification (0: Safe, 1: Unsafe)')
#         plt.xlabel('State/UT')
#         plt.ylabel('Classification')
#         plt.tight_layout()
#         plt.show()
#     except Exception as e:
#         messagebox.showerror("Error", f"Failed to classify states: {e}")

# def show_crime_trend_per_state():
#     try:
#         states = dataset['STATE/UT'].unique()
#         years = sorted(dataset['YEAR'].unique())

#         for state in states:
#             state_data = dataset[dataset['STATE/UT'] == state]
#             total_crime_per_year = state_data.groupby('YEAR')['TOTAL IPC CRIMES'].sum()

#             plt.figure()
#             plt.plot(years, [total_crime_per_year.get(year, 0) for year in years], marker='o')
#             plt.title(f'Total IPC Crimes Over Years in {state}')
#             plt.xlabel('Year')
#             plt.ylabel('Total IPC Crimes')
#             plt.xticks(years, rotation=45)
#             plt.tight_layout()
#             plt.show()
#     except Exception as e:
#         messagebox.showerror("Error", f"Failed to plot crime trends: {e}")

# # Load the background image and create the button frame
# bg_image = load_background_image()
# create_button_frame()

# root.mainloop()

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from io import BytesIO
from sklearn.cluster import KMeans

# Global variable for the dataset and for active button
dataset = None
active_button = None  # To track the currently active button

 