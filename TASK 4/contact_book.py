# import json

# file_name = "contact_list.json"

# def load_data():
#     with open(file_name, "r") as file:
#         return json.load(file)


# def add():

#     contact_list ={}
#     contact_list["name"]=input("Name:")
#     contact_list["phone"]=int(input("Phone:"))
#     contact_list["Email"]=input("Email:")
#     with open(file_name, "a") as file:
#        file.write('\b,')
#        json.dump(contact_list,file, indent=4,separators=(',',':'))
#        file.write(']')




# def search_contact(data):
#     with open(file_name, "r") as file:
#         contacts = json.load(file)
#     print(contacts)
#     print(len(contacts))
#     for contact in contacts:
#         if contact["name"].lower() == data.lower():
#             print(contact)
#         else:
#             print("Contact not found")
#     print("Hello")


# add()
# search_contact("Arantis")














# data = {"name":"bob","ID":45, "age":19 }
# with open("data.json", "w") as file:
#     json.dump(data, file, indent=4)


# Contacts ={"Name":"Arantis","Number":72, "ID":2778282}
# print(Contacts)
# FILENAME="contact.text"
# with open(FILENAME, "w") as file:
#     # text=Contacts
#     file.write("Name: " + Contacts["Name"])
#     file.write(",Number: " + str(Contacts["Number"]))
#     file.write(",ID: " + str(Contacts["ID"]))

