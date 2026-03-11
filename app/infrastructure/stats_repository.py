from .mongo_client import create_mongo_client


client = create_mongo_client()
db = client["casino_game"]
collection = db["player_stats"]


def save_stats(player_name, stats):
    document = {
        "player_name": player_name,
        "stats": stats
    }

    collection.update_one(
        {"player_name": player_name},
        {"$set": document},
        upsert=True
    )


def load_stats(player_name):
    document = collection.find_one({"player_name": player_name})

    if document is None:
        return None

    return document.get("stats")


def update_stats(player_name, stats):
    collection.update_one(
        {"player_name": player_name},
        {"$set": {"stats": stats}},
        upsert=True
    )