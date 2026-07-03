# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design. 
- What classes did you include, and what responsibilities did you assign to each?

My initial UML design includes four classes: Owner, Pet, Task, and Scheduler.

The Owner class keeps track of the owner's information and preferences, including available time for pet care.

The Pet class contains details about the pet, such as name, breed, age, and special care needs.

The Task class defines care activities like feeding, walking, grooming, and medication, along with duration and priority.

The Scheduler class uses the owner's available time and the task list to organize a daily care plan based on priority and time constraints.

### Building Blocks

**Owner**
Attributes:
- name
- available_time
- preferences
- pets

Methods:
- add_pet()
- update_preferences()
- view_schedule()

**Pet**
Attributes:
- name
- breed
- age
- special_needs
- tasks

Methods:
- add_task()
- update_info()

**Task**
Attributes:
- task_name
- duration
- priority
- completed

Methods:
- mark_complete()
- edit_task()

**Scheduler**
Attributes:
- task_list
- daily_plan

Methods:
- generate_schedule()
- sort_tasks()
- display_schedule()

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

My design changed slightly during implementation. I updated the relationship between the Owner and Scheduler classes to show that the Owner uses the Scheduler to create a plan, while the Scheduler reads the Owner’s available time as a constraint for scheduling. This made the system flow and data dependency clearer.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

The scheduler considers the owner's available time, the priority level of each task, and the duration of each task. Higher priority tasks, such as feeding or medication, are scheduled first before lower priority tasks like grooming or playtime.

I decided that priority and available time mattered the most because essential pet care needs should always be completed first, while the schedule must still fit within the owner's time constraints.


**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

One tradeoff my scheduler makes is prioritizing important tasks over less urgent ones, which may cause some lower priority tasks to be left out if there is not enough time. This is reasonable because it ensures the pet's most important needs are handled first. 

Another tradeoff in my design is that the Scheduler acts as the central point for organizing all pet care tasks. This makes scheduling easier to manage in one place, but it could become overloaded if many pets and tasks are added. I chose this design because it keeps scheduling logic organized and makes it easier to sort tasks by priority and time.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
