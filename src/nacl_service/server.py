from typing import get_args, Literal, Union
from mcp.server.lowlevel import Server, NotificationOptions
from mcp.server.models import InitializationOptions
import mcp.server.stdio
import mcp.types as types
import nacl.encoding
import nacl.hash

Hash_Algorithm = Literal["SHA256", "SHA512"]    # TODO add BLAKE2b
Output_Encoding = Literal["Hexadecimal", "Base64"]

SERVER_NAME = "nacl-service"
server = Server(SERVER_NAME)

def generate_hash(
    message: str,
    algorithm: Hash_Algorithm,
    output_encoding: Output_Encoding | None = "Hexadecimal",
) -> types.TextContent:
    # TODO Add error handling?

    messageBytes = message.encode()
    encoder = nacl.encoding.HexEncoder
    digest: bytes

    match output_encoding:
        case "Base64":
            encoder = nacl.encoding.Base64Encoder        

    match algorithm:
        case "SHA256":
            digest = nacl.hash.sha256(
                messageBytes,
                encoder,
            )       
        case "SHA512":
            digest = nacl.hash.sha512(
                messageBytes,
                encoder,
            )

    return types.TextContent(
        type="text",
        text=digest.decode()
    )

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """
    List available tools.
    Each tool specifies its arguments using JSON Schema validation.
    """  
    return [
        types.Tool(
            name="generate_hash",
            description="Generates a hash value from a given message.",
            inputSchema={
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "The message to hash.",
                    },
                    "algorithm": {
                        "enum": list(get_args(Hash_Algorithm)),
                        "description": "The algorithm used to generate the hash value.",
                    },
                    "output_encoding": {
                        "enum": list(get_args(Output_Encoding)),
                        "description": "Encoding for the generated hash value. Defaults to hexadecimal.",
                    },
                },
                "required": ["message, algorithm"]
            },
        )
    ]

@server.call_tool()
async def handle_call_tool(
    name: str,
    arguments: dict,
) -> list[types.TextContent]:
    """
    Handle tool execution requests.
    """
    if name == "generate_hash":
        message = arguments.get("message")
        algorithm = arguments.get("algorithm")
        output_encoding = arguments.get("output_encoding")

        if not message:
            raise ValueError("Missing required argument: message")

        if not algorithm:
            raise ValueError("Missing required argument: algorithm")
        
        if not algorithm in list(get_args(Hash_Algorithm)):
            raise ValueError("Invalid argument: algorithm")
        
        if output_encoding and not output_encoding in list(get_args(Output_Encoding)):
            raise ValueError("Invalid argument: output encoding")

        return [generate_hash(message, algorithm, output_encoding)]
    
    raise ValueError(f"Tool not found: {name}")

async def run():
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name=SERVER_NAME,
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                )
            )
        )

if __name__ == "__main__":
    import asyncio
    asyncio.run(run())