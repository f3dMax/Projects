# Import the csv module, datetime module
import csv
import datetime as dt

print("Welcome to the Contact List Program")

# Function to import contacts from a CSV file
def import_csv(csv_filename):
   
    contacts = {}
    try:
        with open(csv_filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                name, phone, email, birthday_str = row
                birthday = dt.datetime.strptime(birthday_str, '%m/%d/%Y').date()
                contacts[name] = {'Phone': phone, 'Email': email, 'Birthday': birthday}
        print("Contacts imported successfully.")
        return contacts
    except FileNotFoundError:
        print(f"Error: The file {csv_filename} does not exist.")
        return None


def add_contact(contacts, name, phone, email, birthday):
    
    if name in contacts:
        print("Error: Contact already exists.")
        return False
    else:
        birthday_date = dt.datetime.strptime(birthday, '%m/%d/%Y').date()
        contacts[name] = {'Phone': phone, 'Email': email, 'Birthday': birthday_date}
        return True


def view_contacts(contacts):
    
    if not contacts:
        print("No contacts available.")
    else:
        
        pass

def delete_contact(contacts, name):
    
    if name in contacts:
        del contacts[name]
        return True
    else:
        print("Error: Contact does not exist.")
        return False


def next_birthday(contacts):
    
    pass


def save_csv(contacts, filename):
    
    pass


def main():
    
    pass


if __name__ == "__main__":
    main()
