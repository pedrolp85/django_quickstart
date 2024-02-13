# Usa una imagen oficial de Python como imagen base
FROM python:3.10-bullseye

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Establece variables de entorno para Python y Poetry
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VIRTUALENVS_CREATE=false

RUN apt-get update && \
    apt-get install -y libpq-dev gcc build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
# Instala Poetry
RUN pip install --upgrade pip && \
    pip install poetry

# Copia solo los archivos necesarios para instalar dependencias
COPY pyproject.toml poetry.lock* /app/

# Instala dependencias usando Poetry
RUN poetry install --no-interaction --no-ansi

# Copia el resto del código fuente del proyecto al contenedor
COPY . /app/


# CMD ejecuta manage.py runserver por defecto
# se sobreescribe en el compose
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]