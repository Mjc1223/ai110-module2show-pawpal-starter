from pawpal_system import Task, Pet, Owner, Scheduler


def test_task_mark_complete_updates_completed_status():
    task = Task(task_name="Feed pet", duration=15, priority="high")

    assert task.completed is False

    task.mark_complete()

    assert task.completed is True


def test_pet_add_task_increases_task_count():
    pet = Pet(name="Milo", breed="Golden Retriever", age=3, special_needs="Needs walks")
    task = Task(task_name="Walk", duration=20, priority="medium")

    assert len(pet.tasks) == 0

    pet.add_task(task)

    assert len(pet.tasks) == 1


def test_detect_conflicts_returns_warning_for_duplicate_scheduled_time():
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
