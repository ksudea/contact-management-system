# Data Storage
contact_storage = {}

# FUnctions 
import random
import re

def add_contact(name, email, phone, misc):
  if email == "":
    unique_id = phone
  else: 
    unique_id = email
  print(f"Your contact identifier is {unique_id}. This cannot be edited.")
  contact_info = {"name": name, "email": email, "phone": phone, "misc": misc}  
  contact_storage.update({unique_id: contact_info})
  print("Added new contact!")

def edit_contact(id, choice, new_info):
  if choice == 1:
    contact_storage[id]["name"] = new_info
  elif choice == 2:
    if new_info == "" and contact_storage[id]["phone"] == "":
       print("Error: both e-mail and phone number cannot be empty.")
       return
    else:
       contact_storage[id]["email"] = new_info
  elif choice == 3:
    if new_info == "" and contact_storage[id]["email"] == "":
       print("Error: both e-mail and phone number cannot be empty.")
       return
    else:
       contact_storage[id]["phone"] = new_info
  elif choice == 4:
    contact_storage[id]["misc"] = new_info
  else:
    print("Could not edit contact!")
    return
  print("Updated contact!")

def delete_contact(id):
  try:
    contact_storage.pop(id)
  except KeyError:
    print("Cannot delete: No contact with this ID in the directory.")
  except Exception as e:
    print(f"Unexpected error: {e}")
  else: 
    print(f"Successfully deleted contact {id}.")

def search(id):
  try:
    contact_info = contact_storage.get(id, False)
    if contact_info == False:
      print("No contact with this ID in the directory.")
      return
    print(f"Contact {id}")
    for key, value in contact_info.items():
      print(f"{key}:    {value}")
  except KeyError:
    print("No contact with this ID in the directory.")
  except Exception as e:
    print(f"Unexpected error: {e}")

def display_all():
  for key in contact_storage.keys():
    search(key)

def export_contacts():
  pass

def import_contacts():
  pass

# Input handling, validation, and passing to functions
validateName = "\b([A-Z-,a-z. ']{2,})+"
validatePhoneNumberRegex = "/^\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$/"
validateEmailRegex = "^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$"

def get_valid_name():
  name_collected = False
  while not name_collected:
    name = input("Contact name: ")
    if name == "":
       name_collected = True
    match = re.search(r"\b([A-Z-,a-z. ']{2,})+", name)
    if match != None:
          name_collected = True
    else:
       print("Wrong formatting! Make sure the name is more than 2 chars and \n the characters are valid.")
  return name

def get_valid_email():
  email_collected = False
  while not email_collected:
    contact_email = input("Input valid contact e-mail(format: example@domain.com): ")
    if contact_email == "":
        email_collected = True
    match = re.search(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,4}$", contact_email)
    if match != None:
        email_collected = True
    else:
        print("Wrong formatting! Make sure this is a valid e-mail address.")
  return contact_email

def get_valid_phone():
  phone_collected = False
  while not phone_collected:
    print("Valid phone number format: XXXXXXXXXX or +XXXXXXXXXXX \n 10 digits without country code, 12 digits with country code")
    contact_phone = input("Input valid contact phone number: ")
    if contact_phone == "":
       phone_collected = True
    match = re.search(r"^(?=.{10,12}$)\+?\d{1,4}?\(?\d{1,3}?\)?\d{1,4}\d{1,4}\d{1,9}$", contact_phone)
    if match != None:
        phone_collected = True
    else:
        print("Wrong formatting!")
  return contact_phone

def handle_add_contact():
      print("Add a new contact: \n Each contact must have at least a phone number OR e-mail. \n Each contact must have a name.")
      print("Press ENTER to bypass any inputs.")

      contact_name = get_valid_name()
      contact_email = get_valid_email()
      contact_phone = get_valid_phone()
      
      if contact_email == "" and contact_phone == "":
        print("You must enter at least one of: phone number, e-mail. Try again!")
      else:
        contact_misc = input("Add anything else, like notes or an address: ")
        add_contact(contact_name, contact_email, contact_phone, contact_misc)

def handle_edit_contact():
  print("Enter the unique id of the contact you would like to edit.")
  try:
    unique_id = input("Enter unique_id: ")
    contact_entry = contact_storage.get(unique_id, False)
    if contact_entry == False:
        print("Error: no contact with this ID exists.")
    else:
        search(unique_id)
        print("""What would you like to change?
                1. Name
                2. E-mail
                3. Phone number
                4. Misc """)
        choice = int(input("Choose an item to edit (1-4): "))
        print(choice)
    #   new_info = ""
        if choice == 1:
            new_info = get_valid_name()
            edit_contact(unique_id, choice, new_info)
        elif choice == 2:
            new_info = get_valid_email()
            edit_contact(unique_id, choice, new_info)
        elif choice == 3:
            new_info = get_valid_phone()
            edit_contact(unique_id, choice, new_info)
        elif choice == 4:
            new_info = input("New additional info (notes, address, etc): ")
            edit_contact(unique_id, choice, new_info)
        else:
            print("Error! Cannot edit.")
  except (ValueError, TypeError):
      print("Error! Remember, enter an integer between 1-4 as an option.")
  except KeyError:
     print("Error! This ID is probably incorrect.")
  except Exception as e:
      print(f"An error occurred: {e}")


if __name__ == '__main__':
 print("""Welcome to Contact Manager, your premier contact management app!

                Menu:
                1. Add a new contact
                2. Edit an existing contact
                3. Delete a contact
                4. Search for a contact
                5. Display all contacts
                6. Export contacts to a text file
                7. Import contacts from a text file *BONUS*
                8. Quit

            """)
 run_program = True
 while run_program:
   try:
      action = int(input("Enter your choice (1-8):"))
      if action == 1:
        handle_add_contact()
      elif action == 2:
        handle_edit_contact()    
      elif action == 3:
        id = input("Enter unique id of contact:")
        delete_contact(id)
      elif action == 4:
        id = input("Enter unique id of contact:")
        search(id)
      elif action == 5:
        display_all()
      elif action == 6:
        pass
      elif action == 7:
        pass
      elif action == 8:
        run_program = False
      else:
        print("Please enter an integer between 1-8 to make a choice on the menu.")
   except (ValueError, TypeError):
      print("Error! Remember, enter an integer between 1-8.")
   except Exception as e:
      print(f"An error occurred: {e}")
 print("Thanks for using the app!")