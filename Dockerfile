# Usa imagem base do TensorFlow 1.12 (compatível com as dependências)
FROM tensorflow/tensorflow:1.12.0-py3

# Atualiza o sistema e instala dependências
RUN apt-get update -y && \
    apt-get install -y \
    iputils-ping \
    python3-sklearn \
    postgresql-client \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Atualiza pip para evitar problemas de instalação
RUN pip install --upgrade pip==19.0.3

# Cria diretório da aplicação
RUN mkdir /app
VOLUME ["/app"]
WORKDIR /app

# Copia e instala dependências
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 8000
EXPOSE 8000

# Comando padrão
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]