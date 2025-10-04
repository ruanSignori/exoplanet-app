# Usa imagem base do TensorFlow 1.12 (compatível com as dependências)
FROM tensorflow/tensorflow:1.12.0-py3

# Define variáveis de ambiente para encoding
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PYTHONIOENCODING=utf-8

# Atualiza o sistema e instala dependências
RUN apt-get update -y && \
    apt-get install -y \
    iputils-ping \
    python3-sklearn \
    postgresql-client \
    locales \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Configura locale UTF-8
RUN locale-gen en_US.UTF-8

# Atualiza pip para evitar problemas de instalação
RUN python3 -m pip install --upgrade pip==19.0.3

# Cria diretório da aplicação
RUN mkdir /app
VOLUME ["/app"]
WORKDIR /app

# Copia e instala dependências
COPY requirements.txt /app/
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Expõe a porta 8000
EXPOSE 8000

# Comando padrão
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]