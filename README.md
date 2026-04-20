# AI Task Dependency Planner

**What if your to-do list knew what order to do itself?**

That's exactly what this does. The AI Task Dependency Planner takes your messy, tangled web of tasks and dependencies — throws Discrete Mathematics at it — and spits out a clean, validated, visually stunning execution plan. No more "wait, does B come before C or after?" ever again.

---

## The Problem It Solves

You're managing a project. Task B needs Task A done first. Task D needs both B and C. Task E needs D. And someone just added a dependency that accidentally loops back to A.

**Congratulations, you've just broken your entire schedule.**

This planner catches that. Models it as a **Directed Acyclic Graph**, runs **Topological Sort**, detects **cycles before they wreck you**, and shows you exactly what to do — and in what order.

---

## Features

| Feature | What It Does |
|---|---|
| ➕ **Dynamic Task Builder** | Add tasks on the fly — auto-adds tasks from dependency inputs too |
| 🔗 **Dependency Wiring** | Link Task A → Task B ("A must be completed before B") |
| 📊 **Topological Sort Engine** | Generates a mathematically guaranteed execution order using Kahn's Algorithm |
| 🚨 **Cycle Detector** | Catches circular dependencies using DFS and traces the exact cycle path |
| 📈 **Live Graph Visualization** | Renders your task flow as a directed graph — layered layout for valid DAGs, circular layout when cycles exist |
| 🟢 **Real-Time DAG Status** | Tracks task count, dependency count, and graph validity at a glance |
| 🌗 **Dark / Light Mode** | Because late-night debugging deserves good aesthetics |
| ⌨️ **Keyboard Shortcuts** | Press Enter in any input field to add tasks or dependencies instantly |

---

## The Math Behind the Magic

This isn't just a pretty UI — it's **Discrete Mathematics in action**:

```
Your Tasks          →    Set Theory         (tasks as a defined set of nodes)
Your Dependencies   →    Binary Relations   (A depends on B = directed edge A→B)
The Whole Picture   →    Directed Graph     (a complete model of your workflow)
Is It Valid?        →    DAG Validation     (no cycles = schedulable!)
Execution Order     →    Topological Sort   (Kahn's Algorithm with BFS)
Broken Dependency   →    Cycle Detection    (DFS with call-stack tracking)
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
     produces a         Cycle path shown.
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
│     Plan     │   📋 Planner Output  📋 Task List     │
│              │   ──────────────────────────────      │
│  📈 Visualize│   Step 1 → Task A                     │
│     Graph    │   Step 2 → Task C    Dependency List  │
│              │   Step 3 → Task B    ──────────────   │
│  🗑️ Clear All│                                       │
│              │   📈 Graph Visualization              │
│  🌗 Appearance│  ─────────────────────────────────   │
│     Mode     │   [Directed Graph Rendered Here]      │
└──────────────┴───────────────────────────────────────┘
```

---

## Get It Running

This is a **single-file web app** — no build step, no server, no dependencies to install.

```bash
# 1. Grab the repo
git clone https://github.com/your-username/ai-task-dependency-planner.git
cd ai-task-dependency-planner

# 2. Open it
open index.html
```

That's it. One file. Opens in any browser.

---

## Try This First

Once it's open:

1. Hit **Load Sample Data** — loads a pre-built 6-task software project graph instantly
2. Click **Visualize Graph** — see your tasks rendered as a live layered directed graph
3. Click **Generate Plan** — get your topological execution order with full analysis
4. Manually add a dependency that creates a loop — watch the cycle get caught and traced in real time

### Sample Project Included

The built-in sample models a software project workflow:

```
Requirement Analysis → UI Design → Model Integration
Requirement Analysis → Backend Development → Model Integration
Model Integration → Testing → Deployment
```

---

## Dependency Rules

- `A → B` means **A must be completed before B**
- Tasks are auto-added if they appear in a dependency but haven't been added yet
- A task cannot depend on itself
- Duplicate dependencies are rejected
- All dependency pairs must be unique

---

## Execution Plan Output Format

```
================================================
TASK EXECUTION PLAN ANALYSIS
================================================
Status      : Valid dependency structure
Cycle Check : No cycle detected

Execution Order:
1. Requirement Analysis
2. Backend Development
3. UI Design
4. Model Integration
5. Testing
6. Deployment

Interpretation:
The task dependency system forms a DAG.
Therefore, a valid topological ordering exists.
```

If a cycle is detected, the exact cycle path is shown:

```
Cycle Path:
Task A → Task B → Task C → Task A

Please remove cyclic dependencies.
```

---

## Tech Stack

| Tool | Why It's Here |
|---|---|
| **HTML/CSS/JS** | Zero-dependency, runs in any browser |
| **Vanilla JavaScript** | All graph algorithms implemented from scratch — no libraries needed |
| **SVG** | Graph visualization rendered directly in the browser |
| **CSS Variables** | Clean dark/light mode theming |

---

## Graph Visualization

The graph renderer uses two layouts automatically:

- **Layered layout** (valid DAG) — nodes positioned by dependency level, left to right, making execution order visually obvious
- **Circular layout** (cycle detected) — nodes arranged in a circle to make cyclic relationships easy to spot

Edges are drawn as directed arrows (amber colored). Nodes are rendered as labeled circles. Long task names are truncated to keep the graph readable.

---
