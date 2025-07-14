from mesa import Agent, Model
from mesa.time import RandomActivation

class VacuumCleanerAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.location = self.random.choice([0, 1])  # 0: loc_A, 1: loc_B
        self.performance = 0

    def step(self):
        # If current location is dirty, clean it
        if self.model.status[self.location] == 'Dirty':
            self.model.status[self.location] = 'Clean'
            self.performance += 10
        else:
            # Move to the other location
            self.location = 1 - self.location
            self.performance -= 1

class VacuumWorld(Model):
    def __init__(self):
        self.schedule = RandomActivation(self)
        # 0: loc_A, 1: loc_B
        self.status = [self.random.choice(['Clean', 'Dirty']) for _ in range(2)]
        self.agent = VacuumCleanerAgent(1, self)
        self.schedule.add(self.agent)
        self.running = True

    def step(self):
        self.schedule.step()
        # Stop if both locations are clean
        if all(s == 'Clean' for s in self.status):
            self.running = False

if __name__ == "__main__":
    model = VacuumWorld()
    step_count = 0
    print(f"Initial status: {model.status}")
    while model.running:
        model.step()
        step_count += 1
        print(f"Step {step_count}: Agent at loc_{'A' if model.agent.location == 0 else 'B'}, Status: {model.status}, Performance: {model.agent.performance}")
    print(f"Final performance: {model.agent.performance}") 