#!/usr/bin/env python
"""A lattice where at most 1 agent can occupy a cell.

"""

import uuid

from mesa import Agent

class Cell(Agent):
    """Anything that goes on a substrate follows this behaviour."""
    def __init__(self,
                 substrate,
                 energy: float, activated: bool):
        super().__init__(unique_id="cell_" + str(uuid.uuid4()), model=substrate)
        self.energy = energy
        self.activated = activated # TODO: not sure about this. We could do self.activated = self.energy > 0

