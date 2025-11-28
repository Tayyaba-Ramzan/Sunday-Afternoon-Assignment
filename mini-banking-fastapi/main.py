from fastapi import FastAPI
import random

app = FastAPI()

side_hustles=[
    "Freelancing - Start offering your skills online",
    "Dropshipping - Sell products without holding inventory",
    "E-commerce - Start an online store",
    "Affiliate Marketing - Promote products and earn commissions",
    "Content Creation - Start a blog or YouTube channel",
    "Graphic Design - Offer design services to clients",
    "Social Media Management - Help businesses grow their social media presence",
    
]

money_quotes=[
    "The only way to do great work is to love what you do.",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful.",
    "I've failed over and over and over again in my life and that is why I succeed.",
    "The way to get started is to quit talking and begin doing.",
    
]

@app.get("/side_hustles")
def get_side_hustle(apikey:str):
    """Return a random side hustle idea"""
    if apikey != "1234567890":
        return {"error": "Invalid API key"}
    return {"side_hustle": random.choice(side_hustles)}

@app.get("/money_quote")
def get_money_quote(apikey:str):
    """Return a random money quote"""
    if apikey != "1234567890":
        return {"error": "Invalid API key"}
    return {"money_quote": random.choice(money_quotes)}
