import requests

def get_data_from_url(url):
    try:
        # Faz a requisição GET para a URL fornecida
        response = requests.get(url)
        
        # Verifica o status_code da resposta
        if response.status_code == 200:
            # Retorna o conteúdo da resposta se o status_code for 200
            return response.json()  # ou response.text, dependendo do formato esperado
        else:
            # Retorna uma mensagem de erro se o status_code não for 200
            return f"Falha ao obter as informações. Status code: {response.status_code}"
    
    except requests.exceptions.RequestException as e:
        # Captura exceções relacionadas à requisição e retorna uma mensagem de erro
        return f"Erro ao tentar acessar a URL: {e}"

# Exemplo de uso
if __name__ == "__main__":
    url = input("Digite a URL para a requisição GET: ")
    resultado = get_data_from_url(url)
    print(resultado)
