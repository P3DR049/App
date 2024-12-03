from flask import Flask, render_template, request

app = Flask(__name__)

# Rota da Tela Inicial
@app.route('/')
def tela_inicial():
    return render_template('tela_inicial.html')

# Rota da Tela de Escolha
@app.route('/escolha', methods=['GET', 'POST'])
def tela_escolha():
    if request.method == 'POST':
        praia_nome = request.form['nome']
        localizacao = request.form['localizacao']
    else:
        praia_nome = "Praia Selecionada"
        localizacao = "Localização Desconhecida"
    return render_template('tela_escolha.html', praia_nome=praia_nome, localizacao=localizacao)

# Rota da Tela de Pescadores
@app.route('/pescadores', methods=['GET'])
def tela_pescadores():
    praia_nome = request.args.get('praia_nome', 'Praia Desconhecida')
    # Dados simulados
    dados_climaticos = {
        "temperatura": 28,
        "pressao": 1015,
        "vento": 20,
        "descricao": "Céu Limpo",
        "direcao_vento": "NE"
    }
    temperatura_agua = max(dados_climaticos['temperatura'] - 2, 0)
    nivel_mare = "Moderado"
    nivel_ressaca = "Leve"
    correnteza = "Fraca"
    especies = [
        {"especie": "Corvina", "periodo": "Julho a Novembro", "observacao": "Alta temporada"},
        {"especie": "Robalo", "periodo": "Outubro a Março", "observacao": "Proteção: Abril a Setembro"}
    ]
    return render_template(
        'tela_pescadores.html',
        praia_nome=praia_nome,
        dados_climaticos=dados_climaticos,
        temperatura_agua=temperatura_agua,
        nivel_mare=nivel_mare,
        nivel_ressaca=nivel_ressaca,
        correnteza=correnteza,
        especies=especies
    )

# Rota da Tela de Banhistas
@app.route('/banhistas', methods=['GET'])
def tela_banhistas():
    praia_nome = request.args.get('praia_nome', 'Praia Desconhecida')
    # Dados simulados
    dados_climaticos = {
        "temperatura": 30,
        "pressao": 1018,
        "vento": 15,
        "descricao": "Ensolarado",
        "direcao_vento": "SE"
    }
    temperatura_agua = max(dados_climaticos['temperatura'] - 2, 0)
    nivel_mare = "Leve"
    nivel_ressaca = "Leve"
    correnteza = "Fraca"
    return render_template(
        'tela_banhistas.html',
        praia_nome=praia_nome,
        dados_climaticos=dados_climaticos,
        temperatura_agua=temperatura_agua,
        nivel_mare=nivel_mare,
        nivel_ressaca=nivel_ressaca,
        correnteza=correnteza
    )

if __name__ == '__main__':
    app.run(debug=True)
