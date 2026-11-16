# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.run._base.entity import LocalExecutionRunMixin, Run

from digitalhub_runtime_flower.entities.run.flower_app_train.spec import RunSpecFlowerAppTrain
from digitalhub_runtime_flower.entities.run.flower_app_train.status import RunStatusFlowerAppTrain


class RunFlowerAppTrain(LocalExecutionRunMixin, Run):
    """
    RunFlowerAppTrain class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: RunSpecFlowerAppTrain
        self.status: RunStatusFlowerAppTrain
