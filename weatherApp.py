import tkinter as tk
from tkinter import *
import requests
from PIL import Image, ImageTk
#from tkhtmlview import HTMLLabel
import webbrowser

#document/frame root set
root = tk.Tk()

#Setting application favicon image (logo image)
root.iconbitmap('brand1_trans.ico')

#Setting default header text
root.title("Weather App V.1.0.2")

#Setting canvas width and height
HEIGHT = 500
WIDTH = 700

def format_response(weather):

	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']
		country = weather['sys']['country']
		longitude = weather['coord']['lon']
		latitude = weather['coord']['lat']
		cordinate = (longitude,latitude)
		#link = "https://openweathermap.org"
		#icon = weather['weather'][0]['icon']
		final_str = 'City: %s \nConditions: %s \nTemperature(°C): %s \nCountry: %s \nCoordinate(NE): %s ' % (name, desc, temp, country, cordinate)
	except:

		final_str = "There was a problem retrieving \nthat information"

	return final_str


def get_weather(city):
	#weather = response.json()
	if city:
		try:
			weather_key = ""
			url = "https://api.openweathermap.org/data/2.5/weather"
			params = {'APPID': weather_key, 'q': city, 'units': 'Metric'}
			response = requests.get(url, params=params)
			#print(response.json())
			weather = response.json()

			info_display['text'] = format_response(weather)

			icon_name = weather['weather'][0]['icon']
			open_image(icon_name)
			#print(weather)
		
		except:
			extra = "\nPlease enter a Valid City name" 
			#note = "\n " + name + "Is not a valid city name"
			info_display['text'] =weather['message']  + extra 
			

		#except requests.exceptions.HttpError as err:	
			#info_display['text'] = "Connection Error. \nEnsure you are conected to \nthe internet"

	else:
		no_net = "Entry can not be empty \nPlease, enter a city"
		info_display['text'] = no_net
		#print("no_net")
		
		return info_display['text'] 


def open_image(icon):
    size = int(lower_frame.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img


def get_link(url):
    webbrowser.open_new(url)


def on_click(event):
    entry.configure(state=NORMAL)
    entry.delete(0, END)

    # make the callback only work once
    entry.unbind('<Button-1>', on_click_id)


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
entry = tk.Entry(frame, font=('Courier', 15), text="State")
entry.place(relwidth=0.65, relheight=1)
entry.insert(0, "Enter State, City or ZIP")
entry.configure(state=DISABLED)
on_click_id = entry.bind('<Button-1>', on_click)

#Button 
button = tk.Button(frame, text="Get Weather", font=('Courier', 13), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

#Lower frame to hold wide label area
lower_frame = tk.Frame(root, bg="#80c1ff", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.55, anchor="n")

#Wide label for lower frame
info_display = tk.Label(lower_frame, bg="#ffffff", font=('Courier', 15), anchor='nw', justify='left', bd=5)
info_display.place(relwidth=1, relheight=1)

#Link display information
info_link = tk.Label(lower_frame, text="Information Source : Click Here", fg="blue", cursor="hand2", bg="#ffffff", font=('Courier', 10, 'bold'))
info_link.place(relx= 0.5, rely=0.9, relwidth= 0.5, anchor='n')
info_link.bind("<Button-1>", lambda e: get_link("https://openweathermap.org"))

#Weather icons
weather_icon = tk.Canvas(info_display, bg="#ffffff", bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

#Copyright information
copyright = tk.Frame(root, bg="#ffffff")
copyright.place(relx= 0.5, rely = 0.82, relheight=0.15, relwidth=0.5, anchor="n")


#Copyright display message
copyright_message = tk.Label(copyright, font =('Courier', 10, 'bold'), text="Copyright @ToyotechICT Solutions 2020.")
copyright_message.place(relwidth=1, relheight=1)
copyright_message.bind("<Button-2>", lambda e: get_link("https://toyotechict.com.ng"))


#Close of document root
root.mainloop()
