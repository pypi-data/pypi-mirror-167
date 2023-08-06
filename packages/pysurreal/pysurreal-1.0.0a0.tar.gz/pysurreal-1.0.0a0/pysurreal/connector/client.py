from typing import Any

from aiohttp import BasicAuth, ClientSession

from .result import Error, Response, ResultOk, ResultErr, Result


class Client:
    def __init__(self, url: str, namespace: str, database: str, user: str, password: str) -> None:
        self._url = url.removesuffix("/")
        self._namespace = namespace
        self._database = database

        self._user = user
        self._pass = password

        self._session: ClientSession | None = None

    async def open(self) -> None:
        self._session = ClientSession(
            base_url=self._url,
            headers={
                "NS": self._namespace,
                "DB": self._database,
            },
            auth=BasicAuth(self._user, self._pass),
        )

    async def close(self) -> None:
        if self._session is not None:
            await self._session.close()

    async def __aenter__(self) -> "Client":
        await self.open()
        return self

    async def __aexit__(self, *_: Any) -> None:
        await self.close()

    async def raw_query(self, query: str) -> Result:
        if self._session is None:
            raise RuntimeError("Client is not open")

        async with self._session.post(
            "/sql",
            data=query,
            headers={
                "Content-Type": "application/json",
            },
        ) as response:
            data = await response.json()

            if response.status == 200:
                return ResultOk(response=Response(**data[0]))

            return ResultErr(error=Error(**data))
