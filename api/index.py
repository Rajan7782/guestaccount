from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import random
import string

app = FastAPI(title="Account Creator API", version="1.0.0")

# ✅ Helper function: Generate random account name and password
def generate_account(region: str, index: int):
    name = f"RRAJAN{''.join(random.choices(string.ascii_uppercase + string.digits, k=3))}"
    uid = random.randint(4200000000, 4299999999)
    password = f"BNGX_VIP{''.join(random.choices(string.ascii_uppercase + string.digits, k=12))}"
    return {
        "name": name,
        "uid": uid,
        "password": password,
        "region": region.upper()
    }

# ✅ Root route
@app.get("/")
def home():
    return {"status": "ok", "message": "Account Creator API running successfully!"}

# ✅ API route to create accounts
@app.get("/create_account")
def create_account(
    region: str = Query("IND", description="Enter region code (e.g., IND, BR, EU)"),
    count: int = Query(1, description="Number of accounts to create")
):
    if count < 1 or count > 100:
        return JSONResponse(status_code=400, content={"error": "Count must be between 1 and 100"})

    accounts = [generate_account(region, i) for i in range(count)]
    return {"status": "success", "count": count, "accounts": accounts}
