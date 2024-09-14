from fastapi import FastAPI
from api.endpoints import router

app = FastAPI(title="Referral Program", description="Mining Application Referral Program.")
app.include_router(router, prefix="/referral")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8081, reload=True)
