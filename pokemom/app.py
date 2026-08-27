import streamlit as st
import json
import requests

st.set_page_config(
    page_title="Pokédex",
    page_icon="⚡",
    layout="wide"
)

# ==================================
# CSS Personalizado
# ==================================

st.markdown("""
<style>
.main {
    background-color: #0E1117;
}

.pokemon-title {
    text-align: center;
    font-size: 3rem;
    font-weight: bold;
    color: #FFD700;
}

.tipo {
    padding: 8px;
    border-radius: 10px;
    text-align: center;
    font-weight: bold;
    color: white;
    margin-bottom: 5px;
}
</style>
""", unsafe_allow_html=True)

# ==================================
# Cache
# ==================================

@st.cache_data
def carregar_pokemon(nome):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome}"
    return requests.get(url).json()

# ==================================
# Dados
# ==================================

with open("pokemon_index.json", "r", encoding="utf-8") as arquivo:
    nomes_pokemons = json.load(arquivo)

st.markdown(
    '<p class="pokemon-title">⚡ Pokédex Interativa ⚡</p>',
    unsafe_allow_html=True
)

nome = st.selectbox(
    "🔍 Escolha um Pokémon",
    nomes_pokemons.values()
)

dados = carregar_pokemon(nome)

peso = dados["weight"] / 10
altura = dados["height"] / 10
imc = round(peso / (altura ** 2), 1)

# ==================================
# Sprites
# ==================================

col1, col2, col3 = st.columns([2,1,2])

with col1:
    st.image(
        dados["sprites"]["front_default"],
        caption="Normal",
        use_container_width=True
    )

with col2:
    st.subheader("🔊 Sons")
    st.audio(dados["cries"]["latest"])

with col3:
    st.image(
        dados["sprites"]["front_shiny"],
        caption="✨ Shiny",
        use_container_width=True
    )

st.divider()

# ==================================
# Métricas
# ==================================

m1, m2, m3 = st.columns(3)

m1.metric("📏 Altura", f"{altura} m")
m2.metric("⚖️ Peso", f"{peso} kg")
m3.metric("🧮 IMC", imc)

st.divider()

# ==================================
# Abas
# ==================================

tipos, status, locais, habilidades = st.tabs(
    ["🎨 Tipos", "📊 Status", "🗺️ Locais", "⚡ Habilidades"]
)

# ==================================
# Tipos
# ==================================

cores = {
    "fire": "#FF5733",
    "water": "#3498DB",
    "grass": "#2ECC71",
    "electric": "#F1C40F",
    "ice": "#85C1E9",
    "fighting": "#C0392B",
    "poison": "#8E44AD",
    "ground": "#A04000",
    "flying": "#5DADE2",
    "psychic": "#FF1493",
    "bug": "#27AE60",
    "rock": "#7F8C8D",
    "ghost": "#6C3483",
    "dragon": "#2E86C1",
    "dark": "#2C3E50",
    "steel": "#95A5A6",
    "fairy": "#FF69B4",
    "normal": "#BDC3C7"
}

with tipos:
    for tipo in dados["types"]:
        nome_tipo = tipo["type"]["name"]

        st.markdown(
            f"""
            <div class="tipo"
            style="background:{cores.get(nome_tipo,'gray')}">
            {nome_tipo.upper()}
            </div>
            """,
            unsafe_allow_html=True
        )

# ==================================
# Status
# ==================================

with status:

    for stat in dados["stats"]:
        nome_stat = stat["stat"]["name"]
        valor = stat["base_stat"]

        st.write(f"**{nome_stat.upper()}** ({valor})")
        st.progress(min(valor/255, 1.0))

# ==================================
# Locais
# ==================================

with locais:

    locais_pokemon = requests.get(
        dados["location_area_encounters"]
    ).json()

    if locais_pokemon:

        for local in locais_pokemon:
            st.markdown(
                f"📍 {local['location_area']['name']}"
            )

    else:
        st.info("Nenhum local encontrado.")

# ==================================
# Habilidades
# ==================================

with habilidades:

    for habilidade in dados["abilities"]:
        st.success(
            habilidade["ability"]["name"].title()
        )