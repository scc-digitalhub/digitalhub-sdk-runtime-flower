# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub_runtime_flower.entities.function._base.entity import FunctionFlower
from digitalhub_runtime_flower.entities.function.flower_server.spec import FunctionSpecFlowerServer
from digitalhub_runtime_flower.entities.function.flower_server.status import FunctionStatusFlowerServer


class FunctionFlowerServer(FunctionFlower):
    """
    FunctionFlowerServer class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: FunctionSpecFlowerServer
        self.status: FunctionStatusFlowerServer
