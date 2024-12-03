def calcular_temperatura_agua(temperatura_ar):
    """Calcula a temperatura da água baseada na temperatura do ar."""
    return max(temperatura_ar - 2, 0)

def calcular_nivel_mare(pressao, vento_kph, direcao):
    """Calcula o nível da maré com base na pressão e vento."""
    nivel_base = 1.0
    pressao_ajuste = 0.3 if pressao < 1000 else -0.3 if pressao > 1020 else 0
    vento_ajuste = 0.5 if vento_kph > 50 and direcao in ["NE", "E", "SE"] else -0.5 if vento_kph > 50 and direcao in [
        "S", "SW", "W"] else 0
    nivel_final = max(0, nivel_base + pressao_ajuste + vento_ajuste)
    if nivel_final < 1.5:
        return nivel_final, "Leve"
    elif nivel_final < 2.5:
        return nivel_final, "Moderado"
    else:
        return nivel_final, "Alto"

def calcular_nivel_ressaca(vento_kph):
    """Determina o nível de ressaca com base na velocidade do vento."""
    if vento_kph > 50:
        return "Alta"
    elif vento_kph > 30:
        return "Moderada"
    else:
        return "Leve"

def calcular_correnteza(vento_kph):
    """Determina o nível de correnteza com base na velocidade do vento."""
    if vento_kph > 60:
        return "Alta"
    elif vento_kph > 40:
        return "Moderada"
    else:
        return "Leve"
