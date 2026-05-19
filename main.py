from datetime import datetime

while True:
    print("\n1-Add note\n2-Show notes\n3-Delete note\n4-Delete all notes\n5-Exit")
    choice=input("Yapmak istediginiz islemi secin:")
    
    if choice=="1":
        note=input("Enter the note you want to save:")
        date=datetime.now().strftime("%d/%m/%Y %H:%M")

        with open("notes.txt", "a") as file:
            file.write("["+date+"] "+note+"\n")
        
        print("\nNote added...")

    elif choice=="2":
        try:
            with open("notes.txt", "r") as file:
                print("\nNotes:")
                print(file.read())

        except FileNotFoundError:
            print("\nNo notes found yet....")
    
    elif choice=="3":
        note_to_delete=input("Enter the note you want to delete:")

        try:
            with open("notes.txt","r") as file:
                notes=file.readlines()

            with open("notes.txt","w") as file:
                found=False

                for note in notes:
                    real_note = note.split("] ", 1)[1].strip()

                    if note_to_delete.strip() != real_note:
                        file.write(note)
                    else:
                        found=True
            
            if found:
                print("\nNote deleted...")
            else:
                print("\nNote not found...")

        except FileNotFoundError:
            print("\nNotes file not found...")

    elif choice=="4":
        with open("notes.txt","w") as file:
            pass
        print("\nAll notes deleted...")

    elif choice=="5":
        print("\nExiting...")
        break
    else:
        print("Invalid choice...")