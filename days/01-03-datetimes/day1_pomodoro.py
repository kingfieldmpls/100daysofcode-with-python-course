# Enter task name
# Set the timer (default 25 minutes)
# Give updates every minute
# Timer rings, print ASCII
# Check if task is done
# If task is done, add task to done list
# If total tasks % 4 isn't 0, short break (3-5 minutes), start at the top
# If tasks % 4 == 0, take a break (15-30 minutes)
# Setup logging to write out completed tasks and timestamp - other stats?
# Setup a way to leave the timer
# Dialog to start, stop or exit

import time

from datetime import datetime, timedelta


def choose_tasks(tasks_todo=[]):
    """ Manages items from the task list
    Args:
    tasks_todo - list, contains items to complete
    """
    print()
    print("What task do you want to complete?\n")
    for num, task in enumerate(tasks_todo, 1):
        print(f"{num}. {task}\n")
    task_choice = input("Choose from the list or enter a new task: ")
    return(task_choice)


def set_current_task(task_choice, tasks_todo):
    if not task_choice.isdigit():
        tasks_todo.append(task_choice)
        current_task = task_choice
    else:
        current_task = tasks_todo[int(task_choice)-1]
    return current_task


def get_parameters():
    """ TODO - Could also add something to check if int"""
    focus = None
    short_break = None
    long_break = None

    while True:
        focus = input("How long do you want the working "
                      "sessions to be? (20-30 minutes): ")
        if 20 <= int(focus) <= 30:
            break
        else:
            print("Please enter a number between 20 and 30")

    while True:
        short_break = input("How long do you want the short "
                            "breaks to be? (2-5 minutes): ")
        if 2 <= int(short_break) <= 5:
            break
        else:
            print("Please enter a number between 2 and 5")

    while True:
        long_break = input("How long do you want the long "
                           "break to be? (15-30 minutes): ")
        if 15 <= int(long_break) <= 30:
            break
        else:
            print("Please enter a number between 15 and 30")

    return {"focus": int(focus), "short_break": int(short_break), "long_break": int(long_break)}


def setup_pomodoro(current_task, focus=25, short_break=3, long_break=20):
    """ Sets up the basic rules of the pomodor.
    Args:
    current_task: str - thing we're doing
    focus: int - total working length
    short_break: int - short break length
    long_break: int - break after 4 pomodoros
    """
    pomodoros = 0

    while True:
        # start focus timer
        work()
        manage_timer(focus, "working")
        pomodoros += 1
        if pomodoros % 4:
            take_break()
            manage_timer(long_break, "on a long break")
        else:
            take_break()
            manage_timer(short_break, "on a short break")


def manage_timer(timer, timer_type):
    """TODO:
    Use keyboard interrupt to pause
    Give minute by minute time updates
    Print what the instructions are
    """
    print(f"You're currently {timer_type}.\nYou have {timer} minutes remaining")
    try:
        t = timedelta(minutes=timer).seconds
        time.sleep(t)
    except KeyboardInterrupt:
        print("Jigga what?")


def convert_time(interval):
    """Converts user input into datetime objects"""
    converted_time = datetime.strptime(str(interval), "%M")
    return converted_time.seconds


def start_now_pomo():
    """TODO Deal with completed tasks and reset pomo"""


def take_break():
    """ASCII Amazingness for break time - crawford2"""
    print(r"""
         ______   ____  __  _    ___       ____      ____   ____     ___   ____  __  _  __ 
        |      | /    ||  |/ ]  /  _]     /    |    |    \ |    \   /  _] /    ||  |/ ]|  |
        |      ||  o  ||  ' /  /  [_     |  o  |    |  o  )|  D  ) /  [_ |  o  ||  ' / |  |
        |_|  |_||     ||    \ |    _]    |     |    |     ||    / |    _]|     ||    \ |__|
          |  |  |  _  ||     \|   [_     |  _  |    |  O  ||    \ |   [_ |  _  ||     \ __ 
          |  |  |  |  ||  .  ||     |    |  |  |    |     ||  .  \|     ||  |  ||  .  ||  |
          |__|  |__|__||__|\_||_____|    |__|__|    |_____||__|\_||_____||__|__||__|\_||__|
    """)


def work():
    """ASCII Amazingness for break time - crawford2"""
    print(r"""
         __    __   ___   ____   __  _ 
        |  |__|  | /   \ |    \ |  |/ ]
        |  |  |  ||     ||  D  )|  ' / 
        |  |  |  ||  O  ||    / |    \ 
        |  `  '  ||     ||    \ |     \
         \      / |     ||  .  \|  .  |
          \_/\_/   \___/ |__|\_||__|\_|
    """)


def complete_tasks(tasks_todo, tasks_complete, current_task):
    tasks_todo.remove(current_task)
    tasks_complete.append(current_task)


def first_time():
    tasks_todo = []
    tasks_complete = []

    task_choice = choose_tasks()
    print()
    current_task = set_current_task(task_choice, tasks_todo)
    params = get_parameters()
    setup_pomodoro(current_task, **params)


first_time()
