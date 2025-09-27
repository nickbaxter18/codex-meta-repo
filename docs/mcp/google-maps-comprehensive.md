# Google Maps Comprehensive MCP MCP Server

Complete Google Maps integration with 8 tools including geocoding, places search, directions, elevation data, and more using Google's latest APIs.

[What is an MCP Server?](https://www.anthropic.com/news/model-context-protocol)

## Characteristics
Attribute|Details|
|-|-|
**Docker Image**|[mcp/google-maps-comprehensive](https://hub.docker.com/repository/docker/mcp/google-maps-comprehensive)
**Author**|[vicpeacock](https://github.com/vicpeacock)
**Repository**|https://github.com/vicpeacock/google-maps-comprehensive-mcp
**Dockerfile**|https://github.com/vicpeacock/google-maps-comprehensive-mcp/blob/main/Dockerfile
**Docker Image built by**|Docker Inc.
**Docker Scout Health Score**| ![Docker Scout Health Score](https://api.scout.docker.com/v1/policy/insights/org-image-score/badge/mcp/google-maps-comprehensive)
**Verify Signature**|`COSIGN_REPOSITORY=mcp/signatures cosign verify mcp/google-maps-comprehensive --key https://raw.githubusercontent.com/docker/keyring/refs/heads/main/public/mcp/latest.pub`
**Licence**|

## Available Tools (8)
Tools provided by this Server|Short Description
-|-
`maps_directions`|Get directions between two locations using Google Routes API|
`maps_distance_matrix`|Calculate distances and travel times between multiple origins and destinations|
`maps_elevation`|Get elevation data for geographic points using Google Elevation API|
`maps_geocode`|Convert address to coordinates using Google Geocoding API|
`maps_ping`|Check if the Google Maps MCP server is alive|
`maps_place_details`|Get detailed information about a place using Google Places API|
`maps_reverse_geocode`|Get address from latitude/longitude using Google Places Nearby|
`maps_search_places`|Search places using Google Places API (New)|

---
## Tools Details

#### Tool: **`maps_directions`**
Get directions between two locations using Google Routes API
Parameters|Type|Description
-|-|-
`destination`|`string`|Destination address
`origin`|`string`|Origin address
`travelMode`|`string` *optional*|Travel mode

---
#### Tool: **`maps_distance_matrix`**
Calculate distances and travel times between multiple origins and destinations
Parameters|Type|Description
-|-|-
`destinations`|`array`|Array of destination addresses
`origins`|`array`|Array of origin addresses
`mode`|`string` *optional*|Travel mode

---
#### Tool: **`maps_elevation`**
Get elevation data for geographic points using Google Elevation API
Parameters|Type|Description
-|-|-
`locations`|`array`|Array of locations to get elevation for

---
#### Tool: **`maps_geocode`**
Convert address to coordinates using Google Geocoding API
Parameters|Type|Description
-|-|-
`address`|`string`|Address to geocode

---
#### Tool: **`maps_ping`**
Check if the Google Maps MCP server is alive
#### Tool: **`maps_place_details`**
Get detailed information about a place using Google Places API
Parameters|Type|Description
-|-|-
`place_id`|`string`|Google Place ID

---
#### Tool: **`maps_reverse_geocode`**
Get address from latitude/longitude using Google Places Nearby
Parameters|Type|Description
-|-|-
`latitude`|`number`|Latitude coordinate
`longitude`|`number`|Longitude coordinate

---
#### Tool: **`maps_search_places`**
Search places using Google Places API (New)
Parameters|Type|Description
-|-|-
`query`|`string`|Search query for places

---
## Use this MCP Server

```json
{
  "mcpServers": {
    "google-maps-comprehensive": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "GOOGLE_MAPS_API_KEY",
        "mcp/google-maps-comprehensive"
      ],
      "env": {
        "GOOGLE_MAPS_API_KEY": "<YOUR_GOOGLE_MAPS_API_KEY>"
      }
    }
  }
}
```

[Why is it safer to run MCP Servers with Docker?](https://www.docker.com/blog/the-model-context-protocol-simplifying-building-ai-apps-with-anthropic-claude-desktop-and-docker/)
