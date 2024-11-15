
import util

def ler_dados_clientes():
    """Lê o arquivo de clientes e retorna uma lista de dicionários com dados dos clientes."""
    clientes = []
    with open('clientes.txt', 'r') as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(';')
            if len(dados) == 4:  # Verifica se há exatamente 4 valores
                nome, cidade, idade, renda = dados
                cliente = {
                    'nome': nome,
                    'cidade': cidade,
                    'idade': int(idade),
                    'renda_mensal': float(renda)
                }
                clientes.append(cliente)
    return clientes

def main():
    clientes = ler_dados_clientes()
    idades = [c['idade'] for c in clientes]
    rendas = [c['renda_mensal'] for c in clientes]
    print(f"Média de idade: {util.calcular_media(idades):.2f}")
    print(f"Média de renda: R${util.calcular_media(rendas):.2f}")

if __name__ == '__main__':
    main()
