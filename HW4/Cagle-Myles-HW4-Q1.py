#Cagle-Myles-HW
statement = "John made $25.67 on Monday, $40.35 on Tuesday and $74.33 on Wednesday $90.64 on Thursday, $88.88 on Friday, $144.28 on Saturday and $351.97 on Sunday. How much total money did John earn?\n"
earnings = 0
spposition = None
for i in statement:
    try:
        atposition = statement.find("$",spposition)
        spposition = statement.find(" ",atposition)
        host = statement[atposition+1:spposition]
        earnings += float(host)
    except:
        continue

print(statement)    
print("John earned: $",round(earnings,2))
