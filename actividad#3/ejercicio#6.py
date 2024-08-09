class Banco:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar (self, deposito):
        if deposito > 0:
            self.balance = self.balance +deposito
            print (f"Se depositaron {deposito}")
        else:
            print("El deposito debe ser positivo")

    def retirar (self, retiro):
        if retiro > 0 < self.balance:
            self.balance= self.balance -retiro
            print (f"Se retiraron {retiro}")

        else:
            print (f"El retiro debe ser positivo y ser menor al dinero que se tiene en la cuenta")
        

        
    def mostrar_balance (self):
        print(f"Hola {self.propietarios} con numero de cuenta {self.numero_cuenta}")
              
        print(f"El balance de tu cuenta es {self.balance}")

    def cuota (self):
        cuota = self.balance * 0.02
        self.balance -= cuota

        print(f"Se aplico una cuot del 2% y se retiraron {cuota}")



mi_banco = Banco("1123", "valery" , 0)
mi_banco.depositar(50000)
mi_banco.retirar(0)
mi_banco.mostrar_balance()
mi_banco.cuota()

mi_banco.mostrar_balance()
