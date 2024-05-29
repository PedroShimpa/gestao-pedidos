# Usando a imagem oficial do Python como base
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de requisitos e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código do aplicativo
COPY . .

# Define a variável de ambiente para desativar o buffer de saída do Python
ENV PYTHONUNBUFFERED=1

# Instala o watchdog para reinicializar o servidor automaticamente em modo de desenvolvimento
RUN pip install watchdog

# Expõe a porta que o aplicativo irá rodar
EXPOSE 80

# Comando para iniciar o servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
