from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit,unquote
import json
root=Path(__file__).parent/'dist';errors=[];links=0
class Check(HTMLParser):
 def __init__(self,path):super().__init__();self.path=path;self.ids=set();self.h1=0;self.desc=False
 def handle_starttag(self,tag,attrs):
  global links
  a=dict(attrs)
  if tag=='h1':self.h1+=1
  if tag=='meta' and a.get('name')=='description':self.desc=True
  if a.get('id'):
   if a['id'] in self.ids:errors.append((str(self.path),'duplicate id '+a['id']))
   self.ids.add(a['id'])
  for key in ['href','src','poster']:
   if key not in a:continue
   u=urlsplit(a[key])
   if not u.path.startswith('/'):continue
   dest=root/unquote(u.path).lstrip('/');links+=1
   if not dest.is_file() and not (dest/'index.html').is_file():errors.append((str(self.path),a[key]))
pages=[p for p in root.rglob('*.html') if '__qa' not in p.parts]
for p in pages:
 c=Check(p);c.feed(p.read_text())
 if not c.desc:errors.append((str(p),'description missing'))
 if c.h1!=1 and 'confirmed' not in str(p):errors.append((str(p),'expected one h1'))
report={'html_files':len(pages),'internal_links_and_assets':links,'errors':errors}
print(json.dumps(report,indent=2));assert not errors
