from fastapi import APIRouter, Request
from app.dtos.buscadorDto import BuscadorModel
from app.views.buscador.buscador import BuscadorViewSingleton
router = APIRouter()

@router.post("/init/buscador")
async def dispatchBuscador(request: Request, data: BuscadorModel):
    return await BuscadorViewSingleton.dispatch(data)
