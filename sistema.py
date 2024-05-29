import re
import bcrypt
from pymongo import MongoClient
from usuario import Usuario
from utils import consulta_cep

class SistemaCadastroLogin:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.usuarios = self.db['usuarios']

    def cadastrar_usuario(self, nome, telefone, cpf, email, nome_social, cep, numero_residencia, senha):
        if not re.match(r'^\d{6}$', senha):
            return "A senha deve ter exatamente 6 dígitos numéricos!"
        
        if self.usuarios.find_one({"email": email}):
            return "E-mail já cadastrado!"
        
        if self.usuarios.find_one({"cpf": cpf}):
            return "CPF já cadastrado!"
        
        endereco = consulta_cep(cep)
        if not endereco:
            return "CEP inválido ou não encontrado!"
        
        endereco_completo = {
            "cep": cep,
            "logradouro": endereco['logradouro'],
            "bairro": endereco['bairro'],
            "cidade": endereco['localidade'],
            "estado": endereco['uf'],
            "numero": numero_residencia
        }
        
        hashed_password = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
        
        usuario = Usuario(nome, telefone, cpf, email, nome_social, endereco_completo, hashed_password)
        self.usuarios.insert_one(usuario.to_dict())
        
        return "Usuário cadastrado com sucesso!"
    
    def login_usuario(self, email, senha):
        if not re.match(r'^\d{6}$', senha):
            return "A senha deve ter exatamente 6 dígitos numéricos!"
        
        user = self.usuarios.find_one({"email": email})
        
        if not user:
            return "Usuário não encontrado!"
        
        if bcrypt.checkpw(senha.encode('utf-8'), user['senha']):
            return "Login bem-sucedido!"
        else:
            return "Senha incorreta!"
