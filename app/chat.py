from fastapi import APIRouter
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langserve import add_routes
from app.models import InputChat
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

router = APIRouter()

# Define prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [("system", "You are a helpful assistant."),
     MessagesPlaceholder(variable_name="messages"),
     ]
)

# Initialize OpenAI model
model = ChatOpenAI(model="gpt-3.5-turbo")

# Create output parser
parser = StrOutputParser()

# Create and configure the chain
chain = prompt_template | model | parser

# Add chain route to the FastAPI app
add_routes(router, chain, path="/chat", playground_type="chat")
