import re

def extrair_informacoes(anuncio):
    modalidade = None
    if "aluguel" in anuncio or "alugo" in anuncio or "alugar" in anuncio:
        modalidade = "Aluguel"
    elif "venda" in anuncio or "vendo" in anuncio or "vender" or "venda" in anuncio:
        modalidade = "Venda"

    tipo = None
    if "casa" in anuncio.lower():
        tipo = "Casa"
    elif "apartamento" in anuncio.lower():
        tipo = "Apartamento"

    logradouros = ['Rua', 'Avenida', 'rua', 'avenida']

    endereco = None

    logradouros_pattern = "|".join(logradouros)  
    regex_endereco = rf"(?i)({logradouros_pattern})\s[\w\sa-zA-Zçãáàâãéêíóôú]+(?:\s[\w\sa-zA-Zçãáàâãéêíóôú]+)*,\s*(numero\s*)?(\d+)"  # Cria a expressão regular


    match_endereco = re.search(regex_endereco, anuncio)
    if match_endereco:
        endereco = match_endereco.group()

    cep = None
    match_cep = re.search(r"\b\d{5}-\d{3}\b", anuncio)  
    if match_cep:
        cep = match_cep.group()

    area = None
    match_area = re.search(r"(\d+)\s(metros quadrados|m2)", anuncio)
    if match_area:
        area = match_area.group(1)

    valor = None
    match_valor = re.search(r"(\d{1,3}(?:\.\d{3})*(?:,\d{2}))", anuncio)  
    if match_valor:
        valor = match_valor.group(1)


    telefones = []
    match_telefone = re.findall(r"\d{4}-\d{4}|\d{5}-\d{4}", anuncio)  
    telefones = match_telefone


    responsavel = None

    sentencas = anuncio.split('.')
    ultima_sentenca = sentencas[-2].strip() if len(sentencas) > 1 else sentencas[-1].strip()

    match_responsavel = re.search(r"([A-Z][a-zA-Zçãáàâéêíóôú]+(?: [A-Z][a-zA-Zçãáàâéêíóôú]+){1,2})", ultima_sentenca)

    if match_responsavel:
        responsavel = match_responsavel.group(1)  

    print(f"Modalidade: {modalidade}")
    print(f"Tipo: {tipo}")
    print(f"Endereco: {endereco if endereco else 'nao informado'}")
    print(f"CEP: {cep if cep else 'nao informado'}")
    print(f"Area: {area if area else 'nao informado'}")
    print(f"Valor: {valor if valor else 'nao informado'}")
    print(f"Telefone{'s' if len(telefones) > 1 else ''}: {', '.join(telefones) if telefones else 'nao informado'}")
    print(f"Responsavel: {responsavel}")

anuncio = input()
extrair_informacoes(anuncio)
