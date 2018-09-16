
import random



class Random:





    def choose_action(self):

        return random.randint(0,2)

    def recieve_result(self,result):
        return result

    def produce_name(self):
        return "Random"



class Sequential:

    Option = 0

    def choose_action(self):
        if self.Option==2:
            self.Option=0
            return 2
        else:
            self.Option += 1
            return self.Option-1

    def recieve_result(self,result):
        return result

    def produce_name(self):
        return "Sequential"

class Analytical:

    Motstandertrekk = []

    def optimal_move(self):
        a = self.Motstandertrekk.count(0)
        if self.Motstandertrekk.count(1)>a:
            a = self.Motstandertrekk.count(1)
        elif self.Motstandertrekk.count(2)>a:
            a = self.Motstandertrekk.count(2)
        if a == 0:
            return 2
        elif a == 1:
            return 0
        else:
            return 1


    def choose_action(self):
        if len(self.Motstandertrekk) == 0:
            return random.randint(0,2)
        else:
            return self.optimal_move()

    def recieve_result(self,result):
        return result

    def produce_name(self):
        return "Analytical"

class Historical:

    Husk = 0
    Motstandertrekk = []

    def optimal_move(self):
        count = 0
        if self.Husk==0:
            return random.randint(0,2)
        else:
            sekvens = self.Motstandertrekk.index(self, len(self.Motstandertrekk) - self.Husk-1, len(self.Motstandertrekk)-1)
            for tall in self.Motstandertrekk:
                count +=1
                if tall == sekvens[0]:
                    for i in range(0,len(sekvens)):
                        if self.Motstandertrekk[count]==sekvens[i]:



    def choose_action(self):

        return

    def recieve_result(self,result):
        return result

    def produce_name(self):
        return "Historical"
    def
