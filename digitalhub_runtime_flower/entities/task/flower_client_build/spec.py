# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities._mixin.execution.spec import BuildSpecMixin
from digitalhub.entities.task._base.spec import TaskSpecFunction

from digitalhub_runtime_flower.entities._mixin.execution.spec import FlowerClientSpecMixin


class TaskSpecFlowerClientBuild(TaskSpecFunction, BuildSpecMixin, FlowerClientSpecMixin):
    """Specification for a Flower client build task."""
