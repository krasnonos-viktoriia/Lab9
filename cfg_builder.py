import sys
import networkx as nx
import matplotlib.pyplot as plt


# =========================
# TASK 1: process_data()
# =========================
def build_cfg_task1():
    graph = nx.DiGraph()

    # CFG nodes
    graph.add_node("Start")
    graph.add_node("total = 0")
    graph.add_node("for i in range(len(data))")
    graph.add_node("if data[i] < 0")
    graph.add_node("continue")
    graph.add_node("for j in range(data[i])")
    graph.add_node("if j % 2 == 0")
    graph.add_node("total += j")
    graph.add_node("return total")
    graph.add_node("End")

    # CFG edges
    graph.add_edge("Start", "total = 0")
    graph.add_edge("total = 0", "for i in range(len(data))")

    graph.add_edge(
        "for i in range(len(data))",
        "if data[i] < 0",
        label="True"
    )

    graph.add_edge(
        "for i in range(len(data))",
        "return total",
        label="False"
    )

    graph.add_edge(
        "if data[i] < 0",
        "continue",
        label="True"
    )

    graph.add_edge(
        "if data[i] < 0",
        "for j in range(data[i])",
        label="False"
    )

    graph.add_edge(
        "continue",
        "for i in range(len(data))"
    )

    graph.add_edge(
        "for j in range(data[i])",
        "if j % 2 == 0",
        label="True"
    )

    graph.add_edge(
        "for j in range(data[i])",
        "for i in range(len(data))",
        label="False"
    )

    graph.add_edge(
        "if j % 2 == 0",
        "total += j",
        label="True"
    )

    graph.add_edge(
        "if j % 2 == 0",
        "for j in range(data[i])",
        label="False"
    )

    graph.add_edge(
        "total += j",
        "for j in range(data[i])"
    )

    graph.add_edge("return total", "End")

    return graph


def draw_cfg_task1(graph):
    position = nx.spring_layout(
        graph,
        seed=7,
        k=0.7,
        scale=2.2
    )

    # Manual adjustment of node positions
    position["End"] = position["End"] * 0.80
    position["return total"] = position["return total"] * 1.20

    plt.figure(figsize=(18, 11))

    nx.draw(
        graph,
        position,
        with_labels=True,
        node_size=6500,
        font_size=11,
        arrows=True,
        arrowsize=26,
        width=1.8
    )

    edge_labels = nx.get_edge_attributes(graph, "label")

    custom_edge = ("for j in range(data[i])", "for i in range(len(data))")
    edge_labels_without_custom = edge_labels.copy()

    if custom_edge in edge_labels_without_custom:
        del edge_labels_without_custom[custom_edge]

    nx.draw_networkx_edge_labels(
        graph,
        position,
        edge_labels=edge_labels_without_custom,
        font_size=11,
        bbox=dict(facecolor="white", edgecolor="none", alpha=0.8)
    )

    x1, y1 = position["for j in range(data[i])"]
    x2, y2 = position["for i in range(len(data))"]

    manual_x = (x1 + x2) / 2 - 0.25
    manual_y = (y1 + y2) / 2 + 0.30

    plt.text(
        manual_x,
        manual_y,
        "False",
        fontsize=11,
        bbox=dict(facecolor="white", edgecolor="none", alpha=0.8)
    )

    plt.title("CFG for process_data()", fontsize=18)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("cfg_process_data.png", dpi=300)
    plt.show()

    print("CFG for Task 1 saved as cfg_process_data.png")


def print_routes_task1(graph):
    routes = list(nx.all_simple_paths(graph, source="Start", target="End"))

    print("CFG routes for Task 1:")
    for index, route in enumerate(routes, start=1):
        print(f"Route {index}:")
        print(" -> ".join(route))
        print()


# =========================
# TASK 2: process_matrix()
# =========================
def build_cfg_task2():
    graph = nx.DiGraph()

    # CFG nodes
    graph.add_node("Start")
    graph.add_node("count = 0")
    graph.add_node("for i in range(len(matrix))")
    graph.add_node("for j in range(len(matrix[i]))")
    graph.add_node("if matrix[i][j] > 0")
    graph.add_node("for k in range(matrix[i][j])")
    graph.add_node("count += k % 3")
    graph.add_node("return count")
    graph.add_node("End")

    # CFG edges
    graph.add_edge("Start", "count = 0")

    graph.add_edge(
        "count = 0",
        "for i in range(len(matrix))"
    )

    graph.add_edge(
        "for i in range(len(matrix))",
        "for j in range(len(matrix[i]))",
        label="True"
    )

    graph.add_edge(
        "for i in range(len(matrix))",
        "return count",
        label="False"
    )

    graph.add_edge(
        "for j in range(len(matrix[i]))",
        "if matrix[i][j] > 0",
        label="True"
    )

    graph.add_edge(
        "for j in range(len(matrix[i]))",
        "for i in range(len(matrix))",
        label="False"
    )

    graph.add_edge(
        "if matrix[i][j] > 0",
        "for k in range(matrix[i][j])",
        label="True"
    )

    graph.add_edge(
        "if matrix[i][j] > 0",
        "for j in range(len(matrix[i]))",
        label="False"
    )

    graph.add_edge(
        "for k in range(matrix[i][j])",
        "count += k % 3",
        label="True"
    )

    graph.add_edge(
        "for k in range(matrix[i][j])",
        "for j in range(len(matrix[i]))",
        label="False"
    )

    graph.add_edge(
        "count += k % 3",
        "for k in range(matrix[i][j])"
    )

    graph.add_edge("return count", "End")

    return graph


def draw_cfg_task2(graph):
    position = {
        "Start": (0, 8),
        "count = 0": (2, 6),
        "for i in range(len(matrix))": (0, 4),
        "for j in range(len(matrix[i]))": (5, 4),
        "if matrix[i][j] > 0": (9, 4),
        "for k in range(matrix[i][j])": (9, 0),
        "count += k % 3": (9, -4),
        "return count": (-5, 4),
        "End": (-7, 1)
    }

    plt.figure(figsize=(22, 14))

    nx.draw(
        graph,
        position,
        with_labels=True,
        node_size=8500,
        font_size=9,
        arrows=True,
        arrowsize=24,
        width=1.8
    )

    edge_labels = nx.get_edge_attributes(graph, "label")

    nx.draw_networkx_edge_labels(
        graph,
        position,
        edge_labels=edge_labels,
        font_size=10,
        bbox=dict(
            facecolor="white",
            edgecolor="none",
            alpha=0.8
        )
    )

    plt.title(
        "CFG for process_matrix()",
        fontsize=18
    )

    plt.axis("off")
    plt.tight_layout()
    plt.savefig("cfg_process_matrix.png", dpi=300)
    plt.show()

    print("CFG for Task 2 saved as cfg_process_matrix.png")


def print_routes_task2():
    print("Basic independent routes for Task 2:\n")

    routes = [
        [
            "Start",
            "count = 0",
            "for i in range(len(matrix))",
            "return count",
            "End"
        ],
        [
            "Start",
            "count = 0",
            "for i in range(len(matrix))",
            "for j in range(len(matrix[i]))",
            "for i in range(len(matrix))",
            "return count",
            "End"
        ],
        [
            "Start",
            "count = 0",
            "for i in range(len(matrix))",
            "for j in range(len(matrix[i]))",
            "if matrix[i][j] > 0",
            "for j in range(len(matrix[i]))",
            "for i in range(len(matrix))",
            "return count",
            "End"
        ],
        [
            "Start",
            "count = 0",
            "for i in range(len(matrix))",
            "for j in range(len(matrix[i]))",
            "if matrix[i][j] > 0",
            "for k in range(matrix[i][j])",
            "count += k % 3",
            "for k in range(matrix[i][j])",
            "for j in range(len(matrix[i]))",
            "for i in range(len(matrix))",
            "return count",
            "End"
        ]
    ]

    for index, route in enumerate(routes, start=1):
        print(f"Route {index}:")
        print(" -> ".join(route))
        print()


# =========================
# TASK 5: update_task_status()
# =========================
def build_cfg_task5():
    graph = nx.DiGraph()

    # CFG nodes
    graph.add_node("Start")
    graph.add_node("valid_transitions = {...}")
    graph.add_node('if task["status"] == new_status')
    graph.add_node('return "No change"')
    graph.add_node('if new_status not in valid_transitions.get(...)')
    graph.add_node('return "Invalid transition"')
    graph.add_node('if user_role not in ["admin", "manager"]\nand new_status == "closed"')
    graph.add_node('return "Permission denied"')
    graph.add_node('task["status"] = new_status')
    graph.add_node('return "Updated"')
    graph.add_node("End")

    # CFG edges
    graph.add_edge("Start", "valid_transitions = {...}")

    graph.add_edge(
        "valid_transitions = {...}",
        'if task["status"] == new_status'
    )

    graph.add_edge(
        'if task["status"] == new_status',
        'return "No change"',
        label="True"
    )

    graph.add_edge(
        'if task["status"] == new_status',
        'if new_status not in valid_transitions.get(...)',
        label="False"
    )

    graph.add_edge(
        'return "No change"',
        "End"
    )

    graph.add_edge(
        'if new_status not in valid_transitions.get(...)',
        'return "Invalid transition"',
        label="True"
    )

    graph.add_edge(
        'if new_status not in valid_transitions.get(...)',
        'if user_role not in ["admin", "manager"]\nand new_status == "closed"',
        label="False"
    )

    graph.add_edge(
        'return "Invalid transition"',
        "End"
    )

    graph.add_edge(
        'if user_role not in ["admin", "manager"]\nand new_status == "closed"',
        'return "Permission denied"',
        label="True"
    )

    graph.add_edge(
        'if user_role not in ["admin", "manager"]\nand new_status == "closed"',
        'task["status"] = new_status',
        label="False"
    )

    graph.add_edge(
        'return "Permission denied"',
        "End"
    )

    graph.add_edge(
        'task["status"] = new_status',
        'return "Updated"'
    )

    graph.add_edge(
        'return "Updated"',
        "End"
    )

    return graph


def draw_cfg_task5(graph):
    # Manual positions for clear layout
    position = {
        "Start": (0, 10),
        "valid_transitions = {...}": (0, 8),

        'if task["status"] == new_status': (0, 6),
        'return "No change"': (7.5, 6),

        'if new_status not in valid_transitions.get(...)': (0, 4),
        'return "Invalid transition"': (7.5, 4),

        'if user_role not in ["admin", "manager"]\nand new_status == "closed"': (0, 2),
        'return "Permission denied"': (7.5, 2),

        'task["status"] = new_status': (0, 0),
        'return "Updated"': (7.5, 0),

        "End": (12, 3)
    }

    plt.figure(figsize=(22, 13))

    nx.draw(
        graph,
        position,
        with_labels=True,
        node_size=4200,
        font_size=8,
        arrows=True,
        arrowsize=22,
        width=1.5
    )

    edge_labels = nx.get_edge_attributes(graph, "label")

    nx.draw_networkx_edge_labels(
        graph,
        position,
        edge_labels=edge_labels,
        font_size=9,
        bbox=dict(
            facecolor="white",
            edgecolor="none",
            alpha=0.9
        )
    )

    plt.title(
        "CFG for update_task_status()",
        fontsize=18
    )

    plt.axis("off")
    plt.tight_layout()
    plt.savefig("cfg_update_task_status.png", dpi=300)
    plt.show()

    print("CFG for Task 5 saved as cfg_update_task_status.png")


def print_routes_task5():
    print("Basic independent routes for Task 5:\n")

    routes = [
        [
            "Start",
            "valid_transitions = {...}",
            'if task["status"] == new_status',
            'return "No change"',
            "End"
        ],
        [
            "Start",
            "valid_transitions = {...}",
            'if task["status"] == new_status',
            'if new_status not in valid_transitions.get(...)',
            'return "Invalid transition"',
            "End"
        ],
        [
            "Start",
            "valid_transitions = {...}",
            'if task["status"] == new_status',
            'if new_status not in valid_transitions.get(...)',
            'if user_role not in ["admin", "manager"] and new_status == "closed"',
            'return "Permission denied"',
            "End"
        ],
        [
            "Start",
            "valid_transitions = {...}",
            'if task["status"] == new_status',
            'if new_status not in valid_transitions.get(...)',
            'if user_role not in ["admin", "manager"] and new_status == "closed"',
            'task["status"] = new_status',
            'return "Updated"',
            "End"
        ]
    ]

    for index, route in enumerate(routes, start=1):
        print(f"Route {index}:")
        print(" -> ".join(route))
        print()


# =========================
# MAIN
# =========================
def print_help():
    print("Usage:")
    print("python cfg_builder.py 1   -> Task 1: process_data()")
    print("python cfg_builder.py 2   -> Task 2: process_matrix()")
    print("python cfg_builder.py 5   -> Task 5: update_task_status()")
    print()
    print("For each task:")
    print("- CFG diagram will be built")
    print("- routes will be printed")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()

    elif sys.argv[1] == "1":
        cfg = build_cfg_task1()
        draw_cfg_task1(cfg)
        print_routes_task1(cfg)

    elif sys.argv[1] == "2":
        cfg = build_cfg_task2()
        draw_cfg_task2(cfg)
        print_routes_task2()

    elif sys.argv[1] == "5":
        cfg = build_cfg_task5()
        draw_cfg_task5(cfg)
        print_routes_task5()

    else:
        print("Unknown task number.")
        print_help()