class car:
    nome = None
    ano = None
    cor = None
    velM = None
    velA = None
    estado = None

    def ligar(self):
        self.estado = "ligado"
    def desligar(self):
        self.estado = "desligado"
        self.parar()
    def parar(self):
        self.velA = 0
        print("Carro parado")
    def acelerar(self, vel):
        if self.estado == "ligado":
            self.velA += vel
        if self.velA > self.velM:
            self.velA = self.velM
        else:None

fusca = car()
fusca.nome = "Fusca"
fusca.ano = 1965
fusca.cor = "Preto"
fusca.velM = 80
fusca.velA = 20
fusca.estado = "ligado"

ferrari = car()
ferrari.nome = "Ferrari_sr2000"
ferrari.ano = 2014
ferrari.cor = "Vermelho"
ferrari.velM = 300
ferrari.velA = 0
ferrari.estado = "desligado"

fusca.acelerar(20)
ferrari.acelerar(200)
fusca.desligar()
ferrari.ligar()
ferrari.acelerar(320)
ferrari.parar()
ferrari.desligar()
fusca.ligar()
fusca.acelerar(100)
fusca.desligar()
