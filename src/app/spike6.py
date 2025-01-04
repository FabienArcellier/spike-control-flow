"""

"""
from dotenv import load_dotenv

load_dotenv()

import controlflow as cf  # noqa

def main():
    optimist = cf.Agent(name="Optimist", model="openai/gpt-4o-mini")
    pessimist = cf.Agent(name="Pessimist", model="openai/gpt-4o-mini")
    moderator = cf.Agent(name="Moderator")

    results = cf.run(
        "Debate the meaning of life",
        instructions='Give each agent at least three chances to speak.',
        agents=[moderator, optimist, pessimist],
        completion_agents=[moderator],
        turn_strategy=cf.orchestration.turn_strategies.Moderated(moderator=moderator),
    )

    print(results)

if __name__ == '__main__':
    main()
