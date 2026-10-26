#written 10.26.26
#this one is easy af
def selectionSearch(list,word):
    index = -1
    for i in range(len(list)):
        if list[i] == word:
            index = i
            break
    return index

touhous = ["Reimu","Marisa","Cirno","Sakuya","Meiling","Patchouli","Remilia"]
name = "Sakuya"
print(selectionSearch(touhous,name))
