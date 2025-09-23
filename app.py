import streamlit as st

# Coloca título
st.title("Aluguel de Carros")

# Escreve
st.write("Aqui temos carros de luxo exclusivamente para você.")

# Cria uma barra lateral
st.sidebar.title("Barra Lateral")
st.sidebar.image("logo.png")

# Criando a lista
carros = ["Corvette V8", "Bentley", "Jaguar", "McLaren", "Bugatti"]

# Cria caixinha na barra lateral
opcao = st.sidebar.selectbox("ESCOLHA A MARCA" , carros)


# PRINCIPAL ──── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ────
st.title('')
st.markdown(f'## Você alugou o modelo: {opcao}')
st.image(f'{opcao}.png')
st.markdown('---')


# OUTRA PARTE ──── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ────

dias = st.text_input(f'Por quantos dias o {opcao} foi alugado?')
km = st.text_input(f'Quantos km você rodou com o {opcao}?')


# DEFINE DIÁRIA ──── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ────

if opcao == 'Corvette V8':
    diaria = 800

elif opcao == 'Bentley':
    diaria = 700

elif opcao == 'Jaguar':
    diaria = 550

elif opcao == 'McLaren':
    diaria = 570

elif opcao == 'Bugatti':
    diaria = 660

# CALCULAR ──── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── 

if st.button('Calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias + total_km

    st.warning(f'Você alugou o {opcao} por {dias} dias e rodou {km}km. O valor total a pagar é R${aluguel_total:.2f}')