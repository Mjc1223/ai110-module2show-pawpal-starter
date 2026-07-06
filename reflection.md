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

For conflict detection, I chose to check whether tasks have the exact same scheduled time instead of checking whether their durations overlap. This approach keeps the algorithm simple, easy to understand, and efficient for this project. While it may miss more complex scheduling conflicts, it is sufficient for a lightweight scheduler and is easier to maintain and explain.
---

## 3. AI Collaboration

**a. How you used AI**

I used AI throughout the project to help me move from one phase to the next. In our conversations, AI helped me brainstorm the UML structure, generate the Mermaid class diagram, create the initial Python dataclass skeleton in pawpal_system.py, implement the core methods, build a simple demo script in main.py, create pytest tests, and connect the Streamlit app in app.py to the backend classes. It was also helpful when I needed support debugging small issues, refining the scheduler logic, and thinking through how recurring tasks and conflicts should behave. The most useful prompts were the ones that asked for small, targeted help such as how to structure the classes, how to fill in method stubs, and how to make sure the UI and backend worked together without changing the existing design.

**b. Judgment and verification**

I did not accept AI suggestions automatically. I used judgment by checking every suggestion against the project requirements, the existing class structure, and the behavior I wanted to preserve. For example, I kept the same class names, method names, and dataclass design while only adding the logic needed for each method. I also verified the results by running the demo script, running pytest, and checking that the app modules compiled successfully. When a suggestion felt too complicated or changed the design more than necessary, I simplified it or rejected it. That helped me confirm that the AI-generated help was actually useful rather than just plausible.

---

## 4. Testing and Verification

**a. What you tested**

I tested the core behaviors that matter most for the current implementation. That included verifying that a new Task starts as incomplete and becomes complete after mark_complete(), confirming that adding a Task to a Pet increases the pet's task list size, running the demo script to create an owner, pets, tasks, and a schedule, and checking that the Streamlit app and backend modules still compile correctly. I also tested the newer scheduling behaviors such as sorting tasks by scheduled time, creating recurring daily and weekly tasks, and detecting conflicts when two tasks share the same scheduled time. These tests were important because they confirmed that the basic data model and scheduling flow worked end to end.

**b. Confidence**

I am confident that the current backend and demo flow work because they passed the pytest tests and the demo script executed successfully. I also verified that the app could import and compile after connecting the UI to the backend classes. The fact that the scheduler features behaved correctly in the demo run gave me extra confidence that the implementation was not only syntactically correct but also functionally useful. If I had more time, I would test additional edge cases such as empty pet lists, empty task lists, updating pet information, and editing tasks after they had already been created.

---

## 5. Reflection

**a. What went well**

The strongest part of this project was turning an initial design idea into a working system that connected the backend classes, a demo script, tests, and a simple Streamlit interface. I am especially proud that the scheduler became more useful over time by supporting task sorting, recurring tasks, and conflict detection in a way that still stayed organized and understandable.

**b. What you would improve**

If I had another iteration, I would improve the scheduler so it handles more realistic constraints, such as time windows, task order, and owner availability in a more detailed way. I would also make the interface more polished and user-friendly so the schedule is easier for a real pet owner to understand and act on.

**c. Key takeaway**

The biggest lesson from this project is that good software design comes from combining clear structure with careful testing and thoughtful decision-making. AI helped me move faster and think through problems more effectively, but the final quality of the system still depended on reviewing the suggestions, testing the behavior, and making sure the solution fit the original goals.
