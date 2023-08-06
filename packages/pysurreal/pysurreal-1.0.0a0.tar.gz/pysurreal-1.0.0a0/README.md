# pysurreal

Community-created Python connector and ORM for SurrealDB.

## Installation

Raw Python:

```bash
python3 -m pip install pysurreal
```

Poetry:

```bash
poetry add pysurreal
```

## Basic Usage

```py
from asyncio import run

from pysurreal import Client


async def main() -> None:
    async with Client("http://localhost:8000", "namespace", "database", "root", "root") as client:
        result = await client.raw_query("""
            CREATE example:123 SET
                name = 'example',
                list = ['a', 'b', 'c']
            ;
        """)

        if result.error is not None:
            print(result.error.information)
            return

        print(result.response)


run(main())
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contributing

Thank you for your interest in contributing to pysurreal! Please see the [Contributing Guidelines](CONTRIBUTING.md) for more information about contributing.
