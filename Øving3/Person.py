from Øving3 import Cipher

class Person:

    def __init__(self, cipher):
        self.key = (0, 0)
        self.cipher = cipher
        self.melding = ""

    def set_key(self,key):
        self.key= key

    def get_key(self):
        return self.key

    def set_melding(self, melding):
        self.melding = melding

    def get_melding(self):
        return self.melding

    def operate_cipher(self):
        pass


class Sender(Person):

    def operate_cipher(self):
        return self.cipher.encode(self)

    def send(self, receiver):
        self.cipher.generate_keys(self, receiver)
        receiver.receive(self.operate_cipher())


class Receiver(Person):

    def operate_cipher(self):
        self.set_melding(self.cipher.decode(self))

    def receive(self, melding):
        self.set_melding(melding)
        self.operate_cipher()


class Hacker(Person):

    engelsk_ordbok = [line.rstrip('\n') for line in open('EngelskOrdbok.txt')]


    def __init__(self, cipher):
        Person.__init__(self, cipher)
        self.hits = 0

    def receive(self, melding):
        self.set_melding(melding)
        self.set_melding(self.hack(melding, self.cipher))

    def hack(self, melding, cipher):
        if isinstance(cipher, Cipher.Caesar):
            return self.hackCaesar(melding)
        elif isinstance(cipher, Cipher.Multiplication):
            return self.hackMultiplication(melding)
        elif isinstance(cipher, Cipher.Affine):
            return self.hackAffine(melding)
        elif isinstance(cipher, Cipher.Unbreakable):
            return self.hackUnbreakable(melding)
        else:
            return "Ukjent kryptering. Får ikke til å hacke ::(:(:(:(:(:(:(:("

    def hackCaesar(self, melding):
        self.set_melding(melding)
        hits = 0
        key = 0
        person = Person(self.cipher)
        person.set_melding(melding)
        for i in range(2, 95):
            person.set_key((i, 0))
            dekodet_forsøk = self.cipher.decode(person)
            dekodet_forsøk = dekodet_forsøk.split()
            for word in dekodet_forsøk:
                for match in self.engelsk_ordbok:
                    if word == match.rstrip():
                        hits += 1
            if hits > self.hits:
                self.hits = hits
                hits = 0
                key = i
            else:
                hits = 0
        self.set_key((key, 0))
        return self.cipher.decode(self)

    def hackMultiplication(self, melding):
        self.set_melding(melding)
        hits = 0
        key = 0
        person = Person(self.cipher)
        person.set_melding(melding)
        for i in range(2, 95):
            person.set_key((0, i))
            dekodet_forsøk = self.cipher.decode(person)
            dekodet_forsøk = dekodet_forsøk.split()
            for word in dekodet_forsøk:
                for match in self.engelsk_ordbok:
                    if word == match.rstrip():
                        hits += 1
            if hits > self.hits:
                self.hits = hits
                hits = 0
                key = i
            else:
                hits = 0
        self.set_key((0,key))
        return self.cipher.decode(self)

    def hackAffine(self, melding):
        person = Person(self.cipher)
        person.set_melding(melding)
        nøkler = [(x, y) for x in range(95) for y in range(95)]
        hits = [0 for x in range(95*95)]
        for nøkkel in nøkler:
            person.set_key(nøkkel)
            dekodet_melding = self.cipher.decode(person)
            for ord in dekodet_melding.split():
                if ord in self.engelsk_ordbok:
                    hits[nøkler.index(nøkkel)] += 1
        beste_nøkkel = nøkler[hits.index(max(hits))]
        self.set_key(beste_nøkkel)
        return self.cipher.decode(self)

    def hackUnbreakable(self, melding):
        person = Person(self.cipher)
        person.set_melding(melding)
        nøkler = [0 for x in range (len(self.engelsk_ordbok))]
        hits = [0 for x in range (len(self.engelsk_ordbok))]
        decode_key = ""
        index = 0
        for word in self.engelsk_ordbok:
            for bokstav in word:
                decode_key+= self.cipher.ascii_string[(95-self.cipher.ascii_string.index(bokstav)) % 95]
            nøkler[index] = decode_key
            decode_key = ""
            index+=1
        for nøkkel in nøkler:
            person.set_key((nøkkel,0))
            dekodet_melding = self.cipher.decode(person)
            for ord in dekodet_melding.split():
                if ord in self.engelsk_ordbok:
                    hits[nøkler.index(nøkkel)] += 1
        beste_nøkkel = nøkler[hits.index(max(hits))]
        self.set_key((beste_nøkkel,0))
        return self.cipher.decode(self)




