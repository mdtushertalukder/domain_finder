import pyfiglet as f #this module is for creating banner
import socket as s
from termcolor import colored #termcolor is modules and colored is a function

banner=f.figlet_format('sigaba') #this function creates the banner
design=colored(banner,'red')
print(design)

domain_name=input("Enter domain name: ")

print(s.gethostbyname(domain_name)) #gethostbyname is used for translating domain to ip
