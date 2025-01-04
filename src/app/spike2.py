from dotenv import load_dotenv

load_dotenv()

import controlflow as cf  # noqa

def main():
    emails = [
        "Hello, I need an update on the project status.",
        "Subject: Exclusive offer just for you!",
        "Urgent: Project deadline moved up by one week.",
    ]

    # Create a specialized agent
    classifier = cf.Agent(
        name="Email Classifier",
        model="openai/gpt-4o-mini",
        instructions="You are an expert at quickly classifying emails.",
    )

    # Set up a ControlFlow task to classify emails
    classifications = []
    for email in emails:
        classification = cf.run(
            'Classify the email',
            result_type=['important', 'spam'],
            agents=[classifier],
            context=dict(email=email),
        )
        classifications.append(classification)

    print(classifications)

if __name__ == '__main__':
    main()
