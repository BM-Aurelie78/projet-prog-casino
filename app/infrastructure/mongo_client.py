import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()


def create_mongo_client():
    password = os.getenv("MONGO_PASSWORD")

    if not password:
        raise ValueError("MONGO_PASSWORD introuvable dans le fichier .env")

    uri = f"mongodb+srv://Aurel:{password}@cluster0.eec23mq.mongodb.net/?appName=Cluster0"

    client = MongoClient(uri, server_api=ServerApi("1"))
    client.admin.command("ping")
    print("password lu :", password is not None)
    return client


if __name__ == "__main__":
    try:
        create_mongo_client()
        print("Connexion MongoDB réussie")
    except Exception as e:
        print("Erreur MongoDB :", e)
        
