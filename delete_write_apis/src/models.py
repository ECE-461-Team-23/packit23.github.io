# generated by fastapi-codegen:
#   filename:  spec.yaml
#   timestamp: 2023-04-10T18:30:51+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, validator


class Error(BaseModel):
    code: int
    message: str


class PackageData(BaseModel):
    Content: Optional[str] = Field(
        None,
        description='Package contents. This is the zip file uploaded by the user. (Encoded as text using a Base64 encoding).\n\nThis will be a zipped version of an npm package\'s GitHub repository, minus the ".git/" directory." It will, for example, include the "package.json" file that can be used to retrieve the project homepage.\n\nSee https://docs.npmjs.com/cli/v7/configuring-npm/package-json#homepage.',
    )
    URL: Optional[str] = Field(
        None, description='Package URL (for use in public ingest).'
    )
    JSProgram: Optional[str] = Field(
        None, description='A JavaScript program (for use with sensitive modules).'
    )


class User(BaseModel):
    name: str = Field(..., description='', example='Alfalfa')
    isAdmin: bool = Field(..., description='Is this user an admin?')


class UserAuthenticationInfo(BaseModel):
    password: str = Field(
        ...,
        description='Password for a user. Per the spec, this should be a "strong" password.',
    )


class PackageID(BaseModel):
    __root__: str = Field(..., description='')


class PackageRating(BaseModel):
    BusFactor: float = Field(..., description='')
    Correctness: float = Field(..., description='')
    RampUp: float = Field(..., description='')
    ResponsiveMaintainer: float = Field(..., description='')
    LicenseScore: float = Field(..., description='')
    GoodPinningPractice: float = Field(
        ...,
        description='The fraction of its dependencies that are pinned to at least a specific major+minor version, e.g. version 2.3.X of a package. (If there are zero dependencies, they should receive a 1.0 rating. If there are two dependencies, one pinned to this degree, then they should receive a Â½ = 0.5 rating).',
    )
    PullRequest: float = Field(
        ...,
        description='The fraction of project code that was introduced through pull requests with a code review.',
    )
    NetScore: float = Field(..., description='From Part 1')


class Action(Enum):
    CREATE = 'CREATE'
    UPDATE = 'UPDATE'
    DOWNLOAD = 'DOWNLOAD'
    RATE = 'RATE'


class PackageName(BaseModel):
    __root__: str = Field(
        ...,
        description='Name of a package.\n\n- Names should only use typical "keyboard" characters.\n- The name "*" is reserved. See the `/packages` API for its meaning.',
    )


class AuthenticationToken(BaseModel):
    __root__: str = Field(
        ...,
        description='The spec permits you to use any token format you like. You could, for example, look into JSON Web Tokens ("JWT", pronounced "jots"): https://jwt.io.',
    )


class AuthenticationRequest(BaseModel):
    User: User = Field(..., description='')
    Secret: UserAuthenticationInfo = Field(..., description='')


class SemverRange(BaseModel):
    __root__: str = Field(
        ...,
        description='',
        example='Exact (1.2.3)\nBounded range (1.2.3-2.1.0)\nCarat (^1.2.3)\nTilde (~1.2.0)',
    )


class PackageQuery(BaseModel):
    Version: Optional[SemverRange] = Field(None, description='')
    Name: PackageName = Field(..., description='')


class EnumerateOffset(BaseModel):
    __root__: str = Field(..., description='Offset in pagination.', example='1')


class PackageRegEx(BaseModel):
    __root__: str = Field(
        ...,
        description='A regular expression over package names and READMEs that is used for searching for a package.',
    )


class PackageMetadata(BaseModel):
    Name: PackageName = Field(..., description='Package name', example='my-package')
    Version: str = Field(..., description='Package version', example='1.2.3')
    ID: PackageID = Field(
        ...,
        description='Unique ID for use with the /package/{id} endpoint.',
        example='123567192081501',
    )


class PackageHistoryEntry(BaseModel):
    User: User = Field(..., description='')
    Date: datetime = Field(
        ...,
        description='Date of activity using ISO-8601 Datetime standard in UTC format.',
        example='2023-03-23T23:11:15Z',
    )
    PackageMetadata: PackageMetadata = Field(..., description='')
    Action: Action = Field(..., description='')


class Package(BaseModel):
    metadata: PackageMetadata = Field(..., description='')
    data: PackageData = Field(..., description='')
