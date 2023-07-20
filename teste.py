from pandas import 

class player:
    
    def __init__(self, nome, lv):
        self.nome = nome
        self.lv = lv
    
    def uplv(self):
        self.lv = self.lv + 1
        print('Você upou para o lv', self.lv, '!!!')

#player 1

p1 = player("P1", 1)


#player 2

p2 = player("P2",2)

x = DataFrame({'A':[1]})


