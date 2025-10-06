#1
class Conta_bancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False #atributo protegido
    
    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self._ativo
        
    def __str__(self):
        return f"{self.titular} | {self.saldo}"
    
    # método de classe que recebe uma conta e ativa
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True
        
conta1= Conta_bancaria("Aline", "0 reais")
print(conta1)

conta2 = Conta_bancaria("Carlos", 200)

print(f"Antes de ativar: Conta ativa? {conta2._ativo}")

Conta_bancaria.ativar_conta(conta2) # passa o objeto, não o valor

print(f"Depois de ativar: Conta ativa? {conta2._ativo}")

class ClienteBanco:
    def __init__(self, nome, idade, endereco, cpf, profissao):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.profissao = profissao
        self.ativo = False

    def __str__(self):
        return self.nome 
    
    def ativar_conta(self):
        return self.ativo == True


cliente1 = ClienteBanco("Ana", 30, "Rua A", "123.456.789-01", "Backend")
cliente2 = ClienteBanco("Luiza", 25, "Rua B", "987.654.321-01", "Estudante")
cliente3 = ClienteBanco("Vinny Neves", 40, "Rua C", "111.222.333-44", "Frontend")


cliente1.ativar_conta()
status_conta = "ativa" if cliente1.ativo else "inativa"

print(f"A conta do(a) {cliente1} está {status_conta}.")
