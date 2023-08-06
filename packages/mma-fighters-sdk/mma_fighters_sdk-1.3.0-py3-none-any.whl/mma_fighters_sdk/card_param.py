from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Technique:
    level: int
    name: str
    power: float
    max_number_randomize: int


@dataclass
class CardParam:
    name: str
    level: int
    power: float
    health: float
    techniques: Optional[list[Technique]] = field(init=False, default_factory=list)

    max_percent_randomize: int  # Max 25 percent of calculate increase or decrease of power
    max_percent_block: int  # Max 25
    max_percent_miss: int  # Max 25
    max_percent_double_power: int  # Max 35
