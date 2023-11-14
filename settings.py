from envparse import Env

DB_URL = Env().str("DB_URL", default="postgresql://postgres:postgres@0.0.0.0:5432/postgres")
