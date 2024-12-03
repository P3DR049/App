import requests

API_KEY = "e34b3771930e4e90bcd102912242911"
BASE_URL = "http://api.weatherapi.com/v1/current.json"

def obter_dados_climaticos(localizacao):
    """Obtém os dados climáticos de uma localização específica."""
    try:
        response = requests.get(BASE_URL, params={
            "key": API_KEY,
            "q": localizacao,
            "lang": "pt"
        })
        data = response.json()
        if response.status_code == 200 and "current" in data:
            return {
                "temperatura": data["current"].get("temp_c", 0),
                "pressao": data["current"].get("pressure_mb", 0),
                "vento": data["current"].get("wind_kph", 0),
                "descricao": data["current"]["condition"]["text"],
                "direcao_vento": data["current"].get("wind_dir", "--")
            }
    except Exception as e:
        print(f"Erro ao obter dados climáticos: {e}")
        return {"erro": "Não foi possível obter os dados climáticos."}

especies_por_praia = {
    "Saquarema": [
        {"especie": "Corvina", "periodo": "Julho a Novembro", "observacao": "Alta temporada"},
        {"especie": "Robalo", "periodo": "Outubro a Março", "observacao": "Proteção: Abril a Setembro"},
        {"especie": "Pampo", "periodo": "Abril a Outubro", "observacao": "Sazonal"}
    ],
    "Cabo Frio": [
        {"especie": "Sardinha verdadeira", "periodo": "Maio a Outubro", "observacao": "Sazonal, respeitar defeso"},
        {"especie": "Cavalinha", "periodo": "Janeiro a Dezembro", "observacao": "Disponível o ano inteiro"},
        {"especie": "Galo", "periodo": "Abril a Agosto", "observacao": "Proteger durante reprodução"}
    ],
    "Armação dos Búzios": [
        {"especie": "Moreias", "periodo": "Janeiro a Dezembro", "observacao": "Sem defeso específico"},
        {"especie": "Enchova", "periodo": "Abril a Junho", "observacao": "Sazonal"},
        {"especie": "Paru-cinza", "periodo": "Abril a Setembro", "observacao": "Proteção: Outubro a Março"}
    ],
    "Copacabana": [
        {"especie": "Anchova", "periodo": "Março a Junho", "observacao": "Alta temporada"},
        {"especie": "Linguado", "periodo": "Setembro a Novembro", "observacao": "Proteção no resto do ano"},
        {"especie": "Tainha", "periodo": "Maio a Agosto", "observacao": "Respeitar defeso"}
    ]
}
