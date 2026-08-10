from src.vmi.models.protocol import (
    ModelCapabilities,
    ModelRegistry,
    ModelRequest,
    ModelResponse,
)


class DummyModel:

    @property
    def capabilities(self):
        return ModelCapabilities(
            name="dummy",
            provider="test",
            modalities=["text", "music-ir"],
            tasks=["analysis"],
            local=True,
        )

    def analyze(self, request):
        return ModelResponse(
            model="dummy",
            provider="test",
            task=request.task,
            output={
                "ok": True,
            },
        )


def test_model_registry():

    registry = ModelRegistry()

    registry.register(
        "dummy",
        DummyModel(),
    )

    assert registry.list_models() == ["dummy"]

    model = registry.get("dummy")

    assert model.capabilities.local is True


def test_model_request_response():

    request = ModelRequest(
        task="genre_analysis",
        input_data={
            "genre": "trance",
        },
    )

    response = DummyModel().analyze(
        request
    )

    assert response.task == "genre_analysis"
    assert response.output["ok"] is True
