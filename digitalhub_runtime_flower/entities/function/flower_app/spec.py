# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub_runtime_flower.entities.function._base.spec import FunctionSpecFlower
from digitalhub_runtime_flower.entities.function.flower_app.models import FABSource


class FunctionSpecFlowerApp(FunctionSpecFlower):
    """Specification for a Flower application function."""

    fab_source: FABSource | None = None
