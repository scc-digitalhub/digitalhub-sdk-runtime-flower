# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub_runtime_flower.entities.run._base.spec import RunSpecFlowerRun


class RunSpecFlowerAppTrain(RunSpecFlowerRun):
    """Specification for a Flower application training run."""

    fab_source: dict | None = None
    parameters: dict | None = None
    federation: str | None = None
    superlink: str | None = None
    root_certificates: str | None = None
    local_execution: bool = False
