import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Detect the environment (default: development)
ENV = os.getenv("ENV", "development")

# Select the appropriate .env file
env_file = f".env.{ENV}"

# Load environment variables from the selected file
load_dotenv(env_file)

# Get database URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Create the database engine

if not DATABASE_URL:
    raise Exception("DATABASE_URL is not set")

engine = create_engine(DATABASE_URL, echo=True)

# Create a session factory
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base class for ORM models
Base = declarative_base()
