import pytest
from digitalhub.entities._constructors.spec import build_spec
from pydantic import ValidationError

from digitalhub_runtime_flower.entities._mixin.execution.spec import (
    FlowerClientSpecMixin,
    FlowerConnectionSpecMixin,
    FlowerServerSpecMixin,
    FlowerTrainSpecMixin,
)
from digitalhub_runtime_flower.entities.function._base.spec import FunctionSpecFlower
from digitalhub_runtime_flower.entities.function.flower_app.models import FABSource
from digitalhub_runtime_flower.entities.function.flower_app.spec import FunctionSpecFlowerApp
from digitalhub_runtime_flower.entities.run._base.status import RunStatusFlowerBuild
from digitalhub_runtime_flower.entities.run.flower_app_train.spec import RunSpecFlowerAppTrain
from digitalhub_runtime_flower.entities.run.flower_client_build.builder import RunFlowerClientBuildBuilder
from digitalhub_runtime_flower.entities.run.flower_client_build.spec import RunSpecFlowerClientBuild
from digitalhub_runtime_flower.entities.run.flower_client_deploy.spec import RunSpecFlowerClientDeploy
from digitalhub_runtime_flower.entities.run.flower_server_build.builder import RunFlowerServerBuildBuilder
from digitalhub_runtime_flower.entities.run.flower_server_build.spec import RunSpecFlowerServerBuild
from digitalhub_runtime_flower.entities.run.flower_server_deploy.spec import RunSpecFlowerServerDeploy
from digitalhub_runtime_flower.entities.task.flower_app_train.spec import TaskSpecFlowerAppTrain
from digitalhub_runtime_flower.entities.task.flower_client_build.spec import TaskSpecFlowerClientBuild
from digitalhub_runtime_flower.entities.task.flower_client_deploy.spec import TaskSpecFlowerClientDeploy
from digitalhub_runtime_flower.entities.task.flower_server_build.spec import TaskSpecFlowerServerBuild
from digitalhub_runtime_flower.entities.task.flower_server_deploy.spec import TaskSpecFlowerServerDeploy


def test_flower_function_specs_validate_fields_and_nested_fab_source():
    app = build_spec(
        FunctionSpecFlowerApp,
        fab_source={"clientapp": "client:app"},
        requirements="flwr>=1.10",
    )
    client = build_spec(FunctionSpecFlower, requirements=["flwr>=1.10"])

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
        function="function",
        task="task",
        federation="federation",
        local_execution=True,
        schedule="0 0 * * *",
    )
    client_build = build_spec(
        RunSpecFlowerClientBuild,
        function="function",
        task="task",
        superlink="superlink",
        node_config={"partition-id": 1},
        instructions=["pip install flwr"],
    )
    server_build = build_spec(
        RunSpecFlowerServerBuild,
        function="function",
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

    legacy = RunSpecFlowerAppTrain.from_dict({"function": "function", "task": "task", "schedule": "0 0 * * *"})
    assert legacy.to_dict()["schedule"] == "0 0 * * *"


def test_flower_runtime_spec_mixins_have_one_owner():
    assert FlowerConnectionSpecMixin in RunSpecFlowerAppTrain.__mro__
    assert FlowerTrainSpecMixin in TaskSpecFlowerAppTrain.__mro__
    assert FlowerTrainSpecMixin in RunSpecFlowerAppTrain.__mro__

    for spec_class in (
        TaskSpecFlowerClientBuild,
        TaskSpecFlowerClientDeploy,
        RunSpecFlowerClientBuild,
        RunSpecFlowerClientDeploy,
    ):
        assert FlowerClientSpecMixin in spec_class.__mro__

    for spec_class in (
        TaskSpecFlowerServerBuild,
        TaskSpecFlowerServerDeploy,
        RunSpecFlowerServerBuild,
        RunSpecFlowerServerDeploy,
    ):
        assert FlowerServerSpecMixin in spec_class.__mro__

    assert RunFlowerClientBuildBuilder.ENTITY_STATUS_CLASS is RunStatusFlowerBuild
    assert RunFlowerServerBuildBuilder.ENTITY_STATUS_CLASS is RunStatusFlowerBuild
