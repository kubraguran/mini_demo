class Add_notes:
    def __init__(self,title,note):
        self.title = title
        self.note = note
        self.notes = {}

    def add_note(self,title,note):
        if title not in self.notes:
            self.notes[title] = note



    def show_notes(self):
        print(self.notes.items())



    def delete_notes(self,title):
        if title in self.notes:
            del self.notes[title]




def asked():
    return int(input(f"hey, welcome! would like to add some notes? For press '1' \n"))
  

def mynotes():
    add_notes = Add_notes(title="Title", note="Note")

    while True:
        val = asked()

        if val == 1:
           title  = input("enter your title: \n")
           note   = input("enter your note: \n")
           add_notes.add_note(title,note)


        elif val == 2:
            title = input("which title would you like to delete ?")
            add_notes.delete_notes(title)

        else:
           add_notes.show_notes()
           break

    
    
mynotes()


# def ask():
#     return input("devam mi degil mi y or n")

# def deneme():
#     while True:
#         val = ask()
#         if val == 'y':
#             print("denediniz")

#             break



# deneme()