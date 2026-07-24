from pydantic import BaseModel


class PromptRequest(BaseModel):
    prompt: str


class PromptResponse(BaseModel):
    success: bool
    message: str
