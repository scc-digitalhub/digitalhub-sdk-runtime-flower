# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from typing import Optional

from digitalhub.entities.task._base.spec import TaskSpec, TaskValidator


class TaskSpecFlowerClientBuild(TaskSpec):
    """
    TaskSpecFlowerClientBuild specifications.
    """

    def __init__(
        self,
        instructions: list[str] | None = None,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.instructions = instructions


class TaskValidatorFlowerClientBuild(TaskValidator):
    """
    TaskValidatorFlowerClientBuild validator.
    """

    instructions: Optional[list[str]] = None
