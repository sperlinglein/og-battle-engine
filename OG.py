from BattleEngine import UnitAttributes, UnitKind

SmallCargo = UnitKind(0)
LargeCargo = UnitKind(1)
LightFighter = UnitKind(2)
HeavyFighter = UnitKind(3)
Cruiser = UnitKind(4)
Battleship = UnitKind(5)
ColonyShip = UnitKind(6)
Recycler = UnitKind(7)
EspionageProbe = UnitKind(8)
Bomber = UnitKind(9)
SolarSatellite = UnitKind(10)
Destroyer = UnitKind(11)
DeathStar = UnitKind(12)
Battlecruiser = UnitKind(13)
RocketLauncher = UnitKind(14)
LightLaser = UnitKind(15)
HeavyLaser = UnitKind(16)
GaussCannon = UnitKind(17)
IonCannon = UnitKind(18)
PlasmaTurret = UnitKind(19)
SmallShieldDome = UnitKind(20)
LargeShieldDome = UnitKind(21)
Reaper = UnitKind(22)
Pathfinder = UnitKind(23)
Crawler = UnitKind(24)

names = {
    SmallCargo: 'small_cargo',
    LargeCargo: 'large_cargo',
    LightFighter: 'light_fighter',
    HeavyFighter: 'heavy_fighter',
    Cruiser: 'cruiser',
    Battleship: 'battleship',
    ColonyShip: 'colonyship',
    Recycler: 'recycler',
    EspionageProbe: 'espionage_probe',
    Bomber: 'bomber',
    SolarSatellite: 'solar_satellite',
    Destroyer: 'destroyer',
    DeathStar: 'death_star',
    Battlecruiser: 'battlecruiser',
    RocketLauncher: 'rocket_launcher',
    LightLaser: 'light_laser',
    HeavyLaser: 'heavy_laser',
    GaussCannon: 'gauss_cannon',
    IonCannon: 'ion_cannon',
    PlasmaTurret: 'plasma_turret',
    SmallShieldDome: 'small_shield_dome',
    LargeShieldDome: 'large_shield_dome',
    Reaper: 'reaper',
    Pathfinder: 'pathfinder',
    Crawler: 'crawler',
}

units_attributes = {
    SmallCargo: UnitAttributes(
        weapons=5.0,
        shield=10.0,
        armor=4000.0,
        rapid_fire={
            EspionageProbe: 5,
            SolarSatellite: 5,
            Crawler: 5,
        },
        metal=2000,
        crystal=2000
    ),
    LargeCargo: UnitAttributes(
        weapons=5.0,
        shield=25.0,
        armor=12000.0,
        rapid_fire={
            EspionageProbe: 5,
            SolarSatellite: 5,
            Crawler: 5,
        },
        metal=6000,
        crystal=6000
    ),
    LightFighter: UnitAttributes(
        weapons=50.0,
        shield=10.0,
        armor=4000.0,
        rapid_fire={
            EspionageProbe: 5,
            SolarSatellite: 5,
            Crawler: 5,
        },
        metal=3000,
        crystal=1000
    ),
    HeavyFighter: UnitAttributes(
        weapons=150.0,
        shield=25.0,
        armor=10000.0,
        rapid_fire={
            SmallCargo: 3,
            EspionageProbe: 5,
            SolarSatellite: 5,
            Crawler: 5,
        },
        metal=6000,
        crystal=4000
    ),
    Cruiser: UnitAttributes(
        weapons=400.0,
        shield=50.0,
        armor=27000.0,
        rapid_fire={
            LightFighter: 6,
            EspionageProbe: 5,
            SolarSatellite: 5,
            RocketLauncher: 10,
            Crawler: 5,
        },
        metal=20000,
        crystal=7000,
        deuterium=2000
    ),
    Battleship: UnitAttributes(
        weapons=1000.0,
        shield=200.0,
        armor=60000.0,
        rapid_fire={
            EspionageProbe: 5,
            SolarSatellite: 5,
            Crawler: 5,
        },
        metal=45000,
        crystal=15000
    ),
    ColonyShip: UnitAttributes(
        weapons=50.0,
        shield=100.0,
        armor=30000.0,
        rapid_fire={
            EspionageProbe: 5,
            SolarSatellite: 5,
            Crawler: 5,
        },
        metal=10000,
        crystal=20000,
        deuterium=10000
    ),
    Recycler: UnitAttributes(
        weapons=1.0,
        shield=10.0,
        armor=16000.0,
        rapid_fire={
            EspionageProbe: 5,
            SolarSatellite: 5,
            Crawler: 5,
        },
        metal=10000,
        crystal=6000,
        deuterium=2000
    ),
    EspionageProbe: UnitAttributes(
        weapons=0.01,
        shield=0.01,
        armor=1000.0,
        rapid_fire={},
        crystal=1000
    ),
    Bomber: UnitAttributes(
        weapons=1000.0,
        shield=500.0,
        armor=75000.0,
        rapid_fire={
            EspionageProbe: 5,
            SolarSatellite: 5,
            RocketLauncher: 20,
            LightLaser: 20,
            HeavyLaser: 10,
            GaussCannon: 5,
            IonCannon: 10,
            PlasmaTurret: 5,
            Crawler: 5,
        },
        metal=50000,
        crystal=25000,
        deuterium=15000
    ),
    SolarSatellite: UnitAttributes(
        weapons=1.0,
        shield=1.0,
        armor=2000.0,
        rapid_fire={},
        crystal=2000,
        deuterium=500
    ),
    Destroyer: UnitAttributes(
        weapons=2000.0,
        shield=500.0,
        armor=110000.0,
        rapid_fire={
            EspionageProbe: 5,
            SolarSatellite: 5,
            Battlecruiser: 2,
            LightLaser: 10,
            Crawler: 5,
        },
        metal=60000,
        crystal=50000,
        deuterium=15000
    ),
    DeathStar: UnitAttributes(
        weapons=200000.0,
        shield=50000.0,
        armor=9000000.0,
        rapid_fire={
            SmallCargo: 250,
            LargeCargo: 250,
            LightFighter: 200,
            HeavyFighter: 100,
            Cruiser: 33,
            Battleship: 30,
            ColonyShip: 250,
            Recycler: 250,
            EspionageProbe: 1250,
            Bomber: 25,
            Reaper: 10,
            Pathfinder: 30,
            Crawler: 250,
            SolarSatellite: 1250,
            Destroyer: 5,
            Battlecruiser: 15,
            RocketLauncher: 200,
            LightLaser: 200,
            HeavyLaser: 100,
            GaussCannon: 50,
            IonCannon: 100,
        },
        metal=5000000,
        crystal=4000000,
        deuterium=1000000
    ),
    Battlecruiser: UnitAttributes(
        weapons=700.0,
        shield=400.0,
        armor=70000.0,
        rapid_fire={
            SmallCargo: 3,
            LargeCargo: 3,
            HeavyFighter: 4,
            Cruiser: 4,
            Battleship: 7,
            EspionageProbe: 5,
            SolarSatellite: 5,
        },
        metal=30000,
        crystal=40000,
        deuterium=15000
    ),
    RocketLauncher: UnitAttributes(
        weapons=80.0,
        shield=10.0,
        armor=2000.0,
        rapid_fire={},
        metal=2000
    ),
    LightLaser: UnitAttributes(
        weapons=100.0,
        shield=25.0,
        armor=2000.0,
        rapid_fire={},
        metal=1500,
        crystal=500
    ),
    HeavyLaser: UnitAttributes(
        weapons=250.0,
        shield=100.0,
        armor=8000.0,
        rapid_fire={},
        metal=6000,
        crystal=2000
    ),
    GaussCannon: UnitAttributes(
        weapons=1100.0,
        shield=200.0,
        armor=35000.0,
        rapid_fire={},
        metal=20000,
        crystal=15000,
        deuterium=2000
    ),
    IonCannon: UnitAttributes(
        weapons=150.0,
        shield=500.0,
        armor=8000.0,
        rapid_fire={
            Reaper:2,
        },
        metal=5000,
        crystal=3000
    ),
    PlasmaTurret: UnitAttributes(
        weapons=3000.0,
        shield=300.0,
        armor=100000.0,
        rapid_fire={},
        metal=50000,
        crystal=50000,
        deuterium=3000
    ),
    SmallShieldDome: UnitAttributes(
        weapons=1.0,
        shield=2000.0,
        armor=20000.0,
        rapid_fire={},
        metal=10000,
        crystal=10000
    ),
    LargeShieldDome: UnitAttributes(
        weapons=1.0,
        shield=10000.0,
        armor=100000.0,
        rapid_fire={},
        metal=50000,
        crystal=50000
    ),
    Reaper: UnitAttributes(
        weapons=2800.0,
        shield=700.0,
        armor=140000.0,
        rapid_fire={
            EspionageProbe: 5,
            SolarSatellite: 5,
            Crawler: 5,
            Battleship: 7,
            Bomber: 4,
            Destroyer: 3,
        },
        metal=85000,
        crystal=55000,
        deuterium=20000
    ),
    Pathfinder: UnitAttributes(
        weapons=200.0,
        shield=100.0,
        armor=23000.0,
        rapid_fire={
            EspionageProbe: 5,
            SolarSatellite: 5,
            Crawler: 5,
            Cruiser: 3,
            LightFighter: 3,
            HeavyFighter: 2,
        },
        metal=8000,
        crystal=15000,
        deuterium=8000
    ),
    Crawler: UnitAttributes(
        weapons=1.0,
        shield=1.0,
        armor=4000.0,
        rapid_fire={},
        metal=2000,
        crystal=2000,
        deuterium=1000
    ),
}
