import csv, smtplib, ssl
import os

#test


for file in os.listdir("."):
    zuordnung = {file : file[:-4]+"@kgs-rastede.de"}
    print(zuordnung.get(file))
    
    #ni@kgs-rastede.de     file: ni.pdf
    #dict( "ni.pdf": "ni@kgs-rastede.de")

#ni.pdf    <<<<<      ni@kgs-rastede.de   




message = "moin"
from_address = "testtrashmail@gmx.de"
password = input("kgsrastede")     #gültige test adresse mit passwort

context = ssl.create_default_context()
with smtplib.SMTP_SSL("mail.gmx.net", 465, context=context) as server: 
    server.login(from_address, password)
    with open("contacts_file.csv") as file:   
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for file in os.listdir("."):
            server.sendmail(
                from_address,
                zuordnung,
                message,
            )

print("done")
