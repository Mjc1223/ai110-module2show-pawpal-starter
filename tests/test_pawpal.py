from datetime import date, timedelta

from pawpal_system import Task, Pet, Owner, Scheduler


def test_task_mark_complete_updates_completed_status():
    # This checks that marking a task complete changes its status.
    task = Task(task_name="Feed pet", duration=15, priority="high")

    assert task.completed is False

    task.mark_complete()

    assert task.completed is True


def test_pet_add_task_increases_task_count():
    # This checks that adding a task to a pet stores it on the pet.
    pet = Pet(name="Milo", breed="Golden Retriever", age=3, special_needs="Needs walks")
    task = Task(task_name="Walk", duration=20, priority="medium")

    assert len(pet.tasks) == 0

    pet.add_task(task)

    assert len(pet.tasks) == 1


def test_sort_by_time_orders_tasks_chronologically():
    # This checks that tasks are sorted from earliest to latest scheduled time.
    owner = Owner(name="Alex", available_time=180, preferences="Test owner")
    pet = Pet(name="Milo", breed="Golden Retriever", age=3, special_needs="Needs walks")

    task_one = Task(task_name="Walk", duration=20, priority="medium", scheduled_time="10:00")
    task_two = Task(task_name="Feed", duration=10, priority="high", scheduled_time="08:00")
    task_three = Task(task_name="Brush", duration=5, priority="low", scheduled_time="09:00")

    for task in [task_one, task_two, task_three]:
        pet.add_task(task)

    owner.add_pet(pet)

    scheduler = Scheduler(owner)
    scheduler.generate_schedule()
    scheduler.sort_by_time()

    scheduled_times = [task.scheduled_time for task in scheduler.daily_plan]

    assert scheduled_times == ["08:00", "09:00", "10:00"]


def test_mark_complete_creates_next_daily_task():
    # This checks that a daily recurring task creates the next day’s task when completed.
    task = Task(
        task_name="Feed",
        duration=10,
        priority="high",
        frequency="daily",
        due_date=date(2026, 7, 1),
    )

    next_task = task.mark_complete()

    assert task.completed is True
    assert next_task is not None
    assert next_task.completed is False
    assert next_task.frequency == "daily"
    assert next_task.due_date == date(2026, 7, 2)


def test_mark_complete_creates_next_weekly_task():
    # This checks that a weekly recurring task creates the next week’s task when completed.
    task = Task(
        task_name="Groom",
        duration=20,
        priority="medium",
        frequency="weekly",
        due_date=date(2026, 7, 1),
    )

    next_task = task.mark_complete()

    assert task.completed is True
    assert next_task is not None
    assert next_task.completed is False
    assert next_task.frequency == "weekly"
    assert next_task.due_date == date(2026, 7, 8)


def test_detect_conflicts_returns_warning_for_duplicate_scheduled_time():
    # This checks that duplicate scheduled times create a warning instead of crashing.
    owner = Owner(name="Alex", available_time=180, preferences="Test owner")
    pet = Pet(name="Milo", breed="Golden Retriever", age=3, special_needs="Needs walks")
    task_one = Task(task_name="Walk", duration=20, priority="medium", scheduled_time="09:00")
    task_two = Task(task_name="Feed", duration=10, priority="high", scheduled_time="09:00")

    pet.add_task(task_one)
    pet.add_task(task_two)
    owner.add_pet(pet)

    scheduler = Scheduler(owner)
    scheduler.generate_schedule()

    warnings = scheduler.detect_conflicts()

    assert len(warnings) == 1
    assert "09:00" in warnings[0]


def test_filter_by_pet_name_returns_only_matching_tasks():
    # This checks that filtering by pet name returns tasks for that pet only.
    owner = Owner(name="Alex", available_time=180, preferences="Test owner")
    milo = Pet(name="Milo", breed="Golden Retriever", age=3, special_needs="Needs walks")
    luna = Pet(name="Luna", breed="Cat", age=2, special_needs="Needs litter box")

    milo_task = Task(task_name="Walk", duration=20, priority="medium")
    luna_task = Task(task_name="Feed", duration=10, priority="high")

    milo.add_task(milo_task)
    luna.add_task(luna_task)

    owner.add_pet(milo)
    owner.add_pet(luna)

    scheduler = Scheduler(owner)
    filtered_tasks = scheduler.filter_by_pet_name("Milo")

    assert [task.task_name for task in filtered_tasks] == ["Walk"]
    assert all(task.pet_name == "Milo" for task in filtered_tasks)


def test_filter_by_status_returns_only_completed_or_pending_tasks():
    # This checks that filtering by completion status returns only the matching tasks.
    owner = Owner(name="Alex", available_time=180, preferences="Test owner")
    pet = Pet(name="Milo", breed="Golden Retriever", age=3, special_needs="Needs walks")

    completed_task = Task(task_name="Completed task", duration=5, priority="low", completed=True)
    pending_task = Task(task_name="Pending task", duration=10, priority="medium", completed=False)

    pet.add_task(completed_task)
    pet.add_task(pending_task)
    owner.add_pet(pet)

    scheduler = Scheduler(owner)
    completed_tasks = scheduler.filter_by_status(True)
    pending_tasks = scheduler.filter_by_status(False)

    assert [task.task_name for task in completed_tasks] == ["Completed task"]
    assert [task.task_name for task in pending_tasks] == ["Pending task"]
    assert all(task.completed for task in completed_tasks)
    assert all(not task.completed for task in pending_tasks)
