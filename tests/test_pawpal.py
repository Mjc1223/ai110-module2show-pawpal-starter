from pawpal_system import Task, Pet


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
