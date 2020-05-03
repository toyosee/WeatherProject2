import tkinter as tk
from tkinter import *
import requests

root = tk.Tk()

HEIGHT = 700
WIDTH = 500

def format_response(corona):

	try:
		name = corona['locations'][0]['country']
		#desc = corona['locations'][0]['country_code']
		#history = corona['locations']['latest']['confirmed']
		#country = weather['sys']['country']
		#longitude = weather['coord']['lon']
		#latitude = weather['coord']['lat']
		#cordinate = (longitude,latitude)
		#icon = weather['weather'][0]['icon']
		final_str = 'City: %s ' % (name)
	except:

		final_str = "There was a problem retrieving \nthat information"

	return final_str

def get_cases(locations):
	corona_code =id
	url = "https://coronavirus-tracker-api.herokuapp.com/v2/locations"
	params = {'q':locations}
	response = requests.get(url, params=params)
	corona = response.json()
	result = corona['locations']
	'''for location in result:
		locate = location.get('country')
		print(locate)'''
	info_display['text'] = format_response(corona)
	#print(result)



#Setting interface canvas and packing. Window size
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)

#Importing background image to root from file
background_image = tk.PhotoImage(file="landscape.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

canvas.pack()


#Frame variable to hold entry field and button
frame = tk.Frame(root, bg="#80c1ff", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

#Entry form for search/input field
entry = tk.Entry(frame, font=('Courier', 20))
entry.place(relwidth=0.65, relheight=1)

#Button 
button = tk.Button(frame, text="Get Cases", font=('Courier', 13), command=lambda: get_cases(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

#Lower frame to hold wide label area
lower_frame = tk.Frame(root, bg="#80c1ff", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.55, anchor="n")

#Wide label for lower frame
info_display = tk.Label(lower_frame, bg="#ffffff", font=('Courier', 15), anchor='nw', justify='left', bd=5)
info_display.place(relwidth=1, relheight=1)

#Weather icons
#weather_icon = tk.Canvas(info_display, bg="#ffffff", bd=0, highlightthickness=0)
#weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

#Copyright information
copyright = tk.Frame(root, bg="#ffffff")
copyright.place(relx= 0.5, rely = 0.82, relheight=0.15, relwidth=0.5, anchor="n")

#Copyright display message
copyright_message = tk.Label(copyright, font =('Courier', 10), text="Copyright @ToyotechICT Solutions 2020.")
copyright_message.place(relwidth=1, relheight=1)




root.mainloop()