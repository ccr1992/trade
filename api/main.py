from fastapi import FastAPI, status


app = FastAPI(title="Trader",
              description="Trader",
              )

@app.get("/healthcheck",  status_code=status.HTTP_200_OK)
def healthcheck():
    return {"healthcheck": "Everything OK!"}
