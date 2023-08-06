from __future__ import annotations
import asyncio

import hashlib
from functools import cached_property
from typing import Any, Dict, Optional, Tuple, Union
import aiohttp
import msgpack
from pydantic import BaseModel


class Workflow(BaseModel):
    context: Dict[Union[str, Tuple[str, str, Any]], Union[str, bool, int]]
    dependency: Optional[Dict[tuple[str, Any], list[tuple[str, Any]]]]
    session: Optional[aiohttp.ClientSession]

    @cached_property
    def ident(self) -> str:
        return hashlib.sha256(msgpack.packb(self.dict())).hexdigest()

    class Config:
        keep_untouched = (cached_property,)
        arbitrary_types_allowed = True


async def run(
    agents: list[Any],
    dependency: Dict[tuple[str, Any], list[tuple[str, Any]]],
):
    workflow.session = aiohttp.ClientSession()
    workflow.dependency = dependency

    try:
        await asyncio.gather(*[agent.execute() for agent in agents])
    finally:
        await workflow.session.close()


workflow = Workflow(
    context={},
    dependency=None,
    session=None,
)
