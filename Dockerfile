# Image Python
FROM python:3.10-slim

# Dossier de travail
WORKDIR /app

# Copier les fichiers
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le projet
COPY . .

# Exposer le port Streamlit
EXPOSE 8501

# Commande pour lancer l'app
CMD ["streamlit", "run", "app_streamlit.py", "--server.port=8501", "--server.address=0.0.0.0"]