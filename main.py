import streamlit as st
import requests

def click_button(value):
     requests.post("http://127.0.0.1:8000/items", json={"text": value})

st.title('Первая лабораторная работа v1.0')
text = st.text_input('Введите данные, для проверки работоспособности')
if st.button("Отправить", type="secondary"):
     on_click = click_button(text)
     st.rerun()

