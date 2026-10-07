import assert from 'node:assert/strict';
import {readFile,readdir,stat} from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.dirname(fileURLToPath(import.meta.url));
const pub=path.join(root,'public');
const articles=JSON.parse(await readFile(path.join(root,'articles.json'),'utf8'));
async function walk(p){return(await Promise.all((await readdir(p,{withFileTypes:true})).map(d=>d.isDirectory()?walk(path.join(p,d.name)):path.join(p,d.name)))).flat();}
const files=(await walk(pub)).filter(f=>f.endsWith('.html'));
const titles=new Set();
for(const f of files){const html=await readFile(f,'utf8');const title=html.match(/<title>(.*?)<\/title>/)?.[1];assert(title&&!titles.has(title),`Missing or duplicate title in ${f}`);titles.add(title);assert.equal((html.match(/<h1[ >]/g)||[]).length,1,`Expected one h1 in ${f}`);assert(html.includes('As an Amazon Associate I earn from qualifying purchases.'));assert(html.includes('name="description"'));assert(html.includes('Linen &amp; Form'));assert(!/college(?!life3500@gmail.com)|dorm|move-in/i.test(html),`Old brand content in ${f}`);assert(!/href="(?:#|undefined|null)"/.test(html));for(const m of html.matchAll(/(?:href|src)="([^"#]+)(?:#[^"]*)?"/g)){if(!m[1].startsWith('/'))continue;const target=path.join(pub,m[1]);await stat(target).catch(()=>{throw Error(`Broken internal URL ${m[1]} in ${f}`);});}for(const m of html.matchAll(/href="#([^"]+)"/g))assert(html.includes(`id="${m[1]}"`),`Missing anchor ${m[1]} in ${f}`);}
assert.equal(articles.length,10);assert.equal(files.length,17);const ids=articles.flatMap(a=>a.products.map(p=>p.id));assert.equal(new Set(ids).size,ids.length);assert.equal(ids.length,30);
for(const a of articles){const words=[a.intro,a.takeaway,...a.sections.flatMap(s=>[...(s.paragraphs||[]),...(s.items||[])]),...a.products.flatMap(p=>[p.name,p.fit,p.why,p.check,p.skip])].join(' ').split(/\s+/).length;assert(words>=350,`${a.slug} has only ${words} words`);console.log(`${a.slug}: ${words} words`);}
console.log(`PASS: ${files.length} HTML pages, unique metadata, internal links/assets/anchors, disclosures, and 10 substantive articles.`);
