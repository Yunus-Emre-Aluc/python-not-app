from datetime import datetime
import json
import os

while True:
    print("\n1-Add note\n2-Show notes\n3-Delete note\n4-Delete all notes\n5-Exit")
    choice=input("Enter your choice:")
    
    if choice=="1":
        note=input("Enter the note you want to save:")
        date=datetime.now().strftime("%d/%m/%Y %H:%M")

        if os.path.exists("notes.json") and os.path.getsize("notes.json")>0:
            with open("notes.json","r",encoding="utf-8") as file:
                notes=json.load(file)
        else:
            notes=[]

        notes.append(f"[{date}] {note}")

        with open("notes.json","w",encoding="utf-8") as file:
            json.dump(notes,file,ensure_ascii=False,indent=4)
        
        print("\nNote added...")

    elif choice=="2":
        try:
            with open("notes.json","r") as file:
                print("\nNotes:")
                result=json.load(file)
                print(result)

        except FileNotFoundError:
            print("\nNo notes found yet....")
    
    elif choice=="3":
        note_to_delete=input("Enter the note you want to delete:")

        try:
            with open("notes.json","r",encoding="utf-8") as file:
                notes=json.load(file)

            found=False
            updated_notes=[]

            for note in notes:
                real_note=note.split("] ",1)[1].strip()

                if note_to_delete.strip()!=real_note:
                    updated_notes.append(note)
                else:
                    found=True

            with open("notes.json","w",encoding="utf-8") as file:
                json.dump(updated_notes,file,ensure_ascii=False,indent=4)

            if found:
                print("\nNote deleted...")
            else:
                print("\nNote not found...")

        except FileNotFoundError:
            print("\nNotes file not found...")

    elif choice=="4":
        with open("notes.json","w",encoding="utf-8") as file:
            json.dump([],file,ensure_ascii=False,indent=4)
            
        print("\nAll notes deleted...")

    elif choice=="5":
        print("\nExiting...")
        break
    else:
        print("Invalid choice...")