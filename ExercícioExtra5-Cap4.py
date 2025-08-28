import numpy as np


ds = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8-sig')


colunas = [c.strip() for c in ds[0]]
idx_country = colunas.index("Country")
idx_region = colunas.index("Region")
idx_gdp = colunas.index("GDP ($ per capita)")

dados = ds[1:]

regioes = np.char.strip(dados[:, idx_region])
mascara_regiao = (regioes == 'LATIN AMER. & CARIB')


paises_filtrados = dados[mascara_regiao]


gdp_da_regiao = paises_filtrados[:, idx_gdp]


gdp_numerico = gdp_da_regiao.astype(int)

indice_do_maior_gdp = np.argmax(gdp_numerico)


pais_vencedor = paises_filtrados[indice_do_maior_gdp]


nome_pais = pais_vencedor[idx_country].strip()
valor_gdp = pais_vencedor[idx_gdp]

print(f"O país com a maior renda per capita na América do Sul e Caribe é: {nome_pais}")
print(f"Renda per capita: ${valor_gdp}")