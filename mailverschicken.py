import csv, smtplib, ssl
import os


for file in os.listdir("."):
    zuordnung = {file : file[:-4]+"@kgs-rastede.de"}
    print(zuordnung.get(file))
    
    #ni@kgs-rastede.de     file: ni.pdf
    #dict( "ni.pdf": "ni@kgs-rastede.de")

#ni.pdf    <<<<<      ni@kgs-rastede.de   

daten ={ 'moin': 'heisst hall', 'bis bald': 'verabschiedung' }

print(daten.get('moin'))


"""
message = "moin"
from_address = "my@gmail.com"
password = input("Type your password and press enter: ")

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(from_address, password)
    with open("contacts_file.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email, grade in reader:
            server.sendmail(
                from_address,
                email,
                message.format(name=name,grade=grade),
            )
"""