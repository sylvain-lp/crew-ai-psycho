#!/usr/bin/env python

TOPIC="Anxiety, Perfectionism, and Postponement"
import sys
import warnings

from datetime import datetime
from psycho.crew import Psycho

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': TOPIC,
        'current_year': str(datetime.now().year)
    }
    
    # try:
    #     Psycho().crew().kickoff(inputs=inputs)
    # except Exception as e:
    #     raise Exception(f"An error occurred while running the crew: {e}")

    previous_result = None
    for session in range(5):
        result = Psycho().crew().kickoff(
            inputs={
                'topic': TOPIC,
                'current_year': str(datetime.now().year),
                "therapy_session": {"previous_session": previous_result},
                "introspection": {"previous_session": previous_result}
            }
        )
    previous_result = result

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": TOPIC,
        'current_year': str(datetime.now().year)
    }
    try:
        Psycho().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Psycho().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": TOPIC,
        "current_year": str(datetime.now().year)
    }
    
    try:
        Psycho().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
