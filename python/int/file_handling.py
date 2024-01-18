### File Handling ###

# .txt file

txt_file=open('python/int/my_file.txt', 'r+') # r+ lee y escribe pegado al ultimo texto, recordar usar salto de linea o espacio, si usamos w+ sobreescribe el archivo

print(txt_file.read())
'''
Mi nombre es Roberto
Mi apellido es Orazi
Tengo 26 años
mis lenguajes favoritos son Javascript y python
'''
print(txt_file.read(10)) # Leemos solo 10 caracteres
#Mi nombre

print(txt_file.readline())
# Mi nombre es Roberto

print(txt_file.readlines())
# ['Mi nombre es Roberto\n', 'Mi apellido es Orazi\n', 'Tengo 26 años\n', 'mis lenguajes favoritos son Javascript y python']



for line in txt_file.readlines():
    print(line)
'''
Mi nombre es Roberto

Mi apellido es Orazi

Tengo 26 años

mis lenguajes favoritos son Javascript y python
'''

txt_file2=open('python/int/my_file.txt', 'r+')

txt_file2.write(' aunque tambien me gusta c')
print(txt_file2.readline())


txt_file3=open('python/int/my_file3.txt', 'w+')

txt_file3.write(' aunque tambien me gusta c')
print(txt_file2.readline())

import os

txt_file3.close
os.remove('python/int/my_file3.txt')

# .json file por lo general se usa todo en web

import json

json_file = open('python/int/my_json.json', 'w+')

json_test={
    'name': 'Roberto',
    'lastname': 'Orazi',
    'Age': '26',
    'Language': 'Python',
    'Website': 'https://robertoorazi.com.ar'
}

json.dump(json_test, json_file, indent=0)


json_file.close()

with open('python/int/my_json.json') as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict=json.load(open('python/int/my_json.json'))
print(json_dict)
print(json_dict['name'])
# .csv file
import csv

csv_file=open('python/int/my_csv.csv', 'w+')

csv_writer = csv.writer(csv_file)

csv_writer.writerow(['name','surname','age','website'])
csv_writer.writerow(['roberto','orazi','26','https://robertoorazi.com.ar'])

csv_file.close()

with open('python/int/my_csv.csv') as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xml file
import xml


# .xlsx file
# import xlrd hay que instalar dependencia