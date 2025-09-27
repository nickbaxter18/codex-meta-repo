# Docker Hub MCP Server

Docker Hub official MCP server.

[What is an MCP Server?](https://www.anthropic.com/news/model-context-protocol)

## Characteristics
Attribute|Details|
|-|-|
**Docker Image**|[mcp/dockerhub](https://hub.docker.com/repository/docker/mcp/dockerhub)
**Author**|[docker](https://github.com/docker)
**Repository**|https://github.com/docker/hub-mcp
**Dockerfile**|https://github.com/docker/hub-mcp/blob/main/Dockerfile
**Docker Image built by**|Docker Inc.
**Docker Scout Health Score**| ![Docker Scout Health Score](https://api.scout.docker.com/v1/policy/insights/org-image-score/badge/mcp/dockerhub)
**Verify Signature**|`COSIGN_REPOSITORY=mcp/signatures cosign verify mcp/dockerhub --key https://raw.githubusercontent.com/docker/keyring/refs/heads/main/public/mcp/latest.pub`
**Licence**|Apache License 2.0

## Available Tools (13)
Tools provided by this Server|Short Description
-|-
`checkRepository`|Check Repository Exists|
`checkRepositoryTag`|Check Repository Tag|
`createRepository`|Create Repository in namespace|
`dockerHardenedImages`|List available Docker Hardened Images|
`getPersonalNamespace`|Get Personal Namespace|
`getRepositoryInfo`|Get Repository Info|
`getRepositoryTag`|Get Repository Tag|
`listAllNamespacesMemberOf`|List All Namespaces user is a member of|
`listNamespaces`|List Namespaces|
`listRepositoriesByNamespace`|List Repositories by Namespace|
`listRepositoryTags`|List Repository Tags|
`search`|Search Repositories|
`updateRepositoryInfo`|Get Repository Info|

---
## Tools Details

#### Tool: **`checkRepository`**
Check if a repository exists in the given namespace.
Parameters|Type|Description
-|-|-
`namespace`|`string`|
`repository`|`string`|

---
#### Tool: **`checkRepositoryTag`**
Check if a tag exists in a repository
Parameters|Type|Description
-|-|-
`namespace`|`string`|
`repository`|`string`|
`tag`|`string`|

---
#### Tool: **`createRepository`**
Create a new repository in the given namespace. You MUST ask the user for the repository name and if the repository has to be public or private. Can optionally pass a description.
IMPORTANT: Before calling this tool, you must ensure you have:
 The repository name (name).
Parameters|Type|Description
-|-|-
`namespace`|`string`|The namespace of the repository. Required.
`description`|`string` *optional*|The description of the repository
`full_description`|`string` *optional*|A detailed description of the repository
`is_private`|`boolean` *optional*|Whether the repository is private
`name`|`string` *optional*|The name of the repository (required). Must contain a combination of alphanumeric characters and may contain the special characters ., _, or -. Letters must be lowercase.
`registry`|`string` *optional*|The registry to create the repository in

---
#### Tool: **`dockerHardenedImages`**
This API is used to list Docker Hardened Images (DHIs) available in the user organisations. The tool takes the organisation name as input and returns the list of DHI images available in the organisation. It depends on the "listNamespaces" tool to be called first to get the list of organisations the user has access to.
Parameters|Type|Description
-|-|-
`organisation`|`string`|The organisation for which the DHIs are listed for. If user does not explicitly ask for a specific organisation, the "listNamespaces" tool should be called first to get the list of organisations the user has access to.

---
#### Tool: **`getPersonalNamespace`**
Get the personal namespace name
#### Tool: **`getRepositoryInfo`**
Get the details of a repository in the given namespace.
Parameters|Type|Description
-|-|-
`namespace`|`string`|The namespace of the repository (required). If not provided the `library` namespace will be used for official images.
`repository`|`string`|The repository name (required)

---
#### Tool: **`getRepositoryTag`**
Get the details of a tag in a repository. It can be use to show the latest tag details for example.
Parameters|Type|Description
-|-|-
`namespace`|`string`|
`repository`|`string`|
`tag`|`string`|

---
#### Tool: **`listAllNamespacesMemberOf`**
List all namespaces the user is a member of
#### Tool: **`listNamespaces`**
List paginated namespaces
Parameters|Type|Description
-|-|-
`page`|`number` *optional*|The page number to list repositories from
`page_size`|`number` *optional*|The page size to list repositories from

---
#### Tool: **`listRepositoriesByNamespace`**
List paginated repositories by namespace
Parameters|Type|Description
-|-|-
`namespace`|`string`|The namespace to list repositories from
`content_types`|`string` *optional*|Comma-delimited list of content types. Only repositories containing one or more artifacts with one of these content types will be returned. Default is empty to get all repositories.
`media_types`|`string` *optional*|Comma-delimited list of media types. Only repositories containing one or more artifacts with one of these media types will be returned. Default is empty to get all repositories.
`ordering`|`string` *optional*|The ordering of the repositories. Use "-" to reverse the ordering. For example, "last_updated" will order the repositories by last updated in descending order while "-last_updated" will order the repositories by last updated in ascending order.
`page`|`number` *optional*|The page number to list repositories from
`page_size`|`number` *optional*|The page size to list repositories from

---
#### Tool: **`listRepositoryTags`**
List paginated tags by repository
Parameters|Type|Description
-|-|-
`repository`|`string`|The repository to list tags from
`architecture`|`string` *optional*|The architecture to list tags from. If not provided, all architectures will be listed.
`namespace`|`string` *optional*|The namespace of the repository. If not provided the 'library' namespace will be used for official images.
`os`|`string` *optional*|The operating system to list tags from. If not provided, all operating systems will be listed.
`page`|`number` *optional*|The page number to list tags from
`page_size`|`number` *optional*|The page size to list tags from

---
#### Tool: **`search`**
Search for repositories in Docker Hub. It sorts results by best match if no sort criteria is provided. If user asks for secure, production-ready images the "dockerHardenedImages" tool should be called first to get the list of DHI images available in the user organisations (if any) and fallback to search tool if no DHI images are available or user is not authenticated.
Parameters|Type|Description
-|-|-
`query`|`string`|The query to search for
`architectures`|`array` *optional*|The architectures to filter search results
`badges`|`array` *optional*|The trusted content to search for
`categories`|`array` *optional*|The categories names to filter search results
`extension_reviewed`|`boolean` *optional*|Whether to filter search results to only include reviewed extensions
`from`|`number` *optional*|The number of repositories to skip
`images`|`array` *optional*|The images to filter search results
`operating_systems`|`array` *optional*|The operating systems to filter search results
`order`|`string` *optional*|The order to sort the search results by
`size`|`number` *optional*|The number of repositories to return
`sort`|`string` *optional*|The criteria to sort the search results by. If the `sort` field is not set, the best match is used by default. When search extensions, documents are sort alphabetically if none is provided. Do not use it unless user explicitly asks for it.
`type`|`string` *optional*|The type of the repository to search for

---
#### Tool: **`updateRepositoryInfo`**
Update the details of a repository in the given namespace. Description, overview and status are the only fields that can be updated. While description and overview changes are fine, a status change is a dangerous operation so the user must explicitly ask for it.
Parameters|Type|Description
-|-|-
`namespace`|`string`|The namespace of the repository (required)
`repository`|`string`|The repository name (required)
`description`|`string` *optional*|The description of the repository. If user asks for updating the description of the repository, this is the field that should be updated.
`full_description`|`string` *optional*|The full description (overview)of the repository. If user asks for updating the full description or the overview of the repository, this is the field that should be updated. 
`status`|`string` *optional*|The status of the repository. If user asks for updating the status of the repository, this is the field that should be updated. This is a dangerous operation and should be done with caution so user must be prompted to confirm the operation. Valid status are `active` (1) and `inactive` (0). Normally do not update the status if it is not strictly required by the user. It is not possible to change an `inactive` repository to `active` if it has no images.

---
## Use this MCP Server

```json
{
  "mcpServers": {
    "dockerhub": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "HUB_PAT_TOKEN",
        "mcp/dockerhub",
        "--transport=stdio",
        "--username={{dockerhub.username}}"
      ],
      "env": {
        "HUB_PAT_TOKEN": "your_hub_pat_token"
      }
    }
  }
}
```

[Why is it safer to run MCP Servers with Docker?](https://www.docker.com/blog/the-model-context-protocol-simplifying-building-ai-apps-with-anthropic-claude-desktop-and-docker/)
