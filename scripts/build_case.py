"""Render docs/case-study.md into the Case study view of index.html (single source of truth)."""
import re, subprocess, pathlib, shutil
root = pathlib.Path(__file__).resolve().parent.parent
# use an installed marked CLI, or fetch a pinned one through npx (shutil.which also finds the .cmd shims on Windows)
marked = [shutil.which("marked")] if shutil.which("marked") else [shutil.which("npx") or "npx", "--yes", "marked@12.0.2"]
html = subprocess.run(marked + ["--gfm", "-i", str(root/"docs/case-study.md")], capture_output=True, text=True, encoding="utf-8", check=True).stdout
html = re.sub(r"<table>", '<div class="table-wrap"><table>', html).replace("</table>", "</table></div>")
html = re.sub(r'<a href="(http[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', html)
html = re.sub(r"(https?://[^\s<]+)(?=</li>|\s·|<br>|$)", lambda m: m.group(1) if 'href' in m.string[max(0,m.start()-10):m.start()] else f'<a href="{m.group(1)}" target="_blank" rel="noopener">{m.group(1)}</a>', html)
idx = (root/"index.html").read_text(encoding="utf-8")
start, end = "<!--CASE:START-->", "<!--CASE:END-->"
if start not in idx:
    idx = idx.replace('<article class="doc" id="caseDoc"></article>', f'<article class="doc" id="caseDoc">{start}{end}</article>')
idx = re.sub(re.escape(start)+r".*?"+re.escape(end), lambda m: start+html+end, idx, flags=re.S)
(root/"index.html").write_text(idx, encoding="utf-8", newline="")
print("case study rendered:", len(html), "chars")
