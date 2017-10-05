from Øving3 import Person
from Øving3 import Cipher

def main():

    Kryptering = Cipher.Affine()
    Håkon = Person.Sender(Kryptering)
    Toralf = Person.Receiver(Kryptering)
    Keil = Person.Hacker(Kryptering)
    Håkon.set_melding("just looking for some random words here you know")
    Håkon.send(Toralf)
    print(Kryptering.verify(Håkon,Toralf))
    Håkon.send(Keil)
    print(Kryptering.verify(Håkon,Keil))




main()
