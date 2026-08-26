# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.function._base.entity import Function

from digitalhub_runtime_flower.entities._commons.enums import Actions
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


class FunctionFlowerBuild(FunctionFlower):
    """
    Base class for buildable Flower functions.
    """

    def build(
        self,
        wait: bool = True,
        log_info: bool = True,
        extensions: list[dict] | None = None,
        **kwargs,
    ):
        """Build the function using the build action."""
        return super().run(
            Actions.BUILD.value,
            wait=wait,
            log_info=log_info,
            extensions=extensions,
            **kwargs,
        )

    def run(
        self,
        action: str,
        wait: bool = False,
        log_info: bool = True,
        extensions: list[dict] | None = None,
        auto_build: bool = True,
        **kwargs,
    ):
        """Run the function, building it when no image is available."""
        if auto_build and self.spec.image is None:
            self.build(wait=True, log_info=log_info)

        return super().run(
            action,
            wait=wait,
            log_info=log_info,
            extensions=extensions,
            **kwargs,
        )
