# Grafana MCP Server

MCP server for Grafana.

[What is an MCP Server?](https://www.anthropic.com/news/model-context-protocol)

## Characteristics
Attribute|Details|
|-|-|
**Docker Image**|[mcp/grafana](https://hub.docker.com/repository/docker/mcp/grafana)
**Author**|[grafana](https://github.com/grafana)
**Repository**|https://github.com/grafana/mcp-grafana
**Dockerfile**|https://github.com/grafana/mcp-grafana/blob/main/Dockerfile
**Docker Image built by**|Docker Inc.
**Docker Scout Health Score**| ![Docker Scout Health Score](https://api.scout.docker.com/v1/policy/insights/org-image-score/badge/mcp/grafana)
**Verify Signature**|`COSIGN_REPOSITORY=mcp/signatures cosign verify mcp/grafana --key https://raw.githubusercontent.com/docker/keyring/refs/heads/main/public/mcp/latest.pub`
**Licence**|Apache License 2.0

## Available Tools (45)
Tools provided by this Server|Short Description
-|-
`add_activity_to_incident`|Add activity to incident|
`create_incident`|Create incident|
`fetch_pyroscope_profile`|Fetch Pyroscope profile|
`find_error_pattern_logs`|Find error patterns in logs|
`find_slow_requests`|Find slow requests|
`generate_deeplink`|Generate navigation deeplink|
`get_alert_group`|Get IRM alert group|
`get_alert_rule_by_uid`|Get alert rule details|
`get_assertions`|Get assertions summary|
`get_current_oncall_users`|Get current on-call users|
`get_dashboard_by_uid`|Get dashboard details|
`get_dashboard_panel_queries`|Get dashboard panel queries|
`get_dashboard_property`|Get dashboard property|
`get_dashboard_summary`|Get dashboard summary|
`get_datasource_by_name`|Get datasource by name|
`get_datasource_by_uid`|Get datasource by UID|
`get_incident`|Get incident details|
`get_oncall_shift`|Get OnCall shift|
`get_sift_analysis`|Get Sift analysis|
`get_sift_investigation`|Get Sift investigation|
`list_alert_groups`|List IRM alert groups|
`list_alert_rules`|List alert rules|
`list_contact_points`|List notification contact points|
`list_datasources`|List datasources|
`list_incidents`|List incidents|
`list_loki_label_names`|List Loki label names|
`list_loki_label_values`|List Loki label values|
`list_oncall_schedules`|List OnCall schedules|
`list_oncall_teams`|List OnCall teams|
`list_oncall_users`|List OnCall users|
`list_prometheus_label_names`|List Prometheus label names|
`list_prometheus_label_values`|List Prometheus label values|
`list_prometheus_metric_metadata`|List Prometheus metric metadata|
`list_prometheus_metric_names`|List Prometheus metric names|
`list_pyroscope_label_names`|List Pyroscope label names|
`list_pyroscope_label_values`|List Pyroscope label values|
`list_pyroscope_profile_types`|List Pyroscope profile types|
`list_sift_investigations`|List Sift investigations|
`list_teams`|List teams|
`list_users_by_org`|List users by org|
`query_loki_logs`|Query Loki logs|
`query_loki_stats`|Get Loki log statistics|
`query_prometheus`|Query Prometheus metrics|
`search_dashboards`|Search dashboards|
`update_dashboard`|Create or update dashboard|

---
## Tools Details

#### Tool: **`add_activity_to_incident`**
Add a note (userNote activity) to an existing incident's timeline using its ID. The note body can include URLs which will be attached as context. Use this to add context to an incident.
Parameters|Type|Description
-|-|-
`body`|`string` *optional*|The body of the activity. URLs will be parsed and attached as context
`eventTime`|`string` *optional*|The time that the activity occurred. If not provided, the current time will be used
`incidentId`|`string` *optional*|The ID of the incident to add the activity to

---
#### Tool: **`create_incident`**
Create a new Grafana incident. Requires title, severity, and room prefix. Allows setting status and labels. This tool should be used judiciously and sparingly, and only after confirmation from the user, as it may notify or alarm lots of people.
Parameters|Type|Description
-|-|-
`attachCaption`|`string` *optional*|The caption of the attachment
`attachUrl`|`string` *optional*|The URL of the attachment
`isDrill`|`boolean` *optional*|Whether the incident is a drill incident
`labels`|`array` *optional*|The labels to add to the incident
`roomPrefix`|`string` *optional*|The prefix of the room to create the incident in
`severity`|`string` *optional*|The severity of the incident
`status`|`string` *optional*|The status of the incident
`title`|`string` *optional*|The title of the incident

---
#### Tool: **`fetch_pyroscope_profile`**
Fetches a profile from a Pyroscope data source for a given time range. By default, the time range is tha past 1 hour.
The profile type is required, available profile types can be fetched via the list_pyroscope_profile_types tool. Not all
profile types are available for every service. Expect some queries to return empty result sets, this indicates the
profile type does not exist for that query. In such a case, consider trying a related profile type or giving up.
Matchers are not required, but highly recommended, they are generally used to select an application by the service_name
label (e.g. {service_name="foo"}). Use the list_pyroscope_label_names tool to fetch available label names, and the
list_pyroscope_label_values tool to fetch available label values. The returned profile is in DOT format.
Parameters|Type|Description
-|-|-
`data_source_uid`|`string`|The UID of the datasource to query
`profile_type`|`string`|Type profile type, use the list_pyroscope_profile_types tool to fetch available profile types
`end_rfc_3339`|`string` *optional*|Optionally, the end time of the query in RFC3339 format (defaults to now)
`matchers`|`string` *optional*|Optionally, Prometheus style matchers used to filter the result set (defaults to: {})
`max_node_depth`|`integer` *optional*|Optionally, the maximum depth of nodes in the resulting profile. Less depth results in smaller profiles that execute faster, more depth result in larger profiles that have more detail. A value of -1 indicates to use an unbounded node depth (default: 100). Reducing max node depth from the default will negatively impact the accuracy of the profile
`start_rfc_3339`|`string` *optional*|Optionally, the start time of the query in RFC3339 format (defaults to 1 hour ago)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`find_error_pattern_logs`**
Searches Loki logs for elevated error patterns compared to the last day's average, waits for the analysis to complete, and returns the results including any patterns found.
Parameters|Type|Description
-|-|-
`labels`|`object`|Labels to scope the analysis
`name`|`string`|The name of the investigation
`end`|`string` *optional*|End time for the investigation. Defaults to now if not specified.
`start`|`string` *optional*|Start time for the investigation. Defaults to 30 minutes ago if not specified.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`find_slow_requests`**
Searches relevant Tempo datasources for slow requests, waits for the analysis to complete, and returns the results.
Parameters|Type|Description
-|-|-
`labels`|`object`|Labels to scope the analysis
`name`|`string`|The name of the investigation
`end`|`string` *optional*|End time for the investigation. Defaults to now if not specified.
`start`|`string` *optional*|Start time for the investigation. Defaults to 30 minutes ago if not specified.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`generate_deeplink`**
Generate deeplink URLs for Grafana resources. Supports dashboards (requires dashboardUid), panels (requires dashboardUid and panelId), and Explore queries (requires datasourceUid). Optionally accepts time range and additional query parameters.
Parameters|Type|Description
-|-|-
`resourceType`|`string`|Type of resource: dashboard, panel, or explore
`dashboardUid`|`string` *optional*|Dashboard UID (required for dashboard and panel types)
`datasourceUid`|`string` *optional*|Datasource UID (required for explore type)
`panelId`|`integer` *optional*|Panel ID (required for panel type)
`queryParams`|`object` *optional*|Additional query parameters
`timeRange`|`object` *optional*|Time range for the link

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_alert_group`**
Get a specific alert group from Grafana OnCall by its ID. Returns the full alert group details.
Parameters|Type|Description
-|-|-
`alertGroupId`|`string`|The ID of the alert group to retrieve

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_alert_rule_by_uid`**
Retrieves the full configuration and detailed status of a specific Grafana alert rule identified by its unique ID (UID). The response includes fields like title, condition, query data, folder UID, rule group, state settings (no data, error), evaluation interval, annotations, and labels.
Parameters|Type|Description
-|-|-
`uid`|`string`|The uid of the alert rule

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_assertions`**
Get assertion summary for a given entity with its type, name, env, site, namespace, and a time range
Parameters|Type|Description
-|-|-
`endTime`|`string`|The end time in RFC3339 format
`startTime`|`string`|The start time in RFC3339 format
`entityName`|`string` *optional*|The name of the entity to list
`entityType`|`string` *optional*|The type of the entity to list (e.g. Service, Node, Pod, etc.)
`env`|`string` *optional*|The env of the entity to list
`namespace`|`string` *optional*|The namespace of the entity to list
`site`|`string` *optional*|The site of the entity to list

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_current_oncall_users`**
Get the list of users currently on-call for a specific Grafana OnCall schedule ID. Returns the schedule ID, name, and a list of detailed user objects for those currently on call.
Parameters|Type|Description
-|-|-
`scheduleId`|`string`|The ID of the schedule to get current on-call users for

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_dashboard_by_uid`**
Retrieves the complete dashboard, including panels, variables, and settings, for a specific dashboard identified by its UID. WARNING: Large dashboards can consume significant context window space. Consider using get_dashboard_summary for overview or get_dashboard_property for specific data instead.
Parameters|Type|Description
-|-|-
`uid`|`string`|The UID of the dashboard

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_dashboard_panel_queries`**
Use this tool to retrieve panel queries and information from a Grafana dashboard. When asked about panel queries, queries in a dashboard, or what queries a dashboard contains, call this tool with the dashboard UID. The datasource is an object with fields `uid` (which may be a concrete UID or a template variable like "$datasource") and `type`. If the datasource UID is a template variable, it won't be usable directly for queries. Returns an array of objects, each representing a panel, with fields: title, query, and datasource (an object with uid and type).
Parameters|Type|Description
-|-|-
`uid`|`string`|The UID of the dashboard

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_dashboard_property`**
Get specific parts of a dashboard using JSONPath expressions to minimize context window usage. Common paths: '$.title' (title)\, '$.panels[*].title' (all panel titles)\, '$.panels[0]' (first panel)\, '$.templating.list' (variables)\, '$.tags' (tags)\, '$.panels[*].targets[*].expr' (all queries). Use this instead of get_dashboard_by_uid when you only need specific dashboard properties.
Parameters|Type|Description
-|-|-
`jsonPath`|`string`|JSONPath expression to extract specific data (e.g., '$.panels[0].title' for first panel title, '$.panels[*].title' for all panel titles, '$.templating.list' for variables)
`uid`|`string`|The UID of the dashboard

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_dashboard_summary`**
Get a compact summary of a dashboard including title\, panel count\, panel types\, variables\, and other metadata without the full JSON. Use this for dashboard overview and planning modifications without consuming large context windows.
Parameters|Type|Description
-|-|-
`uid`|`string`|The UID of the dashboard

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_datasource_by_name`**
Retrieves detailed information about a specific datasource using its name. Returns the full datasource model, including UID, type, URL, access settings, JSON data, and secure JSON field status.
Parameters|Type|Description
-|-|-
`name`|`string`|The name of the datasource

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_datasource_by_uid`**
Retrieves detailed information about a specific datasource using its UID. Returns the full datasource model, including name, type, URL, access settings, JSON data, and secure JSON field status.
Parameters|Type|Description
-|-|-
`uid`|`string`|The uid of the datasource

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_incident`**
Get a single incident by ID. Returns the full incident details including title, status, severity, labels, timestamps, and other metadata.
Parameters|Type|Description
-|-|-
`id`|`string` *optional*|The ID of the incident to retrieve

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_oncall_shift`**
Get detailed information for a specific Grafana OnCall shift using its ID. A shift represents a designated time period within a schedule when users are actively on-call. Returns the full shift details.
Parameters|Type|Description
-|-|-
`shiftId`|`string`|The ID of the shift to get details for

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_sift_analysis`**
Retrieves a specific analysis from an investigation by its UUID. The investigation ID and analysis ID should be provided as strings in UUID format.
Parameters|Type|Description
-|-|-
`analysisId`|`string`|The UUID of the specific analysis to retrieve
`investigationId`|`string`|The UUID of the investigation as a string (e.g. '02adab7c-bf5b-45f2-9459-d71a2c29e11b')

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`get_sift_investigation`**
Retrieves an existing Sift investigation by its UUID. The ID should be provided as a string in UUID format (e.g. '02adab7c-bf5b-45f2-9459-d71a2c29e11b').
Parameters|Type|Description
-|-|-
`id`|`string`|The UUID of the investigation as a string (e.g. '02adab7c-bf5b-45f2-9459-d71a2c29e11b')

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_alert_groups`**
List alert groups from Grafana OnCall with filtering options. Supports filtering by alert group ID, route ID, integration ID, state (new, acknowledged, resolved, silenced), team ID, time range, labels, and name. For time ranges, use format '{start}_{end}' ISO 8601 timestamp range (e.g., '2025-01-19T00:00:00_2025-01-19T23:59:59' for a specific day). For labels, use format 'key:value' (e.g., ['env:prod', 'severity:high']). Returns a list of alert group objects with their details. Supports pagination.
Parameters|Type|Description
-|-|-
`id`|`string` *optional*|Filter by specific alert group ID
`integrationId`|`string` *optional*|Filter by integration ID
`labels`|`array` *optional*|Filter by labels in format key:value (e.g., ['env:prod', 'severity:high'])
`name`|`string` *optional*|Filter by alert group name
`page`|`integer` *optional*|The page number to return
`routeId`|`string` *optional*|Filter by route ID
`startedAt`|`string` *optional*|Filter by time range in format '{start}_{end}' ISO 8601 timestamp range (UTC assumed, no timezone indicator needed) (e.g., '2025-01-19T00:00:00_2025-01-19T23:59:59')
`state`|`string` *optional*|Filter by alert group state (one of: new, acknowledged, resolved, silenced)
`teamId`|`string` *optional*|Filter by team ID

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_alert_rules`**
Lists Grafana alert rules, returning a summary including UID, title, current state (e.g., 'pending', 'firing', 'inactive'), and labels. Supports filtering by labels using selectors and pagination. Example label selector: `[{'name': 'severity', 'type': '=', 'value': 'critical'}]`. Inactive state means the alert state is normal, not firing
Parameters|Type|Description
-|-|-
`label_selectors`|`array` *optional*|Optionally, a list of matchers to filter alert rules by labels
`limit`|`integer` *optional*|The maximum number of results to return. Default is 100.
`page`|`integer` *optional*|The page number to return.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_contact_points`**
Lists Grafana notification contact points, returning a summary including UID, name, and type for each. Supports filtering by name - exact match - and limiting the number of results.
Parameters|Type|Description
-|-|-
`limit`|`integer` *optional*|The maximum number of results to return. Default is 100.
`name`|`string` *optional*|Filter contact points by name

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_datasources`**
List available Grafana datasources. Optionally filter by datasource type (e.g., 'prometheus', 'loki'). Returns a summary list including ID, UID, name, type, and default status.
Parameters|Type|Description
-|-|-
`type`|`string` *optional*|The type of datasources to search for. For example, 'prometheus', 'loki', 'tempo', etc...

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_incidents`**
List Grafana incidents. Allows filtering by status ('active', 'resolved') and optionally including drill incidents. Returns a preview list with basic details.
Parameters|Type|Description
-|-|-
`drill`|`boolean` *optional*|Whether to include drill incidents
`limit`|`integer` *optional*|The maximum number of incidents to return
`status`|`string` *optional*|The status of the incidents to include. Valid values: 'active', 'resolved'

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_loki_label_names`**
Lists all available label names (keys) found in logs within a specified Loki datasource and time range. Returns a list of unique label strings (e.g., `["app", "env", "pod"]`). If the time range is not provided, it defaults to the last hour.
Parameters|Type|Description
-|-|-
`datasourceUid`|`string`|The UID of the datasource to query
`endRfc3339`|`string` *optional*|Optionally, the end time of the query in RFC3339 format (defaults to now)
`startRfc3339`|`string` *optional*|Optionally, the start time of the query in RFC3339 format (defaults to 1 hour ago)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_loki_label_values`**
Retrieves all unique values associated with a specific `labelName` within a Loki datasource and time range. Returns a list of string values (e.g., for `labelName="env"`, might return `["prod", "staging", "dev"]`). Useful for discovering filter options. Defaults to the last hour if the time range is omitted.
Parameters|Type|Description
-|-|-
`datasourceUid`|`string`|The UID of the datasource to query
`labelName`|`string`|The name of the label to retrieve values for (e.g. 'app', 'env', 'pod')
`endRfc3339`|`string` *optional*|Optionally, the end time of the query in RFC3339 format (defaults to now)
`startRfc3339`|`string` *optional*|Optionally, the start time of the query in RFC3339 format (defaults to 1 hour ago)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_oncall_schedules`**
List Grafana OnCall schedules, optionally filtering by team ID. If a specific schedule ID is provided, retrieves details for only that schedule. Returns a list of schedule summaries including ID, name, team ID, timezone, and shift IDs. Supports pagination.
Parameters|Type|Description
-|-|-
`page`|`integer` *optional*|The page number to return (1-based)
`scheduleId`|`string` *optional*|The ID of the schedule to get details for. If provided, returns only that schedule's details
`teamId`|`string` *optional*|The ID of the team to list schedules for

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_oncall_teams`**
List teams configured in Grafana OnCall. Returns a list of team objects with their details. Supports pagination.
Parameters|Type|Description
-|-|-
`page`|`integer` *optional*|The page number to return

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_oncall_users`**
List users from Grafana OnCall. Can retrieve all users, a specific user by ID, or filter by username. Returns a list of user objects with their details. Supports pagination.
Parameters|Type|Description
-|-|-
`page`|`integer` *optional*|The page number to return
`userId`|`string` *optional*|The ID of the user to get details for. If provided, returns only that user's details
`username`|`string` *optional*|The username to filter users by. If provided, returns only the user matching this username

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_prometheus_label_names`**
List label names in a Prometheus datasource. Allows filtering by series selectors and time range.
Parameters|Type|Description
-|-|-
`datasourceUid`|`string`|The UID of the datasource to query
`endRfc3339`|`string` *optional*|Optionally, the end time of the time range to filter the results by
`limit`|`integer` *optional*|Optionally, the maximum number of results to return
`matches`|`array` *optional*|Optionally, a list of label matchers to filter the results by
`startRfc3339`|`string` *optional*|Optionally, the start time of the time range to filter the results by

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_prometheus_label_values`**
Get the values for a specific label name in Prometheus. Allows filtering by series selectors and time range.
Parameters|Type|Description
-|-|-
`datasourceUid`|`string`|The UID of the datasource to query
`labelName`|`string`|The name of the label to query
`endRfc3339`|`string` *optional*|Optionally, the end time of the query
`limit`|`integer` *optional*|Optionally, the maximum number of results to return
`matches`|`array` *optional*|Optionally, a list of selectors to filter the results by
`startRfc3339`|`string` *optional*|Optionally, the start time of the query

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_prometheus_metric_metadata`**
List Prometheus metric metadata. Returns metadata about metrics currently scraped from targets. Note: This endpoint is experimental.
Parameters|Type|Description
-|-|-
`datasourceUid`|`string`|The UID of the datasource to query
`limit`|`integer` *optional*|The maximum number of metrics to return
`limitPerMetric`|`integer` *optional*|The maximum number of metrics to return per metric
`metric`|`string` *optional*|The metric to query

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_prometheus_metric_names`**
List metric names in a Prometheus datasource. Retrieves all metric names and then filters them locally using the provided regex. Supports pagination.
Parameters|Type|Description
-|-|-
`datasourceUid`|`string`|The UID of the datasource to query
`limit`|`integer` *optional*|The maximum number of results to return
`page`|`integer` *optional*|The page number to return
`regex`|`string` *optional*|The regex to match against the metric names

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_pyroscope_label_names`**
Lists all available label names (keys) found in profiles within a specified Pyroscope datasource, time range, and
optional label matchers. Label matchers are typically used to qualify a service name ({service_name="foo"}). Returns a
list of unique label strings (e.g., ["app", "env", "pod"]). Label names with double underscores (e.g. __name__) are
internal and rarely useful to users. If the time range is not provided, it defaults to the last hour.
Parameters|Type|Description
-|-|-
`data_source_uid`|`string`|The UID of the datasource to query
`end_rfc_3339`|`string` *optional*|Optionally, the end time of the query in RFC3339 format (defaults to now)
`matchers`|`string` *optional*|
`start_rfc_3339`|`string` *optional*|Optionally, the start time of the query in RFC3339 format (defaults to 1 hour ago)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_pyroscope_label_values`**
Lists all available label values for a particular label name found in profiles within a specified Pyroscope datasource,
time range, and optional label matchers. Label matchers are typically used to qualify a service name ({service_name="foo"}).
Returns a list of unique label strings (e.g. for label name "env": ["dev", "staging", "prod"]). If the time range
is not provided, it defaults to the last hour.
Parameters|Type|Description
-|-|-
`data_source_uid`|`string`|The UID of the datasource to query
`name`|`string`|A label name
`end_rfc_3339`|`string` *optional*|Optionally, the end time of the query in RFC3339 format (defaults to now)
`matchers`|`string` *optional*|Optionally, Prometheus style matchers used to filter the result set (defaults to: {})
`start_rfc_3339`|`string` *optional*|Optionally, the start time of the query in RFC3339 format (defaults to 1 hour ago)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_pyroscope_profile_types`**
Lists all available profile types available in a specified Pyroscope datasource and time range. Returns a list of all
available profile types (example profile type: "process_cpu:cpu:nanoseconds:cpu:nanoseconds"). A profile type has the
following structure: <name>:<sample type>:<sample unit>:<period type>:<period unit>. Not all profile types are available
for every service. If the time range is not provided, it defaults to the last hour.
Parameters|Type|Description
-|-|-
`data_source_uid`|`string`|The UID of the datasource to query
`end_rfc_3339`|`string` *optional*|Optionally, the end time of the query in RFC3339 format (defaults to now)
`start_rfc_3339`|`string` *optional*|Optionally, the start time of the query in RFC3339 format (defaults to 1 hour ago)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_sift_investigations`**
Retrieves a list of Sift investigations with an optional limit. If no limit is specified, defaults to 10 investigations.
Parameters|Type|Description
-|-|-
`limit`|`integer` *optional*|Maximum number of investigations to return. Defaults to 10 if not specified.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_teams`**
Search for Grafana teams by a query string. Returns a list of matching teams with details like name, ID, and URL.
Parameters|Type|Description
-|-|-
`query`|`string` *optional*|The query to search for teams. Can be left empty to fetch all teams

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`list_users_by_org`**
List users by organization. Returns a list of users with details like userid, email, role etc.
#### Tool: **`query_loki_logs`**
Executes a LogQL query against a Loki datasource to retrieve log entries or metric values. Returns a list of results, each containing a timestamp, labels, and either a log line (`line`) or a numeric metric value (`value`). Defaults to the last hour, a limit of 10 entries, and 'backward' direction (newest first). Supports full LogQL syntax for log and metric queries (e.g., `{app="foo"} |= "error"`, `rate({app="bar"}[1m])`). Prefer using `query_loki_stats` first to check stream size and `list_loki_label_names` and `list_loki_label_values` to verify labels exist.
Parameters|Type|Description
-|-|-
`datasourceUid`|`string`|The UID of the datasource to query
`logql`|`string`|The LogQL query to execute against Loki. This can be a simple label matcher or a complex query with filters, parsers, and expressions. Supports full LogQL syntax including label matchers, filter operators, pattern expressions, and pipeline operations.
`direction`|`string` *optional*|Optionally, the direction of the query: 'forward' (oldest first) or 'backward' (newest first, default)
`endRfc3339`|`string` *optional*|Optionally, the end time of the query in RFC3339 format
`limit`|`integer` *optional*|Optionally, the maximum number of log lines to return (default: 10, max: 100)
`startRfc3339`|`string` *optional*|Optionally, the start time of the query in RFC3339 format

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`query_loki_stats`**
Retrieves statistics about log streams matching a given LogQL *selector* within a Loki datasource and time range. Returns an object containing the count of streams, chunks, entries, and total bytes (e.g., `{"streams": 5, "chunks": 50, "entries": 10000, "bytes": 512000}`). The `logql` parameter **must** be a simple label selector (e.g., `{app="nginx", env="prod"}`) and does not support line filters, parsers, or aggregations. Defaults to the last hour if the time range is omitted.
Parameters|Type|Description
-|-|-
`datasourceUid`|`string`|The UID of the datasource to query
`logql`|`string`|The LogQL matcher expression to execute. This parameter only accepts label matcher expressions and does not support full LogQL queries. Line filters, pattern operations, and metric aggregations are not supported by the stats API endpoint. Only simple label selectors can be used here.
`endRfc3339`|`string` *optional*|Optionally, the end time of the query in RFC3339 format
`startRfc3339`|`string` *optional*|Optionally, the start time of the query in RFC3339 format

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`query_prometheus`**
Query Prometheus using a PromQL expression. Supports both instant queries (at a single point in time) and range queries (over a time range). Time can be specified either in RFC3339 format or as relative time expressions like 'now', 'now-1h', 'now-30m', etc.
Parameters|Type|Description
-|-|-
`datasourceUid`|`string`|The UID of the datasource to query
`expr`|`string`|The PromQL expression to query
`startTime`|`string`|The start time. Supported formats are RFC3339 or relative to now (e.g. 'now', 'now-1.5h', 'now-2h45m'). Valid time units are 'ns', 'us' (or 'µs'), 'ms', 's', 'm', 'h', 'd'.
`endTime`|`string` *optional*|The end time. Required if queryType is 'range', ignored if queryType is 'instant' Supported formats are RFC3339 or relative to now (e.g. 'now', 'now-1.5h', 'now-2h45m'). Valid time units are 'ns', 'us' (or 'µs'), 'ms', 's', 'm', 'h', 'd'.
`queryType`|`string` *optional*|The type of query to use. Either 'range' or 'instant'
`stepSeconds`|`integer` *optional*|The time series step size in seconds. Required if queryType is 'range', ignored if queryType is 'instant'

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`search_dashboards`**
Search for Grafana dashboards by a query string. Returns a list of matching dashboards with details like title, UID, folder, tags, and URL.
Parameters|Type|Description
-|-|-
`query`|`string` *optional*|The query to search for

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`update_dashboard`**
Create or update a dashboard using either full JSON or efficient patch operations. For new dashboards\, provide the 'dashboard' field. For updating existing dashboards\, use 'uid' + 'operations' for better context window efficiency. Patch operations support complex JSONPaths like '$.panels[0].targets[0].expr'\, '$.panels[1].title'\, '$.panels[2].targets[0].datasource'\, etc. Supports appending to arrays using '/- ' syntax: '$.panels/- ' appends to panels array\, '$.panels[2]/- ' appends to nested array at index 2.
Parameters|Type|Description
-|-|-
`dashboard`|`object` *optional*|The full dashboard JSON. Use for creating new dashboards or complete updates. Large dashboards consume significant context - consider using patches for small changes.
`folderUid`|`string` *optional*|The UID of the dashboard's folder
`message`|`string` *optional*|Set a commit message for the version history
`operations`|`array` *optional*|Array of patch operations for targeted updates. More efficient than full dashboard JSON for small changes.
`overwrite`|`boolean` *optional*|Overwrite the dashboard if it exists. Otherwise create one
`uid`|`string` *optional*|UID of existing dashboard to update. Required when using patch operations.
`userId`|`integer` *optional*|ID of the user making the change

*This tool may perform destructive updates.*

---
## Use this MCP Server

```json
{
  "mcpServers": {
    "grafana": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "GRAFANA_URL",
        "-e",
        "GRAFANA_API_KEY",
        "mcp/grafana",
        "--transport=stdio"
      ],
      "env": {
        "GRAFANA_URL": "http://localhost:3000",
        "GRAFANA_API_KEY": "<your service account token>"
      }
    }
  }
}
```

[Why is it safer to run MCP Servers with Docker?](https://www.docker.com/blog/the-model-context-protocol-simplifying-building-ai-apps-with-anthropic-claude-desktop-and-docker/)
