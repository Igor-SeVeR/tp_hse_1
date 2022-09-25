class Contact:
    def __init__(self, id, name1, name2, name3, phoneNumber, mail):
        self.id = id
        self.name1 = name1
        self.name2 = name2
        self.name3 = name3
        self.phone = phoneNumber
        self.mail = mail


print("Введите название файла")
fileName = input()
file = open(fileName, encoding='utf-8')
contacts = []
id = 0
for s in file:
    id += 1
    q = s.split(",")
    fullName = q[0].split(" ")
    while len(fullName) < 3:
        fullName.append(None)
    if q[1] != '' and q[1] != "\n":
        phoneNumber = q[1].replace(" ", "").replace("\n", "")
    else:
        phoneNumber = None
    if q[2] != '' and q[2] != "\n":
        mail = q[2].replace(" ", "").replace("\n", "")
    else:
        mail = None
    contact = Contact(id, fullName[0], fullName[1], fullName[2], phoneNumber, mail)
    contacts.append(contact)
print("Контакты добавлены в базу")


def getContact(id):
    id -= 1
    ans = "ID - " + str(contacts[id].id) + "\n"
    if contacts[id].name1 != None:
        ans += "ФИО: " + contacts[id].name1
    if contacts[id].name2 != None:
        ans += " " + contacts[id].name2
    if contacts[id].name3 != None:
        ans += " " + contacts[id].name3
    if contacts[id].phone != None:
        ans += "\n" + "Номер телефона: " + contacts[id].phone
    else:
        ans += "\n" + "Номер телефона: " + "None"
    if contacts[id].mail != None:
        ans += "\n" + "Почта: " + contacts[id].mail + "\n"
    else:
        ans += "\n" + "Почта: " + "None" + "\n"
    return ans


def searchByNumber(phone):
    flag = False
    for contact in contacts:
        if contact.phone == phone:
            print(getContact(contact.id))
            flag = True
    if not (flag):
        print("Ничего не найдено")


def searchByMail(mail):
    flag = False
    for contact in contacts:
        if contact.mail == mail:
            print(getContact(contact.id))
            flag = True
    if not (flag):
        print("Ничего не найдено")


def search(fullName):
    ids = []
    if fullName[0] != None:
        for i in range(len(contacts)):
            if fullName[0] == contacts[i].name1:
                ids.append(i)
    if fullName[1] != None:
        if fullName[0] != None:
            for id in ids:
                if fullName[1] != contacts[id].name2:
                    ids.remove(id)
        else:
            for i in range(len(contacts)):
                if fullName[1] == contacts[i].name2:
                    ids.append(i)

    if fullName[2] != None:
        if fullName[0] != None or fullName[1] != None:
            for id in ids:
                if fullName[2] != contacts[id].name3:
                    ids.remove(id)
        else:
            for i in range(len(contacts)):
                if fullName[2] == contacts[i].name3:
                    ids.append(i)

    if len(ids) == 0:
        print("Ничего не найдено")
    else:
        for id in ids:
            print(getContact(id))


def getWithoutPhoneOrMail(num):
    if num == 1:
        for contact in contacts:
            if contact.phone == None:
                print(getContact(contact.id))
        return
    elif num == 2:
        for contact in contacts:
            if contact.mail == None:
                print(getContact(contact.id))
        return
    elif num == 3:
        for contact in contacts:
            if contact.phone == None and contact.mail == None:
                print(getContact(contact.id))
        return


def printAll():
    for contact in contacts:
        print(getContact(contact.id))


def change(id, contact):
    fio = contact.name.split(" ")
    while len(fio) < 3:
        fio.append(None)
    contacts[id - 1].name1 = fio[0]
    contacts[id - 1].name2 = fio[1]
    contacts[id - 1].name3 = fio[2]
    contacts[id - 1].phone = contact.phoneNumber if len(contact.phoneNumber) > 0 else None
    contacts[id - 1].mail = contact.mail if len(contact.mail) > 0 else None


def printCommands():
    print("Список доступных команд: ")
    print("1 - Вывести все контакты", "2 - Поиск по телефону", "3 - Поиск по почте", "4 - Поиск по ФИО",
          "5 - поиск по отсутствию номера/почты", "6 - Изменение контакта", "7 - остановить программу", sep="\n")


printCommands()
call = int(input())
while call != "akdna@@@kdn":
    if call == 1:
        printAll()
    elif call == 2:
        print("Введите телефон")
        phoneNumber = input()
        searchByNumber(phoneNumber)
    elif call == 3:
        print("Введите почту")
        mail = input()
        searchByMail(mail)
    elif call == 4:
        fullName = []
        print("Введите фамилию, либо оставьте пустую строку")
        f = input()
        if f == '':
            fullName.append(None)
        else:
            fullName.append(f)
        print("Введите имя, либо оставьте пустую строку")
        i = input()
        if i == '':
            fullName.append(None)
        else:
            fullName.append(i)
        print("Введите отчество, либо оставьте пустую строку")
        o = input()
        if o == '':
            fullName.append(None)
        else:
            fullName.append(o)
        search(fullName)
    elif call == 5:
        print("Введите по чему хотите искать: ", "1 - без номера", "2 - без почты", "3 - без обоих", sep="\n")
        num = int(input())
        getWithoutPhoneOrMail(num)
    elif call == 6:
        print("Введите id контакта, который хотите изменить и новые данные для него", "(в две разные строки)", sep="\n")
        id = int(input())
        s = input()
        q = s.split(",")
        fullName = q[0].split(" ")
        while len(fullName) < 3:
            fullName.append(None)
        phoneNumber = ""
        if q[1] != '' and q[1] != '\n':
            phoneNumber = q[1].replace(" ", "").replace("\n", "")
        else:
            phoneNumber = None
        mail = ""
        if q[2] != '' and q[2] != '\n':
            mail = q[2].replace(" ", "").replace("\n", "")
        else:
            mail = None
        contact = Contact(id, fullName[0], fullName[1], fullName[2], phoneNumber, mail)
        contacts[id - 1] = contact
    elif call == 7:
        "Вы закрыли программу"
        break
    print()
    printCommands()
    call = int(input())
