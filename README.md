# AI Task Dependency Planner

**What if your to-do list knew what order to do itself?**

That's exactly what this does. The AI Task Dependency Planner takes your messy, tangled web of tasks and dependencies — throws Discrete Mathematics at it — and spits out a clean, validated, visually stunning execution plan. No more "wait, does B come before C or after?" ever again.

---

## The Problem It Solves

You're managing a project. Task B needs Task A done first. Task D needs both B and C. Task E needs D. And someone just added a dependency that accidentally loops back to A.

**Congratulations, you've just broken your entire schedule.**

This planner catches that. Models it as a **Directed Acyclic Graph**, runs **Topological Sort**, detects **cycles before they wreck you**, and shows you exactly what to do — and in what order.

---

## Features That Hit Different

| Feature | What It Does |
|---|---|
| ➕ **Dynamic Task Builder** | Add tasks on the fly — no restarts, no config files |
| 🔗 **Dependency Wiring** | Link Task A → Task B with a single action |
| 📊 **Topological Sort Engine** | Generates a mathematically guaranteed execution order |
| 🚨 **Cycle Detector** | Catches circular dependencies and refuses to let them slide |
| 📈 **Live Graph Visualization** | Renders your entire task flow as a beautiful directed graph |
| 🟢 **Real-Time DAG Status** | Always know if your graph is valid or broken |
| 🌗 **Dark / Light Mode** | Because late-night debugging deserves good aesthetics |

---

## The Math Behind the Magic

This isn't just a pretty UI — it's **Discrete Mathematics in action**:

```
Your Tasks          →    Set Theory         (tasks as a defined set of nodes)
Your Dependencies   →    Binary Relations   (A depends on B = directed edge A→B)
The Whole Picture   →    Directed Graph     (a complete model of your workflow)
Is It Valid?        →    DAG Validation     (no cycles = schedulable!)
Execution Order     →    Topological Sort   (Kahn's Algorithm / DFS)
Broken Dependency   →    Cycle Detection    (caught before it causes chaos)
```

Every button click in this app is a graph algorithm running under the hood. 🤯

---

## How It Works ⚙️

```
   You define tasks & dependencies
              ↓
     Graph is constructed
    (nodes = tasks, edges = deps)
              ↓
       DAG check runs...
         ↙         ↘
       YES        NO — Cycle Found!
        ↓                   ↓
  Topological Sort     Execution halts.
     produces a         User notified.
   valid step order     Fix the loop!
        ↓
  Execution plan
    displayed 
```

Simple rule: **no cycle = plan generated. cycle = hard stop.** The math doesn't negotiate.

---

## The UI at a Glance 🖥️

```
┌──────────────┬───────────────────────────────────────┐
│   Sidebar    │            Main Panel                 │
│              │                                       │
│  ⚡ Load     │   ┌─ Add Task ──┐  ┌─ Add Dep ──┐   │
│     Sample   │   │  Task name  │  │  A  →  B   │   │
│              │   └─────────────┘  └────────────┘   │
│  📊 Generate │                                       │
│     Plan     │   📋 Planner Output                   │
│              │   ──────────────────────────────      │
│  📈 Visualize│   Step 1 → Task A                     │
│     Graph    │   Step 2 → Task C                     │
│              │   Step 3 → Task B                     │
│  🗑️ Clear All│                                       │
│              │   🟢 Status: Valid DAG                │
└──────────────┴───────────────────────────────────────┘
```

---

## Get It Running 

```bash
# 1. Grab the repo
git clone https://github.com/your-username/ai-task-dependency-planner.git
cd ai-task-dependency-planner

# 2. Install what you need
pip install -r requirements.txt

# 3. Launch it
python main.py
```

That's it. Three commands.

---

## Try This First 

Once it's open:

1. Hit **Load Sample Data** — instant pre-built graph, no setup needed
2. Click **Visualize Graph** — see your tasks as a live directed graph
3. Click **Generate Plan** — get your topological execution order
4. Manually add a dependency that creates a loop — watch it get caught in real time

---

## Tech Stack 

| Tool | Why It's Here |
|---|---|
| **Python** | The brain |
| **CustomTkinter** | A GUI that doesn't look like it's from 2003 |
| **NetworkX** | Handles all the heavy graph math |
| **Matplotlib** | Makes the graph actually look good |

---

## Requirements

```
customtkinter
networkx
matplotlib
```

---
