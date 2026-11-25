# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import Status, TaskBuilder

from digitalhub_runtime_flower.entities._base.runtime_entity.builder import RuntimeEntityBuilderFlowerClient
from digitalhub_runtime_flower.entities._commons.enums import EntityKinds
from digitalhub_runtime_flower.entities.task.flower_client_deploy.entity import TaskFlowerClientDeploy
from digitalhub_runtime_flower.entities.task.flower_client_deploy.spec import TaskSpecFlowerClientDeploy


class TaskFlowerClientDeployBuilder(TaskBuilder, RuntimeEntityBuilderFlowerClient):
    """
    TaskFlowerClientDeploy builder.
    """

    ENTITY_CLASS = TaskFlowerClientDeploy
    ENTITY_SPEC_CLASS = TaskSpecFlowerClientDeploy
    ENTITY_STATUS_CLASS = Status
    ENTITY_KIND = EntityKinds.TASK_FLOWER_CLIENT_DEPLOY.value
