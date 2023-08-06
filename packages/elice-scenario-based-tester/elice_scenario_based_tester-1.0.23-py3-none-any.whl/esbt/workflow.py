from __future__ import annotations

import hashlib
from functools import cached_property
from typing import Any, Dict, Optional, Tuple, Union

import msgpack
from pydantic import BaseModel


class Workflow(BaseModel):
    dependency: Optional[Dict[tuple[str, Any], list[tuple[str, Any]]]]
    context: Dict[Union[str, Tuple[str, str, Any]], Union[str, bool, int]]

    @cached_property
    def ident(self) -> str:
        return hashlib.sha256(msgpack.packb(self.dict())).hexdigest()

    class Config:
        keep_untouched = (cached_property,)
        arbitrary_types_allowed = True


workflow = Workflow(
    dependency={},
    context={},
)
