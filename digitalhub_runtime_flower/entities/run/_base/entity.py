# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import BuildRunMixin, Run


class RunFlowerBuild(BuildRunMixin, Run):
    """
    Build run of the Flower server and client.
    """
