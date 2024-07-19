from fastapi import FastAPI
from app.chat import router as chat_router

app = FastAPI(
    title="Chatbot Project",
    version="1.0",
    description="A simple API server using FastAPI and LangChain",
)

app.include_router(chat_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
