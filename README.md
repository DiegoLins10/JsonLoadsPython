
### Exemplo de Código
```python
import json

# Exemplo de string JSON
json_string = '''
{
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
print(data)
```

### Explicação
1. **`json_string`**:
   - É a string JSON que você deseja carregar. Ela deve estar formatada corretamente.

2. **`json.loads`**:
   - Converte a string JSON em um dicionário Python (ou outro tipo correspondente, como listas).

3. **Variável `data`**:
   - Contém os dados convertidos que podem ser usados diretamente no seu código.

Agora, você pode usar `data` no método `get_format_itens_duimp` ou em qualquer outra lógica que precise manipular os dados JSON. Caso tenha um exemplo específico de JSON para transformar, é só compartilhar!
