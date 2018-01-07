#!usr/bin/python
import webbrowser
#taking search input from user
search_input=raw_input(what do you want to search: ")
print "Plz Wait youtube is  about to open!!!!"
#adding two strings
z="https://www.youtube.com/results?search_query=",search_input
webbrowser.open_new_tab(z)
 