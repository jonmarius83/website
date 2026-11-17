"""Offline design preview from the Quarto markdown sources (Pandoc required)."""
from pathlib import Path
import html
import re
import shutil
import subprocess

root = Path(__file__).resolve().parent
preview = root / "preview"
preview.mkdir(exist_ok=True)
shutil.copytree(root / "assets", preview / "assets", dirs_exist_ok=True)
css = (root / "styles.css").read_text()
nav = [
    ("index", "Home", "Home"),
    ("research", "Research", "Research"),
    ("projects", "Projects", "Research projects"),
    ("weep", "WEEP", "Workshop on Education Economics and Policy (WEEP)"),
    ("applied-research", "Applied research", "Applied research and Norwegian reports"),
    ("teaching", "Teaching", "Teaching"),
    ("cv", "CV", "CV & contact"),
]
extra = """
* { box-sizing: border-box; }
body { margin: 0; }
.navbar { padding: 15px max(24px, calc((100% - 1130px)/2)); display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap: 16px; }
.navbar-brand { text-decoration:none; white-space:nowrap; }
.navbar-nav { display:flex; flex-wrap:wrap; gap: 18px; font-size: 14px; }
.nav-link { text-decoration:none; }
.nav-link.active { border-bottom: 2px solid var(--accent); font-weight:650;}
main { max-width: 1130px; margin:0 auto; padding: 42px 28px 56px; min-height: 72vh; }
main.subpage {max-width: 900px;}
footer { max-width:1130px; margin:0 auto; padding: 24px 28px; font-size: 13px; display:flex; justify-content:space-between; flex-wrap:wrap; gap:12px; }
@media(max-width:720px){main{padding:26px 20px 44px}.navbar{padding:16px 20px}.navbar-nav{gap:12px} }
"""
for name, label, title in nav:
    fragment = subprocess.check_output(
        ["pandoc", str(root / (name + ".qmd")), "--from=markdown", "--to=html5", "--wrap=none"],
        text=True,
    )
    fragment = re.sub(r'href="([^"#]+)\.qmd(#[^"]*)?"', lambda m: 'href="' + m.group(1) + '.html' + (m.group(2) or '') + '"', fragment)
    nav_html = "".join(
        f'<a class="nav-link{" active" if link == name else ""}" href="{link}.html">{html.escape(text)}</a>'
        for link, text, _ in nav
    )
    heading = "" if name == "index" else f"<h1>{html.escape(title)}</h1>"
    document = f"""<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} | Jon Marius Vaag Iversen</title><style>{css}{extra}</style></head>
<body><header class="navbar"><a class="navbar-brand" href="index.html">Jon Marius Vaag Iversen</a>
<nav class="navbar-nav" aria-label="Main navigation">{nav_html}</nav></header>
<main class="{'homepage' if name == 'index' else 'subpage'}">{heading}{fragment}</main>
<footer class="nav-footer"><span>© Jon Marius Vaag Iversen</span><span><a href="mailto:jon.iversen@ntnu.no">Contact</a> · <a href="https://www.ntnu.edu/employees/jon.iversen">NTNU</a></span></footer></body>
</html>"""
    (preview / (name + ".html")).write_text(document)
