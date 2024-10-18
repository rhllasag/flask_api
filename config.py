import os 

class Config:
    MONGODB_SETTINGS = {
        'db': os.getenv("MONGODB"),
        'host': os.getenv("MONGOHOST"),
        'port': int(os.getenv("MONGOPORT")),
        'username': os.getenv("MONGOUSER"),
        'password': os.getenv("MONGOPASS"),
    }