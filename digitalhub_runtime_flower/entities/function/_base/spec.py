# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.function._base.spec import FunctionSpec


class FunctionSpecFlower(FunctionSpec):
    """Specification shared by Flower functions."""

    image: str | None = None
    base_image: str | None = None
    requirements: list[str] | str | None = None
