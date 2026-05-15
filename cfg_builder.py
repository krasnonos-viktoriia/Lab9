import sys
import ast
import networkx as nx
import matplotlib.pyplot as plt


# =========================
# DOT EXPORT WITHOUT PYDOT
# =========================
def save_dot_file(graph, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("digraph CFG {\n")
        file.write('    rankdir=TB;\n')
        file.write('    node [shape=ellipse, style=filled, fillcolor=lightblue];\n')

        for node, data in graph.nodes(data=True):
            label = data.get("label", node)
            label = label.replace('"', '\\"')
            label = label.replace("\n", "\\n")
            file.write(f'    {node} [label="{label}"];\n')

        for source, target in graph.edges():
            file.write(f"    {source} -> {target};\n")

        file.write("}\n")


# =========================
# AST ANALYSIS FOR AUTH.PY
# =========================
def analyze_python_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        code = file.read()

    tree = ast.parse(code)

    # Беремо першу функцію з файлу
    func = tree.body[0]

    graph = nx.DiGraph()

    previous_nodes = []
    counter = 0

    print("\nAST statements:\n")

    for statement in func.body:
        label = ast.unparse(statement)

        print(label)

        node = f"n{counter}"
        graph.add_node(node, label=label)

        for previous in previous_nodes:
            graph.add_edge(previous, node)

        previous_nodes = [node]
        counter += 1

    paths = list(
        nx.all_simple_paths(
            graph,
            source="n0",
            target=previous_nodes[0]
        )
    )

    print("\nExecution paths (AST):")
    for path in paths:
        print(path)

    save_dot_file(graph, "cfg_ast.dot")

    complexity = graph.number_of_edges() - graph.number_of_nodes() + 2

    print("\nCyclomatic complexity:", complexity)
    print("\nDOT file saved as cfg_ast.dot")


# =========================
# TASK 6: authenticate_user()
# =========================
def build_cfg_task6():
    graph = nx.DiGraph()

    # CFG nodes
    graph.add_node("Start")
    graph.add_node("if not username or not password")
    graph.add_node('return "Missing credentials"')
    graph.add_node("if username not in db")
    graph.add_node('return "User not found"')
    graph.add_node('attempts = db[username].get("attempts", 0)')
    graph.add_node("if attempts >= 3")
    graph.add_node('return "Account locked"')
    graph.add_node('if db[username]["password"] != password')
    graph.add_node('db[username]["attempts"] = attempts + 1')
    graph.add_node('return "Invalid password"')
    graph.add_node('db[username]["attempts"] = 0')
    graph.add_node('return "Authenticated"')
    graph.add_node("End")

    # CFG edges
    graph.add_edge(
        "Start",
        "if not username or not password"
    )

    graph.add_edge(
        "if not username or not password",
        'return "Missing credentials"',
        label="True"
    )

    graph.add_edge(
        "if not username or not password",
        "if username not in db",
        label="False"
    )

    graph.add_edge(
        'return "Missing credentials"',
        "End"
    )

    graph.add_edge(
        "if username not in db",
        'return "User not found"',
        label="True"
    )

    graph.add_edge(
        "if username not in db",
        'attempts = db[username].get("attempts", 0)',
        label="False"
    )

    graph.add_edge(
        'return "User not found"',
        "End"
    )

    graph.add_edge(
        'attempts = db[username].get("attempts", 0)',
        "if attempts >= 3"
    )

    graph.add_edge(
        "if attempts >= 3",
        'return "Account locked"',
        label="True"
    )

    graph.add_edge(
        "if attempts >= 3",
        'if db[username]["password"] != password',
        label="False"
    )

    graph.add_edge(
        'return "Account locked"',
        "End"
    )

    graph.add_edge(
        'if db[username]["password"] != password',
        'db[username]["attempts"] = attempts + 1',
        label="True"
    )

    graph.add_edge(
        'db[username]["attempts"] = attempts + 1',
        'return "Invalid password"'
    )

    graph.add_edge(
        'return "Invalid password"',
        "End"
    )

    graph.add_edge(
        'if db[username]["password"] != password',
        'db[username]["attempts"] = 0',
        label="False"
    )

    graph.add_edge(
        'db[username]["attempts"] = 0',
        'return "Authenticated"'
    )

    graph.add_edge(
        'return "Authenticated"',
        "End"
    )

    return graph


def draw_cfg_task6(graph):
    position = {
        "Start": (0, 10),

        "if not username or not password": (0, 8),
        'return "Missing credentials"': (8, 8),

        "if username not in db": (0, 6),
        'return "User not found"': (8, 6),

        'attempts = db[username].get("attempts", 0)': (0, 4),

        "if attempts >= 3": (0, 2),
        'return "Account locked"': (8, 2),

        'if db[username]["password"] != password': (0, 0),

        'db[username]["attempts"] = attempts + 1': (4, -2),
        'return "Invalid password"': (8, -2),

        'db[username]["attempts"] = 0': (-4, -2),
        'return "Authenticated"': (-8, -2),

        "End": (12, 3)
    }

    plt.figure(figsize=(26, 16))

    nx.draw(
        graph,
        position,
        with_labels=True,
        node_size=2800,
        font_size=7,
        arrows=True,
        arrowsize=24,
        width=1.7
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

    plt.title("CFG for authenticate_user()", fontsize=18)
    plt.axis("off")
    plt.tight_layout()

    plt.savefig("cfg_authenticate_user.png", dpi=300)
    plt.show()

    print("CFG saved as cfg_authenticate_user.png")


def print_routes_task6():
    print("\nBasic execution paths for authenticate_user():\n")

    routes = [
        [
            "Start",
            "if not username or not password",
            'return "Missing credentials"',
            "End"
        ],
        [
            "Start",
            "if not username or not password",
            "if username not in db",
            'return "User not found"',
            "End"
        ],
        [
            "Start",
            "if not username or not password",
            "if username not in db",
            'attempts = db[username].get("attempts", 0)',
            "if attempts >= 3",
            'return "Account locked"',
            "End"
        ],
        [
            "Start",
            "if not username or not password",
            "if username not in db",
            'attempts = db[username].get("attempts", 0)',
            "if attempts >= 3",
            'if db[username]["password"] != password',
            'db[username]["attempts"] = attempts + 1',
            'return "Invalid password"',
            "End"
        ],
        [
            "Start",
            "if not username or not password",
            "if username not in db",
            'attempts = db[username].get("attempts", 0)',
            "if attempts >= 3",
            'if db[username]["password"] != password',
            'db[username]["attempts"] = 0',
            'return "Authenticated"',
            "End"
        ]
    ]

    for index, route in enumerate(routes, start=1):
        print(f"Path {index}:")
        print(" -> ".join(route))
        print()


def calculate_cyclomatic_complexity_task6():
    predicate_nodes = 4
    complexity = predicate_nodes + 1

    print("Cyclomatic complexity calculation:")
    print("V(G) = P + 1")
    print(f"P = {predicate_nodes}")
    print(f"V(G) = {predicate_nodes} + 1 = {complexity}")


# =========================
# MAIN
# =========================
def print_help():
    print("Usage:")
    print("python cfg_builder.py 6")
    print("python cfg_builder.py ast <file.py>")
    print()
    print("Examples:")
    print("python cfg_builder.py 6")
    print("python cfg_builder.py ast src/auth.py")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()

    elif sys.argv[1] == "6":
        cfg = build_cfg_task6()
        draw_cfg_task6(cfg)
        print_routes_task6()
        calculate_cyclomatic_complexity_task6()

    elif sys.argv[1] == "ast":
        if len(sys.argv) < 3:
            print("Specify Python file.")
        else:
            analyze_python_file(sys.argv[2])

    else:
        print("Unknown command.")
        print_help()