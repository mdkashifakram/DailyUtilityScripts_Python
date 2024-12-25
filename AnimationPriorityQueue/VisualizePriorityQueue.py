import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import Counter, deque
from heapq import heappush, heappop
import heapq

# Extended Task Scheduler to log steps for visualization
def task_scheduler_with_steps(tasks, n):
    # Count task frequencies
    task_counts = Counter(tasks)
    max_heap = [-count for count in task_counts.values()]
    heapq.heapify(max_heap)
    
    cooldown_queue = deque()  # Tracks tasks in their cooldown period
    time = 0
    schedule = []  # Stores the task execution order
    
    # To store intermediate states for visualization
    states = []
    
    while max_heap or cooldown_queue:
        # Log current state
        states.append({
            "time": time,
            "max_heap": list(max_heap),
            "cooldown_queue": list(cooldown_queue),
            "schedule": schedule.copy()
        })
        
        # Step 1: Handle tasks ready from cooldown
        if cooldown_queue and cooldown_queue[0][1] == time:
            task_freq = cooldown_queue.popleft()[0]
            heappush(max_heap, task_freq)

        # Step 2: Schedule a task or idle
        if max_heap:
            task_freq = heappop(max_heap)
            schedule.append(-task_freq)
            if task_freq + 1 < 0:
                cooldown_queue.append((task_freq + 1, time + n + 1))
        else:
            schedule.append("Idle")
        
        time += 1
    
    # Log the final state
    states.append({
        "time": time,
        "max_heap": list(max_heap),
        "cooldown_queue": list(cooldown_queue),
        "schedule": schedule.copy()
    })
    
    return schedule, states


# Animation function
def animate_solution_with_details(tasks, n):
    schedule, states = task_scheduler_with_steps(tasks, n)
    
    fig, ax = plt.subplots(3, 1, figsize=(12, 8))
    ax_schedule, ax_heap, ax_cooldown = ax  # Divide axes for different visualizations
    
    def update(frame):
        ax_schedule.clear()
        ax_heap.clear()
        ax_cooldown.clear()
        
        # Get the current state
        state = states[frame]
        time = state["time"]
        max_heap = state["max_heap"]
        cooldown_queue = state["cooldown_queue"]
        current_schedule = state["schedule"]
        
        # --- Schedule Visualization ---
        ax_schedule.set_title(f"Time: {time} - Task Schedule")
        ax_schedule.bar(range(len(current_schedule)), [1] * len(current_schedule), color="green", alpha=0.7)
        for i, task in enumerate(current_schedule):
            ax_schedule.text(i, 0.5, str(task), ha="center", va="center", fontsize=10, color="white")
        ax_schedule.set_xlim(0, len(schedule))
        ax_schedule.set_ylim(0, 1.5)
        ax_schedule.set_yticks([])
        
        # --- Max Heap Visualization ---
        ax_heap.set_title("Max Heap (Tasks Available)")
        ax_heap.barh(range(len(max_heap)), [-freq for freq in max_heap], color="blue", alpha=0.7)
        for i, freq in enumerate(max_heap):
            ax_heap.text(-freq, i, str(-freq), ha="left", va="center", fontsize=10)
        ax_heap.set_xlim(0, max((-min(max_heap), 1)) + 1 if max_heap else 1)
        ax_heap.set_yticks(range(len(max_heap)))
        ax_heap.set_yticklabels([f"Task {chr(65 + i)}" for i in range(len(max_heap))])  # Assuming 'A' to 'Z'
        
        # --- Cooldown Queue Visualization ---
        ax_cooldown.set_title("Cooldown Queue (Tasks Cooling Down)")
        if cooldown_queue:
            tasks_in_cooldown = [(-freq, time) for freq, time in cooldown_queue]
            ax_cooldown.bar(range(len(tasks_in_cooldown)), [freq for freq, _ in tasks_in_cooldown], color="red", alpha=0.7)
            for i, (freq, ready_time) in enumerate(tasks_in_cooldown):
                ax_cooldown.text(i, freq + 0.1, f"Ready @ {ready_time}", ha="center", va="bottom", fontsize=8)
        ax_cooldown.set_xlim(0, len(cooldown_queue) + 1)
        ax_cooldown.set_ylim(0, max((-min(cooldown_queue)[0] if cooldown_queue else 1), 1) + 1)
        ax_cooldown.set_xticks(range(len(cooldown_queue)))
    
    ani = animation.FuncAnimation(fig, update, frames=len(states), repeat=False,interval=5000)
    plt.tight_layout()
    plt.show()


# Test Input
tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
animate_solution_with_details(tasks, n)
