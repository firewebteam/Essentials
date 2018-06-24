import smtplib
'''Wysyłanie maila'''

content= 'Siema, tu Agent997, sprawdzam maila'
username = 'adresnadawcy@gmail.com'    #konieczne jest
#pswd = 'mojehaslo'
receiver = 'adresodbiorcy@gmail.com'

mail = smtplib.SMTP('smtp.gmail.com', 587)    #podlaczamy sie pod serwer
mail.ehlo()   #testowanie serwera
mail.starttls()  #metoda rozpoczynajaca haszowanie
mail.login(username,input('Podaj haslo'))        #podajemy maila nadawcy i jego haslo (input celem niepodawania hasla w czystej postaci)

mail.sendmail(username,receiver, content)        # podajemy nadawce, odbiorce i tresc wiadomosci (bez tytulu)
mail.close()