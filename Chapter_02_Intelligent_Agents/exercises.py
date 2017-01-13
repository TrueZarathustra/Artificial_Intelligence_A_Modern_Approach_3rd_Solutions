import random

from helper_functions import distance2, TraceAgent, compare_agents, test_agent, rule_match
from vacuum_environment import VacuumEnvironment, TrivialVacuumEnvironment, loc_A, loc_B
from environment import Environment, XYEnvironment, Direction
from thing import Thing, Agent, Obstacle, Wall, Dirt

DIRT_POSSIBILITY = 0.3
ENV_WIDTH = 10
ENV_HEIGHT = 10

# Simple Random Agent
def SimpleRandomVacuumAgent():
    "Randomly choose one of the actions from the vacuum environment."
    return Agent(RandomAgentProgram(['TurnLeft', 'TurnRight', 'Forward', 'Suck', 'NoOp']))


def RandomAgentProgram(actions):
    "An agent that chooses an action at random, ignoring all percepts."
    return lambda percept: random.choice(actions)


# ---------------Simple Reflex Agent---------------------------

def ReflexVacuumAgent():
    "Simple Reflex Vacuum Agent. Does not suits well for this exercise!"
    def program(percept):
        status, bump = percept
        if status == 'Dirty':
            return 'Suck'
        elif bump == 'True':
            return 'TurnRight'
        else:
            return 'Forward'
    return Agent(program)


# ---------------Randomized Reflex Agent---------------------------

def RandomizedReflexVacuumAgent():
    "Simple Reflex Vacuum Agent. Does not suits well for this exercise!"
    def program(percept):
        status, bump = percept
        if status == 'Dirty':
            return 'Suck'
        elif bump == 'True':
            return random.choice(['TurnLeft', 'TurnRight'])
        else:
            return random.choice(['TurnLeft', 'TurnRight', 'Forward'])
    return Agent(program)


# ---------------Randomized Reflex Agent---------------------------


def ReflexVacuumAgentWithState():
    "Simple Reflex Vacuum Agent. Suits for rectangular vacuum environments without walls inside"

    state = {'visited': [],
             'max_left': 0,
             'max_right': 0,
             'max_top': 0,
             'max_down': 0,
             }

    def program(percept):
        status, bump = percept
        pass
        '''
        if status == 'Dirty':
            return 'Suck'
        elif bump == 'True':
            return random.choice(['TurnLeft', 'TurnRight'])
        else:
            return random.choice(['TurnLeft', 'TurnRight', 'Forward'])
        '''
    return Agent(program)


randAgent = SimpleRandomVacuumAgent()
randAgent.name = 'Random Agent'
reflAgent = ReflexVacuumAgent()
reflAgent.name = 'Simple Reflex Agent'
randReflAgent = RandomizedReflexVacuumAgent()
randReflAgent.name = 'Randomized Reflex Agent'

agents = [randAgent, reflAgent, randReflAgent]


def do_test(agent):
    agent.direction = Direction("down")
    e = VacuumEnvironment(ENV_WIDTH, ENV_HEIGHT)
    for i in range(1, e.width-1):
        for j in range(1, e.height-1):
            if random.random() < DIRT_POSSIBILITY:
                d = Dirt()
                e.add_thing(d, (i, j))
    e.add_thing(agent)
    e.run()
    return agent.performance


def do_tests(agents, num_of_tests=100):
    results = {}
    for a in agents:
        sum_perf = 0
        for i in range(num_of_tests):
            sum_perf += do_test(a)
        results[a.name] = sum_perf*1.0/num_of_tests
    return results


results = do_tests(agents, 100)
