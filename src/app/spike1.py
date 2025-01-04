from dotenv import load_dotenv

load_dotenv()

import controlflow as cf  # noqa

def main():
    emails = [
        "Hello, I need an update on the project status.",
        "Subject: Exclusive offer just for you!",
        "Urgent: Project deadline moved up by one week.",
    ]

    reply = cf.run(
        "Write a polite reply to an email",
        context=dict(email=emails[0]),
    )

    print(reply)

if __name__ == '__main__':
    main()
