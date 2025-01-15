# MCP Servers

## Model Context Protocol

The [Model Context Protocol](https://modelcontextprotocol.io/introduction) is an open protocol that aims to standardize how we connect AI models to different data sources and tools.

By creating a universal standard, connecting to AI systems becomes simple and reliable. 
Fragmented integrations can be replaced with a single protocol.

The basic architecture:  
- MCP servers expose data/tools  
- MCP clients are AI applications that connect to MCP servers to consume data/tools.

This project will explore MCP by testing different servers locally with Anthropic Claude (MCP client).


## Servers

### NaCl Service

[NaCl](https://nacl.cr.yp.to/) is a library that provides cryptographic operations like encryption, decryption and hash functions. This service exposes NaCl functionality to MCP clients. It uses [pynacl](https://github.com/pyca/pynacl), a python wrapper for NaCl, under the hood.

Tools:
- `generate_hash()`
Generates a hash value for a given message using a given algorithm (SHA256, SHA512).


## Results

<img src="./src/nacl_service/test_integration/test_generate_hash_1.png" width="800px" />
<img src="./src/nacl_service/test_integration/test_generate_hash_2.png" width="800px" />


## Setup

`claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "nacl": {
      "command": "/Users/<username>/.local/bin/uv",
      "args": [
        "run",
        "--with",
        "mcp",
        "--with",
        "pynacl",
        "/Users/<username>/Desktop/mcp-servers/src/nacl_service/server.py"
      ]
    }
  }
}
```