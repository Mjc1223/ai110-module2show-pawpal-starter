# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

Daily Plan:
1. [Pending] Feed breakfast (Priority: high, Duration: 15m) - Pet: Milo)
2. [Pending] Give medication (Priority: high, Duration: 10m) - Pet: Luna)
3. [Pending] Morning walk (Priority: medium, Duration: 30m) - Pet: Milo)

```
# e.g.:
# Daily plan for Biscuit (Golden Retriever):
#   08:00 — Morning walk (30 min) [priority: high]
#   09:00 — Feeding (10 min) [priority: high]
#   ...
```

## Smarter Scheduling

| Feature | Method | Description |
|---------|--------|-------------|
| Task Sorting | Scheduler.sort_by_time() | Sorts the current daily plan by scheduled time in chronological order. |
| Pet Filtering | Scheduler.filter_by_pet_name() | Returns tasks that belong to a specific pet. |
| Status Filtering | Scheduler.filter_by_status() | Returns tasks that match a completed or pending status. |
| Conflict Detection | Scheduler.detect_conflicts() | Returns warning messages when multiple tasks share the same scheduled time. |
| Daily Recurrence | Task.mark_complete() | Creates the next daily task after a daily recurring task is completed. |
| Weekly Recurrence | Task.mark_complete() | Creates the next weekly task after a weekly recurring task is completed. |

## Demo Walkthrough

1. Launch the Streamlit application to open the PawPal+ interface.
2. Add owner information and create one or more pets.
3. Create care tasks for the selected pet, including priority, duration, and frequency.
4. Generate the schedule to view today's tasks in a clear table sorted by scheduled time.
5. Review warning messages if two tasks share the same scheduled time.
6. Mark a daily or weekly recurring task as complete to automatically create the next occurrence.

## Technologies Used

This project uses:

- Python
- Streamlit
- Pytest
- Dataclasses
- Git
- GitHub

# 🧪 Testing PawPal+

## Running the Tests

The test suite can be run with:

```bash
# Run with coverage:
pytest --cov
```

```bash
python -m pytest
```

## What the Tests Cover

The automated tests verify that the scheduler:

- Sorts tasks by scheduled time
- Filters tasks by pet name
- Filters tasks by completion status
- Detects conflicts when two tasks share the same scheduled time
- Creates the next daily recurring task
- Creates the next weekly recurring task

## Successful Test Run

```text
============================= test session starts ==============================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\calho\Documents\ai110-module2show-pawpal-starter
plugins: anyio-4.14.1
collected 8 items                                                               

tests\test_pawpal.py ........                                            [100%]

============================== 8 passed in 0.15s ==============================
```

## Confidence Level

Confidence: ⭐⭐⭐⭐⭐ (5/5)

Reason:
All implemented features passed automated tests, including sorting, filtering, conflict detection, and recurring task generation. While additional edge-case testing could always be added in the future, the current implementation behaves correctly for the required project functionality.
