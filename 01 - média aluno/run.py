from flask import Flask, render_template, request, redirect

# Cria uma instância do aplicativo Flask
app = Flask(__name__)

# Define a rota para a página inicial
@app.route("/")
def index():
   
    
    return render_template("lancar_notas.html")# Renderiza o template 'index.html' quando a rota '/' é acessada


# Define a rota para validar as notas, aceitando apenas requisições POST
@app.route("/lancar_notas", methods=['POST'])
def lancar_notas():
    # Obtém os dados do formulário enviados via POST
    try:
        nome_aluno = request.form["nome_aluno"]
        nota1 = float(request.form["nota1"])
        nota2 = float(request.form["nota2"])
        nota3 = float(request.form["nota3"])
        media = (nota1 + nota2 + nota3) / 3

        status = "Aprovado" if media >= 7.0 else "Reprovado"
        
        # Define o caminho do arquivo onde as notas serão armazenadas
        caminho_arquivo = 'models/notas.txt'

        # Abre o arquivo em modo de anexação (append) e adiciona os dados
        with open(caminho_arquivo, 'a') as arquivo:
            arquivo.write(f"{nome_aluno};{nota1};{nota2};{nota3};{media:.2f};{status}\n")

        # Redireciona o usuário de volta para a página inicial após o sucesso
        return redirect("/")

    except ValueError:
        # Se houver algum erro de valor, redireciona para a página inicial
        return redirect("/")


# Define a rota para consultar as notas
@app.route("/consulta")
def consultar_notas():
    notas = []  # Lista para armazenar as notas lidas do arquivo
    caminho_arquivo = 'models/notas.txt'

    # Abre o arquivo em modo de leitura
    with open(caminho_arquivo, 'r') as arquivo:
        # Lê cada linha do arquivo
        for nota in arquivo:
            # Divide a linha em partes usando ';' como delimitador
            item = nota.strip().split(';')
            # Adiciona a nota à lista como um dicionário
            notas.append({
                'nome_aluno': item[0],
                'nota1': item[1],
                'nota2': item[2],
                'nota3': item[3],
                'media': item[4],
                'status': item[5] 
            })

    # Renderiza o template 'consulta_notas.html'
    return render_template("consulta_notas.html", notas=notas)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
