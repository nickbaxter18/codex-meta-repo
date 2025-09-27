# Airtable MCP Server MCP Server

Provides AI assistants with direct access to Airtable bases, allowing them to read schemas, query records, and interact with your Airtable data. Supports listing bases, retrieving table structures, and searching through records to help automate workflows and answer questions about your organized data.

[What is an MCP Server?](https://www.anthropic.com/news/model-context-protocol)

## Characteristics
Attribute|Details|
|-|-|
**Docker Image**|[mcp/airtable-mcp-server](https://hub.docker.com/repository/docker/mcp/airtable-mcp-server)
**Author**|[domdomegg](https://github.com/domdomegg)
**Repository**|https://github.com/domdomegg/airtable-mcp-server
**Dockerfile**|https://github.com/domdomegg/airtable-mcp-server/blob/master/Dockerfile
**Docker Image built by**|Docker Inc.
**Docker Scout Health Score**| ![Docker Scout Health Score](https://api.scout.docker.com/v1/policy/insights/org-image-score/badge/mcp/airtable-mcp-server)
**Verify Signature**|`COSIGN_REPOSITORY=mcp/signatures cosign verify mcp/airtable-mcp-server --key https://raw.githubusercontent.com/docker/keyring/refs/heads/main/public/mcp/latest.pub`
**Licence**|MIT License

## Available Tools (13)
Tools provided by this Server|Short Description
-|-
`create_field`|Create a new field in a table|
`create_record`|Create a new record in a table|
`create_table`|Create a new table in a base|
`delete_records`|Delete records from a table|
`describe_table`|Get detailed information about a specific table|
`get_record`|Get a specific record by ID|
`list_bases`|List all accessible Airtable bases|
`list_records`|List records from a table|
`list_tables`|List all tables in a specific base|
`search_records`|Search for records containing specific text|
`update_field`|Update a field's name or description|
`update_records`|Update up to 10 records in a table|
`update_table`|Update a table's name or description|

---
## Tools Details

#### Tool: **`create_field`**
Create a new field in a table
Parameters|Type|Description
-|-|-
`baseId`|`string`|The ID of the base
`nested`|`object`|
`tableId`|`string`|The ID or name of the table

---
#### Tool: **`create_record`**
Create a new record in a table
Parameters|Type|Description
-|-|-
`baseId`|`string`|The ID of the base
`fields`|`object`|The fields for the new record
`tableId`|`string`|The ID or name of the table

---
#### Tool: **`create_table`**
Create a new table in a base
Parameters|Type|Description
-|-|-
`baseId`|`string`|The ID of the base
`fields`|`array`|Array of field definitions
`name`|`string`|The name of the table
`description`|`string` *optional*|Optional description for the table

---
#### Tool: **`delete_records`**
Delete records from a table
Parameters|Type|Description
-|-|-
`baseId`|`string`|The ID of the base
`recordIds`|`array`|Array of record IDs to delete
`tableId`|`string`|The ID or name of the table

---
#### Tool: **`describe_table`**
Get detailed information about a specific table
Parameters|Type|Description
-|-|-
`baseId`|`string`|The ID of the base
`tableId`|`string`|The ID or name of the table
`detailLevel`|`string` *optional*|Level of detail to return

---
#### Tool: **`get_record`**
Get a specific record by ID
Parameters|Type|Description
-|-|-
`baseId`|`string`|The ID of the base
`recordId`|`string`|The ID of the record
`tableId`|`string`|The ID or name of the table

---
#### Tool: **`list_bases`**
List all accessible Airtable bases
#### Tool: **`list_records`**
List records from a table
Parameters|Type|Description
-|-|-
`baseId`|`string`|The ID of the base
`tableId`|`string`|The ID or name of the table
`filterByFormula`|`string` *optional*|A formula used to filter records
`maxRecords`|`number` *optional*|The maximum total number of records that will be returned
`sort`|`array` *optional*|A list of sort objects that specifies how the records will be ordered
`view`|`string` *optional*|The name or ID of a view in the table

---
#### Tool: **`list_tables`**
List all tables in a specific base
Parameters|Type|Description
-|-|-
`baseId`|`string`|The ID of the base
`detailLevel`|`string` *optional*|Level of detail to return

---
#### Tool: **`search_records`**
Search for records containing specific text
Parameters|Type|Description
-|-|-
`baseId`|`string`|The ID of the base
`searchTerm`|`string`|The text to search for
`tableId`|`string`|The ID or name of the table
`fieldIds`|`array` *optional*|Optional array of field IDs to search in
`maxRecords`|`number` *optional*|The maximum total number of records that will be returned
`view`|`string` *optional*|The name or ID of a view in the table

---
#### Tool: **`update_field`**
Update a field's name or description
Parameters|Type|Description
-|-|-
`baseId`|`string`|The ID of the base
`fieldId`|`string`|The ID of the field
`tableId`|`string`|The ID or name of the table
`description`|`string` *optional*|New description for the field
`name`|`string` *optional*|New name for the field

---
#### Tool: **`update_records`**
Update up to 10 records in a table
Parameters|Type|Description
-|-|-
`baseId`|`string`|The ID of the base
`records`|`array`|Array of records to update (max 10)
`tableId`|`string`|The ID or name of the table

---
#### Tool: **`update_table`**
Update a table's name or description
Parameters|Type|Description
-|-|-
`baseId`|`string`|The ID of the base
`tableId`|`string`|The ID or name of the table
`description`|`string` *optional*|New description for the table
`name`|`string` *optional*|New name for the table

---
## Use this MCP Server

```json
{
  "mcpServers": {
    "airtable-mcp-server": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "NODE_ENV",
        "-e",
        "AIRTABLE_API_KEY",
        "mcp/airtable-mcp-server"
      ],
      "env": {
        "NODE_ENV": "production",
        "AIRTABLE_API_KEY": "patABC123.def456ghi789jkl012mno345pqr678stu901vwx"
      }
    }
  }
}
```

[Why is it safer to run MCP Servers with Docker?](https://www.docker.com/blog/the-model-context-protocol-simplifying-building-ai-apps-with-anthropic-claude-desktop-and-docker/)
