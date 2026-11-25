# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import Status

from digitalhub_runtime_flower.entities._base.runtime_entity.builder import RuntimeEntityBuilderFlowerServer
from digitalhub_runtime_flower.entities._commons.enums import EntityKinds
from digitalhub_runtime_flower.entities.function._base.builder import FunctionFlowerBuilder
from digitalhub_runtime_flower.entities.function._base.spec import FunctionSpecFlower
from digitalhub_runtime_flower.entities.function.flower_server.entity import FunctionFlowerServer


class FunctionFlowerServerBuilder(FunctionFlowerBuilder, RuntimeEntityBuilderFlowerServer):
    """
    FunctionFlowerServer builder.
    """

    ENTITY_CLASS = FunctionFlowerServer
    ENTITY_SPEC_CLASS = FunctionSpecFlower
    ENTITY_STATUS_CLASS = Status
    ENTITY_KIND = EntityKinds.FUNCTION_FLOWER_SERVER.value
