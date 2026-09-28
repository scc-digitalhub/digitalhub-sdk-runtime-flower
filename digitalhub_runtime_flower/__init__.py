# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
from digitalhub_runtime_flower.entities import entity_plugins
from digitalhub_runtime_flower.entities._commons.enums import EntityKinds

entity_builders = tuple((plugin.kind, plugin.builder) for plugin in entity_plugins)

try:
    from digitalhub_runtime_flower.runtimes.builder import RuntimeFlowerAppBuilder, RuntimeFlowerBuilder

    kinds = [e.value for e in EntityKinds]
    flower_app = [
        EntityKinds.FUNCTION_FLOWER_APP.value,
        EntityKinds.TASK_FLOWER_APP_TRAIN.value,
        EntityKinds.RUN_FLOWER_APP_TRAIN.value,
    ]
    runtime_builders = tuple((e, RuntimeFlowerAppBuilder if e in flower_app else RuntimeFlowerBuilder) for e in kinds)


except ImportError as e:
    from digitalhub.utils.logger.logger import get_logger

    logger = get_logger(__name__)
    logger.debug(f"Error importing runtime builders: {e}")
    runtime_builders = tuple()
