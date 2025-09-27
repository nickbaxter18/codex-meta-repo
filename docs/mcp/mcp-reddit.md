# Mcp reddit MCP Server

A comprehensive Model Context Protocol (MCP) server for Reddit integration. This server enables AI agents to interact with Reddit programmatically through a standardized interface.

[What is an MCP Server?](https://www.anthropic.com/news/model-context-protocol)

## Characteristics
Attribute|Details|
|-|-|
**Docker Image**|[mcp/reddit-mcp](https://hub.docker.com/repository/docker/mcp/reddit-mcp)
**Author**|[KrishnaRandad2023](https://github.com/KrishnaRandad2023)
**Repository**|https://github.com/KrishnaRandad2023/mcp-reddit
**Dockerfile**|https://github.com/KrishnaRandad2023/mcp-reddit/blob/main/Dockerfile
**Docker Image built by**|Docker Inc.
**Docker Scout Health Score**| ![Docker Scout Health Score](https://api.scout.docker.com/v1/policy/insights/org-image-score/badge/mcp/reddit-mcp)
**Verify Signature**|`COSIGN_REPOSITORY=mcp/signatures cosign verify mcp/reddit-mcp --key https://raw.githubusercontent.com/docker/keyring/refs/heads/main/public/mcp/latest.pub`
**Licence**|MIT License

## Available Tools (6)
Tools provided by this Server|Short Description
-|-
`fetchPosts`|Fetch hot posts from a subreddit|
`getComments`|Get comments for a specific Reddit post|
`getSubredditInfo`|Get information about a subreddit|
`postComment`|Post a comment on a Reddit post|
`postToSubreddit`|Create a new post in a subreddit|
`searchPosts`|Search for posts within a subreddit|

---
## Tools Details

#### Tool: **`fetchPosts`**
Fetch hot posts from a subreddit
Parameters|Type|Description
-|-|-
`subreddit`|`string`|Name of the subreddit
`limit`|`integer` *optional*|Number of posts to fetch (1-100)

---
#### Tool: **`getComments`**
Get comments for a specific Reddit post
Parameters|Type|Description
-|-|-
`post_id`|`string`|Reddit post ID (without 't3_' prefix)

---
#### Tool: **`getSubredditInfo`**
Get information about a subreddit
Parameters|Type|Description
-|-|-
`subreddit`|`string`|Name of the subreddit

---
#### Tool: **`postComment`**
Post a comment on a Reddit post
Parameters|Type|Description
-|-|-
`comment_text`|`string`|Comment text to post
`post_id`|`string`|Reddit post ID (without 't3_' prefix)

---
#### Tool: **`postToSubreddit`**
Create a new post in a subreddit
Parameters|Type|Description
-|-|-
`subreddit`|`string`|Name of the subreddit
`title`|`string`|Post title
`content`|`string` *optional*|Post content (for text posts)
`url`|`string` *optional*|URL (for link posts)

---
#### Tool: **`searchPosts`**
Search for posts within a subreddit
Parameters|Type|Description
-|-|-
`query`|`string`|Search query
`subreddit`|`string`|Name of the subreddit
`limit`|`integer` *optional*|Number of results to return (1-100)

---
## Use this MCP Server

```json
{
  "mcpServers": {
    "mcp-reddit": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "USERNAME",
        "-e",
        "REDDIT_CLIENT_ID",
        "-e",
        "REDDIT_CLIENT_SECRET",
        "-e",
        "REDDIT_PASSWORD",
        "mcp/reddit-mcp"
      ],
      "env": {
        "USERNAME": "yourRedditUsername",
        "REDDIT_CLIENT_ID": "<REDDIT_CLIENT_ID>",
        "REDDIT_CLIENT_SECRET": "<REDDIT_CLIENT_SECRET>",
        "REDDIT_PASSWORD": "<REDDIT_PASSWORD>"
      }
    }
  }
}
```

[Why is it safer to run MCP Servers with Docker?](https://www.docker.com/blog/the-model-context-protocol-simplifying-building-ai-apps-with-anthropic-claude-desktop-and-docker/)
