# SimpleCheckList MCP Server MCP Server

Advanced SimpleCheckList with MCP server and SQLite database for comprehensive task management.

Features:
• Complete project and task management system
• Hierarchical organization (Projects → Groups → Task Lists → Tasks → Subtasks)
• SQLite database for data persistence
• RESTful API with comprehensive endpoints
• MCP protocol compliance for AI assistant integration
• Docker-optimized deployment with stability improvements

**v1.0.1 Update**: Enhanced Docker stability with improved container lifecycle management.
Default mode optimized for containerized deployment with reliable startup and shutdown processes.

Perfect for AI assistants managing complex project workflows and task hierarchies.
.

[What is an MCP Server?](https://www.anthropic.com/news/model-context-protocol)

## Characteristics
Attribute|Details|
|-|-|
**Docker Image**|[mayurkakade/mcp-server:latest](https://hub.docker.com/repository/docker/mayurkakade/mcp-server:latest)
**Author**|[DevMayur](https://github.com/DevMayur)
**Repository**|https://github.com/DevMayur/SimpleCheckList
**Dockerfile**|https://github.com/DevMayur/SimpleCheckList/blob/main/Dockerfile
**Docker Image built by**|DevMayur
**Docker Scout Health Score**|Not available
**Verify Signature**|Not available
**Licence**|

## Available Tools (20)
Tools provided by this Server|Short Description
-|-
`list_projects`|Get all projects from SimpleCheckList|
`create_project`|Create a new project|
`get_project`|Get a specific project by ID|
`update_project`|Update a project|
`delete_project`|Delete a project|
`list_groups`|Get all groups for a project|
`create_group`|Create a new group in a project|
`list_task_lists`|Get all task lists for a group|
`create_task_list`|Create a new task list in a group|
`list_tasks`|Get all tasks for a task list|
`create_task`|Create a new task in a task list|
`toggle_task_completion`|Toggle task completion status|
`update_task`|Update a task|
`delete_task`|Delete a task|
`list_subtasks`|Get all subtasks for a task|
`create_subtask`|Create a new subtask|
`toggle_subtask_completion`|Toggle subtask completion status|
`delete_subtask`|Delete a subtask|
`get_project_stats`|Get statistics for a project|
`get_all_tasks`|Get all tasks with full details across all projects|

---
## Tools Details

#### Tool: **`list_projects`**
Get all projects from SimpleCheckList
#### Tool: **`create_project`**
Create a new project
Parameters|Type|Description
-|-|-
`name`|`string`|Project name
`description`|`string`|Project description
`color`|`string`|Project color (hex code)

---
#### Tool: **`get_project`**
Get a specific project by ID
Parameters|Type|Description
-|-|-
`project_id`|`string`|Project ID

---
#### Tool: **`update_project`**
Update a project
Parameters|Type|Description
-|-|-
`project_id`|`string`|Project ID
`name`|`string`|New project name
`description`|`string`|New project description
`color`|`string`|New project color

---
#### Tool: **`delete_project`**
Delete a project
Parameters|Type|Description
-|-|-
`project_id`|`string`|Project ID

---
#### Tool: **`list_groups`**
Get all groups for a project
Parameters|Type|Description
-|-|-
`project_id`|`string`|Project ID

---
#### Tool: **`create_group`**
Create a new group in a project
Parameters|Type|Description
-|-|-
`project_id`|`string`|Project ID
`name`|`string`|Group name
`description`|`string`|Group description
`order_index`|`number`|Order index for sorting

---
#### Tool: **`list_task_lists`**
Get all task lists for a group
Parameters|Type|Description
-|-|-
`group_id`|`string`|Group ID

---
#### Tool: **`create_task_list`**
Create a new task list in a group
Parameters|Type|Description
-|-|-
`group_id`|`string`|Group ID
`name`|`string`|Task list name
`description`|`string`|Task list description
`order_index`|`number`|Order index for sorting

---
#### Tool: **`list_tasks`**
Get all tasks for a task list
Parameters|Type|Description
-|-|-
`task_list_id`|`string`|Task list ID

---
#### Tool: **`create_task`**
Create a new task in a task list
Parameters|Type|Description
-|-|-
`task_list_id`|`string`|Task list ID
`title`|`string`|Task title
`description`|`string`|Task description
`priority`|`string`|Task priority (low, medium, high)
`due_date`|`string`|Due date (ISO string)
`metadata`|`object`|Additional task metadata

---
#### Tool: **`toggle_task_completion`**
Toggle task completion status
Parameters|Type|Description
-|-|-
`task_id`|`string`|Task ID

---
#### Tool: **`update_task`**
Update a task
Parameters|Type|Description
-|-|-
`task_id`|`string`|Task ID
`title`|`string`|New task title
`description`|`string`|New task description
`priority`|`string`|New task priority
`due_date`|`string`|New due date (ISO string)
`metadata`|`object`|New task metadata

---
#### Tool: **`delete_task`**
Delete a task
Parameters|Type|Description
-|-|-
`task_id`|`string`|Task ID

---
#### Tool: **`list_subtasks`**
Get all subtasks for a task
Parameters|Type|Description
-|-|-
`task_id`|`string`|Task ID

---
#### Tool: **`create_subtask`**
Create a new subtask
Parameters|Type|Description
-|-|-
`task_id`|`string`|Task ID
`title`|`string`|Subtask title
`order_index`|`number`|Order index for sorting

---
#### Tool: **`toggle_subtask_completion`**
Toggle subtask completion status
Parameters|Type|Description
-|-|-
`subtask_id`|`string`|Subtask ID

---
#### Tool: **`delete_subtask`**
Delete a subtask
Parameters|Type|Description
-|-|-
`subtask_id`|`string`|Subtask ID

---
#### Tool: **`get_project_stats`**
Get statistics for a project
Parameters|Type|Description
-|-|-
`project_id`|`string`|Project ID

---
#### Tool: **`get_all_tasks`**
Get all tasks with full details across all projects
## Use this MCP Server

```json
{
  "mcpServers": {
    "simplechecklist": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "mayurkakade/mcp-server:latest",
        "--mode=backend"
      ]
    }
  }
}
```

[Why is it safer to run MCP Servers with Docker?](https://www.docker.com/blog/the-model-context-protocol-simplifying-building-ai-apps-with-anthropic-claude-desktop-and-docker/)
