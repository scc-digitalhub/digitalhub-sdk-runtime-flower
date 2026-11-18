# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities._base.entity.status import Status

from digitalhub_runtime_flower.entities.function._base.entity import FunctionFlowerBuild
from digitalhub_runtime_flower.entities.function._base.spec import FunctionSpecFlower


class FunctionFlowerClient(FunctionFlowerBuild):
    """
    FunctionFlowerClient class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: FunctionSpecFlower
        self.status: Status
