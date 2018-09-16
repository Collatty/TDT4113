import random
import matplotlib.pyplot as plt

class Spiller:

    Name = ""



    def __init__(self):
        self.Resultat = []
        self.Valg = []

    def returner_aksjon(self,a):
        if a==0:
            return "stein"
        elif a==1:
            return "saks"
        elif a==2:
            return "papir"

    def motta_resultat(self, a, b):
        self.Valg.append(a)
        self.Resultat.append(b)

    def oppgi_navn(self):
        return self.Name

class Tilfeldig(Spiller):

    def __init__(self):
        Spiller.__init__(self)
        self.Name = "Tilfeldig"

    def velg_aksjon(self):
        a = random.randint(0,2)
        return self.returner_aksjon(a)

class Sekvensiell(Spiller):

    var = 0

    def __init__(self):
        Spiller.__init__(self)
        self.Name = "Sekvensiell"

    def velg_aksjon(self):
        self.var += 1
        return self.returner_aksjon((self.var-1) % 3)


class MestVanlig(Spiller):



    def __init__(self):
        Spiller.__init__(self)
        self.Name = "MestVanlig"

    def finn_mestVanlig(self):
        for i in range (0,len(self.Valg)):
            self.mestVanlig[self.Valg[i]]+=1
        #print(self.Valg)
        #print(self.mestVanlig)

    def velg_aksjon(self):
       self.mestVanlig=[0,0,0]
       self.finn_mestVanlig()
       mest = self.mestVanlig.index(max(self.mestVanlig))
       if mest == 0:
           return self.returner_aksjon(2)
       elif mest == 1:
           return self.returner_aksjon(0)
       elif mest == 2:
           return self.returner_aksjon(1)

       """
       
       if (self.mestVanlig[0]>self.mestVanlig[1]) and (self.mestVanlig[0]>self.mestVanlig[2]):
           return self.returner_aksjon(2)
       elif (self.mestVanlig[1]>self.mestVanlig[0]) and (self.mestVanlig[1]>self.mestVanlig[2]):
           return self.returner_aksjon(0)
       elif (self.mestVanlig[2]>self.mestVanlig[1]) and (self.mestVanlig[2]>self.mestVanlig[0]):
           return self.returner_aksjon(2)
       else:
           return self.returner_aksjon(random.randint(0,2))
        """
class Historiker(Spiller):




    def __init__(self, Husk):
        Spiller.__init__(self)
        self.Name = "Historiker"
        self.Husk = Husk
        self.HuskeListe = []


    def velg_aksjon(self):
        VanligsteValg = [0,0,0]
        self.HuskeListe = self.Valg[-self.Husk:]
        for i in range (0, (len(self.Valg)-self.Husk)):
            if self.Valg[i:i+self.Husk] == self.HuskeListe:
                VanligsteValg[self.Valg[i+self.Husk]]+=1

        if max(VanligsteValg) == VanligsteValg[0]:
            return self.returner_aksjon(2)
        elif max(VanligsteValg) == VanligsteValg[1]:
            return self.returner_aksjon(0)
        else:
            return self.returner_aksjon(1)



class enkelt_spill():
    a = ""
    b = ""
    resultat1 = 0
    resultat2 = 0
    spiller1_valg = 0
    spiller2_valg = 0

    def __init__(self, spiller1, spiller2):
        self.spiller1 = spiller1
        self.spiller2 = spiller2

    def gjennomfoer_spill(self):
        self.a = self.spiller1.velg_aksjon()
        self.b = self.spiller2.velg_aksjon()
        if self.a == "stein":
            self.spiller1_valg = 0
        elif self.a == "saks":
            self.spiller1_valg = 1
        elif self.a == "papir":
            self.spiller1_valg = 2
        if self.b == "stein":
            self.spiller2_valg = 0
        elif self.b == "saks":
            self.spiller2_valg = 1
        elif self.b == "papir":
            self.spiller2_valg = 2

        if self.a == "stein" and self.b == "saks":
            self.resultat1 = 1
            self.resultat2 = 0
        elif self.a == "saks" and self.b == "papir":
            self.resultat1 = 1
            self.resultat2 = 0
        elif self.a == "papir" and self.b == "stein":
            self.resultat1 = 1
            self.resultat2 = 0
        elif self.a == self.b:
            self.resultat1 = 0.5
            self.resultat2 = 0.5
        else:
            self.resultat1 = 0
            self.resultat2 = 1
        self.__str__()
        self.spiller1.motta_resultat(self.spiller2_valg, self.resultat1)
        self.spiller2.motta_resultat(self.spiller1_valg, self.resultat2)





    def __str__(self):
        print("Spiller 1 spilte " + self.a + " og spiller 2 spilte "+ self.b)
        if(self.resultat1==self.resultat2):
            print("Det ble uavgjort")
        elif self.resultat2>self.resultat1:
            print("Spiller 2 vant")
        else:
            print("Spiller 1 vant")




class MangeSpill:

    def __init__(self, spiller1, spiller2, antall_spill):
        self.spiller1 = spiller1
        self.spiller2 = spiller2
        self.antall_spill = antall_spill

    def arranger_enkeltspill(self):

        spill= enkelt_spill(self.spiller1, self.spiller2)
        spill.gjennomfoer_spill()


    def arranger_turnering(self):
        list = []
        for i in range (0,self.antall_spill):
            self.arranger_enkeltspill()
            list.append(sum(self.spiller1.Resultat)/len(self.spiller1.Resultat))

        print("Spiller 1 " + str(sum(self.spiller1.Resultat)) + " Spiller 2 " + str(sum(self.spiller2.Resultat)))
        plt.plot(list)
        plt.show()


def main():

    print("Skriv inn Spiller1, så Spiller 2, så antall games: \nran = tilfedig, sek = sekvensiell, mes = mest vanlig, his = historiker")
    spiller1 = input()
    spiller2 = input()
    antall_games = int(input())


    if spiller1 == "ran":
        Spiller1 = Tilfeldig()
    elif spiller1 == "sek":
        Spiller1 = Sekvensiell()
    elif spiller1 == "mes":
        Spiller1 = Tilfeldig()
    elif spiller1 == "his":
        Spiller1 = Tilfeldig()

    if spiller2 == "ran":
        Spiller2 = Tilfeldig()
    elif spiller2 == "sek":
        Spiller2 = Sekvensiell()
    elif spiller2 == "mes":
        Spiller2 = MestVanlig()
    elif spiller2 == "his":
        Spiller2 = Historiker(2)

    man = MangeSpill(Spiller1, Spiller2, antall_games)
    man.arranger_turnering()

main()

