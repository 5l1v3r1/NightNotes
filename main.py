# importing all required modules
import time
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from tkinter.font import Font, families
from tkinter.colorchooser import askcolor

# for the program




# setting the night_notes window
night_notes = tk.Tk()

# setting window name/title
night_notes.title('Night Notes')

night_notes.geometry('300x250+300+300')

# setting window background color
# default set to white
night_notes.config(bg = 'white')

# setting window minimum size
night_notes.minsize(width = 400, height = 500)



# defining the saveFile and saveAs functions that will allow
# the user(s) to save the current file in the specified
# format
def saveFile():
        try:
            txt = text_info.get(0.0, END)
            file = open(filename, 'w')
            file.write(txt)
            file.close()
        except:
            saveAs()			                
            

def saveAs():
        file = asksaveasfile('w', initialfile = 'newfile.txt', defaultextension = '.txt', filetypes = [('All Files','*.*'),('Text Documents','*.txt'), ('HTML Files', '*.html')])
        txt = text_info.get(0.0, END)
        try:
            file.write(txt.rstrip())
            showinfo('Saved!','\nFile saved successfully..')
        except:
            showerror('Oops!', '\nFile not saved..')

            
# defining the openFile function that will allow the user(s)
# to open a file and view it's comtents or edit it
def openFile(): 		
		file = askopenfilename(defaultextension = '.txt',filetypes = [('All Files','*.*'),('Text Documents','*.txt'), ('HTML Files', '*.html')]) 
		if file == '': 			
			file = None
		else: 			
			night_notes.title(os.path.basename(file) + ' - Night Notes') 
			text_info.delete(1.0,END) 
			file = open(file,'r') 
			text_info.insert(1.0,file.read()) 
			file.close() 
			
# defining the newFile function that will allow
# the user(s) to create a new file					
def newFile(): 
		night_notes.title('newfile - Night Notes') 
		file = None
		text_info.delete(1.0,END)
			


# dedining the Exit function
# which contains a messagebox that
# will prompt the user(s) whether they
# really wish to close the program or not
def Exit():
    msgBox = askyesno('Exit', '\nAre you sure you want to exit?')
    if msgBox == True:
        night_notes.destroy()


# defining the night_mode function
# which is responsible for switching
# the program to daylight mode or night mode
def night_mode():

    global btnState
    
    if btnState:
        
        # setting text color to black
        # and background color to white
        # if night mode is disabled
        text_info.config(bg = 'white', fg = 'black')
        
        # messagebox will show
        # pop up when night mode has
        # been disabled
        nightModeEnabled = showinfo('Disabled!', '\nNight mode disabled..')
        
        btnState = False


    else:
        
        # setting text color to white
        # and background color to grey17
        # if night mode is enabled
        text_info.config(bg = '#2B2B2B', fg = 'white')
        
        # messagebox will pop up
        # if night mode button is clicked
        nightModeDisabled = showinfo('Enabled!','\nNight mode enabled..')

        btnState = True

def changeFontColor():
        (triple, hexstr) = askcolor()
        if hexstr:
            text_info.config(fg = hexstr)


# defining function to cut
# selected text to the clipboard
def cut(): 
		text_info.event_generate('<<Cut>>') 

# dedining function to copy
# selected text to the clipboard
def copy(): 
		text_info.event_generate('<<Copy>>')
		
# defining function to paste
# selected text to the clipboard	
def paste(): 
		text_info.event_generate('<<Paste>>')

# defining function to select all
# text in the editor		
def select_all():
    text_info.event_generate('<<SelectAll>>')

# definig function to undo text
# inside the editor    
def undo():
    text_info.edit_undo()

# defining function to redo text
# inside the editor        
def redo():
    text_info.edit_redo()

# defining function to add date/time
# inside the editor
def addDate():
        full_date = time.localtime()
        day = str(full_date.tm_mday)
        month = str(full_date.tm_mon)
        year = str(full_date.tm_year)
        date = day + '/' + month + '/' + year
        text_info.insert(INSERT, date, "a")
    
       
# text underline works only if
# text is selected
def underline():
        try:
            current_tags = text_info.tag_names('sel.first')
            if 'underline' in current_tags:
                text_info.tag_remove('underline', 'sel.first', 'sel.last')
            else:
                text_info.tag_add('underline', 'sel.first', 'sel.last')
                underline_font = Font(text_info, text_info.cget("font"))
                underline_font.configure(underline = 1)
                text_info.tag_configure("underline", font = underline_font)
        except:
            pass
            

# text overstrike only works if
# text is selected
def overstrike():
        try:
            current_tags = text_info.tag_names('sel.first')
            if 'overstrike' in current_tags:
                text_info.tag_remove('overstrike', 'sel.first', 'sel.last')
            else:
                text_info.tag_add('overstrike', 'sel.first', 'sel.last')
                overstrike_font = Font(text_info, text_info.cget('font'))
                overstrike_font.configure(overstrike = 1)
                text_info.tag_configure('overstrike', font = overstrike_font)
        except:
            pass

  
   
# text bold only works if
# text is selected   
def bold(): 
        try:
            current_tags = text_info.tag_names('sel.first')
            if 'bold' in current_tags:
                text_info.tag_remove('bold', 'sel.first', 'sel.last')
            else:
                text_info.tag_add('bold', 'sel.first', 'sel.last')
                bold_font = Font(text_info, text_info.cget('font'))
                bold_font.configure(weight = 'bold')
                text_info.tag_configure('bold', font = bold_font)
        except:
            pass


# text italic only works if
# text is selected
def italic():
        try:
            current_tags = text_info.tag_names('sel.first')
            if 'italic' in current_tags:
                text_info.tag_remove('italic', 'sel.first', 'sel.last')
            else:
                text_info.tag_add('italic', 'sel.first', 'sel.last')
                italic_font = Font(text_info, text_info.cget("font"))
                italic_font.configure(slant = 'italic')
                text_info.tag_configure('italic', font = italic_font)
        except:
            pass



# developer info window
def developer_info():
    
    global btnState
    
    # setting window type as toplevel
    developer_info_window = Toplevel()
    
    # setting window name/title
    developer_info_window.title('Contact me')
    
    # setting window size/geometry
    developer_info_window.geometry('700x560')
    
    # set if window will be resizable in both x or y direction
    # default set to False in both directions
    developer_info_window.resizable(False, False)
    
    # setting window background color
    # default set to black
    developer_info_window.config(bg = '#FFFFFF')
    
    # developer info title text label
    developer_info_title = Label(developer_info_window, text = '\nDEVELOPER INFO', font = ('Arial',6, 'bold'), fg = '#000000', bg = '#FFFFFF', underline = '1').pack()
    names_label = Label(developer_info_window, text = 'Names', font = ('Carrois Gothic SC',5, 'underline'), fg = '#000000', bg = '#FFFFFF').place(relx = 0.15, rely = 0.20)
    
    # developer info main text label
    developer_info_mainText = Label(developer_info_window, text = '\nName(s): \n\nAlias(es): ', font = ('Arial',4, 'bold'), fg = '#000000', bg = '#FFFFFF').place(x = 100, y = 150)
    
    # developer name
    developer_name_label = Label(developer_info_window, text = 'RITCHIE.', font = ('Arial',3, 'bold'), fg = '#000000', bg = '#FFFFFF', underline = '0').place(relx = 0.30, rely = 0.32)
    
    # developer alias
    developer_alias_label = Label(developer_info_window, text = 'RLY0NHEART', font = ('Arial',3, 'bold'), fg = '#000000', bg = '#FFFFFF', underline = '0').place(relx = 0.30, rely = 0.42)
    
    # social links label
    social_links_label = Label(developer_info_window, text = '\nSocial links', font = ('Carrois Gothic SC',5, 'underline'), fg = '#000000', bg = '#FFFFFF').place(relx = 0.15, rely = 0.46)
    
    # github link label
    github_link_label = Label(developer_info_window, text = '\nGithub: ', font = ('Arial',4, 'bold'), fg = '#2B2B2B', bg = '#FFFFFF').place(relx = 0.15, rely = 0.59)
    github_link = Label(developer_info_window, text = 'www.github.com/rlyonheart', font = ('Arial', 3, 'underline'),fg = '#000000', bg = '#FFFFFF').place(relx = 0.27, rely = 0.64)
    
    # twitter link label
    twitter_link_label = Label(developer_info_window, text = '\nTwitter: ', font = ('Arial',4, 'bold'), fg = '#2887C8', bg = '#FFFFFF').place(relx = 0.15, rely = 0.68) 
    twitter_link = Label(developer_info_window, text = 'www.twitter.com/rly0nheart', font = ('Arial', 3, 'underline'),fg = '#000000', bg = '#FFFFFF').place(relx = 0.28, rely = 0.73) 
    
    # instagram link label
    instagram_link_label = Label(developer_info_window, text = '\nInstagram: ', font = ('Arial',4, 'bold'), fg = 'orange', bg = '#FFFFFF').place(relx = 0.15, rely = 0.77)
    instagram_link = Label(developer_info_window, text = 'www.instagram.com/rlyonheart', font = ('Arial', 3, 'underline'),fg = '#000000', bg = '#FFFFFF').place(relx = 0.33, rely = 0.82)
    
    # close button widget
    # close button will terminate the help_window window when clicked
    close_button = Button(developer_info_window, text = '??', font = ('Arial', 7, 'bold'), fg = '#2B2B2B', bg = '#FFFFFF', activeforeground = '#FFFFFF', underline = '2', activebackground = '#2B2B2B', highlightbackground = '#FFFFFF', command = lambda:developer_info_window.destroy()).place(relx = 0.85, rely = 0.85, relwidth = 0.10, relheight = 0.11)
    
    if btnState:
        
        # setting all the widgets in the developer info
        # window to adapt to night mode when enabled
        developer_info_window.config(bg = '#2B2B2B')
        developer_info_title = Label(developer_info_window, text = '\nDEVELOPER INFO', font = ('Arial',6, 'bold'), fg = '#FFFFFF', bg = '#2B2B2B', underline = '1').place(x = 213, y = 0)
        names_label = Label(developer_info_window, text = 'Names', font = ('Carrois Gothic SC',5, 'underline'), fg = '#FFFFFF', bg = '#2B2B2B').place(relx = 0.15, rely = 0.20)
        developer_info_mainText = Label(developer_info_window, text = '\nName(s): \n\nAlias(es): ', font = ('Arial',4, 'bold'), fg = '#FFFFFF', bg = '#2B2B2B').place(x = 100, y = 150)
    
        developer_name_label = Label(developer_info_window, text = 'RITCHIE.', font = ('Arial',3, 'bold'), fg = '#FFFFFF', bg = '#2B2B2B', underline = '0').place(relx = 0.30, rely = 0.32)
        developer_alias_label = Label(developer_info_window, text = 'RLY0NHEART', font = ('Arial',3, 'bold'), fg = '#FFFFFF', bg = '#2B2B2B', underline = '0').place(relx = 0.30, rely = 0.42)
    
        social_links_label = Label(developer_info_window, text = '\nSocial links', font = ('Carrois Gothic SC',5, 'underline'), fg = '#FFFFFF', bg = '#2B2B2B').place(relx = 0.15, rely = 0.46)
    
        github_link_label = Label(developer_info_window, text = '\nGithub: ', font = ('Arial',4, 'bold'), fg = 'grey', bg = '#2B2B2B').place(relx = 0.15, rely = 0.59)
        github_link = Label(developer_info_window, text = 'www.github.com/rlyonheart', font = ('Arial', 3, 'underline'),fg = '#FFFFFF', bg = '#2B2B2B').place(relx = 0.27, rely = 0.64)
    
        twitter_link_label = Label(developer_info_window, text = '\nTwitter: ', font = ('Arial',4, 'bold'), fg = '#2887C8', bg = '#2B2B2B').place(relx = 0.15, rely = 0.68) 
        twitter_link = Label(developer_info_window, text = 'www.twitter.com/rly0nheart', font = ('Arial', 3, 'underline'), fg = '#FFFFFF', bg = '#2B2B2B').place(relx = 0.28, rely = 0.73) 
    
        instagram_link_label = Label(developer_info_window, text = '\nInstagram: ', font = ('Arial',4, 'bold'), fg = 'orange', bg = '#2B2B2B').place(relx = 0.15, rely = 0.77)
        instagram_link = Label(developer_info_window, text = 'www.instagram.com/rlyonheart', font = ('Arial', 3, 'underline'),fg = '#FFFFFF', bg = '#2B2B2B').place(relx = 0.33, rely = 0.82)
    
        close_button = Button(developer_info_window, text = '??', font = ('Arial', 7, 'bold'), fg = '#FFFFFF', bg = '#2B2B2B', activeforeground = '#2B2B2B', activebackground = '#FFFFFF', highlightbackground = '#2B2B2B', command = lambda:developer_info_window.destroy()).place(relx = 0.85, rely = 0.85, relwidth = 0.10, relheight = 0.11)
        


# defining a function for the 'about_window' window
def about_window():
    
    global btnState
    
    # setting window type as Toplevel()
    about_window = Toplevel()

    # setting window name/title
    about_window.title('About')

    # setting window size    
    about_window.geometry('700x560')

    # set if window will be resizable in both x or y directions
    # default set to False in both directions
    about_window.resizable(False, False)

    # setting window background color
    # default set to black
    about_window.configure(background = '#FFFFFF')
    
    # text widgets and label widgets
    # in the about_window window
    about_window_software_title_label = Label(about_window, text = '\nNIGHT NOTES v0.5.0', font = ('Arial', 6, 'bold'), underline = '1', fg = '#2B2B2B', bg = '#FFFFFF').pack()
    about_window_aoftware_mainText_label  = Label(about_window, text = '\nNight Notes is a simple text editor software\nwritten in Python3/Tkinter.\nthis software is being developed by\naka', fg = '#2B2B2B', bg = '#FFFFFF', underline = '43', font = ('Arial', 5)).pack()
    all_rights_reserved_label = Label(about_window, text = 'all rights reserved ??2021\nLICENSE MiT', fg = '#2B2B2B', bg = '#FFFFFF', font = ('Arial', 4, 'bold')).place(x = 210, y = 350)
    
    # developer name text label widget
    developer_name_text_label = Label(about_window, text = 'ritchie.' , font = ('Arial', 5, 'bold'), fg = '#2B2B2B', bg = '#FFFFFF').place(relx = 0.82, rely = 0.33)
    # developer alias text label widget
    developer_alias_text_label = Label(about_window, text = 'rly0nheart.', font = ('Arial', 5, 'bold'), fg = '#2B2B2B', bg = '#FFFFFF').place(relx = 0.54, rely = 0.39)
    
    # close button widget
    # close button will terminate the help_window window when clicked
    close_button = Button(about_window, text = '??', font = ('Arial', 7, 'bold'), fg = '#2B2B2B', bg = '#FFFFFF', activeforeground = '#FFFFFF', activebackground = '#2B2B2B', highlightbackground = '#FFFFFF', command = lambda:about_window.destroy()).place(relx = 0.85, rely = 0.85, relwidth = 0.10, relheight = 0.11)
    if btnState:
          
          # setting all the widgets in the about
          # window to adapt to night mode
          about_window.configure(background = '#2B2B2B')
          about_window_software_title_label = Label(about_window, text = '\nNIGHT NOTES v0.5.0', font = ('Arial', 6, 'bold'), underline = '1', bg = '#2B2B2B', fg = '#FFFFFF').place(x = 186, y = 0)
          about_window_aoftware_mainText_label  = Label(about_window, text = '\nNight Notes is a simple text editor software\nwritten in Python3/Tkinter.\nthis software is being developed by\naka', bg = '#2B2B2B', fg = '#FFFFFF', underline = '43', font = ('Arial', 5)).place(x = 77, y = 86)
          all_rights_reserved_label = Label(about_window, text = 'all rights reserved ??2021\nLICENSE MiT', bg = '#2B2B2B', fg = '#FFFFFF', font = ('Arial', 4, 'bold')).place(x = 210, y = 350)
          developer_name_text_label = Label(about_window, text = 'ritchie.' , font = ('Arial', 5, 'bold'), bg = '#2B2B2B', fg = '#FFFFFF').place(relx = 0.82, rely = 0.33)
          developer_alias_text_label = Label(about_window, text = 'rly0nheart.', font = ('Arial', 5, 'bold'), bg = '#2B2B2B', fg = '#FFFFFF').place(relx = 0.54, rely = 0.39)
          close_button = Button(about_window, text = '??', font = ('Arial', 7, 'bold'), bg = '#2B2B2B', fg = '#FFFFFF', activeforeground = '#2B2B2B', activebackground = '#FFFFFF', highlightbackground = '#2B2B2B', command = lambda:about_window.destroy()).place(relx = 0.85, rely = 0.85, relwidth = 0.10, relheight = 0.11)
 
          

# defining the dropdown menu(s)
# in the main night_notes window
menu_bar = Menu(night_notes)

# defining edit dropdown menu
edit_menu = Menu(menu_bar, tearoff = 0)

# defining info dropdown menu
info_menu = Menu(menu_bar, tearoff = 0)

# defining tools dropdown menu
tools_menu = Menu(menu_bar, tearoff = 0)




night_notes.config(menu = menu_bar)

file_menu = Menu(menu_bar)

menu_bar.add_cascade(label = 'file', underline = '0',font = ('Arial', 6), activeforeground = '#FFFFFF',activebackground = '#2B2B2B',menu = file_menu)

file_menu.add_command(label = 'New file', font = ('Arial', 5), activeforeground = '#FFFFFF', activebackground = '#2B2B2B', command = newFile)

file_menu.add_command(label = 'Open file', font = ('Arial', 5), activeforeground = '#FFFFFF', activebackground = '#2B2B2B', command = openFile)

file_menu.add_command(label = 'Save', font = ('Arial', 5), activeforeground = '#FFFFFF', activebackground = '#2B2B2B', command = saveFile)

file_menu.add_command(label = 'Save as..', font = ('Arial', 5), activeforeground = '#FFFFFF', activebackground = '#2B2B2B', command = saveAs)

file_menu.add_separator()

file_menu.add_command(label = 'Exit',font = ('Arial',6), activeforeground = '#FFFFFF', activebackground = '#2B2B2B', command = Exit)


# tools dropdown menu
menu_bar.add_cascade(label = '  edit', font = ('Arial', 6), activeforeground = '#FFFFFF', activebackground = '#2B2B2B', menu = edit_menu)

edit_menu.add_command(label = 'Copy', font = ('Arial', 5), activeforeground = '#FFFFFF', activebackground = '#2B2B2B', command = copy)

edit_menu.add_command(label = 'Cut', font = ('Arial', 5), activeforeground = '#FFFFFF', activebackground = '#2B2B2B', command = cut)

edit_menu.add_command(label = 'Paste', font = ('Arial', 5), activeforeground = '#FFFFFF', activebackground = '#2B2B2B', command = paste)
 
edit_menu.add_command(label = 'Undo', font = ('Arial', 5), activeforeground = '#FFFFFF', activebackground = '#2B2B2B', command = undo)

edit_menu.add_command(label = 'Redo', font = ('Arial', 5), activeforeground = '#FFFFFF', activebackground = '#2B2B2B', command = redo)

edit_menu.add_separator()

edit_menu.add_command(label = 'Select All', font = ('Arial', 5), activeforeground = '#FFFFFF', activebackground = '#2B2B2B', command = select_all)



# tools menu
menu_bar.add_cascade(label = '  tools', font = ('Arial', 6), activeforeground = '#FFFFFF', activebackground = '#2B2B2B', menu = tools_menu)

# font dropdown menu
font_menu = Menu(tools_menu)
tools_menu.add_cascade(label = 'Font', font = ('Arial', 5), activeforeground = '#FFFFFF', activebackground = '#2B2B2B', menu = font_menu)

# font style dropdown menu
font_style = Menu(font_menu)
font_menu.add_cascade(label = 'Font style', font = ('Arial', 5), activeforeground = '#FFFFFF', activebackground = '#2B2B2B', menu = font_style )

font_style.add_command(label = 'Bold', font = ('Arial', 5, 'bold'), activeforeground = '#FFFFFF', activebackground = '#2B2B2B', command = bold)

font_style.add_command(label = 'Italic', font = ('Arial', 5, 'italic'), activeforeground = '#FFFFFF', activebackground = '#2B2B2B', command = italic)

font_style.add_command(label = 'Underline', font = ('Arial', 5, 'underline'), activeforeground = '#FFFFFF', activebackground = '#2B2B2B', command = underline)

font_style.add_command(label = 'Overstrike', font = ('Arial', 5, 'overstrike'), activeforeground = '#FFFFFF', activebackground = '#2B2B2B', command = overstrike)

font_menu.add_command(label = 'Font color', font = ('Arial', 5), activeforeground = '#FFFFFF', activebackground = '#2B2B2B', command = changeFontColor)

tools_menu.add_command(label = 'Add date', font = ('Arial', 5), activeforeground = '#FFFFFF', activebackground = '#2B2B2B', command = addDate)

tools_menu.add_separator()

tools_menu.add_command(label = 'Night mode', font = ('Arial', 5), activeforeground = '#FFFFFF', activebackground = '#2B2B2B', command = night_mode)


# info dropdown menu
menu_bar.add_cascade(label = '  info', font = ('Arial', 6), activeforeground = '#FFFFFF', activebackground = '#2B2B2B', menu = info_menu)

info_menu.add_command(label = 'About', font = ('Arial', 5), activeforeground = '#FFFFFF', activebackground = '#2B2B2B', command = about_window)

info_menu.add_command(label = 'Developer Info', font = ('Arial', 5), activeforeground = '#FFFFFF', activebackground = '#2B2B2B', command = developer_info)


# adding a scrollbar in the night_notes window
# scrollbar is ttk themed
scrollbar = ttk.Scrollbar(night_notes)

# packing the scrollbar in the night_notes window
scrollbar.pack(side = RIGHT, fill = Y)

# setting the night_notes window to accept input
# as text in it
text_info = Text(night_notes, font = ('Roboto Condensed',7), height = 400, width = 400, wrap = 'word', pady = 2, padx = 3, undo = True)
text_info.pack(fill = Y, expand = 1)
text_info.focus_set()

# adding scroll functionality to the scrollbar
scrollbar.config(command = text_info.yview)

# setting button switch state
# (night mode/daylight mode):
btnState = False



# window in mainloop:
night_notes.mainloop()


