import streamlit as st
import Banco

st.title("🏦 Sistema Bancário Phablo")

# No Streamlit, usamos o 'session_state' para manter os dados vivos entre um clique e outro
if 'conta' not in st.session_state:
    st.session_state.conta = Banco('Phablo', 123, '001', 0)

valor = st.number_input("Digite o valor:", min_value=0.0)

if st.button("Depositar Salário"):
    st.session_state.conta.depositar_salario(valor)
    st.success(f"Salário de R${valor} processado!")

if st.button("Sacar"):
    st.session_state.conta.sacar(valor)
    st.warning(f"Tentativa de saque de R${valor}")

st.subheader("Extrato")
for op in st.session_state.conta.historico:
    st.write(op)

st.metric("Saldo Atual", f"R$ {st.session_state.conta.saldo:.2f}")