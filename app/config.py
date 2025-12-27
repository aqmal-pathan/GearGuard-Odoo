class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///gearguard.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "dev-secret"
