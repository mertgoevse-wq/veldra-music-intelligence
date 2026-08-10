from dataclasses import dataclass, field
from typing import Any, Protocol


@dataclass
class ModelCapabilities:
    name: str
    provider: str
    modalities: list[str] = field(default_factory=list)
    tasks: list[str] = field(default_factory=list)
    context_length: int | None = None
    local: bool = False


@dataclass
class ModelRequest:
    task: str
    input_data: dict[str, Any]
    instructions: str = ""
    context: dict[str, Any] = field(default_factory=dict)


@dataclass
class ModelResponse:
    model: str
    provider: str
    task: str
    output: dict[str, Any]
    confidence: float | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


class VMIModelAdapter(Protocol):

    @property
    def capabilities(self) -> ModelCapabilities:
        ...

    def analyze(
        self,
        request: ModelRequest,
    ) -> ModelResponse:
        ...


class ModelRegistry:

    def __init__(self):
        self._models: dict[str, VMIModelAdapter] = {}

    def register(
        self,
        model_id: str,
        adapter: VMIModelAdapter,
    ) -> None:
        self._models[model_id] = adapter

    def get(
        self,
        model_id: str,
    ) -> VMIModelAdapter:
        if model_id not in self._models:
            raise KeyError(
                f"Unknown VMI model: {model_id}"
            )

        return self._models[model_id]

    def list_models(self) -> list[str]:
        return sorted(self._models.keys())
