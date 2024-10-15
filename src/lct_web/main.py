# This file is part of lct-web.
#
# Developed by Michael Reuter.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

"""Main application definition."""

from __future__ import annotations

from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from . import __version__
from .models.index_response import IndexResponse
from .routers import lunar_club, lunar_two, moon_info

__all__ = ["app"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_methods=["GET"],
    allow_headers=["Content-Type"],
)

app.include_router(moon_info.router)
app.include_router(lunar_club.router)
app.include_router(lunar_two.router)


def set_schema() -> dict[str, Any]:
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Lunar Club Tools Web Service API",
        version=__version__,
        description=" ".join(
            [
                "This API provides information related to the Lunar Club and Lunar II ",
                "observing clubs from the Astronomical League. It also provides ephemeris",
                "information.",
            ]
        ),
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = set_schema  # type: ignore


@app.get("/")
async def root() -> IndexResponse:
    return IndexResponse(msg="This is a web service, nothing to see here.")
