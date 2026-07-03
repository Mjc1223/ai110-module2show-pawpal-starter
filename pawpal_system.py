from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Task:
    task_name: str
    duration: int
    priority: str
    completed: bool = False

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completed = True

    def edit_task(self, task_name: Optional[str] = None, duration: Optional[int] = None, priority: Optional[str] = None) -> None:
        """Edit fields of the task. Only non-None values are applied."""
        if task_name is not None:
            self.task_name = task_name
        if duration is not None:
            self.duration = duration
        if priority is not None:
            self.priority = priority


@dataclass
class Pet:
    name: str
    breed: str
    age: int
    special_needs: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a Task to this pet's task list."""
        self.tasks.append(task)

    def update_info(self, breed: Optional[str] = None, age: Optional[int] = None, special_needs: Optional[str] = None) -> None:
        """Update pet information fields when provided."""
        if breed is not None:
            self.breed = breed
        if age is not None:
            self.age = age
        if special_needs is not None:
            self.special_needs = special_needs


@dataclass
class Owner:
    name: str
    available_time: int
    preferences: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a Pet to the owner's pets list."""
        self.pets.append(pet)

    def update_preferences(self, preferences: str) -> None:
        """Update the owner's preferences."""
        self.preferences = preferences

    def view_schedule(self) -> None:
        """Generate and display the schedule for all pets using Scheduler."""
        scheduler = Scheduler(self)
        scheduler.generate_schedule()
        scheduler.sort_tasks()
        scheduler.display_schedule()


class Scheduler:
    def __init__(self, owner: Owner) -> None:
        self.owner: Owner = owner
        self.task_list: List[Task] = []
        self.daily_plan: List[Task] = []

    def generate_schedule(self) -> None:
        """Collect all incomplete tasks from the owner's pets into task_list."""
        self.task_list = []
        for pet in self.owner.pets:
            for task in pet.tasks:
                if not task.completed:
                    self.task_list.append(task)
        # initialize daily_plan as a copy of collected tasks
        self.daily_plan = list(self.task_list)

    def sort_tasks(self) -> None:
        """Sort tasks by priority (high -> medium -> low)."""
        priority_order = {"high": 1, "medium": 2, "low": 3}

        def priority_key(task: Task) -> int:
            return priority_order.get(task.priority.lower(), 99)

        self.daily_plan = sorted(self.task_list, key=priority_key)

    def display_schedule(self) -> None:
        """Print the daily plan in a readable format, grouped by pet when possible."""
        if not self.daily_plan:
            print("No tasks scheduled for today.")
            return

        print("Daily Plan:")
        for idx, task in enumerate(self.daily_plan, start=1):
            # try to find which pet this task belongs to
            pet_name = None
            for pet in self.owner.pets:
                if task in pet.tasks:
                    pet_name = pet.name
                    break
            status = "Done" if task.completed else "Pending"
            print(f"{idx}. [{status}] {task.task_name} (Priority: {task.priority}, Duration: {task.duration}m) - Pet: {pet_name or 'Unknown'})")
