from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import List, Optional


@dataclass
class Task:
    task_name: str
    duration: int
    priority: str
    completed: bool = False
    scheduled_time: Optional[str] = None
    frequency: str = "none"
    due_date: date = field(default_factory=date.today)
    pet_name: Optional[str] = None

    def mark_complete(self) -> Optional["Task"]:
        """Mark the task complete and create the next occurrence for daily or weekly tasks."""
        self.completed = True

        normalized_frequency = self.frequency.lower()
        if normalized_frequency == "daily":
            next_due_date = self.due_date + timedelta(days=1)
            return Task(
                task_name=self.task_name,
                duration=self.duration,
                priority=self.priority,
                completed=False,
                scheduled_time=self.scheduled_time,
                frequency=self.frequency,
                due_date=next_due_date,
                pet_name=self.pet_name,
            )

        if normalized_frequency == "weekly":
            next_due_date = self.due_date + timedelta(days=7)
            return Task(
                task_name=self.task_name,
                duration=self.duration,
                priority=self.priority,
                completed=False,
                scheduled_time=self.scheduled_time,
                frequency=self.frequency,
                due_date=next_due_date,
                pet_name=self.pet_name,
            )

        return None

    def edit_task(
        self,
        task_name: Optional[str] = None,
        duration: Optional[int] = None,
        priority: Optional[str] = None,
    ) -> None:
        """Update task details when new values are provided."""
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
        """Append a task to the pet and remember which pet owns it."""
        task.pet_name = self.name
        self.tasks.append(task)

    def update_info(
        self,
        breed: Optional[str] = None,
        age: Optional[int] = None,
        special_needs: Optional[str] = None,
    ) -> None:
        """Update pet information when new values are provided."""
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
        """Add a pet to the owner's pet list."""
        self.pets.append(pet)

    def update_preferences(self, preferences: str) -> None:
        """Update the owner's preferences."""
        self.preferences = preferences

    def view_schedule(self) -> None:
        """Show the scheduled tasks for all pets."""
        scheduler = Scheduler(self)
        scheduler.generate_schedule()
        scheduler.sort_tasks()
        scheduler.display_schedule()


class Scheduler:
    def __init__(self, owner: Owner) -> None:
        """Initialize the scheduler for a given owner."""
        self.owner: Owner = owner
        self.task_list: List[Task] = []
        self.daily_plan: List[Task] = []

    def filter_by_pet_name(self, pet_name: str) -> List[Task]:
        """Return all tasks belonging to the named pet."""
        return [
            task
            for pet in self.owner.pets
            for task in pet.tasks
            if task.pet_name == pet_name
        ]

    def filter_by_status(self, completed: bool) -> List[Task]:
        """Return tasks matching the requested completed status."""
        return [
            task
            for pet in self.owner.pets
            for task in pet.tasks
            if task.completed is completed
        ]

    def generate_schedule(self) -> None:
        """Collect incomplete tasks from the owner's pets for the current daily plan."""
        self.task_list = []
        for pet in self.owner.pets:
            for task in pet.tasks:
                if not task.completed:
                    self.task_list.append(task)
        # initialize daily_plan as a copy of collected tasks
        self.daily_plan = list(self.task_list)

    def sort_tasks(self) -> None:
        """Sort tasks by priority level for the active daily plan."""
        priority_order = {"high": 1, "medium": 2, "low": 3}

        def priority_key(task: Task) -> int:
            return priority_order.get(task.priority.lower(), 99)

        self.daily_plan = sorted(self.task_list, key=priority_key)

    def sort_by_time(self) -> None:
        """Sort the current daily plan by scheduled time in chronological order."""
        # Use a lambda so the sort order is based on each task's scheduled_time.
        # Tasks without a time are treated as empty strings and will appear first.
        self.daily_plan = sorted(
            self.daily_plan,
            key=lambda task: task.scheduled_time or "",
        )

    def detect_conflicts(self) -> List[str]:
        """Return warnings for tasks that share the same scheduled time."""
        warnings: List[str] = []

        try:
            for index, task in enumerate(self.daily_plan):
                if not task.scheduled_time:
                    continue

                for other_task in self.daily_plan[index + 1 :]:
                    if not other_task.scheduled_time:
                        continue

                    if task.scheduled_time == other_task.scheduled_time:
                        warning = (
                            f"Conflict: {task.task_name} and {other_task.task_name} "
                            f"both use {task.scheduled_time}."
                        )
                        warnings.append(warning)
        except Exception:
            return []

        return warnings

    def display_schedule(self) -> None:
        """Print the daily plan in a readable format."""
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
