# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import ExecutableBuildMixin, Function, Status, parse_requirements

from digitalhub_runtime_flower.entities.function._base.spec import FunctionSpecFlower


class FunctionFlower(Function):
    """
    FunctionFlower class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: FunctionSpecFlower
        self.status: Status

    def _post_create_hook_before_save(self) -> None:
        """
        Hook method called after the creation of the entity but before saving
        in Core.
        Can be overridden in subclasses to implement custom behavior.
        """
        self.spec.requirements = parse_requirements(self.spec.requirements)


class FunctionFlowerBuild(ExecutableBuildMixin, FunctionFlower):
    """
    Base class for buildable Flower functions.
    """
