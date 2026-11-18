# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities._base.entity.status import Status

from digitalhub_runtime_flower.entities._base.runtime_entity.builder import RuntimeEntityBuilderFlowerClient
from digitalhub_runtime_flower.entities._commons.enums import EntityKinds
from digitalhub_runtime_flower.entities.function._base.builder import FunctionFlowerBuilder
from digitalhub_runtime_flower.entities.function._base.spec import FunctionSpecFlower
from digitalhub_runtime_flower.entities.function.flower_client.entity import FunctionFlowerClient


class FunctionFlowerClientBuilder(FunctionFlowerBuilder, RuntimeEntityBuilderFlowerClient):
    """
    FunctionFlowerClient builder.
    """

    ENTITY_CLASS = FunctionFlowerClient
    ENTITY_SPEC_CLASS = FunctionSpecFlower
    ENTITY_STATUS_CLASS = Status
    ENTITY_KIND = EntityKinds.FUNCTION_FLOWER_CLIENT.value
