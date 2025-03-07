filename = "user_input.txt"

with open(filename,"w") as file:
    text = input("Enter some text: ")
    file.write(text)

with open(filename, "r") as file:
    content = file.read()
    print("\nFile Content:\n", content)





    # with open("sample.txt", "w") as folder:
#     folder.write("Hello, this is a test file.")

# with open ("sample.txt", "r") as folder:
    
#     print(folder.read())   

# with open("sample.txt", "a") as folder:
#      folder.write("\nhello,this is a second test file.\n")  

# with open ("sample.txt", "r") as folder:
    
#     print(folder.read())        