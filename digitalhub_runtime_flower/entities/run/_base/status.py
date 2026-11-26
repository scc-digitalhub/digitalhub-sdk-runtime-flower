# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import RunStatus


class RunStatusFlowerRun(RunStatus):
    """
    RunStatusFlowerRun status.
    """

    flwr_run_id: str | None = None


class RunStatusFlowerBuild(RunStatus):
    """Status shared by Flower build runs."""

    outputs: dict | None = None
