FROM python:3.11

ENV TEXT "Hello!"

RUN pip install streamlit
COPY main.py main.py


CMD ["streamlit", "run", "main.py"]
