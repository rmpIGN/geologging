from typing import Any
from typing import Protocol
from typing import type_check_only


@type_check_only
class SupportsGeoInterface(Protocol):
    @property
    def __geo_interface__(self) -> dict[str, Any]: ...
