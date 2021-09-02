from tabulate import tabulate
def addpatient(main):
    a = []
    for i in ['Name', 'Age', 'sex', 'Doctor Name', 'Disease', 'Blood Group']:
        print("Enter your", i,':')
        v = input()
        a.append(v)

    main.append(a)
    print("Patient Info Added Successfully...!")


def printlist(main):
    table = main
    print(tabulate(table))


def searchlist(main):
    for i in range(0, 6):
        print("Press ", i, " to search by", main[0][i],':')
    a = int(input('Enter your choice : '))
    print("Enter value to be searched : ")
    b = input()
    c = []
    h = ['Name', 'Age', 'sex', 'Doctor Name', 'Disease', 'Blood Group']
    c.append(h)
    for i in range(0, len(main)):
        if (main[i][a] == b):
            c.append(main[i])

    printlist(c)
    print("These are The Results Found ...!")


def deletepatientinfo(main):
    print("Enter name to be deleted : ")
    a = input()
    for i in range(0, len(main)):
        if (main[i][0] == a):
            main.pop(i)
            break
    print("Patient Record Deleted Successfully...!")
    # print(main)


def editpatientinfo(main):
    print("Enter your name : ")
    a = input()
    for i in range(0, 6):
        print("Press ", i, " to change", main[0][i],':')
    b = int(input('Enter your choice : '))
    for i in range(0, len(main)):
        if (main[i][0] == a):
            print("Enter the new value : ")
            c = input()
            main[i][b] = c
    print("Patient Info Editted Successfully...!")


def mainmenu(main):
    h = ['Add Patient Info', 'Search patient Info', 'Edit Patient Info', 'Delete patient info', 'Print Info of all patients',
     'Exit the Programme']
    print("|||_MAIN MENU_|||")
    for i in range(0, 6):
        print("Press ", i, " to", h[i],':')
    a = int(input('Enter your choice : '))
    if a == 0:
        addpatient(main)
    elif a == 1:
        searchlist(main)
    elif a == 2:
        editpatientinfo(main)
    elif a == 3:
        deletepatientinfo(main)
    elif a == 4:
        printlist(main)
    elif a == 5:
        print("THANK YOU")
        quit()


print('''__Bhaktivedanta Hospital__''')
h = ['Name', 'Age', 'sex', 'Doctor Name', 'Disease', 'Blood Group']
main = []
main.append(h)
h=['Pratyush','18','Male','Dr.Ganesh','Fever','o+ve']
main.append(h)
h=['Ritesh','22','Male','Dr.Ganesh','cold','o+ve']
main.append(h)
h=['Kamlesh','23','Male','Dr.Ganesh','Body Pain','A+ve']
main.append(h)
mainmenu(main)
while 1:
    print("Do you want to continue? (Y/N)")
    a=input()
    if(a.upper()=='Y'):
        mainmenu(main)
    else:
        print("THANK YOU")
        quit()
