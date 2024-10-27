import os
def create_file(filename):
    try: #try and error method/exception handling
        with open(filename, 'x') as f:      #close krne ki zarurat ni pdegi is se
            print(f"File Name {filename} is created successfully!")
    except FileExistsError:    #occurs when file already exists
        print(f"File Name {filename} already exists!")
    except Exception as E:     #will work for any random error
        print("An error occured!")

def view_all_files():
    files = os.listdir()
    if not files:
        print("No files exist!")
    else:
        print("This is the directory!")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully!")
    except FileNotFoundError:
        print("File not found")
    except Exception as E:     #will work for any random error
        print("An error occured!")

def read_file(filename):
    try:
        with open('sample.txt','r') as f:
            content = f.read()
            print(f"Content of '{filename}':\n{content}")
    except FileNotFoundError:
        print("File not found")
    except Exception as E:     #will work for any random error
        print("An error occured!")

def edit_file(filename):
    try:
        with open('sample.txt','a') as f:
            content=input('Enter data to be added : ')
            f.write(content + "\n")
            print( "content added to {filename} successfully!")
    except FileNotFoundError:
        print("File not found")
    except Exception as E:     #will work for any random error
        print("An error occured!")

def main():
    while True:
        print("File Management APP")
        print("1: Create File")
        print("2: View all Files")
        print("3: Delete File")
        print("4: Read File")
        print("5: Edit File")
        print("6: Exit")

        choice= input("Enter your choice from 1-6 : ")  
        if choice == '1':
            filename = input("Enter the name of file you want to create : ")
            create_file(filename)
        elif choice == '2':
            view_all_files()
        elif choice == '3':
            filename = input("Enter the name of file you want to delete : ")
            delete_file(filename)
        elif choice == '4':
            filename = input("Enter the name of file you want to read : ")
            read_file(filename)
        elif choice == '5':
            filename = input("Enter the name of file you want to edit : ")
            edit_file(filename)
        elif choice == '6':
            print("Goodbye! See you soon!")
            break
        else:
            print("In-Valid Syntax")     

if __name__ == "__main__":
    main()






