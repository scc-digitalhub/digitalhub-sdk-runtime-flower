# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities._base.entity.status import Status
from digitalhub.entities.function._base.builder import FunctionBuilder

from digitalhub_runtime_flower.entities.function._base.entity import FunctionFlower
from digitalhub_runtime_flower.entities.function._base.spec import FunctionSpecFlower


class FunctionFlowerBuilder(FunctionBuilder):
    """
    FunctionFlower builder.
    """

    ENTITY_CLASS = FunctionFlower
    ENTITY_SPEC_CLASS = FunctionSpecFlower
    ENTITY_STATUS_CLASS = Status
