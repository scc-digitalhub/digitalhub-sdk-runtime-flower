# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.entities.task._base.entity import Task

if typing.TYPE_CHECKING:
    pass

from digitalhub_runtime_flower.entities.task.flower_client_deploy.spec import TaskSpecFlowerClientDeploy
from digitalhub_runtime_flower.entities.task.flower_client_deploy.status import TaskStatusFlowerClientDeploy


class TaskFlowerClientDeploy(Task):
    """
    TaskFlowerClientDeploy class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: TaskSpecFlowerClientDeploy
        self.status: TaskStatusFlowerClientDeploy
