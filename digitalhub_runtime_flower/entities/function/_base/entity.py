# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.function._base.entity import Function

from digitalhub_runtime_flower.entities._commons.requirement_parser.parser import RequirementParser
from digitalhub_runtime_flower.entities.function._base.spec import FunctionSpecFlower
from digitalhub_runtime_flower.entities.function._base.status import FunctionStatusFlower


class FunctionFlower(Function):
    """
    FunctionFlower class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: FunctionSpecFlower
        self.status: FunctionStatusFlower

    def _post_create_hook_before_save(self) -> None:
        """
        Hook method called after the creation of the entity but before saving
        in Core.
        Can be overridden in subclasses to implement custom behavior.
        """
        self.spec.requirements = RequirementParser().parse(self.spec.requirements)
