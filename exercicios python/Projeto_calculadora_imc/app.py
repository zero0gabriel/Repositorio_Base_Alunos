import streamlit as st

# ---------------- Sidebar
st.sidebar.image("logo.png")

# ---------------- Body
st.title("Calculadora IMC")

peso = st.text_input("Digite seu peso (kg):")
altura = st.text_input("Digite sua altura (m):")

if st.button("Calcular"):

    try:
        peso = float(peso)
        altura = float(altura)

        imc = peso / (altura ** 2)

        if imc < 18.5:
            class_imc = "abaixo_peso"
            st.warning(f"Seu IMC é {imc:.1f}! Você está abaixo do peso 😔")

        elif imc < 24.9:
            class_imc = "peso_saudavel"
            st.success(f"Seu IMC é {imc:.1f}! Você está com peso saudável 😊")

        elif imc < 29.9:
            class_imc = "sobrepeso"
            st.warning(f"Seu IMC é {imc:.1f}! Você está com sobrepeso 🤨")

        elif imc < 34.9:
            class_imc = "obesidade1"
            st.warning(f"Seu IMC é {imc:.1f}! Você está com obesidade grau 1 🤨")

        elif imc < 39.9:
            class_imc = "obesidade2"
            st.warning(f"Seu IMC é {imc:.1f}! Você está com obesidade grau 2 😟")

        else:
            class_imc = "obesidade3"
            st.error(f"Seu IMC é {imc:.1f}! Você está com obesidade grau 3 😶‍🌫️")

        # Imagem
        st.markdown("---")
        st.image(f"{class_imc}.png")

        # Texto
        with open(f"{class_imc}.txt", "r", encoding="utf-8") as f:
            texto = f.read()

        st.markdown(texto)

    except ValueError:
        st.error("Digite valores válidos para peso e altura!")