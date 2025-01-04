"""

"""
from dotenv import load_dotenv

load_dotenv()

import controlflow as cf  # noqa

def main():
    tasks = cf.plan(
        objective="Analyze customer feedback data",
        n_tasks=3  # Optionally specify the number of tasks
    )

    # Execute the generated plan
    result = cf.run_tasks(tasks)
    print(result)

if __name__ == '__main__':
    main()
