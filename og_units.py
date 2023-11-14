import OG
class KTransporter():
    def __init__(self, num):
        self.name = OG.SmallCargo
        self.num = num
        self.met = 2000
        self.kris = 2000
        self.deut = 0
        self.lad = 5000
        self.fuel = 9
        self.speed = 10000

class GTransporter():
    def __init__(self, num):
        self.name = OG.LargeCargo
        self.num = num
        self.met = 6000
        self.kris = 6000
        self.deut = 0
        self.lad = 2500
        self.fuel = 24
        self.speed = 7500

class LJaeger():
    def __init__(self, num):
        self.name = OG.LightFighter
        self.num = num
        self.met = 3000
        self.kris = 1000
        self.deut = 0
        self.lad = 50
        self.fuel = 9
        self.speed = 12500

class SJaeger():
    def __init__(self, num):
        self.name = OG.HeavyFighter
        self.num = num
        self.met = 6000
        self.kris = 4000
        self.deut = 0
        self.lad = 100
        self.fuel = 36
        self.speed = 10000

class SpioSonde():
    def __init__(self, num):
        self.name = OG.EspionageProbe
        self.num = num
        self.met = 0
        self.kris = 1000
        self.deut = 0
        self.lad = 0
        self.fuel = 1
        self.speed = 100000000

class Kolonieschiff():
    def __init__(self, num):
        self.name = OG.ColonyShip
        self.num = num
        self.met = 10000
        self.kris = 20000
        self.deut = 10000
        self.lad = 7500
        self.fuel = 499
        self.speed = 2500

class Recyler():
    def __init__(self, num):
        self.name = OG.Recycler
        self.num = num
        self.met = num * 10000
        self.kris = 6000
        self.deut = 2000
        self.lad = 100
        self.fuel = 149
        self.speed = 2000
class Kreuzer():
    def __init__(self, num):
        self.name = OG.Cruiser
        self.num = num
        self.met = 20000
        self.kris = 7000
        self.deut = 2000
        self.lad = 800
        self.fuel = 149
        self.speed = 15000

class Schlachtschiff():
    def __init__(self, num):
        self.name = OG.Battleship
        self.num = num
        self.met = 45000
        self.kris = 1500
        self.deut = 0
        self.lad = 1500
        self.fuel = 249
        self.speed = 10000


class Bomber():
    def __init__(self, num):
        self.name = OG.Bomber
        self.num = num
        self.met = 50000
        self.kris = 25000
        self.deut = 15000
        self.lad = 500
        self.fuel = 349
        self.speed = 5000

class Zerstoerer():
    def __init__(self, num):
        self.name = OG.Destroyer
        self.num = num
        self.met = 60000
        self.kris = 50000
        self.deut = 15000
        self.lad = 2000
        self.fuel = 499
        self.speed = 5000

class Todesstern():
    def __init__(self, num):
        self.name = OG.DeathStar
        self.num = num
        self.met = 5000000
        self.kris = 4000000
        self.deut = 1000000
        self.lad = 1000000
        self.fuel = 1
        self.speed = 100

class Schlachtkreuzer():
    def __init__(self, num):
        self.name =OG.Battlecruiser
        self.num = num
        self.met =  30000
        self.kris = 40000
        self.deut = 15000
        self.lad = 750
        self.fuel = 124
        self.speed = 10000

class Reaper():
    def __init__(self, num):
        self.name = OG.Reaper
        self.num = num
        self.met = 85000
        self.kris = 55000
        self.deut = 20000
        self.lad = 10000
        self.fuel = 549
        self.speed = 7000

class Pathfinder():
    def __init__(self, num):
        self.name = OG.Pathfinder
        self.num = num
        self.met = 8000
        self.kris = 15000
        self.deut = 800
        self.lad = 10000
        self.fuel = 149
        self.speed = 12000

class Crawler():
    def __init__(self, num):
        self.name = OG.Crawler
        self.num = num
        self.met = 2000
        self.kris = 2000
        self.deut =1000
        self.lad = 0
        self.fuel = 0
        self.speed = 1

class SolorSat():
    def __init__(self, num):
        self.name = OG.SolarSatellite
        self.num = num
        self.met = 0
        self.kris = 2000
        self.deut = 500
        self.lad = 0
        self.fuel = 0
        self.speed = 1

class Raketwerfer():
    def __init__(self, num):
        self.name = OG.RocketLauncher
        self.num = num
        self.met = 0
        self.kris = 0
        self.deut = 0
        self.lad = 0
        self.fuel = 0
        self.speed = 1

class LLaser():
    def __init__(self, num):
        self.name = OG.LightLaser
        self.num = num
        self.met = 0
        self.kris = 0
        self.deut = 0
        self.lad = 0
        self.fuel = 0
        self.speed = 1

class SLaser():
    def __init__(self, num):
        self.name = OG.HeavyLaser
        self.num = num
        self.met = 0
        self.kris = 0
        self.deut = 0
        self.lad = 0
        self.fuel = 0
        self.speed = 1

class Gausskanone():
    def __init__(self, num):
        self.name = OG.GaussCannon#
        self.num = num
        self.met = 0
        self.kris = 0
        self.deut =0
        self.lad = 0
        self.fuel = 0
        self.speed = 1

class Ionenkanone():
    def __init__(self, num):
        self.name = OG.IonCannon
        self.num = num
        self.met = 0
        self.kris = 0
        self.deut = 0
        self.lad = 0
        self.fuel = 0
        self.speed = 1

class Plasmawerfer():
    def __init__(self, num):
        self.name = OG.PlasmaTurret
        self.num = num
        self.met = 0
        self.kris = 0
        self.deut = 0
        self.lad = 0
        self.fuel = 0
        self.speed = 1

class KSchildkuppel():
    def __init__(self, num):
        self.name = OG.SmallShieldDome
        self.num = num
        self.met = 0
        self.kris = 0
        self.deut = 0
        self.lad = 0
        self.fuel = 0
        self.speed = 1

class GSchildkuppel():
    def __init__(self, num):
        self.name = OG.LargeShieldDome
        self.num = num
        self.met = 0
        self.kris = 0
        self.deut = 0
        self.lad = 0
        self.fuel = 0
        self.speed = 1
