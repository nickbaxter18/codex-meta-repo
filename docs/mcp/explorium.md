# Explorium B2B Data MCP Server

Discover companies, contacts, and business insights—powered by dozens of trusted external data sources.

[What is an MCP Server?](https://www.anthropic.com/news/model-context-protocol)

## Characteristics
Attribute|Details|
|-|-|
**Docker Image**|[mcp/explorium](https://hub.docker.com/repository/docker/mcp/explorium)
**Author**|[explorium-ai](https://github.com/explorium-ai)
**Repository**|https://github.com/explorium-ai/mcp-explorium
**Dockerfile**|https://github.com/explorium-ai/mcp-explorium/blob/main/Dockerfile
**Docker Image built by**|Docker Inc.
**Docker Scout Health Score**| ![Docker Scout Health Score](https://api.scout.docker.com/v1/policy/insights/org-image-score/badge/mcp/explorium)
**Verify Signature**|`COSIGN_REPOSITORY=mcp/signatures cosign verify mcp/explorium --key https://raw.githubusercontent.com/docker/keyring/refs/heads/main/public/mcp/latest.pub`
**Licence**|MIT License

## Available Tools (12)
Tools provided by this Server|Short Description
-|-
`match-business`|Get the Explorium business IDs from business name and/or domain in bulk|
`fetch-businesses`|Fetch businesses from the Explorium API using filter criteria|
`fetch-businesses-statistics`|Fetch aggregated insights into businesses by industry, revenue, employee count, and geographic distribution|
`fetch-businesses-events`|Retrieves business-related events from the Explorium API in bulk|
`enrich-business`|Enriches business data using up to 5 parallel enrichment calls|
`match-prospects`|Match specific individuals to get their Explorium prospect IDs|
`fetch-prospects`|Fetch prospects (employees) from the Explorium API using detailed filter criteria|
`fetch-prospects-events`|Retrieves prospect-related events from the Explorium API in bulk|
`fetch-prospects-statistics`|Fetch aggregated insights into prospects by job department and geographic distribution|
`enrich-prospects`|Enriches prospect data using up to 3 parallel enrichment calls|
`autocomplete`|Autocomplete values for business filters based on a query|
`web-search`|Perform web search using Explorium Search capabilities|

---
## Tools Details

#### Tool: **`match-business`**
Get the Explorium business IDs from business name and/or domain in bulk
#### Tool: **`fetch-businesses`**
Fetch businesses from the Explorium API using filter criteria
#### Tool: **`fetch-businesses-statistics`**
Fetch aggregated insights into businesses by industry, revenue, employee count, and geographic distribution
#### Tool: **`fetch-businesses-events`**
Retrieves business-related events from the Explorium API in bulk
#### Tool: **`enrich-business`**
Enriches business data using up to 5 parallel enrichment calls
#### Tool: **`match-prospects`**
Match specific individuals to get their Explorium prospect IDs
#### Tool: **`fetch-prospects`**
Fetch prospects (employees) from the Explorium API using detailed filter criteria
#### Tool: **`fetch-prospects-events`**
Retrieves prospect-related events from the Explorium API in bulk
#### Tool: **`fetch-prospects-statistics`**
Fetch aggregated insights into prospects by job department and geographic distribution
#### Tool: **`enrich-prospects`**
Enriches prospect data using up to 3 parallel enrichment calls
#### Tool: **`autocomplete`**
Autocomplete values for business filters based on a query
#### Tool: **`web-search`**
Perform web search using Explorium Search capabilities
## Use this MCP Server

```json
{
  "mcpServers": {
    "explorium": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "API_ACCESS_TOKEN",
        "mcp/explorium"
      ],
      "env": {
        "API_ACCESS_TOKEN": "<API_TOKEN>"
      }
    }
  }
}
```

[Why is it safer to run MCP Servers with Docker?](https://www.docker.com/blog/the-model-context-protocol-simplifying-building-ai-apps-with-anthropic-claude-desktop-and-docker/)
