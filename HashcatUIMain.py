from Hashcat_Parameters_dict import Modes, Charsets
import PySimpleGUI

if 1 == 1:
    user_selected_mode = input("Please enter Hash-Mode: ")
    user_selected_charset = input("Please enter Charset: ")


for key, value in Modes.items():
    if user_selected_mode == value:
        Hashmode = key
    if user_selected_charset == value:
        Charset = key


print("hashcat -m", Hashmode, Charset)

