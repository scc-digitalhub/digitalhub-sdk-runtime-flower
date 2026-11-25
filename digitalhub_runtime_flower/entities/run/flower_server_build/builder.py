# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import RunBuilder

from digitalhub_runtime_flower.entities._base.runtime_entity.builder import RuntimeEntityBuilderFlowerServer
from digitalhub_runtime_flower.entities._commons.enums import EntityKinds
from digitalhub_runtime_flower.entities.run._base.status import RunStatusFlowerBuild
from digitalhub_runtime_flower.entities.run.flower_server_build.entity import RunFlowerServerBuild
from digitalhub_runtime_flower.entities.run.flower_server_build.spec import RunSpecFlowerServerBuild


class RunFlowerServerBuildBuilder(RunBuilder, RuntimeEntityBuilderFlowerServer):
    """
    RunFlowerServerBuild builder.
    """

    ENTITY_CLASS = RunFlowerServerBuild
    ENTITY_SPEC_CLASS = RunSpecFlowerServerBuild
    ENTITY_STATUS_CLASS = RunStatusFlowerBuild
    ENTITY_KIND = EntityKinds.RUN_FLOWER_SERVER_BUILD.value
