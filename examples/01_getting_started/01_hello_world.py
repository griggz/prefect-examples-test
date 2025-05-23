# ---
# title: Hello, world!
# description: Your first steps with Prefect – learn how to create a basic flow and understand core concepts.
# dependencies: ["prefect"]
# cmd: ["python", "01_getting_started/hello_world.py"]
# tags: [getting_started, basics]
# ---

# # Welcome to Prefect!
# 
# Prefect helps you build, run, and monitor reliable data workflows. Let's start with 
# the simplest possible example – a "Hello, world!" flow that greets someone by name.
# 
# ### What is a flow?
# 
# In Prefect, a **flow** is the main building block of your workflows. It's simply a 
# Python function decorated with `@flow`:
# 
# ```python
# @flow
# def my_workflow():
#     # Your workflow logic here
#     pass
# ```
# 
# Flows can contain regular Python code, call other flows, orchestrate tasks, handle 
# errors gracefully, and much more. They give you:
# 
# * **Automatic logging** – Track inputs, outputs, and runtime
# * **State management** – Monitor progress through the UI
# * **Observability** – Gain insights into performance and failures
# * **Resilience** – Add retries and error handling with minimal code
# * **Scheduling** – Run workflows on any schedule
# 
# ### Installing Prefect
# 
# For this example, you only need the core package:
# 
# ```bash
# pip install prefect
# ```
#
# ### Running the example
# 
# Execute the flow locally with:
# 
# ```bash
# python 01_getting_started/hello_world.py
# ```
# 
# Now let's look at the code!
from prefect import flow


# ## Creating your first flow
# 
# Below we define a simple flow that greets someone by name. Notice:
# 
# 1. The `@flow` decorator transforms a regular Python function into a Prefect flow
# 2. The function takes a parameter with a default value
# 3. We use `log_prints=True` to capture print statements as logs
# 
# The `log_prints=True` parameter is especially helpful because it:
# * Captures **all** `print()` statements inside the flow
# * Forwards them to Prefect's logging system
# * Makes them visible in the Prefect UI and local logs
# * Saves you from having to use a separate logger
@flow(log_prints=True)
def hello(name: str = "Marvin") -> None:
    """Log a friendly greeting."""
    print(f"Hello, {name}!")


# ## Running your flow
# 
# Running a flow is as simple as calling the function. Below we demonstrate:
# 
# 1. Calling with the default parameter
# 2. Overriding the parameter with a custom value
# 
# Every time you run the flow, Prefect tracks the execution and maintains a record 
# of the run state, parameters, logs, and more.
if __name__ == "__main__":
    # 1️⃣ Run the flow with the default parameter
    hello()  # Logs: "Hello, Marvin!"

    # 2️⃣ Run the flow with a different argument
    hello("Arthur")  # Logs: "Hello, Arthur!"

# ### What just happened?
# 
# When you ran this script, Prefect:
# 
# 1. Registered your `hello` function as a flow
# 2. Created and executed a flow run with the default parameter "Marvin"
# 3. Captured the print statement as a log entry
# 4. Created and executed another flow run with the parameter "Arthur"
# 
# ### Next steps
# 
# This simple example only scratches the surface of what Prefect can do. As you 
# continue, you'll learn about:
# 
# * **Tasks** – Smaller units of work that make up flows
# * **Subflows** – Flows that call other flows
# * **Retries** – Automatic recovery from failures
# * **Deployments** – Schedule and trigger flows from the API
# * **Blocks** – Securely store and use configuration
# 
# Prefect makes complex workflows and orchestration simple while letting you 
# write pure Python code without complex DSLs or configuration formats.
