import time
from importlib.metadata import version
from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel

APP_NAME = "Sourcelens"
APP_VERSION = version("sourcelens")
STARTED_AT = time.monotonic()

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="Agentic codebase intelligence platform.",
)


class RootResponse(BaseModel):
    name: str
    version: str
    description: str
    docs: str
    health: str


class HealthResponse(BaseModel):
    status: Literal["ok"]
    version: str
    uptime_seconds: float


@app.get("/", response_model=RootResponse, tags=["meta"])
async def root() -> RootResponse:
    return RootResponse(
        name=APP_NAME,
        version=APP_VERSION,
        description="Agentic codebase intelligence platform.",
        docs="/docs",
        health="/health",
    )


@app.get("/health", response_model=HealthResponse, tags=["meta"])
async def health() -> HealthResponse:
    return HealthResponse(
        status="ok",
        version=APP_VERSION,
        uptime_seconds=round(time.monotonic() - STARTED_AT, 2),
    )
