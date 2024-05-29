class Usuario:
    def __init__(self, nome, telefone, cpf, email, nome_social, endereco, senha):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.email = email
        self.nome_social = nome_social
        self.endereco = endereco
        self.senha = senha

    def to_dict(self):
        return {
            "nome": self.nome,
            "telefone": self.telefone,
            "cpf": self.cpf,
            "email": self.email,
            "nome_social": self.nome_social,
            "endereco": self.endereco,
            "senha": self.senha
        }
