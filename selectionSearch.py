#written 11.2.26
#this one is easy af
def selectionSearch(list,word):
    index = -1
    for i in range(len(list)):
        if list[i] == word:
            index = i
            break
    return index


#somehwat similar searching function using a for else loop
def searchForElse(list):
    n = str(input('Enter a name that you want to find in the list: '))
    for i in range(len(list)):
        if list[i] == n:
            print(f'Name {n} is found.')
            break
    else:
        print(f'Name {n} is not found.')

touhous = ["Reimu","Marisa","Cirno","Sakuya","Meiling","Patchouli","Remilia"]
name = "Sakuya"

print(selectionSearch(touhous,name))
print(searchForElse(touhous))
