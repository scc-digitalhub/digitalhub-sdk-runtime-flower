# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities._base.entity.status import Status
from digitalhub.entities.task._base.builder import TaskBuilder

from digitalhub_runtime_flower.entities._base.runtime_entity.builder import RuntimeEntityBuilderFlowerServer
from digitalhub_runtime_flower.entities._commons.enums import EntityKinds
from digitalhub_runtime_flower.entities.task.flower_server_deploy.entity import TaskFlowerServerDeploy
from digitalhub_runtime_flower.entities.task.flower_server_deploy.spec import TaskSpecFlowerServerDeploy


class TaskFlowerServerDeployBuilder(TaskBuilder, RuntimeEntityBuilderFlowerServer):
    """
    TaskFlowerServerDeploy builder.
    """

    ENTITY_CLASS = TaskFlowerServerDeploy
    ENTITY_SPEC_CLASS = TaskSpecFlowerServerDeploy
    ENTITY_STATUS_CLASS = Status
    ENTITY_KIND = EntityKinds.TASK_FLOWER_SERVER_DEPLOY.value
