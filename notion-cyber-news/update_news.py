#!/usr/bin/env python3
import json, re, html, urllib.request, xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from datetime import datetime, timezone

RSS_URL = "https://feeds.feedburner.com/TheHackersNews"
OUT = "notion-cyber-news/news.json"
UA = "Mozilla/5.0 (compatible; FadiCyberNewsWidget/1.0)"

def get(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")

def strip_html(s):
    s = html.unescape(s or "")
    s = re.sub(r"<script[\s\S]*?</script>", " ", s, flags=re.I)
    s = re.sub(r"<style[\s\S]*?</style>", " ", s, flags=re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", s).strip()

def first_image_from_html(s):
    if not s: return ""
    pats = [
        r'<img[^>]+src=["\']([^"\']+)["\']',
        r'<img[^>]+data-src=["\']([^"\']+)["\']'
    ]
    for p in pats:
        m = re.search(p, s, flags=re.I)
        if m: return html.unescape(m.group(1))
    return ""

def og_image(url):
    try:
        page = get(url)
    except Exception:
        return ""
    patterns = [
        r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']',
        r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']',
        r'<meta[^>]+name=["\']twitter:image(?::src)?["\'][^>]+content=["\']([^"\']+)["\']',
        r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+name=["\']twitter:image(?::src)?["\']',
    ]
    for p in patterns:
        m = re.search(p, page, flags=re.I)
        if m: return html.unescape(m.group(1))
    return ""

def node_text(node, name):
    x=node.find(name)
    return (x.text or "").strip() if x is not None and x.text else ""

xml = get(RSS_URL)
root = ET.fromstring(xml)
items = root.findall(".//item")
out = []

media_ns = "{http://search.yahoo.com/mrss/}"

for item in items[:8]:
    title = node_text(item, "title")
    link = node_text(item, "link")
    pub = node_text(item, "pubDate")
    desc = node_text(item, "description")
    cats = [(c.text or "").strip() for c in item.findall("category") if c.text]

    image = ""
    for tag in (media_ns+"content", media_ns+"thumbnail"):
        el = item.find(tag)
        if el is not None and el.attrib.get("url"):
            image = el.attrib["url"]; break
    if not image:
        for enc in item.findall("enclosure"):
            if enc.attrib.get("type","").startswith("image/") and enc.attrib.get("url"):
                image=enc.attrib["url"]; break
    if not image:
        image = first_image_from_html(desc)
    if not image and link:
        image = og_image(link)

    try:
        published = parsedate_to_datetime(pub).astimezone(timezone.utc).isoformat()
    except Exception:
        published = datetime.now(timezone.utc).isoformat()

    excerpt = strip_html(desc)
    if len(excerpt) > 260:
        excerpt = excerpt[:257].rstrip() + "…"

    out.append({
        "title": title,
        "link": link,
        "published": published,
        "excerpt": excerpt,
        "categories": cats[:3],
        "image": image
    })

payload = {
    "source": "The Hacker News",
    "source_url": "https://thehackernews.com/",
    "updated_at": datetime.now(timezone.utc).isoformat(),
    "items": out
}
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)
    f.write("\n")
print(f"Wrote {len(out)} stories to {OUT}")
