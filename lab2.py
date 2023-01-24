#- ФИО студента и любая дополнительная информация про студента  
#- использовать функцию print()  
#- условные операторы (if else elif) 
#- ввод данных 
#- комментарий
print("Hello World!\n")
print("What's your name?")
a = input('Write your name & secondname:\n ')
print("Your name is")
#
print("Write something about you:")
b = input('')
print(b)
#
i = 0
while (True):
    print("How old are you?")
    c = int(input('Write your age:\n')) 
    if(c < 18):
        print("Oh, you're a child or teenage") 
        break
    elif(c >= 18 and c < 30):
        print("Oh, you're young")
        break
    elif (c >= 30 and c < 100):
        print("I think you're oldman")
        break
    else:
        print("Something wrong, please try it again.\n")
    i+=1