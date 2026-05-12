import streamlit as st
import calculkadora as calc

st.image("https://static.vecteezy.com/ti/vetor-gratis/p3/6602234-cute-cartoon-kawaii-calculator-vetor.jpg")
st.title("calculadora (●'◡'●)")
st.audio("https://www.fesliyanstudios.com/musicfiles/2019-04-26_-_Tranquility_-_www.fesliyanstudios.com.mp3",autoplay=True)

numero1 = st.number_input("digite o primeiro numero",step=0.1,value=None)
numero2 = st.number_input("digite o segundo numero",step=0.1,value=None)
operacao = st.selectbox("selecine a operacao",(["+","-","*","/"]))

if st.button("Calcular"):
    resultado = calc.calcular(numero1,numero2,operacao)
    st.toast(f"O resultado e: {resultado}",duration="infinite",icon="✅")
