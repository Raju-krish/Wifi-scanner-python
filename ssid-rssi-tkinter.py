
import customtkinter 
from ssid_rssi import *
from tkinter import StringVar

COLORS = {'Green':'#19A42C', 'cement':'#BFC0BF'}
def show_specific_ssid_detail(frame,ssid_var, label):
    ssid = ssid_var.get()
    fetch_ssid_rssi()
    print(SSID_DETAILS)
    string_label = StringVar()
    if ssid not in SSID_DETAILS.keys():
        string_label.set('There was no ' + ssid + ' in scan list')
    else:
        string_label.set('SSID - '+ ssid + ' Signal strength - ' + SSID_DETAILS[ssid])
        print(f'SSID - {ssid} Signal strength - {SSID_DETAILS[ssid]}')
    label.configure(textvariable=string_label)
    frame.configure(fg_color=COLORS['cement'])
    label.pack(padx=10, pady=10)

def create_main_frame(window):
    main_frame = customtkinter.CTkFrame(window, fg_color='white', height=200, width=250)
    width= window.winfo_screenwidth()
    height= window.winfo_screenheight()
    main_frame.place(x=730, y=300)
    ssid_var = StringVar()
    ssid_var.set('Enter ssid to find...!')
    ssid_entry = customtkinter.CTkEntry(window, textvariable=ssid_var, height=40, width=300,
            font=('Titllium', 15, 'bold'), text_color = 'black')
    label = customtkinter.CTkLabel(main_frame, font=('Titllium', 15, 'bold'), text_color=COLORS['Green'])
    
    button_submit = customtkinter.CTkButton(window, text='Find this ssid', cursor='hand2',
            font=('Titllium', 15, 'bold'), text_color='white',
            command=lambda: {fetch_ssid_rssi(), show_specific_ssid_detail(main_frame,ssid_var,label)})

    ssid_entry.place(x = 750, y=150)
    button_submit.place(x = 825, y=200)
    button = customtkinter.CTkButton(window, text='Show all ssid', cursor='hand2',
            font=('Titllium', 15, 'bold'), text_color='white',
            command=lambda: {fetch_ssid_rssi()})
    button.place(x = 825, y=250)
    

window = customtkinter.CTk(fg_color='white')
window.attributes('-zoomed',True)
create_main_frame(window)

window.mainloop()
