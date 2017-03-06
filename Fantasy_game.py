fantasy_list={}

while(True):
    print('Enter an object and its number (separated with a line)')
    
    name = input()
    if name is '':
        break
    
    value = int(input())
    print('\n')

    fantasy_list[name] = value

def display_inventory(fantasy_list):
    for k,v in fantasy_list.items():
        print(str(v) + ' ' + k)

    count = 0

    for k in fantasy_list.values():
        count = count + k

    print('\nTotal number of items '+ str(count))

display_inventory(fantasy_list)
