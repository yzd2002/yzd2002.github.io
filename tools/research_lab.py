"""Bilingual demonstrations for the homepage. The first two use illustrative inputs."""
from html import escape

PROJECT = "https://aigeeksgroup.github.io/EvoVLA/"
GROUNDING = "https://aclanthology.org/2026.emnlp-main.1494/"

def model_figure(zh, prefix):
    """Project overview with a local preview and a full-resolution primary source."""
    t = lambda en, cn: cn if zh else en
    full = PROJECT + "img/overview_page-0001.jpg"
    return f'''<figure class="model-figure"><a href="{full}" aria-label="{t("Open the full EvoVLA architecture diagram","查看 EvoVLA 高清架构原图")}"><img loading="lazy" src="{prefix}assets/evovla-method.webp" width="1100" height="671" alt="{t("EvoVLA architecture showing reward modeling, pose-based exploration and memory","EvoVLA 架构图，展示奖励建模、基于物体姿态的探索与记忆模块")}"></a>
    <figcaption><span class="micro">EvoVLA · ECCV 2026</span><h3>{t("How a robot tracks progress","机器人如何追踪任务进展")}</h3>
    <p>{t("Our model rewards individual stages of a task, explores using object poses, and retrieves earlier observations when a later action needs context.","在长时程任务中，我们按阶段给出奖励，依据物体姿态探索，并在后续动作需要上下文时调取先前的观察。")}</p>
    <div class="inline"><a class="textlink" href="{full}">{t("Full-size figure","高清原图")} ↗</a><a class="textlink" href="{PROJECT}">{t("Project and credits","项目与署名")} ↗</a><a class="textlink" href="{prefix}assets/evovla-stacking.gif">{t("Experiment GIF","实验动图")} ↗</a></div></figcaption></figure>'''


def research_lab(zh, prefix, publications):
    def t(en, cn):
        return cn if zh else en

    def mini_record(source, value, change=False):
        marker = ' data-changing' if change else ''
        return f'<div class="input-doc"{marker}><i aria-hidden="true"></i><small>{source}</small><strong>{value}</strong></div>'

    def illustration(first, second, symbol):
        return f'<div class="evidence-flow">{first}<span class="wire" aria-hidden="true"></span><span class="node" aria-hidden="true">{symbol}</span><span class="wire right" aria-hidden="true"></span>{second}</div>'

    def experiment(key, initial, alternate, primary, heading, question, diagram, result_a, result_b, status_a, status_b, symbol_a, symbol_b, target, paper_name):
        hidden = '' if key == 0 else ' hidden'
        act = t('Change the evidence', '改变证据') if key == 0 else t('Move decision to Tuesday', '将决策移至周二')
        back = t('Restore the source', '还原来源') if key == 0 else t('Move decision to Monday', '将决策移回周一')
        return f'''<section class="study" id="experiment-{key}" data-slide="{key}" data-state="initial"{hidden}
            data-initial="{initial}" data-alternate="{alternate}"
            data-claim-a="{result_a}" data-claim-b="{result_b}" data-toggle="{act}" data-restore="{back}"
            data-status-a="{status_a}" data-status-b="{status_b}" data-symbol-a="{symbol_a}" data-symbol-b="{symbol_b}">
            <div class="study-title"><span>{t("Illustrative example","交互示例")}</span><h2>{heading}</h2><p>{question}</p></div>
            {diagram}<div class="readout" id="result-{key}" role="status" aria-atomic="true"><strong class="state-label">{status_a}</strong><span>{primary}</span><b>{result_a}</b></div>
            <div class="study-actions"><button type="button" data-change aria-controls="result-{key}">{act}</button><a href="{escape(target)}">{paper_name} ↗</a></div>
            </section>'''

    room_a, room_b = t('Room A','A 厅'), t('Room B','B 厅')
    evidence = experiment(0, room_a, room_b, t('Expected response','预期回答'),
        t('When sources disagree','当两份证据发生冲突'), t('Where will the seminar take place?','这场研讨会在哪个厅举行？'),
        illustration(mini_record(t('Program','会议日程'),room_a),mini_record(t('Notice','会务通知'),room_a,True),'='),
        t('Room A, according to both sources.','两份来源均指向 A 厅。'),t('The sources conflict. Verify the venue.','两份来源给出的地点不同，需要核实。'),
        t('Sources agree','证据一致'),t('Conflict detected','发现证据冲突'),'=','≠',GROUNDING,'Beyond Static Grounding')
    earlier, later = t('Monday','周一'),t('Tuesday','周二')
    temporal = experiment(1, earlier, later, t('Evidence available','当时可用的证据'),
        t('What was knowable then?','当时能知道什么？'),t('A Monday schedule is revised on Tuesday. Move the decision date to see which version was available.','周一发布的日程在周二修订。改变决策日期，观察当时能使用哪一版。'),
        illustration(mini_record(t('Revision issued','修订发布于'),later),mini_record(t('Decision made','作出决策于'),earlier,True),'–'),
        t('Only the original schedule.','仅能查阅原始日程。'),t('The revision is now available.','此时已可查阅修订版。'),
        t('Revision unavailable','修订版尚不可用'),t('Revision available','修订版已可用'),'–','✓',publications+'#exact','EXACT-Bench')
    robot = f'''<section class="study film" id="experiment-2" data-slide="2" hidden>
        <div class="study-title"><span>ECCV 2026 · EvoVLA</span><h2>{t('Stacking blocks in the real world','真实环境中的积木堆叠')}</h2></div>
        <video controls playsinline muted preload="none" poster="{prefix}assets/evovla-stacking.jpg" aria-label="{t("Real robot stacking blocks","真实机械臂堆叠积木")}">
        <source src="{prefix}assets/evovla-stacking.mp4" type="video/mp4"></video>
        <div class="film-caption"><span>{t('EvoVLA team footage · 3× speed','EvoVLA 团队实录 · 3 倍速')}</span><a href="{PROJECT}">{t('Full experiment','完整实验')} ↗</a></div></section>'''
    options = [t('Evidence','证据检验'),t('Retrieval','时间检索'),t('Robot demo','机器人实录')]
    buttons = ''.join(f'<button type="button" data-plate="{i}" aria-controls="experiment-{i}" aria-pressed="{str(i==0).lower()}">{label}</button>' for i,label in enumerate(options))
    return f'''<div class="atlas lab" id="robot-demo"><div class="lab-head"><span class="lab-symbol" aria-hidden="true">∿</span><b>{t("Research lab","研究演示")}</b><span>{t("Zida Yang","杨子达")}</span></div>
        <div class="switches" aria-label="{t("Choose a demonstration","选择研究演示")}">{buttons}</div>
        {evidence}{temporal}{robot}<noscript><a class="fallback-film" href="{PROJECT}">{t("Watch the EvoVLA experiment","观看 EvoVLA 实验视频")} ↗</a></noscript></div>'''
