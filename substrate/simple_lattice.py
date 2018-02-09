#!/usr/bin/env python
"""A lattice where at most 1 agent can occupy a cell.

"""


import random

from mesa import Model
from mesa.datacollection import DataCollector
from mesa.space import SingleGrid
from mesa.time import RandomActivation

from agent.base import Cell

class SimpleLattice(Model):
    """A lattice where at most 1 agent can occupy a cell.."""

    def __init__(self,
                 width: int,
                 height: int,
                 goal_density: float):
        """

        Args:
            width: how many divisions on X
            height: how many divisions on Y
            goal_density: what is the density of cells we want (initially).
        """
        assert goal_density >= 0 and goal_density <= 1
        Model.__init__(self)
        self.height = height
        self.width = width
        self.energy = 0.0 # amount of food in environment. TODO: initialize this with a sensible value.
        self.schedule = RandomActivation(self)
        self.space = SingleGrid(width=self.width, height=self.height, torus=False)
        # data collector
        self.datacollector = DataCollector(
            model_reporters={
                "steps": lambda m: m.schedule.steps,
            },
            agent_reporters={
                "pos_x": lambda agent: agent.pos.x,
                "pos_y": lambda agent: agent.pos.y,
            }
        )
        #
        # Set up agents
        self.agents = [Cell(substrate=self, energy=random.random(), activated=random.random() <= goal_density)]
        # TODO: assign them to a particular (x,y) in lattice
        # put everyone on the scheduler:
        [self.schedule.add(agent) for agent in self.agents]
