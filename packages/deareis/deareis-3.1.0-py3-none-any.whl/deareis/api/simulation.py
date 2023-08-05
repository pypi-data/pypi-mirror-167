# DearEIS is licensed under the GPLv3 or later (https://www.gnu.org/licenses/gpl-3.0.html).
# Copyright 2022 DearEIS developers
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# The licenses of DearEIS' dependencies and/or sources of portions of code are included in
# the LICENSES folder.


from time import time as _time
from uuid import uuid4 as _uuid4
import pyimpspec as _pyimpspec
from deareis.data import (
    SimulationResult,
    SimulationSettings,
)


def simulate_spectrum(
    settings: SimulationSettings,
) -> SimulationResult:
    """
    Wrapper for the `pyimpspec.simulate_spectrum` function.

    Simulate the impedance spectrum generated by a circuit in a certain frequency range.

    Parameters
    ----------
    settings: SimulationSettings
        The settings to use when performing the simulation.

    Returns
    -------
    SimulationResult
    """
    assert type(settings) is SimulationSettings, settings
    circuit: _pyimpspec.Circuit = _pyimpspec.parse_cdc(settings.cdc)
    _pyimpspec.analysis.fitting.validate_circuit(circuit)
    return SimulationResult(
        _uuid4().hex,
        _time(),
        circuit,
        settings,
    )
