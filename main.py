import time
import pyautogui
import random


def random_key_press():
    hours = 0
    minutes = 23
    seconds = 0

    random_keys = ['space', 'w', 'a', 's', 'd']

    ms_runtime = (hours * 3600) + (minutes * 60) + seconds
    end_time = time.time() + ms_runtime
    print(f'Program is running for {hours} hours and {minutes} minutes and {seconds} seconds')

    min_interval_minutes = 4.5
    max_interval_minutes = 8.7

    while time.time() <= end_time:
        random_button = random.choice(random_keys)
        pyautogui.keyDown(random_button)
        time.sleep(random.randint(500, 2000) / 1000)  # Sleep in seconds
        pyautogui.keyUp(random_button)
        print(f'Random button pressed: {random_button}')

        remaining_seconds = int(end_time - time.time())
        remaining_minutes = remaining_seconds // 60
        remaining_seconds %= 60

        print(f'Time remaining: {remaining_minutes} minutes and {remaining_seconds} seconds')

        min_interval_ms = int(min_interval_minutes * 60 * 1000)
        max_interval_ms = int(max_interval_minutes * 60 * 1000)
        rand_interval = random.randint(min_interval_ms, max_interval_ms)
        time.sleep(rand_interval / 1000)

    print("Program finished.")


if __name__ == "__main__":
    try:
        print('Press Ctrl+C to exit.')
        print('Program will start in 15 seconds.')
        time.sleep(15)
        random_key_press()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
