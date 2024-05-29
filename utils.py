import requests

def consulta_cep(cep):
    url = f"http://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if "erro" not in data:
            return data
        else:
            return None
    else:
        return None
