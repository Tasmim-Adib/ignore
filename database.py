import os
from schema import Products
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

MONGODB_URL = os.environ.get('MONGODB_URL')
client = AsyncIOMotorClient(MONGODB_URL)
database = client['boycott']

collection = database['products']

async def fetch_one_product(category):
    document = await collection.find_one({"c" : category})
    return document

async def add_product(products):
    document = products
    result = await collection.insert_one(document)
    return document
