from dataclasses import dataclass

from magnumapi.geometry.definitions.RectangularBlockDefinition import RectangularBlockDefinition


@dataclass
class HomogenizedRectangularBlockDefinition(RectangularBlockDefinition):
    """Class for a homogenized rectangular block definition.

    Attributes:
       radius_0 (float):
       radius_1 (float):
       radius_2 (float):
       radius_3 (float):
       phi_0 (float):
       phi_1 (float):
       phi_2 (float):
       phi_3 (float):
    """
    radius_0: float
    radius_1: float
    radius_2: float
    radius_3: float
    phi_0: float
    phi_1: float
    phi_2: float
    phi_3: float
