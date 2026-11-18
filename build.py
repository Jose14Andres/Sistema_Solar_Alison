"""Genera index.html (un solo archivo offline) a partir de src/app.html + three.min.js.

Uso:
    npm install three@0.149.0
    python3 build.py
"""
from pathlib import Path

src = Path("src/app.html").read_text(encoding="utf-8")
three = Path("node_modules/three/build/three.min.js").read_text(encoding="utf-8")
out = src.replace("<script>/*THREE_JS*/</script>", "<script>" + three + "</script>")
Path("index.html").write_text(out, encoding="utf-8")
print(f"index.html: {len(out.encode('utf-8')) / 1024:.0f} KB")
