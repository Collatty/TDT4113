from Øving3 import Utility
from Øving3 import Person
import random
import math


class Cipher:

    ascii_string = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    lengt_of_legal_alphabet = 95

    def encode(self,Person):
        pass

    def decode(self,Person):
        pass

    def generate_keys(self, Person1, Person2):
        pass

    def verify(self, Person1, Person2):
        if isinstance(Person2, Person.Hacker):
            return "Hackingen ga følgende resultat: " + str(Person1.get_melding() == Person2.get_melding()) + "\n" + Person2.get_melding()
        original_melding = Person1.get_melding()
        kodet_melding = self.encode(Person1)
        Person2.set_melding(kodet_melding)
        dekodet_melding = self.decode(Person2)
        Person2.set_melding(dekodet_melding)
        return "Verifiseringstesten gir deg resultatet:\n"+original_melding+"\n"+kodet_melding+"\n"+dekodet_melding+"\n"+str(original_melding == dekodet_melding) \
            if isinstance(kodet_melding, str) else "Verifiseringstesten gir deg resutatet: "+str(original_melding ==dekodet_melding)



class Caesar(Cipher):

    def encode(self, Person):
        kodet_melding = ""
        for bokstav in Person.get_melding():
                kodet_melding += self.ascii_string[(self.ascii_string.index(bokstav)+Person.get_key()[0]) % 95]
        return kodet_melding

    def decode(self, Person):
        dekodet_melding = ""
        for bokstav in Person.get_melding():
            dekodet_melding += self.ascii_string[(self.ascii_string.index(bokstav)-Person.get_key()[0]) % 95]
        return dekodet_melding

    def generate_keys(self, Person1, Person2):
        key = random.randint(2, 94)
        Person1.set_key((key, 0))
        if isinstance(Person2, Person.Receiver):
            Person2.set_key((key, 0))


class Multiplication(Cipher):

    def encode(self, Person):
        kodet_melding = ""
        for bokstav in Person.get_melding():
            kodet_melding += self.ascii_string[(self.ascii_string.index(bokstav)*Person.get_key()[1]) % 95]
        return kodet_melding

    def decode (self, Person):
        dekodet_melding = ""
        for bokstav in Person.get_melding():
            dekodet_melding += self.ascii_string[(self.ascii_string.index(bokstav)*Person.get_key()[1]) % 95]
        return dekodet_melding

    def generate_keys(self, Person1, Person2):
        gcd = 0
        while gcd != 1:
            encode_key = random.randint(1, 94)
            gcd = math.gcd(encode_key,self.lengt_of_legal_alphabet)
        decode_key = Utility.modular_inverse(encode_key, self.lengt_of_legal_alphabet)
        Person1.set_key((0,encode_key))
        if isinstance(Person2, Person.Receiver):
            Person2.set_key((0,decode_key))


class Affine(Cipher):

    def __init__(self):
        self.caesar = Caesar()
        self.multiplication = Multiplication()

    def encode(self, Person):
        original_melding = Person.get_melding()
        kodet_melding = self.multiplication.encode(Person)
        Person.set_melding(kodet_melding)
        kodet_melding = self.caesar.encode(Person)
        Person.set_melding(original_melding)
        return kodet_melding

    def decode(self, Person):
        melding = Person.get_melding()
        dekodet_melding = self.caesar.decode(Person)
        Person.set_melding(dekodet_melding)
        dekodet_melding = self.multiplication.decode(Person)
        Person.set_melding(melding)
        return dekodet_melding

    def generate_keys(self,Person1,Person2):
        key_caesar = random.randint(1, 94)
        gcd = 0
        while gcd != 1:
            encode_key = random.randint(1, 94)
            gcd = math.gcd(encode_key, self.lengt_of_legal_alphabet)
        decode_key = Utility.modular_inverse(encode_key,self.lengt_of_legal_alphabet)
        Person1.set_key((key_caesar, encode_key))
        print(key_caesar,encode_key,decode_key)
        if isinstance(Person2, Person.Receiver):
            Person2.set_key((key_caesar, decode_key))

# En bedre krypteringsversjon av unbreakable enn å bare ha et kodeord
"""
class Unbreakable(Cipher):

    def encode(self,Person):
        kodet_melding = ""
        for i in range (0, len(Person.get_melding())):
            kodet_melding += self.ascii_string[(self.ascii_string.index(Person.get_melding()[i]) + self.ascii_string.index(Person.get_key()[0][i])) % 95]
        return kodet_melding

    def decode(self,Person):
        dekodet_melding = ""
        for i in range (0, len(Person.get_melding())):
            dekodet_melding += self.ascii_string[(self.ascii_string.index(Person.get_melding()[i]) + self.ascii_string.index(Person.get_key()[0][i])) % 95]
        return dekodet_melding

    def generate_keys(self, Person1, Person2):
        keyword = ""
        decode_key = ""
        for bokstav in Person1.get_melding():
            keyword += self.ascii_string[((self.ascii_string.index(bokstav)) + random.randint(0, 94)) % 95]
        for bokstav in keyword:
            decode_key += self.ascii_string[(95-self.ascii_string.index(bokstav)) % 95]
        Person1.set_key((keyword,0))
        if isinstance(Person2,Person.Receiver):
            Person2.set_key((decode_key,0))
"""
class Unbreakable(Cipher):

    def encode(self,Person):
        kodet_melding = ""
        for i in range(0, len(Person.get_melding())):
            kodet_melding += self.ascii_string[(self.ascii_string.index(Person.get_melding()[i]) +
                             self.ascii_string.index(Person.get_key()[0][i % (len(Person.get_key()[0]))])) % 95]
        return kodet_melding

    def decode(self,Person):
        dekodet_melding = ""
        for i in range(0, len(Person.get_melding())):
            dekodet_melding += self.ascii_string[(self.ascii_string.index(Person.get_melding()[i]) +
                             self.ascii_string.index(Person.get_key()[0][i % (len(Person.get_key()[0]))])) % 95]
        return dekodet_melding

    def generate_keys(self, Person1, Person2):
        file = open('EngelskOrdbok.txt', 'r')
        mulige_ord = file.readlines()
        file.close()
        #keyword = mulige_ord[random.randint(0, len(mulige_ord)-1)].strip()
        keyword = "pizza"
        decode_key = ""
        for bokstav in keyword:
            decode_key += self.ascii_string[(95-self.ascii_string.index(bokstav)) % 95]
        Person1.set_key((keyword, 0))
        if isinstance(Person2, Person.Receiver):
            Person2.set_key((decode_key, 0))

class RSA(Cipher):

    def encode(self, Person):
        kodet_liste_med_tall = Utility.blocks_from_text(Person.get_melding(), 1)
        for i in range(0, len(kodet_liste_med_tall)):
            kodet_liste_med_tall[i] = pow(kodet_liste_med_tall[i],Person.get_key()[1], Person.get_key()[0])
        return kodet_liste_med_tall

    def decode(self,Person):
        dekodet_liste_med_tall = Person.get_melding()
        for i in range(0, len(Person.get_melding())):
            dekodet_liste_med_tall[i] = pow(Person.get_melding()[i], Person.get_key()[1], Person.get_key()[0])
        return Utility.text_from_blocks(dekodet_liste_med_tall, 8)

    def generate_keys(self, Person1, Person2):
        prime1 = 0
        prime2 = 0
        gcd = 0
        while gcd != 1:  # Sjekker at nummeret som genereres har modulær invers med hensyn på phi
            while prime1 == prime2:  #Kjører til primtallene er forskjellig
                prime1 = Utility.generate_random_prime(8)
                prime2 = Utility.generate_random_prime(8)
            prime_multiplied = prime1*prime2
            phi = (prime1-1)*(prime2-1)
            random_number = random.randint(3, phi-1)
            gcd = math.gcd(random_number,phi)
        inverse_random_number = Utility.modular_inverse(random_number,phi)
        Person1.set_key((prime_multiplied, random_number))
        if isinstance(Person2, Person.Receiver):
            Person2.set_key((prime_multiplied, inverse_random_number))

