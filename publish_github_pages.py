"""Prepare the generated site for hosting below a GitHub Pages project path."""

from pathlib import Path
import sys


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python publish_github_pages.py /repository-name")

    base_path = "/" + sys.argv[1].strip("/")
    output = Path(__file__).parent / "dist"

    for page in output.rglob("*.html"):
        html = page.read_text(encoding="utf-8")
        for attribute in ("href", "src", "action", "poster"):
            html = html.replace(f'{attribute}="/', f'{attribute}="{base_path}/')
        page.write_text(html, encoding="utf-8")

    # Prevent GitHub Pages from treating asset folders as Jekyll content.
    (output / ".nojekyll").touch()
    print(f"Prepared {output} for GitHub Pages at {base_path}/")


if __name__ == "__main__":
    main()
