from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers import order_controller, menu_items_controller

app = FastAPI()
origins = [
    "http://localhost:3010",  # Adicione aqui o endereço do frontend React
    # Outros domínios podem ser adicionados se necessário
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, OPTIONS, etc)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

app.include_router(order_controller.router)
app.include_router(menu_items_controller.router)
