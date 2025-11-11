from enum import Enum
from result import Result, Ok, Err


class Status(Enum):
    SUCCESS = 0
    NOT_FOUND = 1
    INVALID_ARGUMENT = 2

def find_item(item_id: int) -> tuple[Status, str | None]:
    """
    Simulates finding an item in a database.
    Returns a tuple of (Status, item_name or None).
    """
    if item_id < 0:
        return Status.INVALID_ARGUMENT, None
    elif item_id == 100:
        return Status.SUCCESS, "Found Item A"
    else:
        return Status.NOT_FOUND, None

if __name__ == "__main__":
    status, result = find_item(100)
    if status == Status.SUCCESS:
        print(f"Item found: {result}")
    elif status == Status.NOT_FOUND:
        print("Item not found.")
    else:
        print(f"Error: {status.name}")

class Status(Enum):
    ACTION_A = "Action A"
    ACTION_B = "Action B"
    ACTION_C = "Action C"
    INVALID = "Invalid"

def perform_action(action_id: int) -> Result[Status, str]:
    """
    Simulates performing an action and returns a Result object.
    Ok contains a Status, Err contains an error message.
    """
    if action_id == 1:
        return Ok(Status.ACTION_A)
    elif action_id == 2:
        return Ok(Status.ACTION_B)
    elif action_id == 3:
        return Ok(Status.ACTION_C)
    else:
        return Err("Invalid action ID.")

if __name__ == "__main__":
    action_id = 2  # Change this to test different cases
    result = perform_action(action_id)

    if isinstance(result, Ok):
        status = result.unwrap()
        if status == Status.ACTION_A:
            print("Performing Action A...")
        elif status == Status.ACTION_B:
            print("Performing Action B...")
        elif status == Status.ACTION_C:
            print("Performing Action C...")
    elif isinstance(result, Err):
        print(f"Error: {result.unwrap_err()}")