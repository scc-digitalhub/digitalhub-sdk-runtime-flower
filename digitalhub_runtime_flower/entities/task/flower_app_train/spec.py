# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.task._base.spec import TaskSpecFunction


class TaskSpecFlowerAppTrain(TaskSpecFunction):
    """Specification for a Flower application training task."""

    schedule: str | None = None
