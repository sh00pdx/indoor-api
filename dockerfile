# Usamos una imagen base de Python 3.10
FROM python:3.10

# Establecemos el directorio de trabajo en el contenedor
WORKDIR /

# Instalamos Poetry
RUN pip install poetry

# Copiamos los archivos de configuración de Poetry y los instalamos
COPY pyproject.toml poetry.lock* /
RUN poetry config virtualenvs.create false \
    && poetry install

# Copiamos el resto del código de la aplicación
COPY . /

# Exponemos el puerto en el que se ejecutará la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
