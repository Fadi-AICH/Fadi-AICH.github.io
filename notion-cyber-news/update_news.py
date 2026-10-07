#!/usr/bin/env python3
import base64
import hashlib
import html
import json
import mimetypes
import os
import re
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from urllib.parse import urlparse

RSS_URL = "https://feeds.feedburner.com/TheHackersNews"
OUT = "notion-cyber-news/news.json"
IMAGE_DIR = "notion-cyber-news/images"
UA = "Mozilla/5.0 (compatible; FadiCyberNewsWidget/1.2)"

os.makedirs(IMAGE_DIR, exist_ok=True)

def request(url, accept="*/*", timeout=20):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": accept,
        "Referer": "https://thehackernews.com/",
    })
    return urllib.request.urlopen(req, timeout=timeout)

def get_text(url, timeout=20):
    with request(url, "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", timeout) as r:
        return r.read().decode("utf-8", "replace")

def strip_html(s):
    s = html.unescape(s or "")
    s = re.sub(r"<script[\s\S]*?</script>", " ", s, flags=re.I)
    s = re.sub(r"<style[\s\S]*?</style>", " ", s, flags=re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", s).strip()

def first_image_from_html(s):
    if not s:
        return ""
    for pattern in (
        r'<img[^>]+src=["\']([^"\']+)["\']',
        r'<img[^>]+data-src=["\']([^"\']+)["\']',
    ):
        m = re.search(pattern, s, flags=re.I)
        if m:
            return html.unescape(m.group(1))
    return ""

def og_image(url):
    try:
        page = get_text(url)
    except Exception:
        return ""
    for pattern in (
        r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']',
        r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']',
        r'<meta[^>]+name=["\']twitter:image(?::src)?["\'][^>]+content=["\']([^"\']+)["\']',
        r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+name=["\']twitter:image(?::src)?["\']',
    ):
        m = re.search(pattern, page, flags=re.I)
        if m:
            return html.unescape(m.group(1))
    return ""

def node_text(node, name):
    x = node.find(name)
    return (x.text or "").strip() if x is not None and x.text else ""

def load_previous():
    try:
        with open(OUT, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"items": []}

def optimize_blogger_image(url):
    return re.sub(r"/s(?:1600|1200|1000|800)/", "/s480/", url, count=1)

def extension_from(content_type, url):
    ctype = (content_type or "").split(";")[0].strip().lower()
    if ctype == "image/png":
        return ".png"
    if ctype == "image/webp":
        return ".webp"
    if ctype in ("image/jpeg", "image/jpg"):
        return ".jpg"
    ext = os.path.splitext(urlparse(url).path)[1].lower()
    if ext in (".png", ".webp", ".jpg", ".jpeg"):
        return ".jpg" if ext == ".jpeg" else ext
    return ".jpg"

def cache_image(remote_url, article_link):
    if not remote_url:
        return ""
    remote_url = optimize_blogger_image(remote_url)
    key = hashlib.sha1(article_link.encode("utf-8")).hexdigest()[:16]
    try:
        with request(remote_url, "image/avif,image/webp,image/apng,image/*,*/*;q=0.8", 25) as r:
            data = r.read(2_500_001)
            if len(data) > 2_500_000:
                raise ValueError("image too large")
            ctype = r.headers.get("Content-Type", "")
            if not ctype.lower().startswith("image/"):
                raise ValueError(f"unexpected content type: {ctype}")
            ext = extension_from(ctype, remote_url)
    except Exception as exc:
        print(f"Image cache failed for {article_link}: {exc}")
        return ""
    filename = f"{key}{ext}"
    path = os.path.join(IMAGE_DIR, filename)
    with open(path, "wb") as f:
        f.write(data)
    return f"images/{filename}"

def image_to_data_uri(cache_path):
    if not cache_path:
        return ""
    full = os.path.join("notion-cyber-news", cache_path)
    if not os.path.isfile(full):
        return ""
    mime = mimetypes.guess_type(full)[0] or "image/jpeg"
    with open(full, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("ascii")
    return f"data:{mime};base64,{encoded}"

previous = load_previous()
previous_by_link = {item.get("link"): item for item in previous.get("items", []) if item.get("link")}

xml = get_text(RSS_URL)
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

    prev = previous_by_link.get(link, {})
    cached = prev.get("image_cache", "")
    if not cached and str(prev.get("image", "")).startswith("images/"):
        cached = prev.get("image", "")

    if not (cached and os.path.isfile(os.path.join("notion-cyber-news", cached))):
        remote_image = ""
        for tag in (media_ns + "content", media_ns + "thumbnail"):
            el = item.find(tag)
            if el is not None and el.attrib.get("url"):
                remote_image = el.attrib["url"]
                break
        if not remote_image:
            for enc in item.findall("enclosure"):
                if enc.attrib.get("type", "").startswith("image/") and enc.attrib.get("url"):
                    remote_image = enc.attrib["url"]
                    break
        if not remote_image:
            remote_image = first_image_from_html(desc)
        if not remote_image and link:
            remote_image = og_image(link)
        cached = cache_image(remote_image, link)

    image_data = image_to_data_uri(cached)

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
        "image": image_data,
        "image_cache": cached,
    })

used_images = {os.path.basename(item["image_cache"]) for item in out if item.get("image_cache", "").startswith("images/")}
for filename in os.listdir(IMAGE_DIR):
    path = os.path.join(IMAGE_DIR, filename)
    if os.path.isfile(path) and filename not in used_images:
        os.remove(path)

if previous.get("items") == out:
    print("No article changes; keeping existing news.json timestamp.")
else:
    payload = {
        "source": "The Hacker News",
        "source_url": "https://thehackernews.com/",
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "items": out,
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Wrote {len(out)} stories with embedded thumbnails to {OUT}")
