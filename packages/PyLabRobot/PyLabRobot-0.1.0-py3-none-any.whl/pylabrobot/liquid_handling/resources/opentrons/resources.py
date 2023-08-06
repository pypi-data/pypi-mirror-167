# get_load_params

from functools import partial

from pylabrobot.liquid_handling.resources import TipRack


class OpenTronResource:
  def __init__(self):
    pass

# class OpenTronTipRack(TipRack, OpenTronResource):
#   pass

def load_ot_tiprack(self, name: str, otname: str) -> TipRack:
  data = load_labware_thing(otname)
  tip_rack = TipRack(
    name=name,
    sites=TODO,
    volume=TODO,
  )
  return tip_rack

opentrons_96_tiprack_300ul = partial(load_ot_tiprack, otname="opentrons_96_tiprack_300ul")
