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

class WorkerRushBot(sc2.BotAI):
    async def on_step(self, iteration):
        await self.distribute_workers() #smart distribution of workers
        await self.build_workers()
        await self.build_pylons()
    async def build_workers(self):
        for nexus in self.units(NEXUS).ready.noqueue: #Nexus has to be ready and it's free
            if(self.can_afford(PROBE)):
                await self.do(nexus.train(PROBE))
    async def build_pylons(self):
        if self.supply_left < 5 and not self.already_pending(PYLON):
            nexuses=self.units(NEXUS)
            if (nexuses.ready.exists) and self.can_afford(PYLON):
                await self.build(PYLON, near=nexuses.first)
                


    

run_game(maps.get("Abyssal Reef LE"), [
    Bot(Race.Protoss, WorkerRushBot()),
    Computer(Race.Protoss, Difficulty.Medium)
], realtime=True)
#https://pythonprogramming.net/workers-pylons-starcraft-ii-ai-python-sc2-tutorial/?completed=/starcraft-ii-ai-python-sc2-tutorial/