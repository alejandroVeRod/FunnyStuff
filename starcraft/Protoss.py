#!/usr/local/bin/python3
import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from sc2.ids.unit_typeid import UnitTypeId
from sc2.ids.ability_id import AbilityId
from sc2.ids.buff_id import BuffId
from sc2.ids.upgrade_id import UpgradeId
from sc2.ids.effect_id import EffectId
PROBE = UnitTypeId.PROBE
NEXUS=UnitTypeId.NEXUS
PYLON=UnitTypeId.PYLON
ASSIMILATOR = UnitTypeId.ASSIMILATOR
GATEWAY = UnitTypeId.GATEWAY
CYBERNETICSCORE = UnitTypeId.CYBERNETICSCORE
STALKER = UnitTypeId.STALKER
class WorkerRushBot(sc2.BotAI):
    async def on_step(self, iteration):
        await self.distribute_workers() #smart distribution of workers
        await self.build_workers()
        await self.build_pylons()
        await self.build_assimilators()
        await self.expand()
        await self.offensive_force_buildings()
        await self.build_offensive_force()

    '''
    BUILDING METHODS
    '''
    async def build_workers(self):
        for nexus in self.units(NEXUS).ready.noqueue: #Nexus has to be ready and free
            if(self.can_afford(PROBE)):
                await self.do(nexus.train(PROBE))
    async def build_pylons(self):
        if self.supply_left < 5 and not self.already_pending(PYLON):
            nexuses=self.units(NEXUS)
            if (nexuses.ready.exists) and self.can_afford(PYLON):
                await self.build(PYLON, near=nexuses.first)
    async def build_assimilators(self):
        for nexus in self.units(NEXUS).ready:
            vaspenes=self.state.vespene_geyser.closer_than(15.0,nexus)
            for vaspene in vaspenes:
                if not self.can_afford(ASSIMILATOR):
                    break
                worker = self.select_build_worker(vaspene.position) #select a near worker
                if worker is None:
                    break
                if not self.units(ASSIMILATOR).closer_than(1.0,vaspene).exists:
                    await self.do(worker.build(ASSIMILATOR,vaspene))
    async def expand(self):
        if (self.units(NEXUS).amount < 3) and (self.can_afford(NEXUS)):
            await self.expand_now()

    async def offensive_force_buildings(self):
        if self.units(PYLON).ready.exists:
            pylon= self.units(PYLON).ready.random
            if self.units(GATEWAY).ready.exists:
                if not self.units(CYBERNETICSCORE):
                    if self.can_afford(CYBERNETICSCORE) and not self.already_pending(CYBERNETICSCORE):
                        await self.build(CYBERNETICSCORE,near=pylon)
            else:
                if(self.can_afford(GATEWAY) and not self.already_pending(GATEWAY)):
                    await self.build(GATEWAY,near=pylon)
    async def build_offensive_force(self):
        for gw in self.units(GATEWAY).ready.noqueue:
            if(self.can_afford(STALKER)) and self.supply_left > 0:
                await self.do(gw.train(STALKER))




run_game(maps.get("Abyssal Reef LE"), [
    Bot(Race.Protoss, WorkerRushBot()),
    Computer(Race.Protoss, Difficulty.Medium)
], realtime=True)
#https://pythonprogramming.net/commanding-army-starcraft-ii-ai-python-sc2-tutorial/?completed=/building-army-starcraft-ii-ai-python-sc2-tutorial/