import pytest
from digitalhub.entities._constructors.spec import build_spec
from pydantic import ValidationError

from digitalhub_runtime_flower.entities.function.flower_app.models import FABSource
from digitalhub_runtime_flower.entities.function.flower_app.spec import FunctionSpecFlowerApp
from digitalhub_runtime_flower.entities.function.flower_client.spec import FunctionSpecFlowerClient
from digitalhub_runtime_flower.entities.run.flower_app_train.spec import RunSpecFlowerAppTrain
from digitalhub_runtime_flower.entities.run.flower_client_build.spec import RunSpecFlowerClientBuild
from digitalhub_runtime_flower.entities.run.flower_server_build.spec import RunSpecFlowerServerBuild
from digitalhub_runtime_flower.entities.task.flower_app_train.spec import TaskSpecFlowerAppTrain
from digitalhub_runtime_flower.entities.task.flower_client_build.spec import TaskSpecFlowerClientBuild


def test_flower_function_specs_validate_fields_and_nested_fab_source():
    app = build_spec(
        FunctionSpecFlowerApp,
        fab_source={"clientapp": "client:app"},
        requirements="flwr>=1.10",
    )
    client = build_spec(FunctionSpecFlowerClient, requirements=["flwr>=1.10"])

    assert isinstance(app.fab_source, FABSource)
    assert app.fab_source.clientapp == "client:app"
    assert app.requirements == "flwr>=1.10"
    assert client.requirements == ["flwr>=1.10"]

    with pytest.raises(ValidationError):
        build_spec(FunctionSpecFlowerApp, fab_source={"clientapp": 1})


def test_flower_task_and_run_specs_keep_task_fields_separate():
    task = build_spec(TaskSpecFlowerAppTrain, function="function", schedule="0 0 * * *")
    build_task = build_spec(
        TaskSpecFlowerClientBuild,
        function="function",
        instructions=["pip install flwr"],
    )
    app_run = build_spec(
        RunSpecFlowerAppTrain,
        task="task",
        federation="federation",
        local_execution=True,
        schedule="0 0 * * *",
    )
    client_build = build_spec(
        RunSpecFlowerClientBuild,
        task="task",
        superlink="superlink",
        node_config={"partition-id": 1},
        instructions=["pip install flwr"],
    )
    server_build = build_spec(
        RunSpecFlowerServerBuild,
        task="task",
        auth_public_keys=["key"],
        insecure=True,
        instructions=["pip install flwr"],
    )

    assert task.schedule == "0 0 * * *"
    assert build_task.instructions == ["pip install flwr"]
    assert app_run.federation == "federation"
    assert app_run.local_execution is True
    assert app_run.schedule == "0 0 * * *"
    assert client_build.node_config == {"partition-id": 1}
    assert client_build.instructions == ["pip install flwr"]
    assert server_build.auth_public_keys == ["key"]
    assert server_build.insecure is True
    assert server_build.instructions == ["pip install flwr"]

    legacy = RunSpecFlowerAppTrain.from_dict({"task": "task", "schedule": "0 0 * * *"})
    assert legacy.to_dict()["schedule"] == "0 0 * * *"
