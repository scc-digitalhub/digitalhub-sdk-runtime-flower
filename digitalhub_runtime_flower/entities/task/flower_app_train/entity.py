# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import Status, Task

from digitalhub_runtime_flower.entities.task.flower_app_train.spec import TaskSpecFlowerAppTrain


class TaskFlowerAppTrain(Task):
    """
    TaskFlowerAppTrain class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: TaskSpecFlowerAppTrain
        self.status: Status
