from fastapi import FastAPI
from fastapi.logger import logger

import api


async def init_http_client() -> None:
    logger.info("on_start_up")


async def close_http_client() -> None:
    logger.info("on_shutdown")


def create_app():
    app_ = FastAPI(
        docs_url="/docs", on_startup=[init_http_client],
        on_shutdown=[close_http_client]
    )
    app_.include_router(api.router)
    return app_


app = create_app()
