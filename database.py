import os
from schema import Products
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load variables from .env file
# load_dotenv()

MONGODB_URL = 'mongodb+srv://adibskitto:QsRbJD3MAhcO8IL7@cluster0.96y8ytj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
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
