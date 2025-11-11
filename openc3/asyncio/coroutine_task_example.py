"""
Key Differences Summarized:

Nature:
Coroutines are the "what" (the asynchronous code logic),
while tasks are the "how" (the mechanism to run coroutines concurrently).

Execution:
Coroutines are defined but don't run on their own; tasks are the objects that the event loop actively executes.

Concurrency:
Tasks enable concurrency by allowing the event loop to switch between different coroutines when an await
is encountered, while coroutines are the units of work that can be paused and resumed.
"""
import asyncio

# Define a simple coroutine
async def my_coroutine():
    print("Coroutine started")
    await asyncio.sleep(1)      # Simulate an asynchronous operation
    print("Coroutine finished")

async def main():       # defines a coroutine function
    task = asyncio.create_task(my_coroutine()) # Create a task from the coroutine. wraps/schedules it as a Task on the running loop
    print("Task created")
    await task          # Wait for the task to complete. This allows other tasks to run in the meantime.
    print("Task completed")

# Calling main() produces a coroutine object;
if __name__ == '__main__':
    asyncio.run(main())     # Run the main function in the event loop. This starts the event loop, runs main(), and closes the loop when done.

"""
The event loop is created and run by asyncio.run(main()) at the bottom of openc3/asyncio/coroutine_task_example.py. 
asyncio.create_task() 
schedules the coroutine on that running loop. To get the current loop inside a coroutine use:

loop = asyncio.get_running_loop()
"""