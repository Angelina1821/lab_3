import json

f = open(r"C:\Users\1\OneDrive\Рабочий стол\lab3", 'r', encoding='utf 8')
lines = f.readline()
f.close()
for i in range(len(lines)):
    print(lines[i])
