from fastapi import APIRouter

from app.schemas.aider import (
    PromptRequest,
    PromptResponse,
)

router = APIRouter(
    prefix="/aider"
)


@router.get("/status")
async def status():
    return {
        "status": "online",
        "version": "1.0.0"
    }


@router.post(
    "/chat",
    response_model=PromptResponse,
)
async def chat(
    request: PromptRequest,
):
    return PromptResponse(
        success=True,
        message=f"Received: {request.prompt}",
    )
