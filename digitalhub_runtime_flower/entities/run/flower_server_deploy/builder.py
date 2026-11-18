# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.run._base.builder import RunBuilder
from digitalhub.entities.run._base.status import RunStatus

from digitalhub_runtime_flower.entities._base.runtime_entity.builder import RuntimeEntityBuilderFlowerServer
from digitalhub_runtime_flower.entities._commons.enums import EntityKinds
from digitalhub_runtime_flower.entities.run.flower_server_deploy.entity import RunFlowerServerDeploy
from digitalhub_runtime_flower.entities.run.flower_server_deploy.spec import RunSpecFlowerServerDeploy


class RunFlowerServerDeployBuilder(RunBuilder, RuntimeEntityBuilderFlowerServer):
    """
    RunFlowerServerDeploy builder.
    """

    ENTITY_CLASS = RunFlowerServerDeploy
    ENTITY_SPEC_CLASS = RunSpecFlowerServerDeploy
    ENTITY_STATUS_CLASS = RunStatus
    ENTITY_KIND = EntityKinds.RUN_FLOWER_SERVER_DEPLOY.value
