'''
orientations = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def turn_heading(heading, inc, headings=orientations)
def turn_right(heading)
def turn_left(heading)
def distance(a, b)
def distance2(a, b)
def rule_match(state, rules)
def TraceAgent(agent)
def compare_agents(EnvFactory, AgentFactories, n=10, steps=1000)
def test_agent(AgentFactory, steps, envs)
'''

import copy

from numpy import mean

import math

orientations = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def turn_heading(heading, inc, headings=orientations):
    return headings[(headings.index(heading) + inc) % len(headings)]


def turn_right(heading):
    return turn_heading(heading, -1)


def turn_left(heading):
    return turn_heading(heading, +1)


def distance(a, b):
    """The distance between two (x, y) points."""
    return math.hypot((a[0] - b[0]), (a[1] - b[1]))


def distance2(a, b):
    "The square of the distance between two (x, y) points."
    return (a[0] - b[0])**2 + (a[1] - b[1])**2


def rule_match(state, rules):
    "Find the first rule that matches state."
    for rule in rules:
        if rule.matches(state):
            return rule


def TraceAgent(agent):
    """Wrap the agent's program to print its input and output. This will let
    you see what the agent is doing in the environment."""
    old_program = agent.program

    def new_program(percept):
        action = old_program(percept)
        print('{} perceives {} and does {}'.format(agent, percept, action))
        return action
    agent.program = new_program
    return agent



def compare_agents(EnvFactory, AgentFactories, n=10, steps=1000):
    """See how well each of several agents do in n instances of an environment.
    Pass in a factory (constructor) for environments, and several for agents.
    Create n instances of the environment, and run each agent in copies of
    each one for steps. Return a list of (agent, average-score) tuples."""
    envs = [EnvFactory() for i in range(n)]
    return [(A, test_agent(A, steps, copy.deepcopy(envs)))
            for A in AgentFactories]


def test_agent(AgentFactory, steps, envs):
    "Return the mean score of running an agent in each of the envs, for steps"
    def score(env):
        agent = AgentFactory()
        env.add_thing(agent)
        env.run(steps)
        return agent.performance
    return mean(map(score, envs))