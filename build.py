# Склеивает part1..part5 в artifact-source.html (то, что уходит в артефакт)
# и собирает index.html — самостоятельную страницу для локального просмотра и GitHub.
import re
parts = ["part1.html", "part2.html", "part3.html", "part4.html", "part5.html"]
src = "".join(open(p, encoding="utf-8").read() for p in parts)
open("artifact-source.html", "w", encoding="utf-8", newline="\n").write(src)
m = re.match(r"<title>(.*?)</title>\n", src)
title, rest = m.group(1), src[m.end():]
i = rest.index("</style>") + len("</style>")
head_part, body_part = rest[:i], rest[i:]
FAVICON = ('<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 32 32%27%3E'
           '%3Crect width=%2732%27 height=%2732%27 fill=%27%230d0a08%27/%3E'
           '%3Cpath d=%27M16 3.2a12.8 12.8 0 1 0 11.6 7.4%27 fill=%27none%27 stroke=%27%23c9a36a%27 stroke-width=%272.4%27 stroke-linecap=%27round%27/%3E%3C/svg%3E">')
html = ('<!doctype html>\n<html lang="ru">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        f"<title>{title}</title>\n{FAVICON}\n{head_part}\n</head>\n<body>\n{body_part}\n</body>\n</html>\n")
open("index.html", "w", encoding="utf-8", newline="\n").write(html)
print("ok", len(src), len(html))
