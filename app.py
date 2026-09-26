import streamlit as st

st.title('Конвертер валют')
col1, col2 = st.columns(2)
st.write('Перевод любой валюты в рубли')
x = col1.number_input("", min_value= 0.0, value= 1.0)
rates = {'USD': 84.34, 'KZT': 0.18}
currenccy = col2.selectbox('Валюта', list(rates))
st.success(f'{x * rates[currenccy]:,.2f} RUB')