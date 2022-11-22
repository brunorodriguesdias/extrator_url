endereco = 'Avenida General Anapio Gomes 1081, apartamento 302, Veranópolis, Cachoeirinha, RS, 94920-270'

import re  # Regular Expression -- RegEx

# 5 dígitos + hífen (opcional) + 3 dígitos

padrao = re.compile('[0-9]{5}[-]{0,1}[0-9]{3}')
busca = padrao.search(endereco)  # Match

if busca:
    cep = busca.group()
    print(cep)
else:
    print("cep não encontrado")
