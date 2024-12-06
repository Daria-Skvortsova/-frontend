import streamlit as st
import requests

def click_button_post(value):
     requests.post("http://localhost:8000/items", json={"text": value})

st.title('Первая лабораторная работа v1.0')
text = st.text_input('Введите данные, для проверки работоспособности и нажмите на кнопку')
if st.button("Отправить", type="secondary"):
     on_click = click_button_post(text)
     st.rerun()

def click_button_get():
     value = requests.get("http://localhost:8000/items")
     return value.json()

st.title('Первая лабораторная работа v2.0')

st.text('Нажмите на кнопку, чтобы увидить данные с сервера')
if st.button ("Получить", type ="primary"):
     text = click_button_get()
     st.info(text)

