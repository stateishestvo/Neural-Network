import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import telegram_bot

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("uvicorn")

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    logger.info(f"Received update: {data}")
    update = telegram_bot.process_update(data)
    return JSONResponse({"status": "ok"})

@app.on_event("startup")
async def startup_event():
    telegram_bot.set_webhook()
    logger.info("Webhook set")

@app.on_event("shutdown")
async def shutdown_event():
    telegram_bot.delete_webhook()
    logger.info("Webhook deleted")