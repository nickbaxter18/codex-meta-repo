# Couchbase MCP Server

Couchbase is a distributed document database with a powerful search engine and in-built operational and analytical capabilities.

[What is an MCP Server?](https://www.anthropic.com/news/model-context-protocol)

## Characteristics
Attribute|Details|
|-|-|
**Docker Image**|[mcp/couchbase](https://hub.docker.com/repository/docker/mcp/couchbase)
**Author**|[Couchbase-Ecosystem](https://github.com/Couchbase-Ecosystem)
**Repository**|https://github.com/Couchbase-Ecosystem/mcp-server-couchbase
**Dockerfile**|https://github.com/Couchbase-Ecosystem/mcp-server-couchbase/blob/main/Dockerfile
**Docker Image built by**|Docker Inc.
**Docker Scout Health Score**| ![Docker Scout Health Score](https://api.scout.docker.com/v1/policy/insights/org-image-score/badge/mcp/couchbase)
**Verify Signature**|`COSIGN_REPOSITORY=mcp/signatures cosign verify mcp/couchbase --key https://raw.githubusercontent.com/docker/keyring/refs/heads/main/public/mcp/latest.pub`
**Licence**|Apache License 2.0

## Available Tools (11)
Tools provided by this Server|Short Description
-|-
`delete_document_by_id`|Delete a document by its ID.|
`get_buckets_in_cluster`|Get the names of all the accessible buckets in the cluster.|
`get_collections_in_scope`|Get the names of all collections in the given scope and bucket.|
`get_document_by_id`|Get a document by its ID from the specified scope and collection.|
`get_schema_for_collection`|Get the schema for a collection in the specified scope.|
`get_scopes_and_collections_in_bucket`|Get the names of all scopes and collections in the bucket.|
`get_scopes_in_bucket`|Get the names of all scopes in the given bucket.|
`get_server_configuration_status`|Get the server status and configuration without establishing connection.|
`run_sql_plus_plus_query`|Run a SQL++ query on a scope and return the results as a list of JSON objects.|
`test_cluster_connection`|Test the connection to Couchbase cluster and optionally to a bucket.|
`upsert_document_by_id`|Insert or update a document by its ID.|

---
## Tools Details

#### Tool: **`delete_document_by_id`**
Delete a document by its ID.
    Returns True on success, False on failure.
Parameters|Type|Description
-|-|-
`bucket_name`|`string`|
`collection_name`|`string`|
`document_id`|`string`|
`scope_name`|`string`|

---
#### Tool: **`get_buckets_in_cluster`**
Get the names of all the accessible buckets in the cluster.
#### Tool: **`get_collections_in_scope`**
Get the names of all collections in the given scope and bucket.
Parameters|Type|Description
-|-|-
`bucket_name`|`string`|
`scope_name`|`string`|

---
#### Tool: **`get_document_by_id`**
Get a document by its ID from the specified scope and collection.
    If the document is not found, it will raise an exception.
Parameters|Type|Description
-|-|-
`bucket_name`|`string`|
`collection_name`|`string`|
`document_id`|`string`|
`scope_name`|`string`|

---
#### Tool: **`get_schema_for_collection`**
Get the schema for a collection in the specified scope.
    Returns a dictionary with the collection name and the schema returned by running INFER query on the Couchbase collection.
Parameters|Type|Description
-|-|-
`bucket_name`|`string`|
`collection_name`|`string`|
`scope_name`|`string`|

---
#### Tool: **`get_scopes_and_collections_in_bucket`**
Get the names of all scopes and collections in the bucket.
    Returns a dictionary with scope names as keys and lists of collection names as values.
Parameters|Type|Description
-|-|-
`bucket_name`|`string`|

---
#### Tool: **`get_scopes_in_bucket`**
Get the names of all scopes in the given bucket.
Parameters|Type|Description
-|-|-
`bucket_name`|`string`|

---
#### Tool: **`get_server_configuration_status`**
Get the server status and configuration without establishing connection.
    This tool can be used to verify if the server is running and check the configuration.
#### Tool: **`run_sql_plus_plus_query`**
Run a SQL++ query on a scope and return the results as a list of JSON objects.
Parameters|Type|Description
-|-|-
`bucket_name`|`string`|
`query`|`string`|
`scope_name`|`string`|

---
#### Tool: **`test_cluster_connection`**
Test the connection to Couchbase cluster and optionally to a bucket.
    This tool verifies the connection to the Couchbase cluster and bucket by establishing the connection if it is not already established.
    If bucket name is not provided, it will not try to connect to the bucket specified in the MCP server settings.
    Returns connection status and basic cluster information.
Parameters|Type|Description
-|-|-
`bucket_name`|`string` *optional*|

---
#### Tool: **`upsert_document_by_id`**
Insert or update a document by its ID.
    Returns True on success, False on failure.
Parameters|Type|Description
-|-|-
`bucket_name`|`string`|
`collection_name`|`string`|
`document_content`|`object`|
`document_id`|`string`|
`scope_name`|`string`|

---
## Use this MCP Server

```json
{
  "mcpServers": {
    "couchbase": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "CB_CONNECTION_STRING",
        "-e",
        "CB_USERNAME",
        "-e",
        "CB_BUCKET_NAME",
        "-e",
        "CB_MCP_READ_ONLY_QUERY_MODE",
        "-e",
        "CB_PASSWORD",
        "mcp/couchbase"
      ],
      "env": {
        "CB_CONNECTION_STRING": "couchbases://cb.example.com",
        "CB_USERNAME": "Administrator",
        "CB_BUCKET_NAME": "my-bucket",
        "CB_MCP_READ_ONLY_QUERY_MODE": "true",
        "CB_PASSWORD": "<CB_PASSWORD>"
      }
    }
  }
}
```

[Why is it safer to run MCP Servers with Docker?](https://www.docker.com/blog/the-model-context-protocol-simplifying-building-ai-apps-with-anthropic-claude-desktop-and-docker/)
