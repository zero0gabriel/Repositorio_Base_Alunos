import streamlit as st
import base64


def render_local_gif(file_path):
    with open(file_path, "rb") as f:
        contents = f.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    st.sidebar.markdown(
        # Mude a linha 10 para isso:
        f'<img src="data:image/gif;base64,{data_url}" alt="Opening GIF" width="100%" style="mix-blend-mode: screen;">',
        unsafe_allow_html=True,
    )

musicas = {
    "system of down": {
        "Chop Suey!": "https://youtu.be/CSvFpBOe8eY?si=r7pXmtE5c1Xf8w_u",
        "Toxity": "https://youtu.be/iywaBOMvYLI?si=RrxJAznw0XBWoUqb"
    },

    "Scorpions": {
        "Still Loving you": "https://youtu.be/7pOr3dBFAeY?si=yi0fS3rx7iPkBaqi",
        "Many Men": "https://www.youtube.com/watch?v=5D3crqpClPY"
    }
}

render_local_gif("logo.gif")

artista = st.sidebar.selectbox(
    "Selecione o artista",
    musicas.keys()
)

musicas_artista = musicas[artista]

st.title(artista)

for musica in musicas_artista.items():
    titulo, link = musica

    st.subheader(titulo)
    st.video(link)

