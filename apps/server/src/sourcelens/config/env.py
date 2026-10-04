import os


class Env:
    def __init__(self):
        self.SARVAM_API_KEY = os.environ.get("SARVAM_API_KEY") or ""
        self.DATABASE_URL = os.environ.get("DATABASE_URL") or ""
        self.REDIS_URL = os.environ.get("REDIS_URL") or ""
