import json

# Exemplo de string JSON
json_string = '''
{
    "teste": {
        "id": "123"
    },
    "itensConsulta": [
        {
            "status": "ativo",
            "identificacao": {
                "numero": "123",
                "versao": "1.0",
                "numeroItem": "001"
            },
            "produto": {
                "codigo": "XYZ",
                "versao": "2.0",
                "niResponsavel": "12345678901"
            },
            "caracterizacaoImportacao": {
                "indicador": "SIM",
                "ni": "98765432100"
            }
        },
        {
            "status": "inativo",
            "identificacao": {},
            "produto": {},
            "caracterizacaoImportacao": {}
        }
    ]
}
'''

# Carregar JSON em uma variável Python
data = json.loads(json_string)

# Exibir conteúdo
print(data.get('id', 'doce'))
