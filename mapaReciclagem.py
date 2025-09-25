import folium

# Coordenadas centrais (Curitiba, por exemplo)
mapa = folium.Map(location=[-25.4284, -49.2733], zoom_start=12) # Aumentei um pouco o zoom out para ver todos

# Pontos de coleta fixos (com a indentação corrigida)
pontos = [
        {"nome": "Módulo de Eletrônicos - Parque Barigui", "lat": -25.426213, "lon": -49.324107},
        {"nome": "Módulo de Eletrônicos - Parque São Lourenço", "lat": -25.385300, "lon": -49.255900},
        {"nome": "Módulo de Eletrônicos - Parque Bacacheri", "lat": -25.394167, "lon": -49.223889},
        {"nome": "Módulo de Eletrônicos - Passeio Público", "lat": -25.424400, "lon": -49.267800},
        {"nome": "Módulo de Eletrônicos - Praça do Japão", "lat": -25.443056, "lon": -49.289167},
        {"nome": "Módulo de Eletrônicos - Terminal Santa Cândida", "lat": -25.378056, "lon": -49.236667},
        {"nome": "Módulo de Eletrônicos - Terminal Boqueirão", "lat": -25.512778, "lon": -49.231944},
        {"nome": "Módulo de Eletrônicos - Terminal do Pinheirinho", "lat": -25.515278, "lon": -49.293889},
        {"nome": "Módulo de Eletrônicos - Terminal do Cabral", "lat": -25.407222, "lon": -49.252778},
        {"nome": "Módulo de Eletrônicos - Rua da Cidadania Fazendinha", "lat": -25.476487, "lon": -49.326316},
        {"nome": "Rua da Cidadania Bairro Novo", "lat": -25.549167, "lon": -49.294167},
        {"nome": "Secretaria do Meio Ambiente - Setor de Resíduos Sólidos", "lat": -25.448500, "lon": -49.234600},
        {"nome": "Unilivre - Universidade Livre do Meio Ambiente", "lat": -25.405000, "lon": -49.298056},
        {"nome": "Parque dos Tropeiros", "lat": -25.515000, "lon": -49.351667},
        {"nome": "Loja Havan - Parolin", "lat": -25.459918, "lon": -49.271387},
        {"nome": "Loja Havan - Portão", "lat": -25.478250, "lon": -49.296181},
        {"nome": "Leroy Merlin - Barigui", "lat": -25.433361, "lon": -49.321722},
        {"nome": "Leroy Merlin - Atuba", "lat": -25.388833, "lon": -49.196361},
        {"nome": "Carrefour - Champagnat (Parolim)", "lat": -25.437778, "lon": -49.309444},
        {"nome": "Ponto Frio - Shopping Estação", "lat": -25.437222, "lon": -49.271389},
        {"nome": "Disque Solidariedade (FAS)", "lat": -25.449528, "lon": -49.334185},
        {"nome": "Exército de Salvação", "lat": -25.454210, "lon": -49.292270},
        {"nome": "Asilo São Vicente de Paulo", "lat": -25.419616, "lon": -49.268045},
        {"nome": "Pequeno Cotolengo", "lat": -25.462700, "lon": -49.340000},
        {"nome": "Hospital Pequeno Príncipe", "lat": -25.442831, "lon": -49.280173},
        {"nome": "Amigos do Hospital de Clínicas", "lat": -25.426214, "lon": -49.258756},
        {"nome": "Fundação Ecumênica de Proteção ao Excepcional (FEPE)", "lat": -25.378776, "lon": -49.231268},
        {"nome": "Casa do Pai", "lat": -25.402206, "lon": -49.259928},
        {"nome": "Lar O Bom Caminho", "lat": -25.385202, "lon": -49.232049},
        {"nome": "Associação Cristã de Amparo Social (ACridas)", "lat": -25.467824, "lon": -49.278552},
        {"nome": "Santuário Nossa Senhora do Perpétuo Socorro", "lat": -25.417036, "lon": -49.261895},
        {"nome": "Paróquia São Vicente de Paulo", "lat": -25.434057, "lon": -49.289131},
        {"nome": "Lar Dona Vera", "lat": -25.400323, "lon": -49.220194},
        {"nome": "Associação Beneficente Dika", "lat": -25.496739, "lon": -49.344078},
        {"nome": "Cruz Vermelha Brasileira - Filial do Paraná", "lat": -25.435773, "lon": -49.262512},
        {"nome": "Rua da Cidadania Matriz", "lat": -25.433190, "lon": -49.272190},
        {"nome": "Rua da Cidadania Boa Vista", "lat": -25.385070, "lon": -49.231730},
        {"nome": "Rua da Cidadania Cajuru", "lat": -25.454130, "lon": -49.205730},
        {"nome": "Rua da Cidadania Fazendinha/Portão", "lat": -25.476487, "lon": -49.326316},
        {"nome": "Rua da Cidadania do Tatuquara", "lat": -25.568345, "lon": -49.330553},
        {"nome": "Ecoponto Parque Gomm", "lat": -25.444417, "lon": -49.288105},
        {"nome": "Ecoponto Jandaia", "lat": -25.535639, "lon": -49.278385},
        {"nome": "Ecoponto Vila Nova", "lat": -25.541333, "lon": -49.243583},
        {"nome": "Ecoponto Érico Veríssimo", "lat": -25.526861, "lon": -49.250556},
        {"nome": "Ecoponto Guaçuí", "lat": -25.522278, "lon": -49.263889},
        {"nome": "Ecoponto Cajuru", "lat": -25.462248, "lon": -49.200155},
        {"nome": "Ecoponto Campo de Santana", "lat": -25.611111, "lon": -49.317500},
        {"nome": "Ecoponto Sambaqui", "lat": -25.533056, "lon": -49.263889},
        {"nome": "Ecoponto Icaraí", "lat": -25.485000, "lon": -49.215833},
        {"nome": "Ecoponto Barigui", "lat": -25.426213, "lon": -49.324107},
        {"nome": "Ecoponto Boqueirão", "lat": -25.513460, "lon": -49.231268},
        {"nome": "Ecoponto CIC", "lat": -25.503859, "lon": -49.340914},
        {"nome": "Ecoponto Fazendinha", "lat": -25.476487, "lon": -49.326316},
        {"nome": "Ecoponto Tatuquara", "lat": -25.568345, "lon": -49.330553},
        {"nome": "Ecoponto Uberaba", "lat": -25.484931, "lon": -49.215286},
        {"nome": "Ecoponto Umbará", "lat": -25.556634, "lon": -49.297058},
        {"nome": "Ecoponto Orleans", "lat": -25.429444, "lon": -49.359167},
        {"nome": "Cooperativa Catamare", "lat": -25.477750, "lon": -49.245585},
        {"nome": "Associação de Catadores Nova República", "lat": -25.480053, "lon": -49.337199},
        {"nome": "Cooperativa de Trabalho dos Coletores de Materiais Recicláveis da Caximba (COOCAXA)", "lat": -25.589163, "lon": -49.336594},
]

# Adicionar marcadores no mapa
for ponto in pontos:
    folium.Marker(
        location=[ponto["lat"], ponto["lon"]],
        popup=ponto["nome"],
        icon=folium.Icon(color='green', icon='recycle', prefix='fa')
    ).add_to(mapa)


# Salvar mapa como HTML
# Certifique-se de que a pasta 'templates' existe, ou salve no mesmo diretório
# Exemplo salvando no mesmo diretório:
mapa.save("mapaReciclagem.html") 

