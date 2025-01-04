"""

"""
from dotenv import load_dotenv

load_dotenv()

import controlflow as cf  # noqa
from controlflow.orchestration.handler import Handler  # noqa
from controlflow.events.events import AgentMessage  # noqa

def main():
    class LoggingHandler(Handler):
        def on_event(self, event):
            print(f"Event: {event.event}")

        def on_agent_message(self, event: AgentMessage):
            print(f"Agent {event.agent.name} said: {event.ai_message.content}")

    cf.run("Write a short poem about AI", handlers=[LoggingHandler()])

if __name__ == '__main__':
    main()
