#1
class Conta_bancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False #atributo protegido
        
    def __str__(self):
        return f"{self.titular} | {self.saldo}"
    
    @classmethod
    def ativar_conta(cls, conta):
        conta.ativo = True
        
conta1= Conta_bancaria("Aline", "0 reais")
print(conta1)
conta3 = Conta_bancaria("Carlos", 200)
print(f"Antes de ativar: Conta ativa? {conta3._ativo}")
Conta_bancaria.ativar_conta(conta3)
print(f"Depois de ativar: Conta ativa? {conta3._ativo}")

