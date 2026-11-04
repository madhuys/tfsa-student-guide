"""Every page parses, and every local link and asset it names exists."""
import pathlib
import unittest
from html.parser import HTMLParser
from urllib.parse import urlparse

ROOT = pathlib.Path(__file__).resolve().parents[1]


class Refs(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name in ("href", "src") and value:
                self.refs.append(value)


class SiteTest(unittest.TestCase):
    def test_pages_name_only_files_that_exist(self):
        pages = [p for p in ROOT.rglob("*.html") if ".git" not in p.parts]
        self.assertTrue(pages, "no HTML page")
        for page in pages:
            parser = Refs()
            parser.feed(page.read_text(encoding="utf-8"))
            for ref in parser.refs:
                url = urlparse(ref)
                if url.scheme or url.netloc or ref.startswith("#"):
                    continue
                target = (page.parent / url.path).resolve()
                self.assertTrue(target.exists(), f"{page.name} names {ref}, which does not exist")


if __name__ == "__main__":
    unittest.main()
