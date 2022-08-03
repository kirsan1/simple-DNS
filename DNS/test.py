import webbrowser
i=0
print("Enter name of site:")
word = input()
with open('database.txt') as file:
    for line in file:
        list_words = line.split()
        i=i+1
        if word in list_words:
            webbrowser.open('http://' + line[0:15])
            break
