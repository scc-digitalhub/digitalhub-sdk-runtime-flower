# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities._base.entity.spec import Spec
from digitalhub.entities.task._base.spec import TaskSpecFunction


class FlowerTrainSpecMixin(Spec):
    schedule: str | None = None


class TaskSpecFlowerAppTrain(TaskSpecFunction, FlowerTrainSpecMixin):
    """Specification for a Flower application training task."""
