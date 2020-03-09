from pymongo import MongoClient

class Database:
    """
    The class for the Database.
    """
    def __init__(self):
        """Initialize the Database."""
        self.client = MongoClient()
        self.db = self.client.highscores

    def insert(self, name, score):
        """"Insert a record into the database."""
        record = {
            "name": name,
            "score": score
        }
        result = self.db.scores.insert_one(record)
        # print("Added {0}'s score to database as {1}".format(name, result.inserted_id))

    def get_score(self, name):
        """Get a score by name and return it."""
        score = self.db.scores.find_one({"name": name}).get("score")
        # print(score)
        return(score)

# db = Database()
# db.insert("Bik", 24)
# db.get("Bik")