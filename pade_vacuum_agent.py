from pade.acl.messages import ACLMessage
from pade.misc.utility import start_loop
from pade.core.agent import Agent
from pade.core.agent import AID

class SimpleVacuumAgent(Agent):
    def __init__(self, aid, name):
        super(SimpleVacuumAgent, self).__init__(aid=aid, debug=True)
        self.name = name

    def on_start(self):
        super(SimpleVacuumAgent, self).on_start()
        print(f"{self.name} started.")

    def react(self, message):
        print(f"{self.name} received message: {message.content}")

if __name__ == '__main__':
    agent_a = SimpleVacuumAgent(AID(name='agent_a@localhost:8000'), 'Agent A')
    agent_b = SimpleVacuumAgent(AID(name='agent_b@localhost:8001'), 'Agent B')
    agents = [agent_a, agent_b]
    start_loop(agents) 