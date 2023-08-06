import importlib
from typing import List, Union, Optional

from pylabrobot.liquid_handling.backends import LiquidHandlerBackend
from pylabrobot.liquid_handling.resources import (
  Coordinate,
  Plate,
  Resource,
  Lid,
  Tip,
)
from pylabrobot.liquid_handling.standard import (
  Aspiration,
  Dispense
)

try:
  import opentrons
  USE_OT = True
except:
  USE_OT = False


class OpenTronsBackend(LiquidHandlerBackend):
  """ Backends for the OpenTrons liquid handling robots """

  def __init__(self, left_head=None, right_head=None):
    super().__init__()

    self.left_head = left_head
    self.right_head = right_head

  def setup(self):
    if not USE_OT:
      raise RuntimeError("OpenTrons is not installed. Please run pip install opentrons")

    super().setup()

    execute = importlib.import_module("opentrons.execute")

    self.context: opentrons.protocol_api.ProtocolContext = execute.get_protocol_api(version=2)
    self.context.home() # api/src/execute.py L300

    # Load pipetting head. TODO: make this configurable
    p300 = self.protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tips])

    if False:
      tiprack = self.protocol.load_labware('corning_96_wellplate_360ul_flat', 2)
      plate = self.protocol.load_labware('opentrons_96_tiprack_300ul', 3)
      pipette = self.protocol.load_instrument('p300_single_gen2', mount='left')

  def stop(self):
    self.setup_finished = False

  def __enter__(self):
    self.setup()
    return self

  def __exit__(self, *exc):
    self.stop()
    return False

  def pickup_tips(self, *channels: List[Optional[Tip]], **backend_kwargs):
    """ Pick up tips from the specified resource. """

    self.pipette.pick_up_tip(tiprack['A1'])

  def discard_tips(self, *channels: List[Optional[Tip]], **backend_kwars):
    """ Discard tips from the specified resource. """
    pass

  def aspirate(self, *channels: Optional[Aspiration], **backend_kwargs):
    """ Aspirate liquid from the specified resource using pip. """
    pass

  def dispense(self, *channels: Optional[Dispense], **backend_kwargs):
    """ Dispense liquid from the specified resource using pip. """
    pass

  def pickup_tips96(self, resource: Resource, **backend_kwargs):
    """ Pick up tips from the specified resource using CoRe 96. """
    pass

  def discard_tips96(self, resource: Resource, **backend_kwargs):
    """ Discard tips to the specified resource using CoRe 96. """
    pass

  def aspirate96(
    self,
    resource: Resource,
    pattern: List[List[bool]],
    volume: float,
    **backend_kwargs
  ):
    """ Aspirate liquid from the specified resource using CoRe 96. """
    pass

  def dispense96(
    self,
    resource: Resource,
    pattern: List[List[bool]],
    volume: float,
    **backend_kwargs
  ):
    """ Dispense liquid to the specified resource using CoRe 96. """
    pass

  def move_plate(self, plate: Plate, to: Union[Resource, Coordinate], **backend_kwargs):
    """ Move the specified plate within the robot. """
    pass

  def move_lid(self, lid: Lid, to: Union[Resource, Coordinate], **backend_kwargs):
    """ Move the specified lid within the robot. """
    pass
