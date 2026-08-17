"""Build IGWT.pdf — comprehensive printable notes (lectures, exercises, curriculum)."""
from __future__ import annotations

import html
import re
import subprocess
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent
CHROME = Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
OUT = ROOT / "IGWT.pdf"

CSS = """
@page { size: A4; margin: 16mm 14mm 18mm 14mm; }
html, body { background: #fff; color: #1a1a1a; }
body {
  font-family: "Segoe UI", Calibri, Georgia, serif;
  font-size: 10.5pt;
  line-height: 1.5;
}
h1, h2, h3, h4 {
  font-family: "Segoe UI", Calibri, sans-serif;
  color: #111;
  line-height: 1.25;
  page-break-after: avoid;
}
h1 { font-size: 20pt; margin: 0 0 0.5em; }
h2 { font-size: 14.5pt; margin: 1.2em 0 0.4em; }
h3 { font-size: 12pt; margin: 1em 0 0.35em; }
code, pre { font-family: Consolas, "Cascadia Mono", monospace; }
code { font-size: 9pt; background: #f3f3f3; padding: 0 0.2em; }
pre {
  background: #f4f4f4;
  border: 1px solid #ddd;
  padding: 0.65em 0.8em;
  font-size: 8pt;
  white-space: pre-wrap;
  page-break-inside: avoid;
}
table { border-collapse: collapse; width: 100%; font-size: 9.5pt; margin: 0.6em 0; page-break-inside: avoid; }
th, td { border: 1px solid #bbb; padding: 0.25em 0.4em; vertical-align: top; }
th { background: #efefef; }
blockquote { border-left: 3px solid #ccc; margin: 0.6em 0; padding: 0.1em 0.8em; color: #333; }
hr { border: 0; border-top: 1px solid #ccc; margin: 1.2em 0; }
a { color: #1a4f8b; text-decoration: none; }
.chapter { page-break-before: always; }
.chapter:first-of-type { page-break-before: avoid; }
.toc a { color: #111; }
.cover { margin-top: 18vh; }
.cover h1 { font-size: 28pt; }
.meta { color: #444; }
"""

WIKI = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|([^\]]+))?\]\]")
MD_EXTS = ["tables", "fenced_code", "sane_lists", "smarty"]


def wiki(text: str) -> str:
    def repl(m: re.Match) -> str:
        target = m.group(1).strip()
        label = (m.group(2) or Path(target).name).strip()
        return label

    return WIKI.sub(repl, text)


def md_to_html(text: str) -> str:
    return markdown.markdown(wiki(text), extensions=MD_EXTS)


def collect() -> list[tuple[str, Path]]:
    files: list[tuple[str, Path]] = []

    def add(label: str, path: Path) -> None:
        if path.is_file():
            files.append((label, path))

    front = (
        "00 IGWT Lectures.md",
        "01 subjects.md",
        "02 Curriculum Design Advice.md",
        "Graduation Requirements.md",
        "06 Becoming a Good Teacher.md",
    )
    for name in front:
        add(name, ROOT / name)

    plan_globs = (
        "04 Computational Geometry.md",
        "10 Computer Graphics I.md",
        "07 WebGL and Shader Snippets.md",
        "08 Three.js Snippets.md",
        "09 Computational Geometry Snippets.md",
        "11 Computer Graphics Snippets.md",
        "12 Introduction to Programming.md",
        "13 Web Technologies.md",
        "14 Mathematics for Computer Graphics.md",
        "15 Modern JavaScript Development.md",
        "16 Interactive Web Development.md",
        "17 WebGL Programming.md",
        "18 Three.js Development.md",
        "19 Blender for Real-Time Graphics.md",
        "20 Shader Programming.md",
        "21 Real-Time Rendering.md",
        "22 GPU Programming.md",
        "23 Interactive Experience Development.md",
        "24 Virtual and Augmented Reality.md",
        "25 AI for Interactive Graphics.md",
        "26 Advanced Computer Graphics.md",
        "27 Capstone Project.md",
    )
    for name in plan_globs:
        add(name, ROOT / name)

    folders = (
        "Programming",
        "Web Technologies",
        "Mathematics for Computer Graphics",
        "Computer Graphics",
        "Computational Geometry",
        "Modern JavaScript",
        "Interactive Web",
        "WebGL Programming",
        "ThreeJS Development",
        "Blender",
        "Shader Programming",
        "Real-Time Rendering",
        "GPU Programming",
        "Interactive Experience",
        "XR",
        "AI for Interactive Graphics",
        "Advanced Computer Graphics",
        "Capstone",
        "WebGL",
        "ThreeJS",
        "Teaching",
    )
    skip_names = {"00 Catalog.md"}
    for folder in folders:
        d = ROOT / folder
        if not d.is_dir():
            continue
        md_files = sorted(d.glob("*.md"), key=lambda p: p.name.lower())
        md_files.sort(key=lambda p: (not p.name.lower().startswith("00"), p.name.lower()))
        for p in md_files:
            if p.name in skip_names:
                continue
            add(f"{folder}/{p.name}", p)
        ex = d / "exercises"
        if ex.is_dir():
            ex_files = sorted(ex.glob("*.md"), key=lambda p: p.name.lower())
            for p in ex_files:
                add(f"{folder}/exercises/{p.name}", p)
    return files


def build_html(pairs: list[tuple[str, Path]], *, cover: bool, index0: int = 0) -> str:
    parts: list[str] = []
    if cover:
        toc = [
            "<section class='cover'><h1>IGWT lectures</h1>",
            "<p class='meta'>Interactive Graphics and Web Technologies — full-script session guides, course plans, exercises, teaching handbook.</p>",
            "<h2>Contents</h2><ol class='toc'>",
        ]
        for i, (label, _path) in enumerate(pairs):
            toc.append(f"<li><a href='#s{i}'>{html.escape(label)}</a></li>")
        toc.append("</ol></section>")
        parts.append("".join(toc))
    body = []
    for i, (label, path) in enumerate(pairs):
        n = index0 + i
        raw = path.read_text(encoding="utf-8", errors="replace")
        body.append(
            f"<section class='chapter' id='s{n}'><p class='meta'>{html.escape(label)}</p>{md_to_html(raw)}</section>"
        )
    parts.append("".join(body))
    return (
        "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'/><title>IGWT Lectures</title><style>"
        + CSS
        + "</style></head><body>\n"
        + "".join(parts)
        + "</body></html>"
    )


def chrome_pdf(html_path: Path, pdf_path: Path) -> None:
    uri = html_path.resolve().as_uri()
    subprocess.run(
        [
            str(CHROME),
            "--headless=new",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_path.resolve()}",
            uri,
        ],
        check=True,
    )


def main() -> None:
    from pypdf import PdfReader, PdfWriter

    pairs = collect()
    print(f"collect {len(pairs)} markdown files")
    chunk_n = 28
    tmp = ROOT / "_igwt_chunks"
    tmp.mkdir(exist_ok=True)
    writer = PdfWriter()
    toc_items = "".join(
        f"<li>{html.escape(label)}</li>" for label, _ in pairs
    )
    toc_html = (
        "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'/><title>IGWT Lectures</title><style>"
        + CSS
        + "</style></head><body>"
        "<section class='cover'><h1>IGWT lectures</h1>"
        "<p class='meta'>Full-script session guides for every IGWT course. 75 min lecture + 60 min live coding.</p>"
        f"<h2>Contents ({len(pairs)} files)</h2><ol class='toc'>{toc_items}</ol></section>"
        "</body></html>"
    )
    hp = tmp / "toc.html"
    pdfp = tmp / "toc.pdf"
    hp.write_text(toc_html, encoding="utf-8")
    chrome_pdf(hp, pdfp)
    for page in PdfReader(str(pdfp)).pages:
        writer.add_page(page)
    print("toc pages", len(PdfReader(str(pdfp)).pages))

    for i in range(0, len(pairs), chunk_n):
        chunk = pairs[i : i + chunk_n]
        html_doc = build_html(chunk, cover=False, index0=i)
        hp = tmp / f"part{i:04d}.html"
        pdf_part = tmp / f"part{i:04d}.pdf"
        hp.write_text(html_doc, encoding="utf-8")
        chrome_pdf(hp, pdf_part)
        r = PdfReader(str(pdf_part))
        print(f"chunk {i:4d} files {len(chunk):2d} pages {len(r.pages)}")
        if len(r.pages) < 2:
            raise SystemExit(f"Chrome truncated chunk at {i}")
        for page in r.pages:
            writer.add_page(page)
        hp.unlink(missing_ok=True)
        pdf_part.unlink(missing_ok=True)
    writer.write(OUT)
    for leftover in tmp.glob("*"):
        leftover.unlink()
    tmp.rmdir()
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
