from pawpal_system import Owner, Pet, Task, Scheduler


# Create an owner for the pet care system.
own = Owner(name="Alex", available_time=180, preferences="Prefers morning routines")

# Create pets for the owner.
pet1 = Pet(name="Milo", breed="Golden Retriever", age=3, special_needs="Needs frequent walks")
pet2 = Pet(name="Luna", breed="Siamese", age=2, special_needs="Needs medication in the evening")

# Create tasks with different durations and priorities.
feed_task = Task(task_name="Feed breakfast", duration=15, priority="high")
walk_task = Task(task_name="Morning walk", duration=30, priority="medium")
medication_task = Task(task_name="Give medication", duration=10, priority="high")

# Assign tasks to the pets using the existing Pet methods.
pet1.add_task(feed_task)
pet1.add_task(walk_task)
pet2.add_task(medication_task)

# Add the pets to the owner using the existing Owner method.
own.add_pet(pet1)
own.add_pet(pet2)

# Create a scheduler that uses the owner.
scheduler = Scheduler(owner=own)

# Generate and organize the schedule using the existing Scheduler methods.
scheduler.generate_schedule()
scheduler.sort_tasks()

# Display the final daily plan.
scheduler.display_schedule()
