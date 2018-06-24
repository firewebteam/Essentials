import smtplib
'''Wysyłanie maila'''
# WAZNE program wymaga aby zezwolic mniej bezpiecznym aplikacjom na dostęp do konta https://myaccount.google.com/lesssecureapps
content= 'Siema, tu Agent997, sprawdzam maila'
username = 'adresnadawcy@gmail.com'    #konieczne jest podanie adresu z ktorego sie wysyla i hasla
#pswd = 'mojehaslo'
receiver = 'adresodbiorcy@gmail.com'

mail = smtplib.SMTP('smtp.gmail.com', 587)    #podlaczamy sie pod serwer
mail.ehlo()   #testowanie serwera
mail.starttls()  #metoda rozpoczynajaca haszowanie
mail.login(username,input('Podaj haslo'))        #podajemy maila nadawcy i jego haslo (input celem niepodawania hasla w czystej postaci)

mail.sendmail(username,receiver, content)        # podajemy nadawce, odbiorce i tresc wiadomosci (bez tytulu)
mail.close()