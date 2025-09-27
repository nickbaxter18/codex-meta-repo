# Maestro MCP Server MCP Server

A Model Context Protocol (MCP) server exposing Bitcoin blockchain data through the Maestro API platform. Provides tools to explore blocks, transactions, addresses, inscriptions, runes, and other metaprotocol data.

[What is an MCP Server?](https://www.anthropic.com/news/model-context-protocol)

## Characteristics
Attribute|Details|
|-|-|
**Docker Image**|[mcp/maestro-mcp-server](https://hub.docker.com/repository/docker/mcp/maestro-mcp-server)
**Author**|[maestro-org](https://github.com/maestro-org)
**Repository**|https://github.com/maestro-org/maestro-mcp-server
**Dockerfile**|https://github.com/maestro-org/maestro-mcp-server/blob/main/Dockerfile
**Docker Image built by**|Docker Inc.
**Docker Scout Health Score**| ![Docker Scout Health Score](https://api.scout.docker.com/v1/policy/insights/org-image-score/badge/mcp/maestro-mcp-server)
**Verify Signature**|`COSIGN_REPOSITORY=mcp/signatures cosign verify mcp/maestro-mcp-server --key https://raw.githubusercontent.com/docker/keyring/refs/heads/main/public/mcp/latest.pub`
**Licence**|Apache License 2.0

## Available Tools (35)
Tools provided by this Server|Short Description
-|-
`get_address_activity`|List satoshi balance change activity for an address.|
`get_address_balance`|Get current satoshi balance for an address (confirmed only).|
`get_address_balance_historical`|Get historical satoshi balances per block, with USD valuation.|
`get_address_brc20`|List BRC-20 balances for an address (total and available).|
`get_address_brc20_transfer_inscriptions`|List unspent BRC-20 transfer inscriptions at an address.|
`get_address_inscriptions`|List inscriptions currently controlled by an address.|
`get_address_inscription_activity`|List inscription send/receive/self-transfer activity for an address.|
`get_address_runes`|List Rune balances for an address (total and available).|
`get_address_rune_activity`|List Rune balance increases/decreases/self-transfers for an address.|
`get_address_rune_utxos`|List UTXOs at an address containing Runes.|
`get_address_statistics`|Get address stats: tx counts, UTXOs, sat balance, runes/inscriptions flags.|
`get_address_txs`|List transactions that spent/produced UTXOs for an address.|
`get_address_utxos`|List UTXOs for an address; supports dust and metaprotocol filtering.|
`get_mempool_address_balance`|Get address satoshi balance including mempool-aware estimates.|
`get_mempool_address_runes`|Get mempool-aware Rune balances for an address.|
`list_brc20_assets`|List BRC-20 tickers deployed on-chain.|
`get_brc20_info`|Get BRC-20 metadata and current state.|
`list_supported_dexs`|List supported DEX identifiers for market endpoints.|
`get_dex_ohlc`|Get OHLCV candles for a DEX and symbol.|
`get_btc_price_by_timestamp`|Get BTC-USD price at a given UTC timestamp.|
`get_rune_price_by_timestamp`|Get Rune price (USD and sats) at a given UTC timestamp.|
`rpc_chain_info`|Bitcoin node and chain status from Node RPC.|
`rpc_mempool_info`|Current mempool size, usage, fee thresholds, RBF state.|
`rpc_mempool_transactions`|List transaction IDs currently in the mempool.|
`rpc_block_miner_info`|Get miner metadata for a given block.|
`rpc_block_volume`|Get total transaction output volume (sats) for a block.|
`event_healthcheck`|Event Manager healthcheck.|
`event_list_logs`|List event logs produced by triggers.|
`event_get_log`|Get a single event log by id.|
`event_list_triggers`|List all triggers.|
`event_create_trigger`|Create a new trigger for on-chain events.|
`event_get_trigger`|Get a trigger by id.|
`event_update_trigger`|Update an existing trigger by id.|
`event_delete_trigger`|Delete a trigger by id.|
`event_list_trigger_condition_options`|List condition picklist options for triggers.|

---
## Tools Details

#### Tool: **`get_address_activity`**
List satoshi balance change activity for an address.
Parameters|Type|Description
-|-|-
`address`|`string`|Bech32 or scriptPubKey (hex).
`order`|`string`|asc or desc.
`count`|`integer`|Results per page.
`from`|`integer`|Min block height.
`to`|`integer`|Max block height.
`cursor`|`string`|Pagination cursor.
`activity_kind`|`string`|increase | decrease | self_transfer.
`exclude_self_transfers`|`boolean`|Exclude self-transfers.

---
#### Tool: **`get_address_balance`**
Get current satoshi balance for an address (confirmed only).
Parameters|Type|Description
-|-|-
`address`|`string`|Bech32 or scriptPubKey (hex).

---
#### Tool: **`get_address_balance_historical`**
Get historical satoshi balances per block, with USD valuation.
Parameters|Type|Description
-|-|-
`address`|`string`|Bech32 or scriptPubKey (hex).
`order`|`string`|asc or desc.
`count`|`integer`|Results per page.
`from`|`integer`|Min height or timestamp.
`to`|`integer`|Max height or timestamp.
`cursor`|`string`|Pagination cursor.
`height_params`|`boolean`|If true, from/to are heights; false means timestamps.

---
#### Tool: **`get_address_brc20`**
List BRC-20 balances for an address (total and available).
Parameters|Type|Description
-|-|-
`address`|`string`|Bech32 or scriptPubKey (hex).

---
#### Tool: **`get_address_brc20_transfer_inscriptions`**
List unspent BRC-20 transfer inscriptions at an address.
Parameters|Type|Description
-|-|-
`address`|`string`|Bech32 or scriptPubKey (hex).
`ticker`|`string`|Optional BRC-20 ticker filter.
`count`|`integer`|Results per page.
`order`|`string`|asc or desc.
`cursor`|`string`|Pagination cursor.

---
#### Tool: **`get_address_inscriptions`**
List inscriptions currently controlled by an address.
Parameters|Type|Description
-|-|-
`address`|`string`|Bech32 or scriptPubKey (hex).
`count`|`integer`|Results per page.
`cursor`|`string`|Pagination cursor.

---
#### Tool: **`get_address_inscription_activity`**
List inscription send/receive/self-transfer activity for an address.
Parameters|Type|Description
-|-|-
`address`|`string`|Bech32 or scriptPubKey (hex).
`order`|`string`|asc or desc.
`count`|`integer`|Results per page.
`from`|`integer`|Min block height.
`to`|`integer`|Max block height.
`cursor`|`string`|Pagination cursor.
`inscription_id`|`string`|Filter by inscription id.
`activity_kind`|`string`|send | receive | self_transfer.
`exclude_self_transfers`|`boolean`|Exclude self-transfers.

---
#### Tool: **`get_address_runes`**
List Rune balances for an address (total and available).
Parameters|Type|Description
-|-|-
`address`|`string`|Bech32 or scriptPubKey (hex).

---
#### Tool: **`get_address_rune_activity`**
List Rune balance increases/decreases/self-transfers for an address.
Parameters|Type|Description
-|-|-
`address`|`string`|Bech32 or scriptPubKey (hex).
`order`|`string`|asc or desc.
`count`|`integer`|Results per page.
`from`|`integer`|Min block height.
`to`|`integer`|Max block height.
`cursor`|`string`|Pagination cursor.
`rune`|`string`|Rune ID (e.g., 840000:28) or name.
`activity_kind`|`string`|increased | decreased | self_transfer.
`exclude_self_transfers`|`boolean`|Exclude self-transfers.

---
#### Tool: **`get_address_rune_utxos`**
List UTXOs at an address containing Runes.
Parameters|Type|Description
-|-|-
`address`|`string`|Bech32 or scriptPubKey (hex).
`rune`|`string`|Rune ID or name filter.
`order_by`|`string`|height | amount.
`order`|`string`|asc or desc.
`count`|`integer`|Results per page.
`cursor`|`string`|Pagination cursor.
`from`|`integer`|Min block height.
`to`|`integer`|Max block height.

---
#### Tool: **`get_address_statistics`**
Get address stats: tx counts, UTXOs, sat balance, runes/inscriptions flags.
Parameters|Type|Description
-|-|-
`address`|`string`|Bech32 or scriptPubKey (hex).

---
#### Tool: **`get_address_txs`**
List transactions that spent/produced UTXOs for an address.
Parameters|Type|Description
-|-|-
`address`|`string`|Bech32 or scriptPubKey (hex).
`count`|`integer`|Results per page.
`confirmations`|`integer`|Minimum confirmations.
`order`|`string`|asc or desc.
`from`|`integer`|Min block height.
`to`|`integer`|Max block height.
`cursor`|`string`|Pagination cursor.

---
#### Tool: **`get_address_utxos`**
List UTXOs for an address; supports dust and metaprotocol filtering.
Parameters|Type|Description
-|-|-
`address`|`string`|Bech32 or scriptPubKey (hex).
`filter_dust`|`boolean`|Exclude UTXOs < 100k sats.
`filter_dust_threshold`|`integer`|Custom dust threshold (sats).
`exclude_metaprotocols`|`boolean`|Exclude Rune/inscription UTXOs.
`ignore_used_brc20`|`boolean`|Keep UTXOs with used BRC-20 if excluding metaprotocols.
`count`|`integer`|Results per page.
`order`|`string`|asc or desc.
`from`|`integer`|Min block height.
`to`|`integer`|Max block height.
`cursor`|`string`|Pagination cursor.

---
#### Tool: **`get_mempool_address_balance`**
Get address satoshi balance including mempool-aware estimates.
Parameters|Type|Description
-|-|-
`address`|`string`|Bech32 or scriptPubKey (hex).

---
#### Tool: **`get_mempool_address_runes`**
Get mempool-aware Rune balances for an address.
Parameters|Type|Description
-|-|-
`address`|`string`|Bech32 or scriptPubKey (hex).

---
#### Tool: **`list_brc20_assets`**
List BRC-20 tickers deployed on-chain.
Parameters|Type|Description
-|-|-
`count`|`integer`|Results per page.
`cursor`|`string`|Pagination cursor.

---
#### Tool: **`get_brc20_info`**
Get BRC-20 metadata and current state.
Parameters|Type|Description
-|-|-
`ticker`|`string`|BRC-20 ticker (e.g., ORDI).

---
#### Tool: **`list_supported_dexs`**
List supported DEX identifiers for market endpoints.
#### Tool: **`get_dex_ohlc`**
Get OHLCV candles for a DEX and symbol.
Parameters|Type|Description
-|-|-
`dex`|`string`|all | magiceden | dotswap.
`symbol`|`string`|Trading pair, e.g., BTC-840000:28.
`mempool`|`string`|included | excluded | only.
`resolution`|`string`|1m,5m,15m,30m,1h,4h,1d,1w,1M.
`from`|`integer`|Unix seconds start.
`to`|`integer`|Unix seconds end.

---
#### Tool: **`get_btc_price_by_timestamp`**
Get BTC-USD price at a given UTC timestamp.
Parameters|Type|Description
-|-|-
`timestamp`|`integer`|Unix seconds.

---
#### Tool: **`get_rune_price_by_timestamp`**
Get Rune price (USD and sats) at a given UTC timestamp.
Parameters|Type|Description
-|-|-
`rune_id`|`string`|Rune ID in <block>:<tx_index>.
`timestamp`|`integer`|Unix seconds.

---
#### Tool: **`rpc_chain_info`**
Bitcoin node and chain status from Node RPC.
#### Tool: **`rpc_mempool_info`**
Current mempool size, usage, fee thresholds, RBF state.
#### Tool: **`rpc_mempool_transactions`**
List transaction IDs currently in the mempool.
#### Tool: **`rpc_block_miner_info`**
Get miner metadata for a given block.
Parameters|Type|Description
-|-|-
`height_or_hash`|`string`|Block height or block hash.

---
#### Tool: **`rpc_block_volume`**
Get total transaction output volume (sats) for a block.
Parameters|Type|Description
-|-|-
`height_or_hash`|`string`|Block height or block hash.

---
#### Tool: **`event_healthcheck`**
Event Manager healthcheck.
#### Tool: **`event_list_logs`**
List event logs produced by triggers.
Parameters|Type|Description
-|-|-
`page`|`integer`|Page number (1+).
`limit`|`integer`|Items per page (1–100).
`trigger_id`|`string`|Filter by trigger id.
`chain`|`string`|Filter by chain (bitcoin).
`network`|`string`|Filter by network (mainnet/testnet).

---
#### Tool: **`event_get_log`**
Get a single event log by id.
Parameters|Type|Description
-|-|-
`id`|`string`|Event log id.

---
#### Tool: **`event_list_triggers`**
List all triggers.
#### Tool: **`event_create_trigger`**
Create a new trigger for on-chain events.
Parameters|Type|Description
-|-|-
`name`|`string`|Trigger name.
`chain`|`string`|bitcoin.
`network`|`string`|mainnet or testnet.
`type`|`string`|transaction.
`webhook_url`|`string`|Webhook endpoint (URL).
`filters`|`array`|Filter objects per schema.
`confirmations`|`integer`|Required confirmations.
`status`|`string`|active or paused.

---
#### Tool: **`event_get_trigger`**
Get a trigger by id.
Parameters|Type|Description
-|-|-
`id`|`string`|Trigger id.

---
#### Tool: **`event_update_trigger`**
Update an existing trigger by id.
Parameters|Type|Description
-|-|-
`id`|`string`|Trigger id.
`name`|`string`|Updated name.
`chain`|`string`|bitcoin.
`network`|`string`|mainnet or testnet.
`type`|`string`|transaction.
`webhook_url`|`string`|Webhook endpoint (URL).
`filters`|`array`|Filter objects per schema.
`confirmations`|`integer`|Required confirmations.
`status`|`string`|active or paused.

---
#### Tool: **`event_delete_trigger`**
Delete a trigger by id.
Parameters|Type|Description
-|-|-
`id`|`string`|Trigger id.

---
#### Tool: **`event_list_trigger_condition_options`**
List condition picklist options for triggers.
Parameters|Type|Description
-|-|-
`trigger_type`|`string`|transaction.

---
## Use this MCP Server

```json
{
  "mcpServers": {
    "maestro-mcp-server": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "API_KEY_API_KEY",
        "mcp/maestro-mcp-server"
      ],
      "env": {
        "API_KEY_API_KEY": "your-maestro-api-key"
      }
    }
  }
}
```

[Why is it safer to run MCP Servers with Docker?](https://www.docker.com/blog/the-model-context-protocol-simplifying-building-ai-apps-with-anthropic-claude-desktop-and-docker/)
