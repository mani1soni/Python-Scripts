#!usr/bin/python
import webbrowser

def option_type(option):
	return {
        1 : "Repositories",
        2 : "Code",
        3 : "Commits",
        4 : "Issues",
        5 : "Users"
    }[option]


#taking search input from user
search_input=input("what do you want to search: ")
option_input=input("please select an option: \n 1) Repositories [Default] \n 2) Code \n 3) Commits \n 4) Issues \n 5) Users \n")
#If option_input is empty use the default one 
if(option_input == ""):
	option = "Repositories"
else:
	option = option_type(int(option_input))
print("Plz Wait github is  about to open!!!!")
#adding strings
z="https://github.com/search?q=",search_input,"&type=",option
webbrowser.open_new_tab(''.join(z))
 

