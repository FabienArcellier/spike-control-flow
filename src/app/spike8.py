"""

"""
import random
from dotenv import load_dotenv

load_dotenv()

import controlflow as cf  # noqa

def main():
    def roll_dice():
        '''roll one die'''
        return random.randint(1, 6)

    task = cf.Task(
        "Roll 3 dice and report the results",
        max_llm_calls=4,
        tools=[roll_dice],
    )

    # this will fail
    result = task.run()
    print(result)

if __name__ == '__main__':
    main()
