from mesa import Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
from agent import WorkerAgent, CorporationAgent, GovernmentAgent

class AIWFModel(Model):
    def __init__(self, N_workers, N_corporations, N_government, automation_level):
        self.num_workers = N_workers
        self.num_corporations = N_corporations
        self.num_government = N_government
        self.automation_level = automation_level
        self.schedule = RandomActivation(self)

        # Track metrics
        self.unemployment_rate = 0
        self.corporate_automation_rate = 0

        # Create agents
        for i in range(self.num_workers):
            worker = WorkerAgent(i, self)
            self.schedule.add(worker)

        for i in range(self.num_workers, self.num_workers + self.num_corporations):
            corp = CorporationAgent(i, self)
            self.schedule.add(corp)

        for i in range(self.num_workers + self.num_corporations,
                       self.num_workers + self.num_corporations + self.num_government):
            gov = GovernmentAgent(i, self)
            self.schedule.add(gov)

        # Data collection
        self.datacollector = DataCollector(
            model_reporters={"Unemployment Rate": self.get_unemployment_rate})

    def step(self):
        self.schedule.step()
        self.update_stats()
        self.datacollector.collect(self)

    def update_stats(self):
        employed_workers = [agent for agent in self.schedule.agents
                            if isinstance(agent, WorkerAgent) and agent.employed]
        total_workers = [agent for agent in self.schedule.agents if isinstance(agent, WorkerAgent)]
        self.unemployment_rate = 1 - (len(employed_workers) / len(total_workers))

    def get_unemployment_rate(self):
        return self.unemployment_rate
