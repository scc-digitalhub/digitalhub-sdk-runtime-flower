# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from digitalhub.factory.plugins import CrudPlugin, EntityPlugin

from digitalhub_runtime_flower.entities.function.flower_app.builder import FunctionFlowerAppBuilder
from digitalhub_runtime_flower.entities.function.flower_app.crud import new_function_flower_app
from digitalhub_runtime_flower.entities.function.flower_client.builder import FunctionFlowerClientBuilder
from digitalhub_runtime_flower.entities.function.flower_client.crud import new_function_flower_client
from digitalhub_runtime_flower.entities.function.flower_server.builder import FunctionFlowerServerBuilder
from digitalhub_runtime_flower.entities.function.flower_server.crud import new_function_flower_server
from digitalhub_runtime_flower.entities.run.flower_app_train.builder import RunFlowerAppTrainBuilder
from digitalhub_runtime_flower.entities.run.flower_client_build.builder import RunFlowerClientBuildBuilder
from digitalhub_runtime_flower.entities.run.flower_client_deploy.builder import RunFlowerClientDeployBuilder
from digitalhub_runtime_flower.entities.run.flower_server_build.builder import RunFlowerServerBuildBuilder
from digitalhub_runtime_flower.entities.run.flower_server_deploy.builder import RunFlowerServerDeployBuilder
from digitalhub_runtime_flower.entities.task.flower_app_train.builder import TaskFlowerAppTrainBuilder
from digitalhub_runtime_flower.entities.task.flower_client_build.builder import TaskFlowerClientBuildBuilder
from digitalhub_runtime_flower.entities.task.flower_client_deploy.builder import TaskFlowerClientDeployBuilder
from digitalhub_runtime_flower.entities.task.flower_server_build.builder import TaskFlowerServerBuildBuilder
from digitalhub_runtime_flower.entities.task.flower_server_deploy.builder import TaskFlowerServerDeployBuilder

function_flower_app_plugin = EntityPlugin(
    builder=FunctionFlowerAppBuilder,
    shortcuts=(CrudPlugin(new_function_flower_app),),
)
function_flower_server_plugin = EntityPlugin(
    builder=FunctionFlowerServerBuilder,
    shortcuts=(CrudPlugin(new_function_flower_server),),
)
function_flower_client_plugin = EntityPlugin(
    builder=FunctionFlowerClientBuilder,
    shortcuts=(CrudPlugin(new_function_flower_client),),
)

entity_plugins = (
    function_flower_app_plugin,
    function_flower_server_plugin,
    function_flower_client_plugin,
    EntityPlugin(builder=TaskFlowerAppTrainBuilder),
    EntityPlugin(builder=TaskFlowerServerBuildBuilder),
    EntityPlugin(builder=TaskFlowerServerDeployBuilder),
    EntityPlugin(builder=TaskFlowerClientBuildBuilder),
    EntityPlugin(builder=TaskFlowerClientDeployBuilder),
    EntityPlugin(builder=RunFlowerAppTrainBuilder),
    EntityPlugin(builder=RunFlowerServerBuildBuilder),
    EntityPlugin(builder=RunFlowerServerDeployBuilder),
    EntityPlugin(builder=RunFlowerClientBuildBuilder),
    EntityPlugin(builder=RunFlowerClientDeployBuilder),
)
