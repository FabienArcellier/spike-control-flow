"""

"""
from dotenv import load_dotenv

load_dotenv()

import controlflow as cf  # noqa

def main():
    task_1 = cf.Task('Write a poem about AI')
    task_2 = cf.Task('Critique the poem', depends_on=[task_1])

    results = cf.run_tasks([task_1, task_2])
    print(results)

if __name__ == '__main__':
    main()
