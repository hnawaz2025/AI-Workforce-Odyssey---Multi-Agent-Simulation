
from mesa import Agent

class WorkerAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.skill_level = 1.0  # 1.0 = skilled, 0.0 = unskilled
        self.employed = True

    def step(self):
        # Decide to reskill, adapt, or resist based on environment
        if self.model.automation_level > 0.5:
            if self.random.random() < 0.6:  # chance to reskill
                self.skill_level += 0.1
            else:
                self.employed = False  # Lose job if not reskilling fast enough

class CorporationAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.strategy = "human-centric"  # Can be 'automation', 'augmentation', 'human-centric'

    def step(self):
        if self.model.automation_level > 0.7:
            self.strategy = "automation"
        elif self.model.automation_level > 0.3:
            self.strategy = "augmentation"
        else:
            self.strategy = "human-centric"

class GovernmentAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.policy = "neutral"  # 'subsidy', 'taxation', 'regulation'

    def step(self):
        if self.model.unemployment_rate > 0.1:
            self.policy = "subsidy"
        elif self.model.corporate_automation_rate > 0.7:
            self.policy = "regulation"
        else:
            self.policy = "neutral"
