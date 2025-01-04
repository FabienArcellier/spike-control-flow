"""

"""
from dotenv import load_dotenv

load_dotenv()

import controlflow as cf  # noqa

def main():
    name_task = cf.Task("Get the user's name", interactive=True)
    poem_task = cf.Task('Write a poem about the user', depends_on=[name_task])

    poem = poem_task.run()
    print(poem)

if __name__ == '__main__':
    main()
