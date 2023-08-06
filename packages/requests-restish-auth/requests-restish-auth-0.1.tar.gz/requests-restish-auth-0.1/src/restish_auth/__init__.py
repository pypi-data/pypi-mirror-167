import datetime
import json
import subprocess
from pathlib import Path

from requests.auth import AuthBase


class RestishAuth(AuthBase):
    def __init__(self, section):
        restish_path = Path.home() / ".restish"
        with open(restish_path / "apis.json", "r") as f:
            apis = json.load(f)

        if section not in apis:
            raise ValueError(f"Section {section!r} not found in restish APIs.")

        def read_cache():
            with open(restish_path / "cache.json", "r") as f:
                cache = json.load(f)
            return cache

        cache = read_cache()

        has_token = False
        if f"{section}:default" in cache:
            now = datetime.datetime.now().isoformat()
            token = cache[f"{section}:default"]
            if token["expires"][: len(now)] > now:
                has_token = True

        if not has_token:
            subprocess.check_call(
                ["restish", section],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            token = read_cache()[f"{section}:default"]

        self.auth_header = " ".join((token["type"], token["token"]))

    def __call__(self, request):
        request.headers["Authorization"] = self.auth_header
        return request
