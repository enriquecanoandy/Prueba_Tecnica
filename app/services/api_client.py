import httpx
import os
from dotenv import load_dotenv

load_dotenv()

EXTERNAL_API_URL = os.getenv("EXTERNAL_API_URL") 
API_NINJAS_KEY = os.getenv("EXTERNAL_API_KEY")  
    
##print("API_NINJAS_KEY:", API_NINJAS_KEY)

async def fetch_city_info(city: str):
    try:
        url = f"{EXTERNAL_API_URL}?city={city}"
        headers = {"X-Api-Key": API_NINJAS_KEY}

        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers, timeout=10)

        data = response.json()
        
        if not data:
            return {"error": "city_not_found"}

        return data[0]

    except Exception as e:
        return {"error": str(e)}

