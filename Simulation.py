#
# Composing an attack fleet to win against the defender
#

import OG
from BattleEngine import BattleEngine, Combatant, UnitKind

#
# Config
#
class Config:
    simulations: int
    seed: int
    msu_fleet_ratio_from: float
    msu_fleet_ratio_to: float
    is_combined_defender_fleet_and_defense: bool

    def __init__(self, simulations: int = 10, seed: int = 1,
                 fleet_ratio_from: float = 5.0, fleet_ratio_to: float = 7.0,
                 combine_defender_fleet_and_defense: bool = False) -> None:
        self.simulations = simulations
        self.seed = seed
        self.msu_fleet_ratio_from = fleet_ratio_from
        self.msu_fleet_ratio_to = fleet_ratio_to
        self.is_combined_defender_fleet_and_defense = combine_defender_fleet_and_defense

class MSU:
    # resources
    metal: float
    crystal: float
    deuterium: float
    # fleet and defense
    attacker_fleet: float
    defender_fleet: float
    defender_defense: float
    defender_combined: float
    attacker: dict
    defender: dict

    def __init__(self, metal: float = 3.0, crystal: float = 2.0, deuterium: float = 1.0) -> None:
        self.metal = metal / metal
        self.crystal = metal / crystal
        self.deuterium = metal / deuterium
        self.attacker_fleet = 0.0
        self.defender_fleet = 0.0
        self.defender_defense = 0.0
        self.defender_combined = 0.0
        self.attacker = dict( total = 0 )
        self.defender = dict( total = 0, total_fleet = 0, total_defense = 0 )
        pass

    def _calc_msu(self, unit: UnitKind, count: int):
        msu = OG.units_attributes[unit].metal * self.metal * count 
        + OG.units_attributes[unit].crystal * self.crystal * count 
        + OG.units_attributes[unit].deuterium * self.deuterium * count
        
        return msu

    def calc_msu_attacker(self, attacker: Combatant):
        for kind, count in attacker.unit_groups.items():
            msu = self._calc_msu(kind, count)
            self.attacker[kind] = msu
            self.attacker['total'] = self.attacker['total'] + msu
        pass

    def calc_msu_defender(self, defender: Combatant):
        for kind, count in defender.unit_groups.items():
            msu = self._calc_msu(kind, count)
            self.defender[kind] = msu
            self.defender['total'] = self.defender['total'] + msu
        pass

    def _calc_msu_defender_fleet(self):
        pass

    def _calc_msu_defender_defense(self):
        pass

    def _calc_msu_defender_combined(self):
        self.defender_combined = self.defender_fleet + self.defender_defense
        pass

#
# attacker and defender config
#
attackers = [
    Combatant(
        weapons_technology=10,
        shielding_technology=10,
        armor_technology=10,
        unit_groups={
            OG.LightFighter: 1000
        }
    )
]

defenders = [
    Combatant(
        weapons_technology=10,
        shielding_technology=10,
        armor_technology=10,
        unit_groups={
            OG.LightFighter: 100,
            OG.HeavyFighter: 100
        }
    )
]

#
# Simulation
#
def calc_msu():
    return 0

def calc_msu_fleet():
    return 0

def calc_msu_def():
    return 0

simulation = dict(
    duration = 0,
    simulations = 0,
    rounds = 0
)

attacker_units = dict()
defender_units = dict()

units = dict()
units['small_cargo'] = {
    "before": 0,
    "after": 0,
    "lost": 0
}

combatant = dict()
combatant['id'] = 0
combatant['type'] = ""
combatant['technologies'] = {}
combatant['units'] = []

technologies = dict()
technologies['weapons'] = 0
technologies['shielding'] = 0
technologies['armor'] = 0