# A MCP server for EAN-Search.org

This official MCP server allows you to access the product database on [EAN-Search.org](https://www.ean-search.org) from your AI toolchain.

This MCP server supports local communication over stdio. If you AI tools already support streamable http,
please use our remote MCP server which is much easier to install. See
https://www.ean-search.org/blog/mcp-server-for-ai.html

mcp-name: io.github.eansearch/eansearch-mcp-server

## Installation

Here is a sample configuration for Claude Desktop (claude_desktop_config.json):
```json
{
  "mcpServers": {
    "eansearch": {
      "command": "c:\\Users\\You\\.local\\bin\\uv.exe",
      "args": [
        "--directory",
        "c:\\PATH\\TO\\eansearch-mcp-server",
        "run",
        "eansearch-mcp-server.py"
      ],
      "env": {
        "EAN_SEARCH_API_TOKEN": "<your API key here>"
      }
    }
  }
}
```

