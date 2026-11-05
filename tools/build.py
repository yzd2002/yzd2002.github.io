"""Build a dependency-free, bilingual academic website: python tools/build.py"""
from pathlib import Path
from html import escape as esc
from math import exp
from content import papers, repos, SCHOLAR, GITHUB, AUTHOR, GH, paper
ROOT=Path(__file__).resolve().parents[1]
AS=ROOT/'assets'
AS.mkdir(exist_ok=True)
papers += [
 paper('cost','A Comparative Study of GPT-5.2 and Qwen-Max for Chinese Film Script Continuation','CoST 2026','proceedings',2026,'Miaotong Yuan, Zida Yang, Yuxuan Cao','https://doi.org/10.23919/COSTCPS00105.2026.00074',role='Co-first author'),
 paper('ptcp','Research on the Asymmetry of PTCP Bias Based on Loss Aversion','Chinese Control Conference 2023','proceedings',2023,'Zida Yang, Jiaze Jiao, Weiwei Han','https://doi.org/10.23919/CCC58697.2023.10240686')]
papers.sort(key=lambda p:(-p['year'],{'accepted':0,'proceedings':1,'workshop':2,'supplement':3,'preprint':4,'abstract':5}[p['category']]))
def put(name,data):
    f=ROOT/name
    f.parent.mkdir(parents=True,exist_ok=True)
    f.write_text(data,encoding='utf-8',newline='\n')
def link(url,text,cls=''):
    return f'<a href="{esc(url,quote=True)}" class="{cls}">{text}</a>'
def ei(s):return esc(str(s),quote=True)
def terrain(n):
    # A perspective wireframe of an analytic surface. An illustration, not empirical data.
    peaks=[[(.38,.50,.92,.027),(.70,.69,.65,.020),(.74,.19,.46,.015)],[(.27,.36,.62,.019),(.54,.53,1.0,.030),(.79,.72,.37,.014)],[(.31,.63,.73,.022),(.59,.30,.85,.023),(.72,.64,.52,.019)]][n]
    def point(x,y):
        h=sum(a*exp(-((x-u)**2+(y-v)**2)/s) for u,v,a,s in peaks)
        return (222+217*(x-y),140+84*(x+y)-125*h)
    def xy(x,y):return ','.join(f'{v:.2f}' for v in point(x,y))
    def line(vary,fixed,start=0,end=1):
        return 'M'+' L'.join(xy(start+(end-start)*i/90,fixed) if vary else xy(fixed,start+(end-start)*i/90) for i in range(91))
    wire=''.join(f'<path d="{line(True,j/44)}" opacity="{.44+.4*j/44:.2f}"/>' for j in range(45))+''.join(f'<path d="{line(False,j/38)}" opacity=".34"/>' for j in range(39))
    x,y=point(peaks[0][0],peaks[0][1]);return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 329" fill="none" aria-hidden="true"><defs><pattern id="g" width="20" height="20" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="0.65" fill="#81a99c" opacity=".40"/></pattern></defs><path fill="url(#g)" d="M0 0h460v329H0z"/><g stroke="#a1cfb7" stroke-width=".86" stroke-linecap="round">{wire}</g><path d="{line(True,peaks[0][1])}" stroke="#ffab79" stroke-width="2"/><path d="M{x:.1f} {y:.1f} v-19 l20 -16 h38" stroke="#ffc69b" stroke-width="1" stroke-dasharray="2 3"/><circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="#ff986d" stroke="#183a37" stroke-width="1.5"/><text x="{x+62:.1f}" y="{y-32:.1f}" font-size="9" font-family="monospace" fill="#ffcaad">P.0{n+1}</text></svg>'''
for i in range(3):put('assets/terrain-'+str(i+1)+'.svg',terrain(i))
def art(i):
    grid='<defs><pattern id="dots" width="12" height="12" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="0.9" fill="currentColor" opacity=".20"/></pattern></defs><rect width="240" height="118" fill="url(#dots)"/>'
    shapes=[
    '<g transform="translate(72 12)" fill="#f7e3d5" stroke="#99462f" stroke-width="1.7"><path d="M0 21L53 5l44 14-53 17zM0 36l44 17 53-19M0 51l44 17 53-19M0 66l44 17 53-19"/><path d="M43 36v48" stroke-dasharray="2 4"/><circle cx="97" cy="19" r="5" fill="#a6452c"/></g>',
    '<g transform="translate(58 24)" stroke="#355b65" stroke-width="1.6" fill="none"><path d="M0 34h33l29-27h34M33 34h65M33 34l29 27h34" stroke-dasharray="3 3"/><circle cx="0" cy="34" r="7" fill="#355b65"/><circle cx="33" cy="34" r="4" fill="#edf3ee"/><path d="M98 0h23v15H98zM98 27h23v15H98zM98 54h23v15H98z" fill="#ebf2ee"/><path d="m102 34 4 4 9-10" stroke="#ab4934" stroke-width="2"/></g>',
    '<g transform="translate(56 14)" stroke="#506744" stroke-width="2" fill="none"><path d="M0 87h132M14 83l13-30 9 3-7 27M30 53l39-36 8 9-41 33M76 21l33 20-4 7-34-19M106 44l11 8m-3-4 9-4 6 5m-15 4 1 9 7 1"/><circle cx="30" cy="55" r="6" fill="#ecedda"/><circle cx="73" cy="23" r="8" fill="#ecedda"/><path d="M104 68l10-5 11 5v12l-11 6-10-6zm0 0 10 6 11-6m-11 6v12" stroke="#ac553c"/></g>'
    ][i]
    grid = grid.replace('dots', f'dots{i}')
    return f'<svg viewBox="0 0 240 118" aria-hidden="true">{grid}{shapes}</svg>'
for zn in [False,True]:
    t=lambda en,zh:zh if zn else en
    path='/zh/' if zn else '/'
    pre='../' if zn else './'
    out='zh/' if zn else ''
    pub=path+'publications.html'
    cat={'accepted':t('Accepted','已录用'),'proceedings':t('Proceedings','会议论文'),'workshop':t('Workshops','工作坊'),'supplement':t('Journal supplements','期刊增刊'),'preprint':t('Preprints','预印本'),'abstract':t('Abstracts','会议摘要')}
    def authors(p):
        return ', '.join('<strong>Zida Yang</strong>' if a=='Zida Yang' else ei(a) for a in p['authors'].split(', ') if a)
    def title_links(p):
        items=([('Record',p['url'])] if p['url'] else [])+list(p['links'])
        labels={'Record':t('Publication','成果记录'),'Code':t('Code','代码'),'Dataset':t('Data','数据'),'Reading list':t('Reading list','资源清单'),'Paper':t('Paper','论文')}
        return ''.join(link(u,labels.get(l,l)+' ↗','textlink') for l,u in items)
    def head(active):
        main=t('Research','研究主页'); idx=t('Publications','学术成果'); projects=t('Projects','开源项目')
        other=('/' if zn else '/zh/')+('publications.html' if active=='index' else '')
        return f'<a href="#main" class="skip">{t("Skip to content","跳至正文")}</a><header class="top"><div class="wrap nav"><a href="{path}" class="brand"><span class="stamp" aria-hidden="true">ZY</span><b>Zida Yang</b></a><nav aria-label="{t("Main navigation","主导航")}">{link(path,main,"active" if active=="home" else "")}{link(pub,idx,"active" if active=="index" else "")}{link(path+"#projects",projects)}<a class="lang" href="{other}" lang="{t("zh-CN","en")}">{t("中文","EN")}</a></nav></div></header>'
    def footer():
        return f'<footer class="wrap"><span>Zida Yang <span lang="zh">杨子达</span></span><span>{t("Guanghua School of Management · Peking University","北京大学 · 光华管理学院")}</span>{link(GITHUB,"GitHub ↗")} {link(SCHOLAR,"Google Scholar ↗")}</footer>'
    def page(body,active):
        name='Zida Yang · 杨子达' if not zn else '杨子达 · Zida Yang'
        title=name+' | '+(t('Research at Peking University','北京大学 · 学术主页') if active=='home' else t('Publications','学术成果'))
        canon='https://yzd2002.github.io'+path+('publications.html' if active=='index' else '')
        desc=t('Zida Yang studies trustworthy AI and decision support at Peking University. Explore research on evidence, retrieval, and embodied intelligence.','北京大学光华管理学院杨子达的学术主页，收录可信人工智能、信息检索与具身智能研究、开放资源及论文记录。')
        return f'<!doctype html><html lang="{t("en","zh-CN")}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#183e38"><title>{title}</title><meta name="description" content="{desc}"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:url" content="{canon}"><link rel="canonical" href="{canon}"><link rel="alternate" hreflang="en" href="https://yzd2002.github.io/{("publications.html" if active=="index" else "")}"><link rel="alternate" hreflang="zh-CN" href="https://yzd2002.github.io/zh/{("publications.html" if active=="index" else "")}"><link rel="icon" type="image/svg+xml" href="{pre}assets/mark.svg"><link rel="stylesheet" href="{pre}assets/site.css"><script src="{pre}assets/site.js" defer></script></head><body>{head(active)}<main id="main">{body}</main>{footer()}</body></html>'
    questions=[t('Does the answer follow the evidence?','答案是否跟随证据变化？'),t('Was the evidence available then?','作出判断时，这条证据已经存在吗？'),t('Did the robot finish the task?','机器人真的完成了任务吗？')]
    tabnames=[t('Evidence','证据'),t('Time','时间'),t('Action','行动')]
    ids=['2026.emnlp-main.1494','exact','evovla']
    plate=''.join(f'<div class="plate-slide" data-slide="{i}" {"" if i==0 else "hidden"}><img width="460" height="329" src="{pre}assets/terrain-{i+1}.svg" alt=""><div class="plate-q">{link(pub+"#"+ids[i],questions[i]+" ↗")}</div></div>' for i in range(3))
    atlas=f'<figure class="atlas"><div class="atlas-bar"><span>ZY / RESEARCH ATLAS</span><span id="plate-number">FIG. 01 / 03</span></div>{plate}<div class="switches" aria-label="{t("Research themes","研究主题")}">'+''.join(f'<button data-plate="{i}" aria-pressed="{str(i==0).lower()}">{s}</button>' for i,s in enumerate(tabnames))+'</div></figure>'
    hero=f'''<section class="hero wrap"><div class="intro"><p class="eyebrow"><i></i>{t("PEKING UNIVERSITY · RESEARCH PROFILE","北京大学 · 学术主页")}</p><div class="identity"><div><h1>{t('Zida <em>Yang</em>','杨子达')}</h1><p class="altname">{t('杨子达','Zida Yang')}</p></div><img class="portrait" src="{pre}assets/zida-yang.jpg" width="192" height="256" alt="{t('Portrait of Zida Yang','杨子达肖像')}"></div><p class="position">{t('Ph.D. student in Management Science and Information Systems<br>Guanghua School of Management, Peking University','北京大学光华管理学院博士研究生<br>企业管理专业 · 管理科学与信息系统方向')}</p><p class="lead">{t('I study when AI can be trusted to act on evidence. My work tests how language models respond to changing information and how robots recognize progress in a task.','我研究人工智能在什么条件下能依据证据可靠行动：当信息变化时，语言模型会不会修正答案？执行复杂任务时，机器人能否识别真正的进展？')}</p><div class="actions">{link(pub,t("Explore publications","浏览学术成果")+" <span>→</span>","btn")} {link(SCHOLAR,"Google Scholar ↗","quietlink")}</div></div>{atlas}</section>'''
    latest=f'<aside class="latest"><div class="wrap"><span class="eyebrow">{t("LATEST / NOV 2026","近况 / 2026.11")}</span><p>{t("Three papers accepted to <strong>WSDM 2027 Findings</strong>.","三篇论文获 <strong>WSDM 2027 Findings</strong> 录用。")}</p>{link(pub+"#mechedit",t("View the papers","查看论文")+" →","textlink")}</div></aside>'
    featids=['2026.emnlp-main.1205','2026.emnlp-main.1494','evovla']
    cards=''
    for i,id in enumerate(featids):
        p=next(x for x in papers if x['id']==id)
        short=['EMER-Guard','Beyond Static Grounding','EvoVLA'][i]
        cards+=f'<article class="feature"><a class="cover c{i}" href="{p["url"]}" aria-label="{ei(short)}">{art(i)}</a><div class="ftext"><span class="micro">{p["venue"]}</span><h3>{link(p["url"],short)}</h3><p>{ei(p["cn"] if zn else p["note"])}</p>{link(p["url"],t("Read the research","阅读研究")+" ↗","textlink")}</div></article>'
    feature=f'<section class="wrap section" id="research"><div class="section-head"><div><h2>{t("Selected work","代表研究")}</h2></div>{link(pub,t("Full research index","完整成果目录")+" →","textlink")}</div><div class="cards">{cards}</div></section>'
    groups=[('EvoVLA',GH+'AIGeeksGroup/EvoVLA',t('Model, code and a long-horizon manipulation benchmark.','视觉语言动作模型、代码与长时程操作基准。')),('MobileVLA-R1',GH+'AIGeeksGroup/MobileVLA-R1',t('Training resources for mobile robot navigation and action.','移动机器人的导航与行动模型训练资源。')),('Awesome GC-VWM',GH+'AIGeeksGroup/Awesome-GC-VWM',t('An annotated reading list for geometry-consistent video world models.','关于几何一致性视频世界模型的论文、数据集与基准清单。'))]
    lines=''.join(f'<a class="project-row" href="{u}"><span><b>{s}</b><small>{d}</small></span><em>↗</em></a>' for s,u,d in groups)
    kinds={'Research fork':'合作研究 · 复刻','Fork':'复刻','Repository':'项目仓库','Project':'项目','Profile':'个人资料','Website':'网站'}
    directory=''.join(f'<li><a href="{GITHUB}/{name}"><b>{ei(name)} ↗</b></a><span>{kinds[k] if zn else k}</span><small>{c if zn else e}</small></li>' for name,k,e,c in repos)
    pro=f'<section class="resource" id="projects"><div class="wrap projectgrid"><div><h2>{t("Code &amp; resources","代码与资源")}</h2><p>{t("Our project repositories bring together implementations, data and reading lists for studying embodied intelligence and world models.","团队的开放项目提供实现代码、数据与阅读清单，方便复现具身智能研究，也便于追踪世界模型的发展。")}</p>{link(GITHUB,t("GitHub profile","GitHub 个人资料")+" ↗","textlink")}</div><div>{lines}</div></div><div class="wrap"><details class="repos"><summary>{t("Personal repository directory","个人公开仓库目录")} <span>{len(repos):02}</span></summary><ul>{directory}</ul></details></div></section>'
    about=f'<section class="wrap section about"><div><h2>{t("About","关于我")}</h2></div><div><p>{t("I am a doctoral student at the Guanghua School of Management, Peking University, where I began my Ph.D. in 2024. My training in management science shapes the questions I ask about AI: what evidence was available, which constraints mattered, and what would have changed the decision?","我于 2024 年进入北京大学光华管理学院攻读博士学位。管理科学训练影响着我研究人工智能的方式：作出决策时有哪些证据可用，哪些约束真正起作用，又有哪些变化足以改变判断？")}</p><p>{t("I also study the people behind AI systems. Two INDL-9 conference abstracts explore how workers can verify data provenance and participate in the governance of AI supply chains.","我也关注人工智能系统背后的劳动者。两篇 INDL-9 会议摘要讨论劳动者如何核验数据来源，以及如何参与人工智能供应链治理。")}</p><div class="inline">{link("https://indl-9.sciencesconf.org/736729",t("Worker-verified traceability","劳动者核验的可追溯性")+" ↗","textlink")}{link("https://indl-9.sciencesconf.org/736739",t("Labour bill of materials","劳动物料清单")+" ↗","textlink")}{link(AUTHOR,"ACL Anthology ↗","textlink")}</div></div></section>'
    put(out+'index.html',page(hero+latest+feature+pro+about,'home'))
    tools=f'<div class="filters" hidden><label class="search"><span>⌕</span><input id="search" type="search" autocomplete="off" aria-label="{t("Search publications","搜索学术成果")}" placeholder="{t("Search title, author, venue…","搜索标题、作者、会议…")}"></label><div class="pills" aria-label="{t("Filter by type","按类型筛选")}">'+''.join(f'<button data-filter="{k}" aria-pressed="{str(k=="all").lower()}">{v}</button>' for k,v in [('all',t('All','全部')),*cat.items()])+'</div></div>'
    rows=''
    for p in papers:
        role={'Co-first & corresponding author':'共同第一作者、通讯作者','Co-first author':'共同第一作者'}.get(p['role'],p['role']) if zn else p['role']
        by=authors(p)

        note=ei(p['cn'] if zn else p['note'])
        rows+=f'<article class="paper" id="{p["id"]}" data-cat="{p["category"]}"><div class="meta"><span>{p["year"]}</span><small>{cat[p["category"]]}</small></div><div class="record"><div class="venue">{ei(p["venue"])}{(" · "+t("Accepted","已录用")) if p["category"]=="accepted" else ""}</div><h3 lang="en">{link(p["url"],ei(p["title"])) if p["url"] else ei(p["title"])}</h3>{("<p class=by>"+by+"</p>") if by else ""}{("<small class=role>"+ei(role)+"</small>") if role else ""}{("<p class=note>"+note+"</p>") if note else ""}<div class="inline">{title_links(p)}</div></div></article>'
    hdr=f'<div class="lib-hero"><div class="wrap"><h1>{t("Publications","学术成果")}</h1><p>{t("Research papers, accepted work, preprints and conference abstracts.","论文、已录用成果、预印本与会议摘要。")}</p>{link(AUTHOR,"ACL Anthology ↗","textlink")} {link(SCHOLAR,"Google Scholar ↗","textlink")}</div></div>'
    put(out+'publications.html',page(hdr+f'<section class="wrap catalogue">{tools}<p id="matches" aria-live="polite"></p><div id="records">{rows}</div><p id="empty" hidden>{t("No matching work. Try another term or category.","没有匹配结果，请尝试其他关键词或类别。")}</p></section>','index'))
