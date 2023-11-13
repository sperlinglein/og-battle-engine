#test
from PyQt5 import QtWidgets, uic, QtCore
import OG, sys, og_units
from BattleEngine import BattleEngine, Combatant
import scipy, _thread, time
from numpy import arange

form_class = uic.loadUiType("battleSim.ui")[0]

class wrapOutCome():
    def __init__(self, outcome):
        for kind, stats in outcome[0].round_stats(-1).items():
            match kind:
                case 0:
                    self.kt = og_units.KTransporter(stats.num_remaining_units)
                case 1:
                    self.gt = og_units.GTransporter(stats.num_remaining_units)
                case 2:
                    self.lj = og_units.LJaeger(stats.num_remaining_units)
                case 3:
                    self.sj = og_units.SJaeger(stats.num_remaining_units)
                case 4:
                    self.k = og_units.Kreuzer(stats.num_remaining_units)
                case 5:
                    self.ss = og_units.Schlachtschiff(stats.num_remaining_units)
                case 6:
                    self.kolo = og_units.Kolonieschiff(stats.num_remaining_units)
                case 7:
                    self.recs = og_units.Recyler(stats.num_remaining_units)
                case 8:
                    self.spio = og_units.SpioSonde(stats.num_remaining_units)
                case 9:
                    self.bb = og_units.Bomber(stats.num_remaining_units)
                case 10:
                    self.sat = og_units.SolorSat(stats.num_remaining_units)
                case 11:
                    self.zr = og_units.Zerstoerer(stats.num_remaining_units)
                case 12:
                    self.ts = og_units.Todesstern(stats.num_remaining_units)
                case 13:
                    self.sx = og_units.Schlachtkreuzer(stats.num_remaining_units)
                case 14:
                    self.raks = og_units.Raketwerfer(stats.num_remaining_units)
                case 15:
                    self.ll = og_units.LLaser(stats.num_remaining_units)
                case 16:
                    self.sl = og_units.SLaser(stats.num_remaining_units)
                case 17:
                    self.gk = og_units.Gausskanone(stats.num_remaining_units)
                case 18:
                    self.ik = og_units.Ionenkanone(stats.num_remaining_units)
                case 19:
                    self.pw = og_units.Plasmawerfer(stats.num_remaining_units)
                case 20:
                    self.ks = og_units.KSchildkuppel(stats.num_remaining_units)
                case 21:
                    self.gs = og_units.GSchildkuppel(stats.num_remaining_units)
                case 22:
                    self.rp = og_units.Reaper(stats.num_remaining_units)
                case 23:
                    self.pa = og_units.Pathfinder(stats.num_remaining_units)
                case 24:
                    self.cr = og_units.Crawler(stats.num_remaining_units)

class BattleMainWindow(QtWidgets.QMainWindow, form_class):


    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.startBattelBut.clicked.connect(self.startBattle)
        self.startOptimzeBut.clicked.connect(self.optimizeAttack)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.__myUpdate)
        self.timer.start(200) #Optimizer caan lead to big Lags in GUI -> force Repaint all 0.2s -> 5fps


    def loadData(self):
        # load Attacker
        attackers = [
            Combatant(
                weapons_technology=int(self.waffen_A1.text()),
                shielding_technology=int(self.schilde_A1.text()),
                armor_technology=int(self.panzer_A1.text()),
                unit_groups={
                    OG.SmallCargo: int(self.kt_A1.text()),
                    OG.LargeCargo: int(self.gt_A1.text()),
                    OG.LightFighter: int(self.lj_A1.text()),
                    OG.HeavyFighter: int(self.sj_A1.text()),
                    OG.Cruiser: int(self.k_A1.text()),
                    OG.Battleship: int(self.ss_A1.text()),
                    OG.ColonyShip: int(self.kolo_A1.text()),
                    OG.Recycler: int(self.recs_A1.text()),
                    OG.EspionageProbe: int(self.spio_A1.text()),
                    OG.Bomber: int(self.bb_A1.text()),
                    OG.Destroyer: int(self.zr_A1.text()),
                    OG.DeathStar: int(self.ts_A1.text()),
                    OG.Battlecruiser: int(self.sx_A1.text()),
                    OG.Reaper: int(self.rp_A1.text()),
                    OG.Pathfinder: int(self.pa_A1.text()),
                },
            ),
        ]
        # load Defender
        defenders = [
            Combatant(
                weapons_technology=int(self.waffen_D1.text()),
                shielding_technology=int(self.schilde_D1.text()),
                armor_technology=int(self.panzer_D1.text()),
                unit_groups={
                    OG.SmallCargo: int(self.kt_D1.text()),
                    OG.LargeCargo: int(self.gt_D1.text()),
                    OG.LightFighter: int(self.lj_D1.text()),
                    OG.HeavyFighter: int(self.sj_D1.text()),
                    OG.Cruiser: int(self.k_D1.text()),
                    OG.Battleship: int(self.ss_D1.text()),
                    OG.ColonyShip: int(self.kolo_D1.text()),
                    OG.Recycler: int(self.recs_D1.text()),
                    OG.EspionageProbe: int(self.spio_D1.text()),
                    OG.Bomber: int(self.bb_D1.text()),
                    OG.Destroyer: int(self.zr_D1.text()),
                    OG.DeathStar: int(self.ts_D1.text()),
                    OG.Battlecruiser: int(self.sx_D1.text()),
                    OG.Reaper: int(self.rp_D1.text()),
                    OG.Pathfinder: int(self.pa_D1.text()),
                    OG.Crawler: int(self.cr_D1.text()),
                    OG.SolarSatellite: int(self.sat_D1.text()),
                    OG.RocketLauncher: int(self.raks_D1.text()),
                    OG.LightLaser: int(self.ll_D1.text()),
                    OG.HeavyLaser: int(self.sl_D1.text()),
                    OG.GaussCannon: int(self.gk_D1.text()),
                    OG.IonCannon: int(self.ik_D1.text()),
                    OG.PlasmaTurret: int(self.pw_D1.text()),
                    OG.SmallShieldDome: int(self.ks_D1.isChecked()),
                    OG.LargeShieldDome: int(self.gs_D1.isChecked()),
                },
            ),
        ]
        return attackers, defenders
    def calcBattle(self, attacker, defender):
        # init Battle Engine
        engine = BattleEngine('BattleEngine-win.exe', OG.units_attributes)
        num_rounds = []
        attackers_outcomes = []
        defenders_outcomes = []

        # calc Battla 100 times
        for i in range(10):
            outcome = engine.simulate(attacker, defender)[0]
            num_rounds.append(outcome.num_rounds)
            attackers_outcomes.append(wrapOutCome(outcome.attackers_outcomes))
            defenders_outcomes.append(wrapOutCome(outcome.defenders_outcomes))

        return num_rounds, attackers_outcomes,defenders_outcomes
    def analyzBattele(self, attacker, defender, attacker_outcomes, defender_outcomes):
        # Analyses
        vMetA = 0
        vKrisA = 0
        vDeutA = 0

        vMetD = 0
        vKrisD = 0
        vDeutD = 0

        remainA = 0
        remainD = 0

        for i in attacker_outcomes[-1].__dict__.keys():
            bufA = 0
            bufD = 0
            for j in range(10):
               bufA = bufA + getattr(attacker_outcomes[j], i).num
               bufD = bufD + getattr(defender_outcomes[j], i).num

            bufA = bufA / 10
            remainA = remainA + bufA
            try:
                getattr(self, i + "_res_A1").display(bufA)
                vMetA = vMetA + (attacker[0].unit_groups[getattr(attacker_outcomes[-1], i).name] - bufA) * getattr(attacker_outcomes[-1], i).met
                vKrisA = vKrisA + (attacker[0].unit_groups[getattr(attacker_outcomes[-1], i).name] - bufA) * getattr(attacker_outcomes[-1], i).kris
                vDeutA = vDeutA + (attacker[0].unit_groups[getattr(attacker_outcomes[-1], i).name] - bufA) * getattr(attacker_outcomes[-1], i).deut
            except:
                pass
            bufD = bufD / 10
            remainD = remainD + bufD
            try:
                getattr(self, i + "_res_D1").display(bufD)
                vMetD = vMetD + (defender[0].unit_groups[getattr(defender_outcomes[-1], i).name] - bufD) * getattr(defender_outcomes[-1], i).met
                vKrisD = vKrisD + (defender[0].unit_groups[getattr(defender_outcomes[-1], i).name] - bufD) * getattr(defender_outcomes[-1], i).kris
                vDeutD = vDeutD + (defender[0].unit_groups[getattr(defender_outcomes[-1], i).name] - bufD) * getattr(defender_outcomes[-1], i).deut
            except:
                pass
        return vMetA, vKrisA, vDeutA, vMetD, vKrisD, vDeutD, remainA, remainD
    def showLosses(self, vMetA, vKrisA, vDeutA, vMetD, vKrisD, vDeutD, fuel):
        self.tfMet.display(int((vMetA+vMetD)*0.7))
        self.tfKris.display(int((vKrisA + vKrisD) * 0.7))
        self.tfDeut.display(int((vDeutA + vDeutD) * 0.7))
        self.vMetA_res.display(int(vMetA))
        self.vKrisA_res.display(int(vKrisA))
        self.vDeutA_res.display(int(vDeutA))
        self.vMetD_res.display(int(vMetD))
        self.vKrisD_res.display(int(vKrisD))
        self.vDeutD_res.display(int(vDeutD))

        mseA = vMetA + (vKrisA * float(self.mseMet.text()) / float(self.mseKris.text()) ) + (vDeutA + fuel) * float(self.mseMet.text()) / float(self.mseDeut.text())
        self.mseA_res.display(int(mseA))
    def calcFuel(self, attacker):
        minSpeed = 9999999

        if int(self.gala_A1.text()) != int(self.gala_D1.text()):
            entf = abs(int(self.gala_A1.text())-int(self.gala_D1.text()))*20000
        elif int(self.system_A1.text()) != int(self.system_D1.text()):
            entf = abs(int(self.system_A1.text())-int(self.system_D1.text()))*95 + 2700
        else:
            entf = abs(int(self.platz_A1.text())-int(self.platz_D1.text()))*5 + 1000

        verbrenn = 1 + float(self.verbrenn_A1.text()) * 0.1
        impuls = 1 + float(self.verbrenn_A1.text()) * 0.2
        hyper = 1 + float(self.hyper_A1.text()) * 0.3
        speedSlow = 0

        kt = attacker[0].unit_groups[OG.SmallCargo]
        gt = attacker[0].unit_groups[OG.LargeCargo]
        lj = attacker[0].unit_groups[OG.LightFighter]
        sj = attacker[0].unit_groups[OG.HeavyFighter]
        k = attacker[0].unit_groups[OG.Cruiser]
        ss = attacker[0].unit_groups[OG.Battleship]
        kolo = attacker[0].unit_groups[OG.ColonyShip]
        recs = attacker[0].unit_groups[OG.Recycler]
        spio = attacker[0].unit_groups[OG.EspionageProbe]
        bb = attacker[0].unit_groups[OG.Bomber]
        zer = attacker[0].unit_groups[OG.Destroyer]
        ts = attacker[0].unit_groups[OG.DeathStar]
        sx = attacker[0].unit_groups[OG.Battlecruiser]
        rp = attacker[0].unit_groups[OG.Reaper]
        pa = attacker[0].unit_groups[OG.Pathfinder]



        if kt > 0 and og_units.KTransporter(0).speed < minSpeed:
            minSpeed = og_units.KTransporter(0).speed
        if gt > 0 and og_units.GTransporter(0).speed < minSpeed:
            minSpeed = og_units.GTransporter(0).speed
        if lj > 0 and og_units.LJaeger(0).speed  < minSpeed:
            minSpeed = og_units.LJaeger(0).speed
        if sj > 0 and og_units.SJaeger(0).speed  < minSpeed:
            minSpeed = og_units.SJaeger(0).speed
        if k > 0 and og_units.Kreuzer(0).speed  < minSpeed:
            minSpeed = og_units.Kreuzer(0).speed
        if ss > 0 and og_units.Schlachtschiff(0).speed  < minSpeed:
            minSpeed = og_units.Schlachtschiff(0).speed
        if kolo > 0 and og_units.Kolonieschiff(0).speed  < minSpeed:
            minSpeed = og_units.Recyler(0).speed
        if recs > 0 and og_units.Recyler(0).speed  < minSpeed:
            minSpeed = og_units.Recyler(0).speed
        if spio > 0 and og_units.SpioSonde(0).speed < minSpeed:
            minSpeed = og_units.SpioSonde(0).speed
        if bb > 0 and og_units.Bomber(0).speed < minSpeed:
            minSpeed = og_units.Bomber(0).speed
        if zer > 0 and og_units.Zerstoerer(0).speed  < minSpeed:
            minSpeed = og_units.Zerstoerer(0).speed
        if ts > 0 and og_units.Todesstern(0).speed  < minSpeed:
            minSpeed = og_units.Todesstern(0).speed
        if sx > 0 and og_units.Schlachtkreuzer(0).speed  < minSpeed:
            minSpeed = og_units.Schlachtkreuzer(0).speed
        if rp > 0 and og_units.Reaper(0).speed < minSpeed:
            minSpeed = og_units.Reaper(0).speed
        if pa > 0 and og_units.Pathfinder(0).speed < minSpeed:
            minSpeed = og_units.Pathfinder(0).speed


        fuel = 0
        if kt > 0 :
            fuel = fuel + (kt * og_units.KTransporter(0).fuel * entf / 35000 * (((minSpeed / og_units.KTransporter(0).speed) ** 0.5) +1)**2)
        if gt > 0 :
            fuel = fuel + (gt * og_units.GTransporter(0).fuel * entf / 35000 * (((minSpeed / og_units.GTransporter(0).speed) ** 0.5)+1)**2)
        if lj > 0 :
            fuel = fuel + (lj * og_units.LJaeger(0).fuel * entf/ 35000 * (((minSpeed / og_units.LJaeger(0).speed) ** 0.5)+1)**2)
        if sj > 0 :
            fuel = fuel + (sj * og_units.SJaeger(0).fuel * entf / 35000 * (((minSpeed / og_units.SJaeger(0).speed) ** 0.5) + 1) ** 2)
        if k > 0 :
            fuel = fuel + (k * og_units.Kreuzer(0).fuel * entf / 35000 * (((minSpeed / og_units.Kreuzer(0).speed ) ** 0.5) + 1) ** 2)
        if ss > 0:
            fuel = fuel + (ss * og_units.Schlachtschiff(0).fuel * entf / 35000 * (((minSpeed / og_units.Schlachtschiff(0).speed ) ** 0.5) + 1) ** 2)
        if kolo > 0:
            fuel = fuel + (kolo * og_units.Kolonieschiff(0).fuel * entf / 35000 * (((minSpeed / og_units.Kolonieschiff(0).speed ) ** 0.5) + 1) ** 2)
        if recs > 0:
            fuel = fuel + (recs * og_units.Recyler(0).fuel * entf / 35000 * (((minSpeed / og_units.Recyler(0).speed ) ** 0.5) + 1) ** 2)
        if spio > 0:
            fuel = fuel + (spio * og_units.SpioSonde(0).fuel * entf / 35000 * (((minSpeed / og_units.SpioSonde(0).speed ) ** 0.5) + 1) ** 2)
        if bb > 0:
            fuel = fuel + (bb * og_units.Bomber(0).fuel * entf / 35000 * (((minSpeed / og_units.Bomber(0).speed ) ** 0.5) + 1) ** 2)
        if zer > 0:
            fuel = fuel + (zer * og_units.Zerstoerer(0).fuel * entf / 35000 * (((minSpeed / og_units.Zerstoerer(0).speed) ** 0.5) + 1) ** 2)
        if ts > 0:
            fuel = fuel + (ts * og_units.Todesstern(0).fuel * entf / 35000 * (((minSpeed / og_units.Todesstern(0).speed ) ** 0.5) + 1) ** 2)
        if sx > 0:
            fuel = fuel + (sx * og_units.Schlachtkreuzer(0).fuel * entf / 35000 * (((minSpeed / og_units.Schlachtkreuzer(0).speed ) ** 0.5) + 1) ** 2)
        if rp > 0:
            fuel = fuel + (rp * og_units.Reaper(0).fuel * entf / 35000 * (((minSpeed / og_units.Reaper(0).speed) ** 0.5) + 1) ** 2)
        if pa > 0:
            fuel = fuel + (pa * og_units.Pathfinder(0).fuel * entf / 35000 * (((minSpeed / og_units.Pathfinder(0).speed ) ** 0.5) + 1) ** 2)

        self.verbrauch_A1.display(int(fuel))
        return fuel
    def startBattle(self):
        attacker, defender = self.loadData()
        rounds, attacker_out, defender_out = self.calcBattle(attacker, defender)
        vMetA, vKrisA, vDeutA, vMetD, vKrisD, vDeutD, remainA, remainD = self.analyzBattele(attacker, defender, attacker_out, defender_out)
        fuel = self.calcFuel(attacker)
        self.showLosses(vMetA, vKrisA, vDeutA, vMetD, vKrisD, vDeutD,fuel)

    def optimizerStart(self,a):
        # Check best fit Standard fleets
        # x0 = [KT:0, GT:1, LJ:2, SJ:3, K:4, SS:5, KO:6, Rc:7, Sp:8, BB:9, ZR:10, TS:11, SX:12, RP:13, Pa:14]
        xB = [0, 0, 10, 10, 10, 10, 0, 0, 0, 10, 10, 0, 10, 10, 0]  # alle Kampsschife base 10 Stueck
        self.initRes = []
        self.running = []
        count = 0

        for lj in arange(0.001, 1.0, 0.4):
            xB[2] = int(lj * self.bounds[2][1])
            for k in arange(0.001, 1.0, 0.4):
                xB[4] = int(k * self.bounds[2][1])
                self.running.append(True)
                _thread.start_new_thread(self.optimizerInitWorker, (xB.copy(), self.defenderOpt, count))
                time.sleep(1)
                count = count + 1

        self.optimizerWaiInit()
    def optimizerInitWorker(self, x, defender, count):
        #print("worker",count, "mit",x)
        for ss in arange(0.001, 1.0, 0.4):
            x[5] = int(ss * self.bounds[5][1])
            for bb in arange(0.001, 1.0, 0.4):
                x[9] = int(bb * self.bounds[9][1])
                for zr in arange(0.001, 1.0, 0.4):
                    x[10] = int(zr * self.bounds[10][1])
                    for sx in arange(0.001, 1.0, 0.4):
                        x[12] = int(sx * self.bounds[12][1])
                        for rp in arange(0.001, 1, 0.4):
                            x[13] = int(rp * self.bounds[13][1])
                            buf = self.optimzeWorker(x, defender)
                            self.initRes.append([buf, x.copy()])
                            #print(self.initRes[-1])
            #print("Bomber ", xB[2], xB[4], xB[5], xB[9], xB[10], xB[12], xB[13])
        self.running[count] = False
        #print("Worker",count, "done")

    def optimizerWaiInit(self):
        while (True in self.running):
            time.sleep(1)

        sortRes = sorted(self.initRes, key=lambda x: x[0])
        #print("Init Best fleet ", sortRes[0])
        #print("Init worst fleet ", sortRes[-1])
        res = scipy.optimize.minimize(self.optimzeWorker, sortRes[0][1], args=self.defenderOpt, bounds=self.bounds,
                                      method='Nelder-Mead')
        #print(res.message)
        #print(res.fun)
        #print(res.x)

        self.kt_A1.setText(str(int(res.x[0])))
        self.gt_A1.setText(str(int(res.x[1])))
        self.lj_A1.setText(str(int(res.x[2])))
        self.sj_A1.setText(str(int(res.x[3])))
        self.k_A1.setText(str(int(res.x[4])))
        self.ss_A1.setText(str(int(res.x[5])))
        self.kolo_A1.setText(str(int(res.x[6])))
        self.recs_A1.setText(str(int(res.x[7])))
        self.spio_A1.setText(str(int(res.x[8])))
        self.bb_A1.setText(str(int(res.x[9])))
        self.zr_A1.setText(str(int(res.x[10])))
        self.ts_A1.setText(str(int(res.x[11])))
        self.sx_A1.setText(str(int(res.x[12])))
        self.rp_A1.setText(str(int(res.x[13])))
        self.pa_A1.setText(str(int(res.x[14])))
        self.startBattle()
        self.activateWindow()

        self.timer.stop()


    def optimzeWorker(self, attackerOpt, defender):
        #adjust attacker
        attackers = [
            Combatant(
                weapons_technology=int(self.waffen_A1.text()),
                shielding_technology=int(self.schilde_A1.text()),
                armor_technology=int(self.panzer_A1.text()),
                unit_groups={
                    OG.SmallCargo: int(attackerOpt[0]),
                    OG.LargeCargo: int(attackerOpt[1]),
                    OG.LightFighter: int(attackerOpt[2]),
                    OG.HeavyFighter: int(attackerOpt[3]),
                    OG.Cruiser: int(attackerOpt[4]),
                    OG.Battleship: int(attackerOpt[5]),
                    OG.ColonyShip: int(attackerOpt[6]),
                    OG.Recycler: int(attackerOpt[7]),
                    OG.EspionageProbe: int(attackerOpt[8]),
                    OG.Bomber: int(attackerOpt[9]),
                    OG.Destroyer: int(attackerOpt[10]),
                    OG.DeathStar: int(attackerOpt[11]),
                    OG.Battlecruiser: int(attackerOpt[12]),
                    OG.Reaper: int(attackerOpt[13]),
                    OG.Pathfinder: int(attackerOpt[14]),
                },
            ),
        ]
        rounds, attacker_out, defender_out = self.calcBattle(attackers,defender )
        vMetA, vKrisA, vDeutA, vMetD, vKrisD, vDeutD, remainA, remainD = self.analyzBattele(attackers, defender,attacker_out,defender_out)
        if remainD > 0:
            # print("punish")
            return 10e14

        else:
            #Metallkosten + (X / Y) * Kristallkosten + (X / Z) * Deuteriumkosten
            fuel = self.calcFuel(attackers)
            difM = vMetA
            difK = vKrisA * float(self.mseMet.text()) / float(self.mseKris.text())
            difD = (vDeutA + fuel) * float(self.mseMet.text()) / float(self.mseDeut.text())
            ret = difM + difK + difD
            #print(ret)
            return ret

    def optimizeAttack(self):
        # init data load
        x, self.defenderOpt = self.loadData()  # defener stays, attacker gets adjusted
        #load max Limits
        self.bounds = [(0,int(self.maxKt.text())),
                  (0, int(self.maxGt.text())),
                  (0, int(self.maxLj.text())),
                  (0, int(self.maxSj.text())),
                  (0, int(self.maxK.text())),
                  (0, int(self.maxSs.text())),
                  (0, int(self.maxKolo.text())),
                  (0, int(self.maxRec.text())),
                  (0, int(self.maxSpio.text())),
                  (0, int(self.maxBb.text())),
                  (0, int(self.maxZr.text())),
                  (0, int(self.maxTs.text())),
                  (0, int(self.maxSx.text())),
                  (0, int(self.maxRp.text())),
                  (0, int(self.maxPa.text()))
        ]

        _thread.start_new_thread(self.optimizerStart, (self,))

    def __myUpdate(self):
        self.repaint()



if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    window = BattleMainWindow()
    window.show()
    sys.exit(app.exec_())