from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    task_name: str
    duration: int
    priority: str
    completed: bool = False

    def mark_complete(self) -> None:
        pass

    def edit_task(self) -> None:
        pass


@dataclass
class Pet:
    name: str
    breed: str
    age: int
    special_needs: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        pass

    def update_info(self) -> None:
        pass


@dataclass
class Owner:
    name: str
    available_time: int
    preferences: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        pass

    def update_preferences(self, preferences: str) -> None:
        pass

    def view_schedule(self) -> None:
        pass


class Scheduler:
    def __init__(self) -> None:
        self.task_list: List[Task] = []
        self.daily_plan: List[Task] = []

    def generate_schedule(self) -> None:
        pass

    def sort_tasks(self) -> None:
        pass

    def display_schedule(self) -> None:
        pass
