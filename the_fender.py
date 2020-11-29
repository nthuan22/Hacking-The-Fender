#import the CSV module
import csv

#import the json module.
import json

# create a new list and save it to the variable compromised_users
compromised_users = []

#open up the file itself. Store it in a file object called password_file. 
with open('passwords.csv') as password_file:
  #Pass the password_file object holder to CSV reader for parsing. 
  password_csv = csv.DictReader(password_file)

  #Create a for loop and save each row of the CSV into the temporary variable password_row
  for password_row in password_csv:
    #print(password_row['Username'])
    compromised_users.append(password_row['Username'])

#Start a new with block, opening a file called compromised_users.txt
with open('compromised_users.txt', 'w') as compromised_user_file:
  #Iterate over each of your compromised_users.
  for compromised_user in compromised_users:
    compromised_user_file.write(compromised_user)

#Open a new JSON file in write-mode called boss_message.json.
with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}
  json.dump(boss_message_dict, boss_message)

#Create a new with block and open "new_passwords.csv" in write-mode.
with open('new_passwords.csv', 'w') as new_passwords_obj:
  slash_null_sig = """
   _  _     ___   __  ____ 
  / )( \   / __) /  \(_  _)
  ) \/ (  ( (_ \(  O ) )(
  \____/   \___/ \__/ (__)
   _  _   __    ___  __ _  ____  ____           
  / )( \ / _\  / __)(  / )(  __)(    \    
  ) __ (/    \( (__  )  (  ) _)  ) D ( 
  \_)(_/\_/\_/ \___)(__\_)(____)(____/
          ____  __     __   ____  _  _
   ___   / ___)(  )   / _\ / ___)/ )( \
   (___)  \___ \/ (_/\/    \\___ \) __ (
          (____/\____/\_/\_/(____/\_)(_/
  __ _  _  _  __    __ 
  (  ( \/ )( \(  )  (  )
  /    /) \/ (/ (_/\/ (_/\
  \_)__)\____/\____/\____/              
  """
  new_passwords_obj.write(slash_null_sig)
