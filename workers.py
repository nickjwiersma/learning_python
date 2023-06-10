Team = {}
Team['CEO'] = 'Nick Jan Wiersma'
Team['Co-founder'] = 'Nick Jan Wiersma', 'Luis Urbina', 'Karol Valencia', 'Adolfo Morán'
Team['Head of Legal Design'] = 'Karol Andrea Valencia Jaen'
Team['Legal Project Manager'] = 'Mariana Anahí Pérez'
Team['Junior Legal Technologist'] = 'Angie Soraya Cueva Zuzunaga'
Team['Legal Design Trainee'] = 'Andrea  Gabriela Supo Soto', 'Naomi Antonella García Urquizo',  'Nicholas Ricketts Fernández',  'Agnes Macedo de Jesus',  'Ana Damaris Colquehuanca Mendoza',  'Lucía Francesca Chávez Zeballos'
Team['Community Manager'] = 'Andrea  Gabriela Supo Soto'
Team['UX UI Designer'] = 'Vanessa Melina Cuentas Córdova', 'Micaela Lilian García'
Team['Back End Developer'] = 'Orane Farquharson'
Team['Legal Designer'] = 'Claudia Ordoñez Escobedo'
Team['External IT Consultant'] = 'Luis Urbina', 'Julio Bonifacio'
Team['CRP'] = 'Claudia Ordoñez Escobedo'
Team['Scrum Master'] = 'Mariana Anahí Pérez'
Team['Investor'] = 'Adolfo Morán', 'Karol Valencia', 'Luis Urbina', 'Nick Jan Wiersma'
print ("you can ask for:")
print ("CEO")
print ("Co-founder")
print ("Head of Legal Design")
print ("Junior Legal Technologist")
print ("Legal Design Trainee")
print ("Community Manager")
print ("UX UI Designer")
print ("Back End Developer")
print ("Legal Designer")
print ("External IT Consultant")
print ("CRP")
print ("Scrum Master")
print ("Investor")
# get user input and print the value associated with the key
a = input('Which position would you like to know? ')
print('---------------------------------')
print('The worker/s on this position are:')
# if there is only one person in the section use -         print(Team[a])
# if there is more people working on the same position we need a loop to show them correctly.
# -indent-for item in Team[a]:
# -indent--indent-print(item)
if a == 'Legal Design Trainee':
    for item in Team[a]:
        print(item)
elif a == 'CEO':
    print(Team[a])
elif a == 'Co-founder':
    for item in Team[a]:
        print(item)
elif a == 'Head of Legal Design':
    print(Team[a])
elif a == 'Junior Legal Project Manager':
    print(Team[a])
elif a == 'Junior Legal Technologist':
    print(Team[a])
elif a == 'Legal Design Trainee':
    for item in Team[a]:
        print(item)
elif a == 'Community Manager':
    print(Team[a])
elif a == 'UX UI Designer':
    for item in Team[a]:
        print(item)
elif a == 'Back End Developer':
    print(Team[a])
elif a == 'Legal Designer':
    print(Team[a])
elif a == 'External IT Consultant':
    for item in Team[a]:
        print(item)
elif a == 'CRP':
    print(Team[a])
elif a == 'Scrum Master':
    print(Team[a])


elif a == 'Investor':
    for item in Team[a]:
        print(item)
else:
    print('Wrong input.')
