import html
import re

import requests
import streamlit as st


st.set_page_config(
    page_title="Atlas CEP | Encontre lugares",
    page_icon="📍",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown(
    """
    <style>
        :root {
            --ink: #0f1d3a;
            --muted: #66758f;
            --violet: #6d5dfc;
            --pink: #f361a6;
            --cyan: #44d7d3;
            --cream: #f9fbff;
        }

        .stApp {
            background:
                radial-gradient(circle at 88% 7%, rgba(68, 215, 211, 0.24) 0, transparent 25rem),
                radial-gradient(circle at 56% 95%, rgba(243, 97, 166, 0.13) 0, transparent 28rem),
                linear-gradient(135deg, #f8faff 0%, #eef4ff 52%, #fbf9ff 100%);
            color: var(--ink);
            font-family: Inter, "Segoe UI", sans-serif;
        }

        [data-testid="stSidebar"] {
            background:
                radial-gradient(circle at 12% 4%, rgba(68, 215, 211, 0.24) 0, transparent 12rem),
                linear-gradient(165deg, #111d42 0%, #15295a 52%, #0d6b78 135%);
            border-right: 1px solid rgba(255, 255, 255, 0.08);
        }
        [data-testid="stSidebar"] * {
            color: #f9fbff;
        }
        [data-testid="stSidebar"] code {
            background: rgba(255, 255, 255, 0.16);
            border: 1px solid rgba(255, 255, 255, 0.19);
            border-radius: 6px;
            color: #d8ffff !important;
            padding: 0.12rem 0.35rem;
        }
        [data-testid="stSidebar"] [data-baseweb="input"] {
            background: rgba(255, 255, 255, 0.98);
            border: 2px solid transparent;
            border-radius: 14px;
            box-shadow: 0 10px 24px rgba(3, 15, 42, 0.22);
            transition: border-color 180ms ease, box-shadow 180ms ease;
        }
        [data-testid="stSidebar"] [data-baseweb="input"]:focus-within {
            border-color: var(--cyan);
            box-shadow: 0 0 0 4px rgba(68, 215, 211, 0.18), 0 10px 24px rgba(3, 15, 42, 0.22);
        }
        [data-testid="stSidebar"] [data-baseweb="input"] input,
        [data-testid="stSidebar"] [data-baseweb="input"] input::placeholder {
            color: #36456a !important;
        }
        [data-testid="stSidebar"] .stCaption {
            color: #c9d8f6 !important;
        }
        [data-testid="stSidebar"] hr {
            border-color: rgba(255, 255, 255, 0.16);
            margin: 1.7rem 0;
        }

        .block-container {
            max-width: 1200px;
            padding-top: 3rem;
            padding-bottom: 2.4rem;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 0.8rem;
            margin: 0.5rem 0 0.8rem;
        }
        .brand-mark {
            display: grid;
            place-items: center;
            width: 2.65rem;
            height: 2.65rem;
            border-radius: 13px;
            background: linear-gradient(135deg, var(--pink), #ffb36a);
            box-shadow: 0 10px 20px rgba(243, 97, 166, 0.28);
            font-size: 1.3rem;
        }
        .brand h2 {
            margin: 0;
            color: #ffffff;
            font-size: 1.38rem;
            letter-spacing: -0.04em;
        }
        .brand p {
            margin: 0.1rem 0 0;
            color: #bfd5ff;
            font-size: 0.75rem;
            letter-spacing: 0.08em;
            font-weight: 800;
        }
        .sidebar-tip {
            margin: 0.5rem 0 0;
            color: #c9d8f6;
            font-size: 0.92rem;
            line-height: 1.55;
        }

        .hero {
            position: relative;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 2rem;
            min-height: 250px;
            padding: 2.4rem 2.7rem;
            border: 1px solid rgba(255, 255, 255, 0.34);
            border-radius: 28px;
            background:
                radial-gradient(circle at 75% 15%, rgba(68, 215, 211, 0.68) 0, transparent 12rem),
                radial-gradient(circle at 96% 78%, rgba(243, 97, 166, 0.6) 0, transparent 16rem),
                linear-gradient(128deg, #111d42 0%, #283d8c 65%, #6153e8 130%);
            box-shadow: 0 24px 60px rgba(29, 41, 100, 0.28);
            margin-bottom: 1.6rem;
            isolation: isolate;
        }
        .hero::before {
            content: "";
            position: absolute;
            inset: auto -15% -52% auto;
            z-index: -1;
            width: 30rem;
            height: 30rem;
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 50%;
            box-shadow: 0 0 0 3.7rem rgba(255, 255, 255, 0.06), 0 0 0 7.5rem rgba(255, 255, 255, 0.04);
        }
        .hero-copy {
            max-width: 720px;
        }
        .eyebrow {
            margin: 0 0 0.75rem;
            color: #91fbf6;
            font-size: 0.74rem;
            font-weight: 850;
            letter-spacing: 0.16em;
        }
        .hero h1 {
            max-width: 690px;
            margin: 0;
            color: #ffffff;
            font-size: clamp(2.25rem, 4.6vw, 4rem);
            letter-spacing: -0.055em;
            line-height: 1.02;
        }
        .hero-description {
            max-width: 590px;
            margin: 1rem 0 0;
            color: #dce8ff;
            font-size: 1.05rem;
            line-height: 1.6;
        }
        .hero-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 0.55rem;
            margin-top: 1.35rem;
        }
        .hero-tags span {
            padding: 0.42rem 0.72rem;
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 999px;
            background: rgba(255, 255, 255, 0.11);
            color: #ffffff;
            font-size: 0.78rem;
            font-weight: 700;
        }
        .hero-pin {
            position: relative;
            flex: 0 0 auto;
            display: grid;
            place-items: center;
            width: 9.5rem;
            height: 9.5rem;
            border: 1px solid rgba(255, 255, 255, 0.28);
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.12);
            box-shadow: inset 0 0 32px rgba(255, 255, 255, 0.16), 0 20px 36px rgba(11, 17, 62, 0.25);
            animation: drift 5s ease-in-out infinite;
        }
        .hero-pin::after {
            content: "";
            position: absolute;
            width: 5rem;
            height: 5rem;
            border: 1px dashed rgba(255, 255, 255, 0.65);
            border-radius: 50%;
            animation: spin 18s linear infinite;
        }
        .hero-pin span {
            z-index: 1;
            font-size: 3.5rem;
            filter: drop-shadow(0 10px 8px rgba(0, 0, 0, 0.18));
        }

        .result-card {
            position: relative;
            overflow: hidden;
            padding: 1.8rem 2rem;
            border: 1px solid rgba(99, 86, 252, 0.14);
            border-radius: 24px;
            background: linear-gradient(122deg, #ffffff 0%, #f6f4ff 100%);
            box-shadow: 0 20px 44px rgba(66, 55, 146, 0.13);
            margin: 0.4rem 0 1.25rem;
        }
        .result-card::after {
            content: "";
            position: absolute;
            right: -2.5rem;
            bottom: -4.2rem;
            width: 13rem;
            height: 13rem;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(243, 97, 166, 0.23), rgba(243, 97, 166, 0));
        }
        .result-layout {
            position: relative;
            z-index: 1;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1.2rem;
        }
        .result-card .eyebrow {
            color: #6d5dfc;
        }
        .result-card h2 {
            margin: 0;
            color: var(--ink);
            font-size: clamp(1.65rem, 3vw, 2.2rem);
            letter-spacing: -0.045em;
        }
        .result-place {
            margin: 0.55rem 0 0;
            color: #64708a;
            font-size: 1rem;
        }
        .state-pill {
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            margin-top: 1rem;
            padding: 0.42rem 0.7rem;
            border-radius: 999px;
            background: #edfafa;
            color: #137d80;
            font-size: 0.8rem;
            font-weight: 800;
        }
        .result-icon {
            display: grid;
            place-items: center;
            min-width: 4.6rem;
            width: 4.6rem;
            height: 4.6rem;
            border-radius: 22px;
            background: linear-gradient(135deg, var(--violet), var(--pink));
            box-shadow: 0 16px 28px rgba(109, 93, 252, 0.3);
            font-size: 2rem;
        }

        [data-testid="stMetric"] {
            position: relative;
            overflow: hidden;
            min-height: 118px;
            padding: 1.1rem 1.2rem;
            border: 1px solid rgba(90, 97, 185, 0.12);
            border-radius: 18px;
            background: rgba(255, 255, 255, 0.82);
            box-shadow: 0 11px 28px rgba(48, 57, 124, 0.07);
            transition: transform 180ms ease, box-shadow 180ms ease;
        }
        [data-testid="stMetric"]:hover {
            transform: translateY(-3px);
            box-shadow: 0 18px 34px rgba(48, 57, 124, 0.13);
        }
        [data-testid="stMetric"]::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: linear-gradient(90deg, var(--violet), var(--pink), var(--cyan));
        }
        [data-testid="stMetric"] [data-testid="stMetricLabel"],
        [data-testid="stMetric"] [data-testid="stMetricLabel"] * {
            color: #7a87a1 !important;
            font-weight: 750;
        }
        [data-testid="stMetric"] [data-testid="stMetricValue"],
        [data-testid="stMetric"] [data-testid="stMetricValue"] * {
            color: var(--ink) !important;
            font-weight: 800;
        }

        .section-title {
            display: flex;
            align-items: center;
            gap: 0.55rem;
            margin: 1.7rem 0 0.7rem;
            color: var(--ink);
            font-weight: 800;
            font-size: 1.1rem;
            letter-spacing: -0.02em;
        }
        .section-title::before {
            content: "";
            width: 0.65rem;
            height: 0.65rem;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--pink), var(--violet));
            box-shadow: 0 0 0 5px rgba(109, 93, 252, 0.09);
        }
        [data-testid="stVerticalBlockBorderWrapper"] {
            overflow: hidden;
            border: 1px solid rgba(90, 97, 185, 0.13) !important;
            border-radius: 20px !important;
            background: rgba(255, 255, 255, 0.76);
            box-shadow: 0 16px 34px rgba(48, 57, 124, 0.08);
        }
        .coordinates {
            padding: 1.35rem;
            border: 1px solid rgba(90, 97, 185, 0.13);
            border-radius: 20px;
            background: rgba(255, 255, 255, 0.8);
            box-shadow: 0 16px 34px rgba(48, 57, 124, 0.08);
            color: #4d5d78;
            line-height: 1.65;
        }
        .coordinate-item {
            padding: 0.72rem 0;
            border-bottom: 1px solid #e9ecf7;
        }
        .coordinate-item:last-child {
            border-bottom: 0;
            padding-bottom: 0;
        }
        .coordinate-label {
            display: block;
            color: #8390aa;
            font-size: 0.7rem;
            font-weight: 800;
            letter-spacing: 0.1em;
            text-transform: uppercase;
        }
        .coordinate-value {
            color: var(--ink);
            font-size: 0.96rem;
            font-weight: 700;
        }
        [data-testid="stDownloadButton"] button {
            width: 100%;
            margin-top: 0.35rem;
            border: 1px solid rgba(109, 93, 252, 0.24);
            border-radius: 12px;
            background: rgba(255, 255, 255, 0.7);
            color: #5747e7;
            font-weight: 800;
        }
        [data-testid="stDownloadButton"] button:hover {
            border-color: transparent;
            background: linear-gradient(135deg, var(--violet), #8a7cff);
            color: white;
        }

        .empty-state {
            padding: 3.2rem 1.7rem 2rem;
            border: 1px solid rgba(109, 93, 252, 0.17);
            border-radius: 26px;
            background: rgba(255, 255, 255, 0.68);
            box-shadow: 0 18px 40px rgba(48, 57, 124, 0.08);
            text-align: center;
        }
        .empty-state .icon {
            display: grid;
            place-items: center;
            width: 5rem;
            height: 5rem;
            margin: 0 auto 1rem;
            border-radius: 24px;
            background: linear-gradient(135deg, #ebe8ff, #dcffff);
            box-shadow: 0 15px 26px rgba(109, 93, 252, 0.14);
            font-size: 2.4rem;
            animation: drift 5s ease-in-out infinite;
        }
        .empty-state h2 {
            margin: 0;
            color: var(--ink);
            font-size: 1.75rem;
            letter-spacing: -0.04em;
        }
        .empty-state > p {
            margin: 0.7rem 0 0;
            color: #64708a;
        }
        .feature-row {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 0.9rem;
            max-width: 720px;
            margin: 2rem auto 0;
        }
        .feature {
            display: flex;
            align-items: center;
            gap: 0.6rem;
            min-width: 180px;
            padding: 0.8rem 0.9rem;
            border: 1px solid #e8e9f7;
            border-radius: 14px;
            background: #ffffff;
            color: #55627c;
            text-align: left;
            font-size: 0.8rem;
        }
        .feature-icon {
            display: grid;
            place-items: center;
            width: 2.1rem;
            height: 2.1rem;
            border-radius: 10px;
            background: #f0efff;
            font-size: 1rem;
        }
        .feature strong {
            display: block;
            color: var(--ink);
            font-size: 0.85rem;
        }
        .footer {
            margin-top: 2.8rem;
            color: #7c88a2;
            font-size: 0.84rem;
            text-align: center;
        }

        [data-testid="stFormSubmitButton"] button {
            min-height: 48px;
            border: 0;
            border-radius: 14px;
            background: linear-gradient(135deg, #ffb54d, #ff7c80);
            box-shadow: 0 12px 24px rgba(255, 124, 128, 0.25);
            color: #321e22 !important;
            font-weight: 850;
            letter-spacing: 0.01em;
            transition: transform 180ms ease, box-shadow 180ms ease;
        }
        [data-testid="stFormSubmitButton"] button:hover {
            background: linear-gradient(135deg, #ffc85f, #ff8c92);
            box-shadow: 0 16px 30px rgba(255, 124, 128, 0.34);
            transform: translateY(-2px);
        }
        [data-testid="stFormSubmitButton"] button:focus:not(:active) {
            box-shadow: 0 0 0 3px rgba(68, 215, 211, 0.55), 0 16px 30px rgba(255, 124, 128, 0.34);
        }

        @keyframes drift {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-8px); }
        }
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
        @media (max-width: 780px) {
            .block-container { padding-top: 1.5rem; }
            .hero { min-height: auto; padding: 2rem 1.5rem; }
            .hero-pin { display: none; }
            .hero h1 { font-size: 2.4rem; }
            .result-card { padding: 1.5rem; }
            .feature { min-width: 100%; }
        }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data(ttl=3600, show_spinner=False)
def consultar_cep(cep: str) -> dict | None:
    """Busca um CEP na API e guarda o resultado por uma hora."""
    resposta = requests.get(
        f"https://cep.awesomeapi.com.br/json/{cep}",
        timeout=10,
    )

    if resposta.status_code == 404:
        return None

    resposta.raise_for_status()
    dados = resposta.json()

    if not isinstance(dados, dict):
        raise ValueError("A resposta recebida não tem o formato esperado.")

    return dados


def texto_seguro(valor: object, padrao: str = "Não informado") -> str:
    """Prepara um texto para aparecer com segurança dentro do HTML."""
    if valor is None or not str(valor).strip():
        return padrao
    return html.escape(str(valor).strip())


with st.sidebar:
    st.markdown(
        """
        <div class="brand">
            <div class="brand-mark">📍</div>
            <div><h2>Atlas CEP</h2><p>ENCONTRE LUGARES</p></div>
        </div>
        <p class="sidebar-tip">Descubra endereços brasileiros com uma busca simples e um mapa pronto para explorar.</p>
        """,
        unsafe_allow_html=True,
    )
    st.divider()

    with st.form("formulario_busca", border=False):
        cep_digitado = st.text_input(
            "CEP para pesquisar",
            placeholder="Ex.: 01001-000",
            help="Digite 8 números. Você pode usar o hífen.",
        )
        pesquisar = st.form_submit_button("✨ Buscar CEP", use_container_width=True)

    st.divider()
    st.markdown("**Formatos aceitos**")
    st.caption("`01001000` ou `01001-000`")
    st.caption("As coordenadas mostram uma aproximação da localização do CEP.")


st.markdown(
    """
    <section class="hero">
        <div class="hero-copy">
            <p class="eyebrow">ATLAS DE ENDEREÇOS DO BRASIL</p>
            <h1>Todo lugar começa com um CEP.</h1>
            <p class="hero-description">Encontre endereços, coordenadas e sua localização no mapa em uma busca rápida, clara e bonita.</p>
            <div class="hero-tags">
                <span>⚡ Busca rápida</span>
                <span>🗺️ Mapa interativo</span>
                <span>✦ Dados organizados</span>
            </div>
        </div>
        <div class="hero-pin" aria-hidden="true"><span>📍</span></div>
    </section>
    """,
    unsafe_allow_html=True,
)

erro = None

if pesquisar:
    # Aceita somente os formatos 12345678 ou 12345-678.
    if not re.fullmatch(r"\d{5}-?\d{3}", cep_digitado):
        erro = "Digite um CEP válido com 8 números, por exemplo: 01001-000."
    else:
        cep = cep_digitado.replace("-", "")

        try:
            with st.spinner("Consultando o nosso atlas de endereços..."):
                busca = consultar_cep(cep)
        except requests.exceptions.RequestException:
            erro = "Não consegui conversar com o serviço de CEP. Tente novamente em alguns instantes."
        except ValueError:
            erro = "O serviço de CEP enviou uma resposta inesperada. Tente novamente."
        else:
            if busca is None:
                erro = "Não encontrei esse CEP. Confira os números e tente novamente."
            else:
                st.session_state["resultado_cep"] = busca

if erro:
    st.error(erro, icon="⚠️")

busca = st.session_state.get("resultado_cep")

if busca:
    endereco = texto_seguro(busca.get("address"))
    bairro = texto_seguro(busca.get("district"))
    cidade = texto_seguro(busca.get("city"))
    estado = texto_seguro(busca.get("state"))
    ddd = texto_seguro(busca.get("ddd"), "—")
    cep_encontrado = texto_seguro(busca.get("cep"), "—")
    latitude = busca.get("lat")
    longitude = busca.get("lng")

    st.markdown(
        f"""
        <section class="result-card">
            <div class="result-layout">
                <div>
                    <p class="eyebrow">LOCALIZAÇÃO ENCONTRADA</p>
                    <h2>{endereco}</h2>
                    <p class="result-place">{bairro} &nbsp;•&nbsp; {cidade}/{estado}</p>
                    <span class="state-pill">✦ CEP confirmado</span>
                </div>
                <div class="result-icon" aria-hidden="true">📍</div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

    coluna_cep, coluna_cidade, coluna_ddd = st.columns(3)
    coluna_cep.metric("CEP", cep_encontrado)
    coluna_cidade.metric("Cidade", cidade)
    coluna_ddd.metric("DDD", ddd)

    try:
        dados_mapa = {"lat": [float(latitude)], "lon": [float(longitude)]}
    except (TypeError, ValueError):
        dados_mapa = None

    mapa, detalhes = st.columns([1.45, 0.75], gap="large")

    with mapa:
        st.markdown('<p class="section-title">Veja o local no mapa</p>', unsafe_allow_html=True)
        if dados_mapa:
            with st.container(border=True):
                st.map(dados_mapa, zoom=15, height=500)
        else:
            st.warning("Este CEP foi encontrado, mas não possui coordenadas para mostrar no mapa.")

    with detalhes:
        st.markdown('<p class="section-title">Ficha do endereço</p>', unsafe_allow_html=True)
        st.markdown(
            f"""
            <div class="coordinates">
                <div class="coordinate-item"><span class="coordinate-label">Bairro</span><span class="coordinate-value">{bairro}</span></div>
                <div class="coordinate-item"><span class="coordinate-label">Estado</span><span class="coordinate-value">{estado}</span></div>
                <div class="coordinate-item"><span class="coordinate-label">Latitude</span><span class="coordinate-value">{texto_seguro(latitude, 'Indisponível')}</span></div>
                <div class="coordinate-item"><span class="coordinate-label">Longitude</span><span class="coordinate-value">{texto_seguro(longitude, 'Indisponível')}</span></div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.info("As coordenadas mostram uma aproximação da localização do CEP.", icon="💡")

        resumo = (
            "ATLAS CEP — FICHA DO ENDEREÇO\n\n"
            f"CEP: {cep_encontrado}\n"
            f"Endereço: {endereco}\n"
            f"Bairro: {bairro}\n"
            f"Cidade/UF: {cidade}/{estado}\n"
            f"DDD: {ddd}\n"
            f"Latitude: {texto_seguro(latitude, 'Indisponível')}\n"
            f"Longitude: {texto_seguro(longitude, 'Indisponível')}\n"
        )
        st.download_button(
            "↓ Baixar ficha do endereço",
            data=resumo,
            file_name=f"atlas-cep-{cep_encontrado}.txt",
            mime="text/plain",
            use_container_width=True,
        )
else:
    st.markdown(
        """
        <section class="empty-state">
            <div class="icon">🧭</div>
            <h2>Seu próximo destino está a um CEP de distância.</h2>
            <p>Digite um CEP no painel à esquerda e deixe o Atlas encontrar o caminho.</p>
            <div class="feature-row">
                <div class="feature"><div class="feature-icon">⚡</div><div><strong>Rápido</strong>resultado em segundos</div></div>
                <div class="feature"><div class="feature-icon">📍</div><div><strong>Visual</strong>um ponto direto no mapa</div></div>
                <div class="feature"><div class="feature-icon">✦</div><div><strong>Organizado</strong>dados prontos para usar</div></div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    '<p class="footer">Atlas CEP &nbsp;•&nbsp; encontre lugares, sem complicações.</p>',
    unsafe_allow_html=True,
)
