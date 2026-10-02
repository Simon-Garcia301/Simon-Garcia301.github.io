"""Check a generated Jekyll site for local links, media, and project references."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
import sys

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids=set(); self.links=[]; self.images=[]; self.refs=[]
        self.h1=0; self.stack=[]; self.nested_controls=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.add(a['id'])
        if tag=='a' and 'href' in a: self.links.append(a['href'])
        if tag in ('link','script'):
            url=a.get('href') or a.get('src')
            if url: self.links.append(url)
        if tag=='img': self.images.append(a)
        if tag=='h1': self.h1+=1
        if tag in ('button','input','select','textarea') and 'a' in self.stack: self.nested_controls.append(tag)
        if tag not in ('img','meta','link','br','hr','input','source'): self.stack.append(tag)
    def handle_endtag(self,tag):
        if tag in self.stack:
            self.stack=self.stack[:len(self.stack)-1-self.stack[::-1].index(tag)]

def check(root):
    pages={p:Page() for p in root.rglob('*.html')}
    failures=[]; checked=0; images=0; projects=[]
    for path,page in pages.items(): page.feed(path.read_text(encoding='utf-8'))
    for path,page in pages.items():
        for url in page.links+[im.get('src','') for im in page.images]:
            parts=urlsplit(url)
            if parts.scheme or parts.netloc: continue
            checked+=1
            target=root/unquote(parts.path).lstrip('/') if parts.path.startswith('/') else path.parent/unquote(parts.path)
            if not parts.path: target=path
            if target.is_dir(): target=target/'index.html'
            if not target.exists(): failures.append(f'{path.relative_to(root)}: missing target {url}'); continue
            if parts.fragment and target.suffix=='.html':
                target_page=pages.get(target)
                if target_page is None:
                    target_page=Page();target_page.feed(target.read_text(encoding='utf-8'))
                if unquote(parts.fragment) not in target_page.ids: failures.append(f'{path.relative_to(root)}: missing fragment {url}')
        images+=len(page.images)
        for im in page.images:
            if 'alt' not in im or not im['alt'].strip(): failures.append(f'{path.relative_to(root)}: missing image alt text: {im.get("src")}')
        if page.nested_controls: failures.append(f'{path.relative_to(root)}: interactive elements nested inside links')
        if path.parent.parent.parent.name=='projects' and path.parent.name=='index':
            # Current collection permalinks are /projects/<project>/index/.
            projects.append(str(path.relative_to(root)))
            if page.h1!=1: failures.append(f'{path.relative_to(root)}: expected one h1')
            refs={id for id in page.ids if id.startswith('ref-')}
            if not refs: failures.append(f'{path.relative_to(root)}: no numbered references')
            for ref in refs:
                if '#'+ref not in page.links: failures.append(f'{path.relative_to(root)}: uncited reference {ref}')
        text=path.read_text(encoding='utf-8')
        if '{%' in text or '{{' in text: failures.append(f'{path.relative_to(root)}: unprocessed Liquid')
    for forbidden in ('docs','private-drafts','portfolio-review','Reference'):
        if (root/forbidden).exists(): failures.append(f'Review-only directory in public output: {forbidden}')
    if (root/'README.md').exists(): failures.append('Template README in public output')
    return {'status':'PASS' if not failures else 'FAIL','html_pages':len(pages),'project_pages':projects,'local_targets_checked':checked,'images_checked':images,'failures':failures}

if __name__=='__main__':
    result=check(Path(sys.argv[1] if len(sys.argv)>1 else '_site').resolve())
    print(json.dumps(result,indent=2))
    sys.exit(0 if result['status']=='PASS' else 1)
