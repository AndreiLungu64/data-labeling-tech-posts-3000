import os
import pandas as pd
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

def extract_posts(xml_path, max_posts=1000):
    posts = []
    tree = ET.parse(xml_path)
    root = tree.getroot()

    for row in root.findall('row'):
        post_id = row.attrib.get('Id')
        title = row.attrib.get('Title', '')
        body_html = row.attrib.get('Body', '')

        soup = BeautifulSoup(body_html, 'html.parser')
        body = soup.get_text(separator=' ', strip=True)

        text = f"{title}. {body}".strip() if title else body.strip()

        if len(text) > 50:
            posts.append({'id': post_id, 'text': text})
        if len(posts) >= max_posts:
            break

    return pd.DataFrame(posts)

output_dir = "./csv_datasets/original_csv"
os.makedirs(output_dir, exist_ok=True)

datasets = {
    "codereview_raw.csv": "./xml_datasets/codereview.stackexchange.com/Posts.xml",
    "webapps_raw.csv": "./xml_datasets/webapps.stackexchange.com/Posts.xml",
    "workplace_raw.csv": "./xml_datasets/workplace.stackexchange.com/Posts.xml",
}

for filename, xml_path in datasets.items():
    df = extract_posts(xml_path)
    out_csv = os.path.join(output_dir, filename)
    df.to_csv(out_csv, index=False)
    print(f"Saved {len(df)} posts to {out_csv}")
