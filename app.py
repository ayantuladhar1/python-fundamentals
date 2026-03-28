import os
import re
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, unquote

CONTENT_DIR = "python_collections"

def get_all_files():
    files = []
    for root, dirs, filenames in os.walk(CONTENT_DIR):
        dirs.sort()
        for filename in sorted(filenames):
            if filename.endswith(".md"):
                full_path = os.path.join(root, filename)
                rel_path = os.path.relpath(full_path, CONTENT_DIR)
                files.append(rel_path)
    return files

def read_md_file(rel_path):
    full_path = os.path.join(CONTENT_DIR, rel_path)
    if not os.path.exists(full_path):
        return None
    with open(full_path, "r", encoding="utf-8") as f:
        return f.read()

def md_to_html(md_text):
    lines = md_text.split("\n")
    html_parts = []
    in_code_block = False
    code_lang = ""
    code_lines = []

    for line in lines:
        if line.startswith("```"):
            if in_code_block:
                escaped = "\n".join(
                    l.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                    for l in code_lines
                )
                lang_class = f' class="language-{code_lang}"' if code_lang else ""
                html_parts.append(f'<pre><code{lang_class}>{escaped}</code></pre>')
                in_code_block = False
                code_lines = []
                code_lang = ""
            else:
                in_code_block = True
                code_lang = line[3:].strip()
        elif in_code_block:
            code_lines.append(line)
        else:
            line = re.sub(r"^### (.+)$", r"<h3>\1</h3>", line)
            line = re.sub(r"^## (.+)$", r"<h2>\1</h2>", line)
            line = re.sub(r"^# (.+)$", r"<h1>\1</h1>", line)
            line = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", line)
            line = re.sub(r"\*(.+?)\*", r"<em>\1</em>", line)
            line = re.sub(r"`(.+?)`", r"<code>\1</code>", line)
            if line.startswith("- ") or line.startswith("* "):
                line = f"<li>{line[2:]}</li>"
            elif line.strip() == "":
                line = "<br>"
            else:
                line = f"<p>{line}</p>"
            html_parts.append(line)

    return "\n".join(html_parts)

def build_sidebar(files, current_file=None):
    items = []
    last_dir = None
    for rel_path in files:
        parts = rel_path.split(os.sep)
        if len(parts) == 1:
            dir_name = "Core Concepts"
        else:
            dir_name = parts[0].replace("_", " ").replace("-", " ").title()

        if dir_name != last_dir:
            if last_dir is not None:
                items.append("</ul>")
            items.append(f'<div class="section-header">{dir_name}</div><ul>')
            last_dir = dir_name

        display = os.path.basename(rel_path)
        display = re.sub(r"^\d+-", "", display).replace(".md", "").replace("_", " ").replace("-", " ").title()
        active = ' class="active"' if rel_path == current_file else ""
        encoded = rel_path.replace(os.sep, "/")
        items.append(f'<li><a href="/view/{encoded}"{active}>{display}</a></li>')

    if last_dir is not None:
        items.append("</ul>")
    return "\n".join(items)

def render_page(title, body, files, current_file=None):
    sidebar = build_sidebar(files, current_file)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; display: flex; height: 100vh; background: #f8f9fa; color: #333; }}
  #sidebar {{ width: 280px; min-width: 220px; background: #1e1e2e; color: #cdd6f4; overflow-y: auto; display: flex; flex-direction: column; }}
  #sidebar h2 {{ padding: 20px 16px 12px; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; color: #89b4fa; border-bottom: 1px solid #313244; }}
  .section-header {{ padding: 12px 16px 4px; font-size: 11px; text-transform: uppercase; letter-spacing: 0.8px; color: #6c7086; font-weight: 700; }}
  #sidebar ul {{ list-style: none; padding: 0 0 8px; }}
  #sidebar ul li a {{ display: block; padding: 6px 16px 6px 24px; color: #cdd6f4; text-decoration: none; font-size: 13px; border-left: 3px solid transparent; transition: all 0.15s; }}
  #sidebar ul li a:hover {{ background: #313244; color: #89b4fa; }}
  #sidebar ul li a.active {{ background: #313244; color: #89b4fa; border-left-color: #89b4fa; }}
  #main {{ flex: 1; overflow-y: auto; padding: 40px; }}
  .content {{ max-width: 860px; margin: 0 auto; background: #fff; border-radius: 8px; box-shadow: 0 1px 4px rgba(0,0,0,0.08); padding: 40px; }}
  h1 {{ font-size: 28px; margin-bottom: 20px; color: #1e1e2e; border-bottom: 2px solid #89b4fa; padding-bottom: 10px; }}
  h2 {{ font-size: 20px; margin: 28px 0 12px; color: #1e1e2e; }}
  h3 {{ font-size: 16px; margin: 20px 0 8px; color: #333; }}
  p {{ margin: 8px 0; line-height: 1.7; }}
  li {{ margin: 4px 0 4px 20px; line-height: 1.6; }}
  code {{ background: #f0f0f0; padding: 2px 6px; border-radius: 4px; font-family: 'Fira Code', monospace; font-size: 13px; color: #e06c75; }}
  pre {{ background: #282c34; border-radius: 8px; padding: 20px; margin: 16px 0; overflow-x: auto; }}
  pre code {{ background: none; color: #abb2bf; padding: 0; font-size: 13.5px; line-height: 1.6; }}
  strong {{ color: #1e1e2e; }}
  .welcome {{ text-align: center; padding: 60px 20px; color: #6c7086; }}
  .welcome h1 {{ border: none; color: #89b4fa; }}
  .welcome p {{ font-size: 16px; margin-top: 12px; }}
  br {{ display: block; margin: 4px 0; content: ""; }}
</style>
</head>
<body>
<div id="sidebar">
  <h2>Python Fundamentals</h2>
  {sidebar}
</div>
<div id="main">
  <div class="content">
    {body}
  </div>
</div>
</body>
</html>"""

class Handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

    def do_GET(self):
        parsed = urlparse(self.path)
        path = unquote(parsed.path)
        files = get_all_files()

        if path == "/" or path == "":
            body = """
            <div class="welcome">
              <h1>Python Fundamentals</h1>
              <p>A hands-on reference covering core Python concepts.</p>
              <p style="margin-top: 24px; color: #89b4fa;">Select a topic from the sidebar to get started.</p>
            </div>"""
            html = render_page("Python Fundamentals", body, files)
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))

        elif path.startswith("/view/"):
            rel_path = path[len("/view/"):]
            rel_path = rel_path.replace("/", os.sep)
            content = read_md_file(rel_path)
            if content is None:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"Not found")
                return
            html_content = md_to_html(content)
            filename = os.path.basename(rel_path)
            title = re.sub(r"^\d+-", "", filename).replace(".md", "").replace("_", " ").replace("-", " ").title()
            html = render_page(title, html_content, files, rel_path)
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 5000), Handler)
    print("Serving Python Fundamentals at http://0.0.0.0:5000")
    server.serve_forever()
