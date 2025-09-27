# Gmail MCP Server MCP Server

A Model Context Protocol server for Gmail operations using IMAP/SMTP with app password authentication. Supports listing messages, searching emails, and sending messages.

[What is an MCP Server?](https://www.anthropic.com/news/model-context-protocol)

## Characteristics
Attribute|Details|
|-|-|
**Docker Image**|[yashtekwani/gmail-mcp](https://hub.docker.com/repository/docker/yashtekwani/gmail-mcp)
**Author**|[Sallytion](https://github.com/Sallytion)
**Repository**|https://github.com/Sallytion/Gmail-MCP
**Dockerfile**|https://github.com/Sallytion/Gmail-MCP/blob/main/Dockerfile
**Docker Image built by**|Sallytion
**Docker Scout Health Score**|Not available
**Verify Signature**|Not available
**Licence**|

## Available Tools (3)
Tools provided by this Server|Short Description
-|-
`listMessages`|List recent messages from Gmail inbox|
`findMessage`|Search for messages containing specific words or phrases|
`sendMessage`|Send an email message|

---
## Tools Details

#### Tool: **`listMessages`**
List recent messages from Gmail inbox
Parameters|Type|Description
-|-|-
`count`|`number`|Number of messages to retrieve (default: 10, max: 100)

---
#### Tool: **`findMessage`**
Search for messages containing specific words or phrases
Parameters|Type|Description
-|-|-
`query`|`string`|Search query (supports Gmail search syntax)

---
#### Tool: **`sendMessage`**
Send an email message
Parameters|Type|Description
-|-|-
`to`|`string`|Recipient email address
`subject`|`string`|Email subject
`body`|`string`|Email message body
`cc`|`string`|CC email address (optional)
`bcc`|`string`|BCC email address (optional)

---
## Use this MCP Server

```json
{
  "mcpServers": {
    "gmail-mcp": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "EMAIL_ADDRESS",
        "-e",
        "IMAP_HOST",
        "-e",
        "IMAP_PORT",
        "-e",
        "SMTP_HOST",
        "-e",
        "SMTP_PORT",
        "-e",
        "EMAIL_PASSWORD",
        "yashtekwani/gmail-mcp"
      ],
      "env": {
        "EMAIL_ADDRESS": "your-email@gmail.com",
        "IMAP_HOST": "imap.gmail.com",
        "IMAP_PORT": "993",
        "SMTP_HOST": "smtp.gmail.com",
        "SMTP_PORT": "587",
        "EMAIL_PASSWORD": "<your-gmail-app-password>"
      }
    }
  }
}
```

[Why is it safer to run MCP Servers with Docker?](https://www.docker.com/blog/the-model-context-protocol-simplifying-building-ai-apps-with-anthropic-claude-desktop-and-docker/)
