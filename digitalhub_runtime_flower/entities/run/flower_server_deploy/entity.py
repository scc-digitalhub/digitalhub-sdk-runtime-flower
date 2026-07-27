# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.run._base.entity import Run

from digitalhub_runtime_flower.entities.run.flower_server_deploy.spec import RunSpecFlowerServerDeploy
from digitalhub_runtime_flower.entities.run.flower_server_deploy.status import RunStatusFlowerServerDeploy


class RunFlowerServerDeploy(Run):
    """
    RunFlowerServerDeploy class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: RunSpecFlowerServerDeploy
        self.status: RunStatusFlowerServerDeploy
