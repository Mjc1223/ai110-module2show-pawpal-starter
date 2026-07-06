import streamlit as st

from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Jordan", available_time=180, preferences="General pet care")

owner = st.session_state.owner

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value=owner.name)
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

if st.button("Add pet"):
    if pet_name.strip():
        owner.name = owner_name or owner.name
        pet = Pet(name=pet_name, breed=species, age=0, special_needs="")
        owner.add_pet(pet)
        st.success(f"Added {pet.name} to {owner.name}'s pet list.")
    else:
        st.warning("Please enter a pet name before adding a pet.")

if owner.pets:
    st.write("Current pets:")
    st.table(
        [
            {
                "name": pet.name,
                "breed": pet.breed,
                "age": pet.age,
                "special_needs": pet.special_needs,
            }
            for pet in owner.pets
        ]
    )
else:
    st.info("No pets yet. Add one above.")

st.markdown("### Tasks")
st.caption("Add a few tasks. These will be attached to the selected pet and used by the scheduler.")

pet_names = [pet.name for pet in owner.pets]
selected_pet_name = st.selectbox("Select pet", pet_names) if pet_names else None

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if st.button("Add task"):
    if not pet_names:
        st.warning("Please add a pet first.")
    else:
        selected_pet = next(pet for pet in owner.pets if pet.name == selected_pet_name)
        task = Task(task_name=task_title, duration=int(duration), priority=priority)
        selected_pet.add_task(task)
        st.success(f"Added task to {selected_pet.name}.")

if owner.pets:
    st.write("Current tasks by pet:")
    for pet in owner.pets:
        if pet.tasks:
            st.write(f"**{pet.name}**")
            st.table(
                [
                    {
                        "task": task.task_name,
                        "duration": task.duration,
                        "priority": task.priority,
                        "completed": task.completed,
                    }
                    for task in pet.tasks
                ]
            )
        else:
            st.caption(f"{pet.name} has no tasks yet.")
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.divider()

st.subheader("Build Schedule")
st.caption("This button now uses your backend scheduler to display a day plan.")

if st.button("Generate schedule"):
    scheduler = Scheduler(owner=owner)
    scheduler.generate_schedule()
    scheduler.sort_tasks()

    if not scheduler.daily_plan:
        st.info("No tasks scheduled for today.")
    else:
        schedule_rows = [
            {
                "task": task.task_name,
                "priority": task.priority,
                "duration": f"{task.duration}m",
                "pet": next(
                    (pet.name for pet in owner.pets if task in pet.tasks),
                    "Unknown",
                ),
            }
            for task in scheduler.daily_plan
        ]
        st.write("Scheduled tasks:")
        st.table(schedule_rows)
