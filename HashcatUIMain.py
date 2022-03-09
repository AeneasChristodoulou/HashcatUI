from Hashcat_Parameters_dict import the_options


if 1 == 1:
    user_selected = input("Please enter Hash-Mode: ")


for key, value in the_options.items():
    if user_selected == value:
        Hashmode = key


print("hashcat -m", Hashmode)