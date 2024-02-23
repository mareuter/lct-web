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

from fastapi import FastAPI

from .models.index import IndexResponse
from .routers import lunar_club, lunar_two, moon_info

__all__ = ["app"]

app = FastAPI()

app.include_router(moon_info.router)
app.include_router(lunar_club.router)
app.include_router(lunar_two.router)


@app.get("/")
async def root() -> IndexResponse:
    return IndexResponse(msg="This is a web service, nothing to see here.")
