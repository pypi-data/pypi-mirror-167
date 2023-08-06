import datetime
import json
import subprocess
from pathlib import Path

from requests.auth import AuthBase


class RestishAuth(AuthBase):
    def __init__(self, section):
        self.section = section
        self._auth_header = None

    @property
    def auth_header(self):
        if not self._auth_header:
            restish_path = Path.home() / ".restish"
            with open(restish_path / "apis.json", "r") as f:
                apis = json.load(f)

            if self.section not in apis:
                raise ValueError(
                    f"Section {self.section!r} not found in restish APIs."
                )

            def read_cache():
                with open(restish_path / "cache.json", "r") as f:
                    cache = json.load(f)
                return cache

            cache = read_cache()

            has_token = False
            if f"{self.section}:default" in cache:
                now = datetime.datetime.now().isoformat()
                token = cache[f"{self.section}:default"]
                if token["expires"][: len(now)] > now:
                    has_token = True

            if not has_token:
                subprocess.check_call(
                    ["restish", self.section],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
                token = read_cache()[f"{self.section}:default"]

            self._auth_header = " ".join((token["type"], token["token"]))
        return self._auth_header

    def __call__(self, request):
        request.headers["Authorization"] = self.auth_header
        return request
