import folium

# Coordenadas centrais (Curitiba, por exemplo)
mapa = folium.Map(location=[-25.4284, -49.2733], zoom_start=12) # Aumentei um pouco o zoom out para ver todos

# Pontos de coleta fixos (com a indentação corrigida)
pontos = [
    {"nome": "Ecoponto Centro", "lat": -25.4284, "lon": -49.2733},
    {"nome": "Cooperativa Verde Vida", "lat": -25.4432, "lon": -49.2801},
    {"nome": "Ponto de Coleta Bairro Novo", "lat": -25.4701, "lon": -49.2621},
    {"nome": "Ecoponto Parque Gomm", "lat": -25.4444178, "lon": -49.2881057},
    {"nome": "Ecoponto Jandaia", "lat": -25.535639, "lon": -49.278385},
    {"nome": "Ecoponto Vila Nova", "lat": -25.541333, "lon": -49.243583},
    {"nome": "Ecoponto Érico Veríssimo", "lat": -25.526861, "lon": -49.250556},
    {"nome": "Ecoponto Guaçuí", "lat": -25.522278, "lon": -49.263889},
    {"nome": "Ecoponto Cajuru", "lat": -25.462248, "lon": -49.200155},
    {"nome": "Ecoponto Campo de Santana", "lat": -25.611111, "lon": -49.3175},
    {"nome": "Ecoponto Sambaqui", "lat": -25.533056, "lon": -49.263889},
    {"nome": "Ecoponto Icaraí", "lat": -25.485, "lon": -49.215833},
    {"nome": "Ecoponto Metropolitano", "lat": -25.419444, "lon": -49.3625},
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

