# GitHub Official MCP Server

Official GitHub MCP Server, by GitHub. Provides seamless integration with GitHub APIs, enabling advanced automation and interaction capabilities for developers and tools.

[What is an MCP Server?](https://www.anthropic.com/news/model-context-protocol)

## Characteristics
Attribute|Details|
|-|-|
**Docker Image**|[ghcr.io/github/github-mcp-server](https://hub.docker.com/repository/docker/ghcr.io/github/github-mcp-server)
**Author**|[github](https://github.com/github)
**Repository**|https://github.com/github/github-mcp-server
**Dockerfile**|https://github.com/github/github-mcp-server/blob/main/Dockerfile
**Docker Image built by**|github
**Docker Scout Health Score**|Not available
**Verify Signature**|Not available
**Licence**|MIT License

## Available Tools (96)
Tools provided by this Server|Short Description
-|-
`add_comment_to_pending_review`|Add review comment to the requester's latest pending pull request review|
`add_issue_comment`|Add comment to issue|
`add_sub_issue`|Add sub-issue|
`assign_copilot_to_issue`|Assign Copilot to issue|
`cancel_workflow_run`|Cancel workflow run|
`create_and_submit_pull_request_review`|Create and submit a pull request review without comments|
`create_branch`|Create branch|
`create_gist`|Create Gist|
`create_issue`|Open new issue|
`create_or_update_file`|Create or update file|
`create_pending_pull_request_review`|Create pending pull request review|
`create_pull_request`|Open new pull request|
`create_repository`|Create repository|
`delete_file`|Delete file|
`delete_pending_pull_request_review`|Delete the requester's latest pending pull request review|
`delete_workflow_run_logs`|Delete workflow logs|
`dismiss_notification`|Dismiss notification|
`download_workflow_run_artifact`|Download workflow artifact|
`fork_repository`|Fork repository|
`get_code_scanning_alert`|Get code scanning alert|
`get_commit`|Get commit details|
`get_dependabot_alert`|Get dependabot alert|
`get_discussion`|Get discussion|
`get_discussion_comments`|Get discussion comments|
`get_file_contents`|Get file or directory contents|
`get_global_security_advisory`|Get a global security advisory|
`get_issue`|Get issue details|
`get_issue_comments`|Get issue comments|
`get_job_logs`|Get job logs|
`get_latest_release`|Get latest release|
`get_me`|Get my user profile|
`get_notification_details`|Get notification details|
`get_project`|Get project|
`get_pull_request`|Get pull request details|
`get_pull_request_diff`|Get pull request diff|
`get_pull_request_files`|Get pull request files|
`get_pull_request_review_comments`|Get pull request review comments|
`get_pull_request_reviews`|Get pull request reviews|
`get_pull_request_status`|Get pull request status checks|
`get_release_by_tag`|Get a release by tag name|
`get_secret_scanning_alert`|Get secret scanning alert|
`get_tag`|Get tag details|
`get_team_members`|Get team members|
`get_teams`|Get teams|
`get_workflow_run`|Get workflow run|
`get_workflow_run_logs`|Get workflow run logs|
`get_workflow_run_usage`|Get workflow usage|
`list_branches`|List branches|
`list_code_scanning_alerts`|List code scanning alerts|
`list_commits`|List commits|
`list_dependabot_alerts`|List dependabot alerts|
`list_discussion_categories`|List discussion categories|
`list_discussions`|List discussions|
`list_gists`|List Gists|
`list_global_security_advisories`|List global security advisories|
`list_issue_types`|List available issue types|
`list_issues`|List issues|
`list_notifications`|List notifications|
`list_org_repository_security_advisories`|List org repository security advisories|
`list_project_fields`|List project fields|
`list_projects`|List projects|
`list_pull_requests`|List pull requests|
`list_releases`|List releases|
`list_repository_security_advisories`|List repository security advisories|
`list_secret_scanning_alerts`|List secret scanning alerts|
`list_starred_repositories`|List starred repositories|
`list_sub_issues`|List sub-issues|
`list_tags`|List tags|
`list_workflow_jobs`|List workflow jobs|
`list_workflow_run_artifacts`|List workflow artifacts|
`list_workflow_runs`|List workflow runs|
`list_workflows`|List workflows|
`manage_notification_subscription`|Manage notification subscription|
`manage_repository_notification_subscription`|Manage repository notification subscription|
`mark_all_notifications_read`|Mark all notifications as read|
`merge_pull_request`|Merge pull request|
`push_files`|Push files to repository|
`remove_sub_issue`|Remove sub-issue|
`reprioritize_sub_issue`|Reprioritize sub-issue|
`request_copilot_review`|Request Copilot review|
`rerun_failed_jobs`|Rerun failed jobs|
`rerun_workflow_run`|Rerun workflow run|
`run_workflow`|Run workflow|
`search_code`|Search code|
`search_issues`|Search issues|
`search_orgs`|Search organizations|
`search_pull_requests`|Search pull requests|
`search_repositories`|Search repositories|
`search_users`|Search users|
`star_repository`|Star repository|
`submit_pending_pull_request_review`|Submit the requester's latest pending pull request review|
`unstar_repository`|Unstar repository|
`update_gist`|Update Gist|
`update_issue`|Edit issue|
`update_pull_request`|Edit pull request|
`update_pull_request_branch`|Update pull request branch|

---
## Tools Details

#### Tool: **`add_comment_to_pending_review`**
Add review comment to the requester's latest pending pull request review. A pending review needs to already exist to call this (check with the user if not sure).
Parameters|Type|Description
-|-|-
`body`|`string`|The text of the review comment
`owner`|`string`|Repository owner
`path`|`string`|The relative path to the file that necessitates a comment
`pullNumber`|`number`|Pull request number
`repo`|`string`|Repository name
`subjectType`|`string`|The level at which the comment is targeted
`line`|`number` *optional*|The line of the blob in the pull request diff that the comment applies to. For multi-line comments, the last line of the range
`side`|`string` *optional*|The side of the diff to comment on. LEFT indicates the previous state, RIGHT indicates the new state
`startLine`|`number` *optional*|For multi-line comments, the first line of the range that the comment applies to
`startSide`|`string` *optional*|For multi-line comments, the starting side of the diff that the comment applies to. LEFT indicates the previous state, RIGHT indicates the new state

---
#### Tool: **`add_issue_comment`**
Add a comment to a specific issue in a GitHub repository.
Parameters|Type|Description
-|-|-
`body`|`string`|Comment content
`issue_number`|`number`|Issue number to comment on
`owner`|`string`|Repository owner
`repo`|`string`|Repository name

---
#### Tool: **`add_sub_issue`**
Add a sub-issue to a parent issue in a GitHub repository.
Parameters|Type|Description
-|-|-
`issue_number`|`number`|The number of the parent issue
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`sub_issue_id`|`number`|The ID of the sub-issue to add. ID is not the same as issue number
`replace_parent`|`boolean` *optional*|When true, replaces the sub-issue's current parent issue

---
#### Tool: **`assign_copilot_to_issue`**
Assign Copilot to a specific issue in a GitHub repository.

This tool can help with the following outcomes:
- a Pull Request created with source code changes to resolve the issue


More information can be found at:
- https://docs.github.com/en/copilot/using-github-copilot/using-copilot-coding-agent-to-work-on-tasks/about-assigning-tasks-to-copilot
Parameters|Type|Description
-|-|-
`issueNumber`|`number`|Issue number
`owner`|`string`|Repository owner
`repo`|`string`|Repository name

---
#### Tool: **`cancel_workflow_run`**
Cancel a workflow run
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`run_id`|`number`|The unique identifier of the workflow run

---
#### Tool: **`create_and_submit_pull_request_review`**
Create and submit a review for a pull request without review comments.
Parameters|Type|Description
-|-|-
`body`|`string`|Review comment text
`event`|`string`|Review action to perform
`owner`|`string`|Repository owner
`pullNumber`|`number`|Pull request number
`repo`|`string`|Repository name
`commitID`|`string` *optional*|SHA of commit to review

---
#### Tool: **`create_branch`**
Create a new branch in a GitHub repository
Parameters|Type|Description
-|-|-
`branch`|`string`|Name for new branch
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`from_branch`|`string` *optional*|Source branch (defaults to repo default)

---
#### Tool: **`create_gist`**
Create a new gist
Parameters|Type|Description
-|-|-
`content`|`string`|Content for simple single-file gist creation
`filename`|`string`|Filename for simple single-file gist creation
`description`|`string` *optional*|Description of the gist
`public`|`boolean` *optional*|Whether the gist is public

---
#### Tool: **`create_issue`**
Create a new issue in a GitHub repository.
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`title`|`string`|Issue title
`assignees`|`array` *optional*|Usernames to assign to this issue
`body`|`string` *optional*|Issue body content
`labels`|`array` *optional*|Labels to apply to this issue
`milestone`|`number` *optional*|Milestone number
`type`|`string` *optional*|Type of this issue

---
#### Tool: **`create_or_update_file`**
Create or update a single file in a GitHub repository. If updating, you must provide the SHA of the file you want to update. Use this tool to create or update a file in a GitHub repository remotely; do not use it for local file operations.
Parameters|Type|Description
-|-|-
`branch`|`string`|Branch to create/update the file in
`content`|`string`|Content of the file
`message`|`string`|Commit message
`owner`|`string`|Repository owner (username or organization)
`path`|`string`|Path where to create/update the file
`repo`|`string`|Repository name
`sha`|`string` *optional*|Required if updating an existing file. The blob SHA of the file being replaced.

---
#### Tool: **`create_pending_pull_request_review`**
Create a pending review for a pull request. Call this first before attempting to add comments to a pending review, and ultimately submitting it. A pending pull request review means a pull request review, it is pending because you create it first and submit it later, and the PR author will not see it until it is submitted.
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`pullNumber`|`number`|Pull request number
`repo`|`string`|Repository name
`commitID`|`string` *optional*|SHA of commit to review

---
#### Tool: **`create_pull_request`**
Create a new pull request in a GitHub repository.
Parameters|Type|Description
-|-|-
`base`|`string`|Branch to merge into
`head`|`string`|Branch containing changes
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`title`|`string`|PR title
`body`|`string` *optional*|PR description
`draft`|`boolean` *optional*|Create as draft PR
`maintainer_can_modify`|`boolean` *optional*|Allow maintainer edits

---
#### Tool: **`create_repository`**
Create a new GitHub repository in your account or specified organization
Parameters|Type|Description
-|-|-
`name`|`string`|Repository name
`autoInit`|`boolean` *optional*|Initialize with README
`description`|`string` *optional*|Repository description
`organization`|`string` *optional*|Organization to create the repository in (omit to create in your personal account)
`private`|`boolean` *optional*|Whether repo should be private

---
#### Tool: **`delete_file`**
Delete a file from a GitHub repository
Parameters|Type|Description
-|-|-
`branch`|`string`|Branch to delete the file from
`message`|`string`|Commit message
`owner`|`string`|Repository owner (username or organization)
`path`|`string`|Path to the file to delete
`repo`|`string`|Repository name

*This tool may perform destructive updates.*

---
#### Tool: **`delete_pending_pull_request_review`**
Delete the requester's latest pending pull request review. Use this after the user decides not to submit a pending review, if you don't know if they already created one then check first.
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`pullNumber`|`number`|Pull request number
`repo`|`string`|Repository name

---
#### Tool: **`delete_workflow_run_logs`**
Delete logs for a workflow run
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`run_id`|`number`|The unique identifier of the workflow run

*This tool may perform destructive updates.*

---
#### Tool: **`dismiss_notification`**
Dismiss a notification by marking it as read or done
Parameters|Type|Description
-|-|-
`threadID`|`string`|The ID of the notification thread
`state`|`string` *optional*|The new state of the notification (read/done)

---
#### Tool: **`download_workflow_run_artifact`**
Get download URL for a workflow run artifact
Parameters|Type|Description
-|-|-
`artifact_id`|`number`|The unique identifier of the artifact
`owner`|`string`|Repository owner
`repo`|`string`|Repository name

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`fork_repository`**
Fork a GitHub repository to your account or specified organization
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`organization`|`string` *optional*|Organization to fork to

---
#### Tool: **`get_code_scanning_alert`**
Get details of a specific code scanning alert in a GitHub repository.
Parameters|Type|Description
-|-|-
`alertNumber`|`number`|The number of the alert.
`owner`|`string`|The owner of the repository.
`repo`|`string`|The name of the repository.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_commit`**
Get details for a commit from a GitHub repository
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`sha`|`string`|Commit SHA, branch name, or tag name
`include_diff`|`boolean` *optional*|Whether to include file diffs and stats in the response. Default is true.
`page`|`number` *optional*|Page number for pagination (min 1)
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_dependabot_alert`**
Get details of a specific dependabot alert in a GitHub repository.
Parameters|Type|Description
-|-|-
`alertNumber`|`number`|The number of the alert.
`owner`|`string`|The owner of the repository.
`repo`|`string`|The name of the repository.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_discussion`**
Get a specific discussion by ID
Parameters|Type|Description
-|-|-
`discussionNumber`|`number`|Discussion Number
`owner`|`string`|Repository owner
`repo`|`string`|Repository name

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_discussion_comments`**
Get comments from a discussion
Parameters|Type|Description
-|-|-
`discussionNumber`|`number`|Discussion Number
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`after`|`string` *optional*|Cursor for pagination. Use the endCursor from the previous page's PageInfo for GraphQL APIs.
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_file_contents`**
Get the contents of a file or directory from a GitHub repository
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner (username or organization)
`repo`|`string`|Repository name
`path`|`string` *optional*|Path to file/directory (directories must end with a slash '/')
`ref`|`string` *optional*|Accepts optional git refs such as `refs/tags/{tag}`, `refs/heads/{branch}` or `refs/pull/{pr_number}/head`
`sha`|`string` *optional*|Accepts optional commit SHA. If specified, it will be used instead of ref

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_global_security_advisory`**
Get a global security advisory
Parameters|Type|Description
-|-|-
`ghsaId`|`string`|GitHub Security Advisory ID (format: GHSA-xxxx-xxxx-xxxx).

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_issue`**
Get details of a specific issue in a GitHub repository.
Parameters|Type|Description
-|-|-
`issue_number`|`number`|The number of the issue
`owner`|`string`|The owner of the repository
`repo`|`string`|The name of the repository

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_issue_comments`**
Get comments for a specific issue in a GitHub repository.
Parameters|Type|Description
-|-|-
`issue_number`|`number`|Issue number
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`page`|`number` *optional*|Page number for pagination (min 1)
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_job_logs`**
Download logs for a specific workflow job or efficiently get all failed job logs for a workflow run
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`failed_only`|`boolean` *optional*|When true, gets logs for all failed jobs in run_id
`job_id`|`number` *optional*|The unique identifier of the workflow job (required for single job logs)
`return_content`|`boolean` *optional*|Returns actual log content instead of URLs
`run_id`|`number` *optional*|Workflow run ID (required when using failed_only)
`tail_lines`|`number` *optional*|Number of lines to return from the end of the log

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_latest_release`**
Get the latest release in a GitHub repository
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`repo`|`string`|Repository name

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_me`**
Get details of the authenticated GitHub user. Use this when a request is about the user's own profile for GitHub. Or when information is missing to build other tool calls.
#### Tool: **`get_notification_details`**
Get detailed information for a specific GitHub notification, always call this tool when the user asks for details about a specific notification, if you don't know the ID list notifications first.
Parameters|Type|Description
-|-|-
`notificationID`|`string`|The ID of the notification

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_project`**
Get Project for a user or org
Parameters|Type|Description
-|-|-
`owner`|`string`|If owner_type == user it is the handle for the GitHub user account. If owner_type == org it is the name of the organization. The name is not case sensitive.
`owner_type`|`string`|Owner type
`project_number`|`number`|The project's number

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_pull_request`**
Get details of a specific pull request in a GitHub repository.
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`pullNumber`|`number`|Pull request number
`repo`|`string`|Repository name

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_pull_request_diff`**
Get the diff of a pull request.
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`pullNumber`|`number`|Pull request number
`repo`|`string`|Repository name

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_pull_request_files`**
Get the files changed in a specific pull request.
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`pullNumber`|`number`|Pull request number
`repo`|`string`|Repository name
`page`|`number` *optional*|Page number for pagination (min 1)
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_pull_request_review_comments`**
Get pull request review comments. They are comments made on a portion of the unified diff during a pull request review. These are different from commit comments and issue comments in a pull request.
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`pullNumber`|`number`|Pull request number
`repo`|`string`|Repository name

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_pull_request_reviews`**
Get reviews for a specific pull request.
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`pullNumber`|`number`|Pull request number
`repo`|`string`|Repository name

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_pull_request_status`**
Get the status of a specific pull request.
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`pullNumber`|`number`|Pull request number
`repo`|`string`|Repository name

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_release_by_tag`**
Get a specific release by its tag name in a GitHub repository
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`tag`|`string`|Tag name (e.g., 'v1.0.0')

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_secret_scanning_alert`**
Get details of a specific secret scanning alert in a GitHub repository.
Parameters|Type|Description
-|-|-
`alertNumber`|`number`|The number of the alert.
`owner`|`string`|The owner of the repository.
`repo`|`string`|The name of the repository.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_tag`**
Get details about a specific git tag in a GitHub repository
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`tag`|`string`|Tag name

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_team_members`**
Get member usernames of a specific team in an organization. Limited to organizations accessible with current credentials
Parameters|Type|Description
-|-|-
`org`|`string`|Organization login (owner) that contains the team.
`team_slug`|`string`|Team slug

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_teams`**
Get details of the teams the user is a member of. Limited to organizations accessible with current credentials
Parameters|Type|Description
-|-|-
`user`|`string` *optional*|Username to get teams for. If not provided, uses the authenticated user.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_workflow_run`**
Get details of a specific workflow run
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`run_id`|`number`|The unique identifier of the workflow run

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_workflow_run_logs`**
Download logs for a specific workflow run (EXPENSIVE: downloads ALL logs as ZIP. Consider using get_job_logs with failed_only=true for debugging failed jobs)
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`run_id`|`number`|The unique identifier of the workflow run

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_workflow_run_usage`**
Get usage metrics for a workflow run
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`run_id`|`number`|The unique identifier of the workflow run

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_branches`**
List branches in a GitHub repository
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`page`|`number` *optional*|Page number for pagination (min 1)
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_code_scanning_alerts`**
List code scanning alerts in a GitHub repository.
Parameters|Type|Description
-|-|-
`owner`|`string`|The owner of the repository.
`repo`|`string`|The name of the repository.
`ref`|`string` *optional*|The Git reference for the results you want to list.
`severity`|`string` *optional*|Filter code scanning alerts by severity
`state`|`string` *optional*|Filter code scanning alerts by state. Defaults to open
`tool_name`|`string` *optional*|The name of the tool used for code scanning.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_commits`**
Get list of commits of a branch in a GitHub repository. Returns at least 30 results per page by default, but can return more if specified using the perPage parameter (up to 100).
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`author`|`string` *optional*|Author username or email address to filter commits by
`page`|`number` *optional*|Page number for pagination (min 1)
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)
`sha`|`string` *optional*|Commit SHA, branch or tag name to list commits of. If not provided, uses the default branch of the repository. If a commit SHA is provided, will list commits up to that SHA.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_dependabot_alerts`**
List dependabot alerts in a GitHub repository.
Parameters|Type|Description
-|-|-
`owner`|`string`|The owner of the repository.
`repo`|`string`|The name of the repository.
`severity`|`string` *optional*|Filter dependabot alerts by severity
`state`|`string` *optional*|Filter dependabot alerts by state. Defaults to open

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_discussion_categories`**
List discussion categories with their id and name, for a repository or organisation.
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`repo`|`string` *optional*|Repository name. If not provided, discussion categories will be queried at the organisation level.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_discussions`**
List discussions for a repository or organisation.
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`after`|`string` *optional*|Cursor for pagination. Use the endCursor from the previous page's PageInfo for GraphQL APIs.
`category`|`string` *optional*|Optional filter by discussion category ID. If provided, only discussions with this category are listed.
`direction`|`string` *optional*|Order direction.
`orderBy`|`string` *optional*|Order discussions by field. If provided, the 'direction' also needs to be provided.
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)
`repo`|`string` *optional*|Repository name. If not provided, discussions will be queried at the organisation level.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_gists`**
List gists for a user
Parameters|Type|Description
-|-|-
`page`|`number` *optional*|Page number for pagination (min 1)
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)
`since`|`string` *optional*|Only gists updated after this time (ISO 8601 timestamp)
`username`|`string` *optional*|GitHub username (omit for authenticated user's gists)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_global_security_advisories`**
List global security advisories from GitHub.
Parameters|Type|Description
-|-|-
`affects`|`string` *optional*|Filter advisories by affected package or version (e.g. "package1,package2@1.0.0").
`cveId`|`string` *optional*|Filter by CVE ID.
`cwes`|`array` *optional*|Filter by Common Weakness Enumeration IDs (e.g. ["79", "284", "22"]).
`ecosystem`|`string` *optional*|Filter by package ecosystem.
`ghsaId`|`string` *optional*|Filter by GitHub Security Advisory ID (format: GHSA-xxxx-xxxx-xxxx).
`isWithdrawn`|`boolean` *optional*|Whether to only return withdrawn advisories.
`modified`|`string` *optional*|Filter by publish or update date or date range (ISO 8601 date or range).
`published`|`string` *optional*|Filter by publish date or date range (ISO 8601 date or range).
`severity`|`string` *optional*|Filter by severity.
`type`|`string` *optional*|Advisory type.
`updated`|`string` *optional*|Filter by update date or date range (ISO 8601 date or range).

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_issue_types`**
List supported issue types for repository owner (organization).
Parameters|Type|Description
-|-|-
`owner`|`string`|The organization owner of the repository

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_issues`**
List issues in a GitHub repository. For pagination, use the 'endCursor' from the previous response's 'pageInfo' in the 'after' parameter.
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`after`|`string` *optional*|Cursor for pagination. Use the endCursor from the previous page's PageInfo for GraphQL APIs.
`direction`|`string` *optional*|Order direction. If provided, the 'orderBy' also needs to be provided.
`labels`|`array` *optional*|Filter by labels
`orderBy`|`string` *optional*|Order issues by field. If provided, the 'direction' also needs to be provided.
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)
`since`|`string` *optional*|Filter by date (ISO 8601 timestamp)
`state`|`string` *optional*|Filter by state, by default both open and closed issues are returned when not provided

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_notifications`**
Lists all GitHub notifications for the authenticated user, including unread notifications, mentions, review requests, assignments, and updates on issues or pull requests. Use this tool whenever the user asks what to work on next, requests a summary of their GitHub activity, wants to see pending reviews, or needs to check for new updates or tasks. This tool is the primary way to discover actionable items, reminders, and outstanding work on GitHub. Always call this tool when asked what to work on next, what is pending, or what needs attention in GitHub.
Parameters|Type|Description
-|-|-
`before`|`string` *optional*|Only show notifications updated before the given time (ISO 8601 format)
`filter`|`string` *optional*|Filter notifications to, use default unless specified. Read notifications are ones that have already been acknowledged by the user. Participating notifications are those that the user is directly involved in, such as issues or pull requests they have commented on or created.
`owner`|`string` *optional*|Optional repository owner. If provided with repo, only notifications for this repository are listed.
`page`|`number` *optional*|Page number for pagination (min 1)
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)
`repo`|`string` *optional*|Optional repository name. If provided with owner, only notifications for this repository are listed.
`since`|`string` *optional*|Only show notifications updated after the given time (ISO 8601 format)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_org_repository_security_advisories`**
List repository security advisories for a GitHub organization.
Parameters|Type|Description
-|-|-
`org`|`string`|The organization login.
`direction`|`string` *optional*|Sort direction.
`sort`|`string` *optional*|Sort field.
`state`|`string` *optional*|Filter by advisory state.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_project_fields`**
List Project fields for a user or org
Parameters|Type|Description
-|-|-
`owner`|`string`|If owner_type == user it is the handle for the GitHub user account. If owner_type == org it is the name of the organization. The name is not case sensitive.
`owner_type`|`string`|Owner type
`projectNumber`|`string`|The project's number.
`per_page`|`number` *optional*|Number of results per page (max 100, default: 30)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_projects`**
List Projects for a user or org
Parameters|Type|Description
-|-|-
`owner`|`string`|If owner_type == user it is the handle for the GitHub user account. If owner_type == org it is the name of the organization. The name is not case sensitive.
`owner_type`|`string`|Owner type
`per_page`|`number` *optional*|Number of results per page (max 100, default: 30)
`query`|`string` *optional*|Filter projects by a search query (matches title and description)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_pull_requests`**
List pull requests in a GitHub repository. If the user specifies an author, then DO NOT use this tool and use the search_pull_requests tool instead.
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`base`|`string` *optional*|Filter by base branch
`direction`|`string` *optional*|Sort direction
`head`|`string` *optional*|Filter by head user/org and branch
`page`|`number` *optional*|Page number for pagination (min 1)
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)
`sort`|`string` *optional*|Sort by
`state`|`string` *optional*|Filter by state

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_releases`**
List releases in a GitHub repository
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`page`|`number` *optional*|Page number for pagination (min 1)
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_repository_security_advisories`**
List repository security advisories for a GitHub repository.
Parameters|Type|Description
-|-|-
`owner`|`string`|The owner of the repository.
`repo`|`string`|The name of the repository.
`direction`|`string` *optional*|Sort direction.
`sort`|`string` *optional*|Sort field.
`state`|`string` *optional*|Filter by advisory state.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_secret_scanning_alerts`**
List secret scanning alerts in a GitHub repository.
Parameters|Type|Description
-|-|-
`owner`|`string`|The owner of the repository.
`repo`|`string`|The name of the repository.
`resolution`|`string` *optional*|Filter by resolution
`secret_type`|`string` *optional*|A comma-separated list of secret types to return. All default secret patterns are returned. To return generic patterns, pass the token name(s) in the parameter.
`state`|`string` *optional*|Filter by state

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_starred_repositories`**
List starred repositories
Parameters|Type|Description
-|-|-
`direction`|`string` *optional*|The direction to sort the results by.
`page`|`number` *optional*|Page number for pagination (min 1)
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)
`sort`|`string` *optional*|How to sort the results. Can be either 'created' (when the repository was starred) or 'updated' (when the repository was last pushed to).
`username`|`string` *optional*|Username to list starred repositories for. Defaults to the authenticated user.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_sub_issues`**
List sub-issues for a specific issue in a GitHub repository.
Parameters|Type|Description
-|-|-
`issue_number`|`number`|Issue number
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`page`|`number` *optional*|Page number for pagination (default: 1)
`per_page`|`number` *optional*|Number of results per page (max 100, default: 30)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_tags`**
List git tags in a GitHub repository
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`page`|`number` *optional*|Page number for pagination (min 1)
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_workflow_jobs`**
List jobs for a specific workflow run
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`run_id`|`number`|The unique identifier of the workflow run
`filter`|`string` *optional*|Filters jobs by their completed_at timestamp
`page`|`number` *optional*|Page number for pagination (min 1)
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_workflow_run_artifacts`**
List artifacts for a workflow run
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`run_id`|`number`|The unique identifier of the workflow run
`page`|`number` *optional*|Page number for pagination (min 1)
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_workflow_runs`**
List workflow runs for a specific workflow
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`workflow_id`|`string`|The workflow ID or workflow file name
`actor`|`string` *optional*|Returns someone's workflow runs. Use the login for the user who created the workflow run.
`branch`|`string` *optional*|Returns workflow runs associated with a branch. Use the name of the branch.
`event`|`string` *optional*|Returns workflow runs for a specific event type
`page`|`number` *optional*|Page number for pagination (min 1)
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)
`status`|`string` *optional*|Returns workflow runs with the check run status

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_workflows`**
List workflows in a repository
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`page`|`number` *optional*|Page number for pagination (min 1)
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`manage_notification_subscription`**
Manage a notification subscription: ignore, watch, or delete a notification thread subscription.
Parameters|Type|Description
-|-|-
`action`|`string`|Action to perform: ignore, watch, or delete the notification subscription.
`notificationID`|`string`|The ID of the notification thread.

---
#### Tool: **`manage_repository_notification_subscription`**
Manage a repository notification subscription: ignore, watch, or delete repository notifications subscription for the provided repository.
Parameters|Type|Description
-|-|-
`action`|`string`|Action to perform: ignore, watch, or delete the repository notification subscription.
`owner`|`string`|The account owner of the repository.
`repo`|`string`|The name of the repository.

---
#### Tool: **`mark_all_notifications_read`**
Mark all notifications as read
Parameters|Type|Description
-|-|-
`lastReadAt`|`string` *optional*|Describes the last point that notifications were checked (optional). Default: Now
`owner`|`string` *optional*|Optional repository owner. If provided with repo, only notifications for this repository are marked as read.
`repo`|`string` *optional*|Optional repository name. If provided with owner, only notifications for this repository are marked as read.

---
#### Tool: **`merge_pull_request`**
Merge a pull request in a GitHub repository.
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`pullNumber`|`number`|Pull request number
`repo`|`string`|Repository name
`commit_message`|`string` *optional*|Extra detail for merge commit
`commit_title`|`string` *optional*|Title for merge commit
`merge_method`|`string` *optional*|Merge method

---
#### Tool: **`push_files`**
Push multiple files to a GitHub repository in a single commit
Parameters|Type|Description
-|-|-
`branch`|`string`|Branch to push to
`files`|`array`|Array of file objects to push, each object with path (string) and content (string)
`message`|`string`|Commit message
`owner`|`string`|Repository owner
`repo`|`string`|Repository name

---
#### Tool: **`remove_sub_issue`**
Remove a sub-issue from a parent issue in a GitHub repository.
Parameters|Type|Description
-|-|-
`issue_number`|`number`|The number of the parent issue
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`sub_issue_id`|`number`|The ID of the sub-issue to remove. ID is not the same as issue number

---
#### Tool: **`reprioritize_sub_issue`**
Reprioritize a sub-issue to a different position in the parent issue's sub-issue list.
Parameters|Type|Description
-|-|-
`issue_number`|`number`|The number of the parent issue
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`sub_issue_id`|`number`|The ID of the sub-issue to reprioritize. ID is not the same as issue number
`after_id`|`number` *optional*|The ID of the sub-issue to be prioritized after (either after_id OR before_id should be specified)
`before_id`|`number` *optional*|The ID of the sub-issue to be prioritized before (either after_id OR before_id should be specified)

---
#### Tool: **`request_copilot_review`**
Request a GitHub Copilot code review for a pull request. Use this for automated feedback on pull requests, usually before requesting a human reviewer.
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`pullNumber`|`number`|Pull request number
`repo`|`string`|Repository name

---
#### Tool: **`rerun_failed_jobs`**
Re-run only the failed jobs in a workflow run
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`run_id`|`number`|The unique identifier of the workflow run

---
#### Tool: **`rerun_workflow_run`**
Re-run an entire workflow run
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`run_id`|`number`|The unique identifier of the workflow run

---
#### Tool: **`run_workflow`**
Run an Actions workflow by workflow ID or filename
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`ref`|`string`|The git reference for the workflow. The reference can be a branch or tag name.
`repo`|`string`|Repository name
`workflow_id`|`string`|The workflow ID (numeric) or workflow file name (e.g., main.yml, ci.yaml)
`inputs`|`object` *optional*|Inputs the workflow accepts

---
#### Tool: **`search_code`**
Fast and precise code search across ALL GitHub repositories using GitHub's native search engine. Best for finding exact symbols, functions, classes, or specific code patterns.
Parameters|Type|Description
-|-|-
`query`|`string`|Search query using GitHub's powerful code search syntax. Examples: 'content:Skill language:Java org:github', 'NOT is:archived language:Python OR language:go', 'repo:github/github-mcp-server'. Supports exact matching, language filters, path filters, and more.
`order`|`string` *optional*|Sort order for results
`page`|`number` *optional*|Page number for pagination (min 1)
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)
`sort`|`string` *optional*|Sort field ('indexed' only)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`search_issues`**
Search for issues in GitHub repositories using issues search syntax already scoped to is:issue
Parameters|Type|Description
-|-|-
`query`|`string`|Search query using GitHub issues search syntax
`order`|`string` *optional*|Sort order
`owner`|`string` *optional*|Optional repository owner. If provided with repo, only issues for this repository are listed.
`page`|`number` *optional*|Page number for pagination (min 1)
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)
`repo`|`string` *optional*|Optional repository name. If provided with owner, only issues for this repository are listed.
`sort`|`string` *optional*|Sort field by number of matches of categories, defaults to best match

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`search_orgs`**
Find GitHub organizations by name, location, or other organization metadata. Ideal for discovering companies, open source foundations, or teams.
Parameters|Type|Description
-|-|-
`query`|`string`|Organization search query. Examples: 'microsoft', 'location:california', 'created:>=2025-01-01'. Search is automatically scoped to type:org.
`order`|`string` *optional*|Sort order
`page`|`number` *optional*|Page number for pagination (min 1)
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)
`sort`|`string` *optional*|Sort field by category

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`search_pull_requests`**
Search for pull requests in GitHub repositories using issues search syntax already scoped to is:pr
Parameters|Type|Description
-|-|-
`query`|`string`|Search query using GitHub pull request search syntax
`order`|`string` *optional*|Sort order
`owner`|`string` *optional*|Optional repository owner. If provided with repo, only pull requests for this repository are listed.
`page`|`number` *optional*|Page number for pagination (min 1)
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)
`repo`|`string` *optional*|Optional repository name. If provided with owner, only pull requests for this repository are listed.
`sort`|`string` *optional*|Sort field by number of matches of categories, defaults to best match

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`search_repositories`**
Find GitHub repositories by name, description, readme, topics, or other metadata. Perfect for discovering projects, finding examples, or locating specific repositories across GitHub.
Parameters|Type|Description
-|-|-
`query`|`string`|Repository search query. Examples: 'machine learning in:name stars:>1000 language:python', 'topic:react', 'user:facebook'. Supports advanced search syntax for precise filtering.
`minimal_output`|`boolean` *optional*|Return minimal repository information (default: true). When false, returns full GitHub API repository objects.
`page`|`number` *optional*|Page number for pagination (min 1)
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`search_users`**
Find GitHub users by username, real name, or other profile information. Useful for locating developers, contributors, or team members.
Parameters|Type|Description
-|-|-
`query`|`string`|User search query. Examples: 'john smith', 'location:seattle', 'followers:>100'. Search is automatically scoped to type:user.
`order`|`string` *optional*|Sort order
`page`|`number` *optional*|Page number for pagination (min 1)
`perPage`|`number` *optional*|Results per page for pagination (min 1, max 100)
`sort`|`string` *optional*|Sort users by number of followers or repositories, or when the person joined GitHub.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`star_repository`**
Star a GitHub repository
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`repo`|`string`|Repository name

---
#### Tool: **`submit_pending_pull_request_review`**
Submit the requester's latest pending pull request review, normally this is a final step after creating a pending review, adding comments first, unless you know that the user already did the first two steps, you should check before calling this.
Parameters|Type|Description
-|-|-
`event`|`string`|The event to perform
`owner`|`string`|Repository owner
`pullNumber`|`number`|Pull request number
`repo`|`string`|Repository name
`body`|`string` *optional*|The text of the review comment

---
#### Tool: **`unstar_repository`**
Unstar a GitHub repository
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`repo`|`string`|Repository name

---
#### Tool: **`update_gist`**
Update an existing gist
Parameters|Type|Description
-|-|-
`content`|`string`|Content for the file
`filename`|`string`|Filename to update or create
`gist_id`|`string`|ID of the gist to update
`description`|`string` *optional*|Updated description of the gist

---
#### Tool: **`update_issue`**
Update an existing issue in a GitHub repository.
Parameters|Type|Description
-|-|-
`issue_number`|`number`|Issue number to update
`owner`|`string`|Repository owner
`repo`|`string`|Repository name
`assignees`|`array` *optional*|New assignees
`body`|`string` *optional*|New description
`duplicate_of`|`number` *optional*|Issue number that this issue is a duplicate of. Only used when state_reason is 'duplicate'.
`labels`|`array` *optional*|New labels
`milestone`|`number` *optional*|New milestone number
`state`|`string` *optional*|New state
`state_reason`|`string` *optional*|Reason for the state change. Ignored unless state is changed.
`title`|`string` *optional*|New title
`type`|`string` *optional*|New issue type

---
#### Tool: **`update_pull_request`**
Update an existing pull request in a GitHub repository.
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`pullNumber`|`number`|Pull request number to update
`repo`|`string`|Repository name
`base`|`string` *optional*|New base branch name
`body`|`string` *optional*|New description
`draft`|`boolean` *optional*|Mark pull request as draft (true) or ready for review (false)
`maintainer_can_modify`|`boolean` *optional*|Allow maintainer edits
`reviewers`|`array` *optional*|GitHub usernames to request reviews from
`state`|`string` *optional*|New state
`title`|`string` *optional*|New title

---
#### Tool: **`update_pull_request_branch`**
Update the branch of a pull request with the latest changes from the base branch.
Parameters|Type|Description
-|-|-
`owner`|`string`|Repository owner
`pullNumber`|`number`|Pull request number
`repo`|`string`|Repository name
`expectedHeadSha`|`string` *optional*|The expected SHA of the pull request's HEAD ref

---
## Use this MCP Server

```json
{
  "mcpServers": {
    "github-official": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "GITHUB_PERSONAL_ACCESS_TOKEN",
        "ghcr.io/github/github-mcp-server"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "<YOUR_TOKEN>"
      }
    }
  }
}
```

[Why is it safer to run MCP Servers with Docker?](https://www.docker.com/blog/the-model-context-protocol-simplifying-building-ai-apps-with-anthropic-claude-desktop-and-docker/)
