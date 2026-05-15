from task5 import update_task_status

# 1. State transition tests
def test_open_to_in_progress():
    task = {"status": "open"}

    result = update_task_status(task, "in_progress", "user")

    assert result == "Updated"
    assert task["status"] == "in_progress"
def test_open_to_closed_admin():
    task = {"status": "open"}

    result = update_task_status(task, "closed", "admin")

    assert result == "Updated"
    assert task["status"] == "closed"
def test_open_to_closed_manager():
    task = {"status": "open"}

    result = update_task_status(task, "closed", "manager")

    assert result == "Updated"
    assert task["status"] == "closed"
def test_open_to_closed_user_permission_denied():
    task = {"status": "open"}

    result = update_task_status(task, "closed", "user")

    assert result == "Permission denied"
    assert task["status"] == "open"
def test_in_progress_to_closed_admin():
    task = {"status": "in_progress"}

    result = update_task_status(task, "closed", "admin")

    assert result == "Updated"
    assert task["status"] == "closed"
def test_in_progress_to_closed_manager():
    task = {"status": "in_progress"}

    result = update_task_status(task, "closed", "manager")

    assert result == "Updated"
    assert task["status"] == "closed"
def test_in_progress_to_closed_user_permission_denied():
    task = {"status": "in_progress"}

    result = update_task_status(task, "closed", "user")

    assert result == "Permission denied"
    assert task["status"] == "in_progress"
def test_in_progress_to_on_hold():
    task = {"status": "in_progress"}

    result = update_task_status(task, "on_hold", "user")

    assert result == "Updated"
    assert task["status"] == "on_hold"
def test_on_hold_to_in_progress():
    task = {"status": "on_hold"}

    result = update_task_status(task, "in_progress", "user")

    assert result == "Updated"
    assert task["status"] == "in_progress"
def test_closed_to_open_invalid():
    task = {"status": "closed"}

    result = update_task_status(task, "open", "admin")

    assert result == "Invalid transition"
    assert task["status"] == "closed"
def test_closed_to_in_progress_invalid():
    task = {"status": "closed"}

    result = update_task_status(task, "in_progress", "admin")

    assert result == "Invalid transition"
    assert task["status"] == "closed"
def test_closed_to_on_hold_invalid():
    task = {"status": "closed"}

    result = update_task_status(task, "on_hold", "admin")

    assert result == "Invalid transition"
    assert task["status"] == "closed"
def test_open_to_on_hold_invalid():
    task = {"status": "open"}

    result = update_task_status(task, "on_hold", "admin")

    assert result == "Invalid transition"
    assert task["status"] == "open"
def test_in_progress_to_open_invalid():
    task = {"status": "in_progress"}

    result = update_task_status(task, "open", "admin")

    assert result == "Invalid transition"
    assert task["status"] == "in_progress"
def test_on_hold_to_open_invalid():
    task = {"status": "on_hold"}

    result = update_task_status(task, "open", "admin")

    assert result == "Invalid transition"
    assert task["status"] == "on_hold"
def test_on_hold_to_closed_invalid():
    task = {"status": "on_hold"}

    result = update_task_status(task, "closed", "admin")

    assert result == "Invalid transition"
    assert task["status"] == "on_hold"
def test_no_change_open():
    task = {"status": "open"}

    result = update_task_status(task, "open", "admin")

    assert result == "No change"
    assert task["status"] == "open"
def test_no_change_in_progress():
    task = {"status": "in_progress"}

    result = update_task_status(task, "in_progress", "admin")

    assert result == "No change"
    assert task["status"] == "in_progress"
def test_no_change_on_hold():
    task = {"status": "on_hold"}

    result = update_task_status(task, "on_hold", "admin")

    assert result == "No change"
    assert task["status"] == "on_hold"
def test_no_change_closed():
    task = {"status": "closed"}

    result = update_task_status(task, "closed", "admin")

    assert result == "No change"
    assert task["status"] == "closed"

# Branch coverage tests
def test_branch_no_change_true():
    task = {"status": "open"}
    assert update_task_status(task, "open", "admin") == "No change"
def test_branch_invalid_transition_true():
    task = {"status": "open"}
    assert update_task_status(task, "on_hold", "admin") == "Invalid transition"
def test_branch_permission_denied_true():
    task = {"status": "open"}
    assert update_task_status(task, "closed", "user") == "Permission denied"
def test_branch_updated_false_permission_condition():
    task = {"status": "open"}
    assert update_task_status(task, "in_progress", "user") == "Updated"
    assert task["status"] == "in_progress"
def test_branch_closed_by_admin():
    task = {"status": "open"}
    assert update_task_status(task, "closed", "admin") == "Updated"
    assert task["status"] == "closed"

# 2. Condition coverage tests
def test_condition_admin_closed():
    task = {"status": "open"}

    result = update_task_status(task, "closed", "admin")

    assert result == "Updated"
    assert task["status"] == "closed"
def test_condition_manager_closed():
    task = {"status": "open"}

    result = update_task_status(task, "closed", "manager")

    assert result == "Updated"
    assert task["status"] == "closed"
def test_condition_user_closed():
    task = {"status": "open"}

    result = update_task_status(task, "closed", "user")

    assert result == "Permission denied"
    assert task["status"] == "open"
def test_condition_admin_in_progress():
    task = {"status": "open"}

    result = update_task_status(task, "in_progress", "admin")

    assert result == "Updated"
    assert task["status"] == "in_progress"
def test_condition_manager_in_progress():
    task = {"status": "open"}

    result = update_task_status(task, "in_progress", "manager")

    assert result == "Updated"
    assert task["status"] == "in_progress"
def test_condition_user_in_progress():
    task = {"status": "open"}

    result = update_task_status(task, "in_progress", "user")

    assert result == "Updated"
    assert task["status"] == "in_progress"

# 3. Minimal independent condition tests
def test_independent_condition_role_allowed():
    task = {"status": "open"}

    result = update_task_status(task, "closed", "admin")

    assert result == "Updated"
    assert task["status"] == "closed"
def test_independent_condition_role_not_allowed():
    task = {"status": "open"}

    result = update_task_status(task, "closed", "user")

    assert result == "Permission denied"
    assert task["status"] == "open"
def test_independent_condition_status_not_closed():
    task = {"status": "open"}

    result = update_task_status(task, "in_progress", "user")

    assert result == "Updated"
    assert task["status"] == "in_progress"