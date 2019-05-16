from pyfiglet import figlet_format
from termcolor import colored

valid_colors = ("red", "green", "blue", "magenta", "cyan", "white", "yellow")

msg = input("what message do you want to print? ")
color = input("what color? ")
if color not in valid_colors:
    color = "green"

result = figlet_format(msg)
color_art = colored(result, color=color)
print(color_art)