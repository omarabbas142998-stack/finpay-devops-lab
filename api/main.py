from fastapi import FastAPI, HTTPException

app = FastAPI(title="FinPay API")

# In-memory fake data (temporary — real DB comes in Phase 3)
accounts = [
    {"id": 1, "owner": "Alice", "balance": 1500.00},
    {"id": 2, "owner": "Bob", "balance": 2300.50},
]

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "Welcome to FinPay API"}

@app.get("/accounts")
def get_accounts():
    return accounts

@app.get("/accounts/{account_id}")
def get_account(account_id: int):
    for acc in accounts:
        if acc["id"] == account_id:
            return acc
    raise HTTPException(status_code=404, detail="Account not found")
