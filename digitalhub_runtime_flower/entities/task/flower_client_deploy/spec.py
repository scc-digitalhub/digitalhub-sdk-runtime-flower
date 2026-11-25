# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import TaskSpecFunction

from digitalhub_runtime_flower.entities._mixin.execution.spec import FlowerClientSpecMixin


class TaskSpecFlowerClientDeploy(TaskSpecFunction, FlowerClientSpecMixin):
    """Specification for a Flower client deployment task."""
