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

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
# Paste your pytest output here
```

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | | e.g., by priority, duration |
| Filtering | | e.g., skip tasks if time runs out |
| Conflict handling | | e.g., overlapping time slots |
| Recurring tasks | | e.g., daily vs. weekly |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->

## Smarter Scheduling

### Sorting
Scheduler.sort_by_time() sorts tasks by scheduled time in chronological order.

### Filtering
The scheduler collects only incomplete tasks from the owner's pets, so completed tasks are filtered out of the active daily plan.

### Conflict Detection
The scheduler checks tasks in the daily plan for matching scheduled_time values and prints a warning instead of crashing.

### Recurring Tasks
Completing a daily or weekly recurring task automatically creates the next occurrence using Python's timedelta.

# Testing PawPal+

## Running the Tests

The test suite can be run with:

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
