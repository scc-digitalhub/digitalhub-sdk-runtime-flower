# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import RunBuilder

from digitalhub_runtime_flower.entities._base.runtime_entity.builder import RuntimeEntityBuilderFlowerClient
from digitalhub_runtime_flower.entities._commons.enums import EntityKinds
from digitalhub_runtime_flower.entities.run._base.status import RunStatusFlowerBuild
from digitalhub_runtime_flower.entities.run.flower_client_build.entity import RunFlowerClientBuild
from digitalhub_runtime_flower.entities.run.flower_client_build.spec import RunSpecFlowerClientBuild


class RunFlowerClientBuildBuilder(RunBuilder, RuntimeEntityBuilderFlowerClient):
    """
    RunFlowerClientBuild builder.
    """

    ENTITY_CLASS = RunFlowerClientBuild
    ENTITY_SPEC_CLASS = RunSpecFlowerClientBuild
    ENTITY_STATUS_CLASS = RunStatusFlowerBuild
    ENTITY_KIND = EntityKinds.RUN_FLOWER_CLIENT_BUILD.value
