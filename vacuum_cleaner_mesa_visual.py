from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.visualization.modules import CanvasGrid, ChartModule, TextElement
from mesa.visualization.ModularVisualization import ModularServer

class Dirt(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

class VacuumCleanerAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.performance = 0

    def step(self):
        cell_contents = self.model.grid.get_cell_list_contents([self.pos])
        dirt = [obj for obj in cell_contents if isinstance(obj, Dirt)]
        if dirt:
            for d in dirt:
                self.model.grid.remove_agent(d)
            self.performance += 10
        else:
            # Move to the other cell
            new_pos = (1, 0) if self.pos == (0, 0) else (0, 0)
            self.model.grid.move_agent(self, new_pos)
            self.performance -= 1
        self.model.step_count += 1
        self.model.datacollector.collect(self.model)

class VacuumWorld(Model):
    def __init__(self):
        self.grid = MultiGrid(2, 1, torus=False)
        self.schedule = RandomActivation(self)
        self.agent = VacuumCleanerAgent(1, self)
        self.grid.place_agent(self.agent, (0, 0))
        self.schedule.add(self.agent)
        self.grid.place_agent(Dirt(2, self), (0, 0))
        self.grid.place_agent(Dirt(3, self), (1, 0))
        self.running = True
        self.step_count = 0
        from mesa.datacollection import DataCollector
        self.datacollector = DataCollector(
            model_reporters={"Performance": lambda m: m.agent.performance}
        )
        self.datacollector.collect(self)

    def step(self):
        self.schedule.step()
        dirty_cells = [obj for cell in self.grid.coord_iter() for obj in cell[0] if isinstance(obj, Dirt)]
        if not dirty_cells:
            self.running = False

class AgentStatsElement(TextElement):
    def render(self, model):
        loc = 'A' if model.agent.pos == (0, 0) else 'B'
        return f"Step: {model.step_count} | Agent Location: {loc} | Performance: {model.agent.performance}"

def agent_portrayal(agent):
    if isinstance(agent, VacuumCleanerAgent):
        return {"Shape": "circle", "Color": "blue", "Filled": "true", "Layer": 1, "r": 0.5}
    elif isinstance(agent, Dirt):
        return {"Shape": "rect", "Color": "brown", "Filled": "true", "Layer": 0, "w": 1, "h": 1}

grid = CanvasGrid(agent_portrayal, 2, 1, 400, 200)
chart = ChartModule([
    {"Label": "Performance", "Color": "Black"}
])

server = ModularServer(
    VacuumWorld,
    [grid, AgentStatsElement(), chart],
    "Vacuum Cleaner Model",
    {}
)
server.port = 8521  # Default
server.launch() 