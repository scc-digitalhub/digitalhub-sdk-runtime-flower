# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.run._base.spec import RunSpecFunction


class RunSpecFlowerRun(RunSpecFunction):
    """Specification shared by Flower runs."""

    image: str | None = None
    base_image: str | None = None
    requirements: list[str] | None = None
