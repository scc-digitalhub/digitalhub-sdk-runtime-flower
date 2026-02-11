# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.entities.run._base.entity import Run

if typing.TYPE_CHECKING:
    pass

from digitalhub_runtime_flower.entities.run.flower_app_train.spec import RunSpecFlowerAppTrain
from digitalhub_runtime_flower.entities.run.flower_app_train.status import RunStatusFlowerAppTrain


class RunFlowerAppTrain(Run):
    """
    RunFlowerAppTrain class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: RunSpecFlowerAppTrain
        self.status: RunStatusFlowerAppTrain

    def local_execution(self) -> bool:
        """
        Check if run has local execution.

        Returns
        -------
        bool
            True if run has local execution, False otherwise.
        """
        return self.spec.local_execution
