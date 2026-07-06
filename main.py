from datetime import date

from pawpal_system import Owner, Pet, Task, Scheduler


# Create an owner for the pet care system.
own = Owner(name="Alex", available_time=180, preferences="Prefers morning routines")

# Create pets for the owner.
pet1 = Pet(name="Milo", breed="Golden Retriever", age=3, special_needs="Needs frequent walks")
pet2 = Pet(name="Luna", breed="Siamese", age=2, special_needs="Needs medication in the evening")

# Create tasks with different durations, priorities, and intentionally out-of-order times.
feed_task = Task(
    task_name="Feed breakfast",
    duration=15,
    priority="high",
    scheduled_time="09:30",
    frequency="daily",
    due_date=date(2026, 7, 5),
)
walk_task = Task(
    task_name="Morning walk",
    duration=30,
    priority="medium",
    scheduled_time="08:00",
    frequency="weekly",
    due_date=date(2026, 7, 5),
)
medication_task = Task(
    task_name="Give medication",
    duration=10,
    priority="high",
    scheduled_time="10:15",
    frequency="none",
    due_date=date(2026, 7, 5),
)
conflict_task = Task(
    task_name="Evening check",
    duration=15,
    priority="medium",
    scheduled_time="09:30",
    frequency="none",
    due_date=date(2026, 7, 5),
)

# Assign tasks to the pets using the existing Pet methods.
pet1.add_task(feed_task)
pet1.add_task(walk_task)
pet2.add_task(medication_task)
pet2.add_task(conflict_task)

# Add the pets to the owner using the existing Owner method.
own.add_pet(pet1)
own.add_pet(pet2)

# Create a scheduler that uses the owner.
scheduler = Scheduler(owner=own)

# Generate and organize the schedule using the existing Scheduler methods.
scheduler.generate_schedule()

print("Tasks before sorting by time:")
for task in scheduler.daily_plan:
    print(f"- {task.task_name}: {task.scheduled_time}")

scheduler.sort_by_time()

print("\nTasks after sorting by time:")
for task in scheduler.daily_plan:
    print(f"- {task.task_name}: {task.scheduled_time}")

print("\nConflict detection demo:")
conflicts = scheduler.detect_conflicts()
if conflicts:
    for warning in conflicts:
        print(f"- {warning}")
else:
    print("- No conflicts detected.")

print("\nRecurring task demo:")
print("Daily recurring task before completion:")
print(f"- {feed_task.task_name} | Frequency: {feed_task.frequency} | Due: {feed_task.due_date}")

next_daily_task = feed_task.mark_complete()
if next_daily_task is not None:
    pet1.add_task(next_daily_task)

print("\nNew daily recurring task created:")
print(f"- {next_daily_task.task_name} | Frequency: {next_daily_task.frequency} | Due: {next_daily_task.due_date}")

print("\nWeekly recurring task before completion:")
print(f"- {walk_task.task_name} | Frequency: {walk_task.frequency} | Due: {walk_task.due_date}")

next_weekly_task = walk_task.mark_complete()
if next_weekly_task is not None:
    pet2.add_task(next_weekly_task)

print("\nNew weekly recurring task created:")
print(f"- {next_weekly_task.task_name} | Frequency: {next_weekly_task.frequency} | Due: {next_weekly_task.due_date}")

# Display the final daily plan.
scheduler.display_schedule()
