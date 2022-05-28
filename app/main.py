from fastapi import FastAPI

from routes.index import api_router
from common.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.ROUTES_STR}/openapi.json"
)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(orgin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)