from dataclasses import dataclass
from typing import Any


@dataclass(slots=True, frozen=True)
class Response:
    time: str
    status: str
    result: Any = None
    error: Any = None
    detail: str | None = None


@dataclass(slots=True, frozen=True)
class Error:
    code: int
    details: str
    description: str
    information: str


@dataclass(slots=True, frozen=True)
class ResultOk:
    response: Response
    error: Error | None = None


@dataclass(slots=True, frozen=True)
class ResultErr:
    error: Error
    response: Response | None = None


Result = ResultOk | ResultErr
