from typing import Any, Callable, Dict

from google.protobuf import json_format


class GrpcApiRequestAssistant:
    def __init__(self, metadata_provider: Callable):
        super().__init__()
        self._metadata_provider = metadata_provider

    async def execute_call(self, call: Callable, request) -> Dict[str, Any]:
        metadata = await self._metadata_provider()
        response = await call(request, metadata=metadata)

        result = json_format.MessageToDict(
            message=response,
            including_default_value_fields=True,
        )

        return result
