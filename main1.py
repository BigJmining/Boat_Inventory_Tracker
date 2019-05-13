#!/usr/bin/env python3

## written by Jason Lohrey


import json, io
from PIL import Image


try:
    to_unicode = unicode
except NameError:
    to_unicode = str


def get_storage_image():
    img_boat1 = Image.open("vessel_layout_test1.jpeg") # 788 x 1976
    img_X, img_Y = (788,1976)
    
    bow_storage = (300,0,500,210)
    stern_storage = (30,1785,700,1785)
    port_storage = (30,700,300,1000)
    starboard_storage = (400,700,700,1000)

    if vessel_inventory['tools'][get_tool_info][1] == 'bow':
        storage_selection = img_boat1.crop(bow_storage)
    if vessel_inventory['tools'][get_tool_info][1] == 'stern':
        storage_selection = img_boat1.crop(stern_storage)
    if vessel_inventory['tools'][get_tool_info][1] == 'port':
        storage_selection = img_boat1.crop(port_storage)
    if vessel_inventory['tools'][get_tool_info][1] == 'starboard':
        storage_selection = img_boat1.crop(starboard_storage)

    storage_selection.show()




filename = 'tools.json'

## for debugging use
filename1 = 'testing.json'
filename2 = 'inventory.json'

with open(filename, 'r') as f:
	data = f.read()
	vessel_inventory = json.loads(data)


def print_intro():
    print(f"""
    Welcome to Vessel Inventory Management Program (VIMP)

    a)  Add new tool to inventory.
    b)  Check if item is in inventory & where its located.
    c)  Display inventory.
    d)  Remove tool from inventory

    n)  Exit.

    """)


def print_inventory():
## to print a list
    print('ITEM - COUNT - LOCATION')
    for k,v in vessel_inventory['tools'].items():
        if len(v) > 1:
            print(k,'-', v[0], '-', v[1], 'storage')
        else:
            print(k,'-', v[0], '-', v[1], 'storage')
    print('\n')

def remove_tool():
    pass


#### ADD new tool to vessel
def add_new_tool():
    addingTOOL = 'y' #input('Add a tool to database? (y/n): ')

    if addingTOOL == 'y':
        while 1:
            toolNEW = {'tools':{}}
            add_tool = str(input('Tool to add: '))
            num_of_tool = int(input('How many: '))
            location_tool = str(input('Where placed: '))
            tool_to_add = [num_of_tool , location_tool]

            toolNEW = vessel_inventory
            
            toolNEW['tools'][add_tool] = tool_to_add
            print(toolNEW)

            with io.open(f"tools.json", 'w', encoding='utf8') as outfile:
                                str_ = json.dumps(toolNEW,
                                                    indent=4, 
                                                    sort_keys=True,
                                                    separators=(',', ': '), 
                                                    ensure_ascii=False)

                                outfile.write(to_unicode(str_))
            
            again = input('Another? (y/n): ')
            
            if again == 'y':
                print('working...')
                pass
            else:
                break
    if addingTOOL != 'y':
        print('Goodbye')
    
        
#### check on inventory
def check_inventory():
    with open(filename, 'r') as f:
        global vessel_inventory
        data = f.read()
        vessel_inventory = json.loads(data)

    # print(vessel_inventory)
    while 1:
        global get_tool_info
        get_tool_info = input('Looking for: ')
        try:
            
            print(f"""
            There is {vessel_inventory['tools'][get_tool_info][0]} {get_tool_info}.
            Location: {vessel_inventory['tools'][get_tool_info][1]}
            """)
            
            # if vessel_inventory['tools'][get_tool_info][1] == 'bow':
            get_storage_image()

        except KeyError:
            print('Not in inventory\n')
        
        again = input('Something else? (y/n): ')
        if again == 'y':
            pass
        
        if again == 'p':
            print_inventory()

        if again == 'n':
            print('goodbye')
            break


def main():
    print_intro()

    selection = input('>>>: ')
    
    if selection == 'a':
        add_new_tool()
    
    if selection == 'b':
        check_inventory()
    
    if selection == 'c':
        print_inventory()
    
    if selection == 'd':
        remove_tool()

    if selection == 'n':
        print('Goodbye')
    
    

if __name__ == "__main__":
    main()
