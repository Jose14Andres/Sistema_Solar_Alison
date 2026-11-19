"""Genera index.html (un solo archivo offline) a partir de src/app.html, three.min.js y la narración grabada.

Uso:
    npm install three@0.149.0
    python3 build.py
"""
import base64, json, subprocess
from pathlib import Path

src = Path("src/app.html").read_text(encoding="utf-8")
three = Path("node_modules/three/build/three.min.js").read_text(encoding="utf-8")

def data_uri(path):
    return "data:audio/mpeg;base64," + base64.b64encode(Path(path).read_bytes()).decode()

man = json.loads(Path("audio/manifest.json").read_text(encoding="utf-8"))
clips = {}
for c in man["clips"]:
    clips[c["who"] + "|" + c["text"]] = data_uri(c["file"])
silent = data_uri("audio/silencio.mp3")

out = src.replace("<script>/*THREE_JS*/</script>", "<script>" + three + "</script>")
out = out.replace("const CLIPS=/*CLIPS*/{};", "const CLIPS=" + json.dumps(clips, ensure_ascii=False) + ";")
out = out.replace("const SILENT=/*SILENT*/'';", "const SILENT=" + json.dumps(silent) + ";")
Path("index.html").write_text(out, encoding="utf-8")
print(f"index.html: {len(out.encode('utf-8')) / 1024:.0f} KB · {len(clips)} frases grabadas")
