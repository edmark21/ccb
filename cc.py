logo = '''
+++++++++++++++++++++++++++++++++

_________                    .___.__  __    _________                  .___
\_   ___ \_______   ____   __| _/|__|/  |_  \_   ___ \_____ _______  __| _/
/    \  \/\_  __ \_/ __ \ / __ | |  \   __\ /    \  \/\__  \\_  __ \/ __ | 
\     \____|  | \/\  ___// /_/ | |  ||  |   \     \____/ __ \|  | \/ /_/ | 
 \______  /|__|    \___  >____ | |__||__|    \______  (____  /__|  \____ | 
        \/             \/     \/                    \/     \/           \/ 

        '''
print(logo)




import re
n = int(input())
for i in range(n):
    s = input()
    if len(s) == 19:
        if s[0] in ("4","5","6"):
            if bool(re.match("[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}$",s)):
                lst = []
                for z in range(len(s)):
                    if s[z] != "-":
                        lst.append(s[z])
                bool_4 = 1
                for t in range(3,len(lst)):
                    if lst[t] == lst[t-1] and lst[t] == lst[t-2] and lst[t] == lst[t-3]:
                        bool_4 = 0
                if bool_4 == 1:
                    print("Valid")
                else:
                    print("Invalid")
            else:
                print("Invalid")
        else:
            print("Invalid")
        
    elif len(s) == 16:
        if s[0] in ("4","5","6"):
            if bool(re.match("[0-9]*$",s)):
                lst = []
                for k in range(len(lst)):
                    lst.append(s[k])
                bool_4 = 1
                for t in range(3,len(lst)):
                    if lst[t] == lst[t-1] and lst[t] == lst[t-2] and lst[t] == lst[t-3]:
                        bool_4 = 0
                if bool_4 == 1:
                    print("Valid")
                else:
                    print("Invalid")
            else:
                print("Invalid")
        else:
            print("Invalid")
                    
                
                
    else:
        print("Invalid")
