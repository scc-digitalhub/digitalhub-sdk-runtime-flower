# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from digitalhub.plugins import (
    Action,
    BuilderDef,
    CrudPlugin,
    ExecFamily,
    FunctionBuilder,
    RunBuilder,
    RunStatus,
    Status,
    TaskBuilder,
)

from digitalhub_runtime_flower.entities._commons.enums import Actions, EntityKinds
from digitalhub_runtime_flower.entities.function._base.spec import FunctionSpecFlower
from digitalhub_runtime_flower.entities.function.flower_app.builder import FunctionFlowerAppBaseBuilder
from digitalhub_runtime_flower.entities.function.flower_app.crud import new_function_flower_app
from digitalhub_runtime_flower.entities.function.flower_app.entity import FunctionFlowerApp
from digitalhub_runtime_flower.entities.function.flower_app.spec import FunctionSpecFlowerApp
from digitalhub_runtime_flower.entities.function.flower_client.crud import new_function_flower_client
from digitalhub_runtime_flower.entities.function.flower_client.entity import FunctionFlowerClient
from digitalhub_runtime_flower.entities.function.flower_server.crud import new_function_flower_server
from digitalhub_runtime_flower.entities.function.flower_server.entity import FunctionFlowerServer
from digitalhub_runtime_flower.entities.run._base.status import RunStatusFlowerBuild
from digitalhub_runtime_flower.entities.run.flower_app_train.entity import RunFlowerAppTrain
from digitalhub_runtime_flower.entities.run.flower_app_train.spec import RunSpecFlowerAppTrain
from digitalhub_runtime_flower.entities.run.flower_client_build.entity import RunFlowerClientBuild
from digitalhub_runtime_flower.entities.run.flower_client_build.spec import RunSpecFlowerClientBuild
from digitalhub_runtime_flower.entities.run.flower_client_deploy.entity import RunFlowerClientDeploy
from digitalhub_runtime_flower.entities.run.flower_client_deploy.spec import RunSpecFlowerClientDeploy
from digitalhub_runtime_flower.entities.run.flower_server_build.entity import RunFlowerServerBuild
from digitalhub_runtime_flower.entities.run.flower_server_build.spec import RunSpecFlowerServerBuild
from digitalhub_runtime_flower.entities.run.flower_server_deploy.entity import RunFlowerServerDeploy
from digitalhub_runtime_flower.entities.run.flower_server_deploy.spec import RunSpecFlowerServerDeploy
from digitalhub_runtime_flower.entities.task.flower_app_train.entity import TaskFlowerAppTrain
from digitalhub_runtime_flower.entities.task.flower_app_train.spec import TaskSpecFlowerAppTrain
from digitalhub_runtime_flower.entities.task.flower_client_build.entity import TaskFlowerClientBuild
from digitalhub_runtime_flower.entities.task.flower_client_build.spec import TaskSpecFlowerClientBuild
from digitalhub_runtime_flower.entities.task.flower_client_deploy.entity import TaskFlowerClientDeploy
from digitalhub_runtime_flower.entities.task.flower_client_deploy.spec import TaskSpecFlowerClientDeploy
from digitalhub_runtime_flower.entities.task.flower_server_build.entity import TaskFlowerServerBuild
from digitalhub_runtime_flower.entities.task.flower_server_build.spec import TaskSpecFlowerServerBuild
from digitalhub_runtime_flower.entities.task.flower_server_deploy.entity import TaskFlowerServerDeploy
from digitalhub_runtime_flower.entities.task.flower_server_deploy.spec import TaskSpecFlowerServerDeploy

# Imported on first use: the entities register even when the runtime cannot be
# imported, and the import error is reported when a run executes locally.
RUNTIME_FLOWER_APP_BUILDER = "digitalhub_runtime_flower.runtimes.builder:RuntimeFlowerAppBuilder"
RUNTIME_FLOWER_BUILDER = "digitalhub_runtime_flower.runtimes.builder:RuntimeFlowerBuilder"

flower_app = ExecFamily(
    executable=BuilderDef(
        EntityKinds.FUNCTION_FLOWER_APP,
        FunctionFlowerApp,
        FunctionSpecFlowerApp,
        Status,
        base=FunctionFlowerAppBaseBuilder,
        shortcuts=(CrudPlugin(new_function_flower_app),),
    ),
    actions={
        Actions.TRAIN: Action(
            task=BuilderDef(
                EntityKinds.TASK_FLOWER_APP_TRAIN, TaskFlowerAppTrain, TaskSpecFlowerAppTrain, Status, base=TaskBuilder
            ),
            run=BuilderDef(
                EntityKinds.RUN_FLOWER_APP_TRAIN, RunFlowerAppTrain, RunSpecFlowerAppTrain, RunStatus, base=RunBuilder
            ),
        ),
    },
    runtime_builder=RUNTIME_FLOWER_APP_BUILDER,
)

flower_server = ExecFamily(
    executable=BuilderDef(
        EntityKinds.FUNCTION_FLOWER_SERVER,
        FunctionFlowerServer,
        FunctionSpecFlower,
        Status,
        base=FunctionBuilder,
        shortcuts=(CrudPlugin(new_function_flower_server),),
    ),
    actions={
        Actions.BUILD: Action(
            task=BuilderDef(
                EntityKinds.TASK_FLOWER_SERVER_BUILD,
                TaskFlowerServerBuild,
                TaskSpecFlowerServerBuild,
                Status,
                base=TaskBuilder,
            ),
            run=BuilderDef(
                EntityKinds.RUN_FLOWER_SERVER_BUILD,
                RunFlowerServerBuild,
                RunSpecFlowerServerBuild,
                RunStatusFlowerBuild,
                base=RunBuilder,
            ),
        ),
        Actions.DEPLOY: Action(
            task=BuilderDef(
                EntityKinds.TASK_FLOWER_SERVER_DEPLOY,
                TaskFlowerServerDeploy,
                TaskSpecFlowerServerDeploy,
                Status,
                base=TaskBuilder,
            ),
            run=BuilderDef(
                EntityKinds.RUN_FLOWER_SERVER_DEPLOY,
                RunFlowerServerDeploy,
                RunSpecFlowerServerDeploy,
                RunStatus,
                base=RunBuilder,
            ),
        ),
    },
    runtime_builder=RUNTIME_FLOWER_BUILDER,
)

flower_client = ExecFamily(
    executable=BuilderDef(
        EntityKinds.FUNCTION_FLOWER_CLIENT,
        FunctionFlowerClient,
        FunctionSpecFlower,
        Status,
        base=FunctionBuilder,
        shortcuts=(CrudPlugin(new_function_flower_client),),
    ),
    actions={
        Actions.BUILD: Action(
            task=BuilderDef(
                EntityKinds.TASK_FLOWER_CLIENT_BUILD,
                TaskFlowerClientBuild,
                TaskSpecFlowerClientBuild,
                Status,
                base=TaskBuilder,
            ),
            run=BuilderDef(
                EntityKinds.RUN_FLOWER_CLIENT_BUILD,
                RunFlowerClientBuild,
                RunSpecFlowerClientBuild,
                RunStatusFlowerBuild,
                base=RunBuilder,
            ),
        ),
        Actions.DEPLOY: Action(
            task=BuilderDef(
                EntityKinds.TASK_FLOWER_CLIENT_DEPLOY,
                TaskFlowerClientDeploy,
                TaskSpecFlowerClientDeploy,
                Status,
                base=TaskBuilder,
            ),
            run=BuilderDef(
                EntityKinds.RUN_FLOWER_CLIENT_DEPLOY,
                RunFlowerClientDeploy,
                RunSpecFlowerClientDeploy,
                RunStatus,
                base=RunBuilder,
            ),
        ),
    },
    runtime_builder=RUNTIME_FLOWER_BUILDER,
)

entity_plugins = (
    *flower_app.plugins(),
    *flower_server.plugins(),
    *flower_client.plugins(),
)
