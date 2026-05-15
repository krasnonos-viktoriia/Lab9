from itertools import product


def expected_result(username, password):
    if not username or not password:
        return "Missing credentials"
    return "Authenticated"


def generate_console_table():
    usernames = ["alice", ""]
    passwords = ["secret", ""]

    rows = []

    for username, password in product(usernames, passwords):
        a = not username
        b = not password
        result = a or b
        expected = expected_result(username, password)

        rows.append((a, b, result, repr(username), repr(password), expected))

    print("=== auth: not username or not password ===")
    print(
        f"{'A(not user)':>14} "
        f"{'B(not pwd)':>12} "
        f"{'A∨B':>6} "
        f"{'username':>12} "
        f"{'password':>12} "
        f"{'expected':>28}"
    )
    print("-" * 90)

    for a, b, result, username, password, expected in rows:
        print(
            f"{str(a):>14} "
            f"{str(b):>12} "
            f"{str(result):>6} "
            f"{username:>12} "
            f"{password:>12} "
            f"{expected:>28}"
        )


def generate_html_table():
    usernames = ["alice", ""]
    passwords = ["secret", ""]

    html = """
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>Condition Table Auth</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 30px;
        }

        h2 {
            text-align: center;
        }

        table {
            border-collapse: collapse;
            width: 100%;
            margin-top: 20px;
        }

        th, td {
            border: 1px solid #333;
            padding: 8px 10px;
            text-align: center;
        }

        th {
            background-color: #e6e6e6;
        }

        .true {
            background-color: #d9f2d9;
        }

        .false {
            background-color: #f2d9d9;
        }
    </style>
</head>
<body>
    <h2>auth: not username or not password</h2>

    <table>
        <tr>
            <th>A(not user)</th>
            <th>B(not pwd)</th>
            <th>A∨B</th>
            <th>username</th>
            <th>password</th>
            <th>expected</th>
        </tr>
"""

    for username, password in product(usernames, passwords):
        a = not username
        b = not password
        result = a or b
        expected = expected_result(username, password)

        html += f"""
        <tr>
            <td class="{str(a).lower()}">{a}</td>
            <td class="{str(b).lower()}">{b}</td>
            <td class="{str(result).lower()}">{result}</td>
            <td>{repr(username)}</td>
            <td>{repr(password)}</td>
            <td>{expected}</td>
        </tr>
"""

    html += """
    </table>
</body>
</html>
"""

    with open("condition_table_auth.html", "w", encoding="utf-8") as file:
        file.write(html)

    print("\nHTML table saved as condition_table_auth.html")


if __name__ == "__main__":
    generate_console_table()
    generate_html_table()