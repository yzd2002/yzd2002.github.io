"""Public, editorially curated research records. WSDM entries report acceptance only."""
ACL='https://aclanthology.org/'
GH='https://github.com/'
SCHOLAR='https://scholar.google.com/citations?user=0XE_GW4AAAAJ'
GITHUB=GH+'yzd2002'
AUTHOR=ACL+'people/zida-yang/'
def paper(id,title,venue,category,year,authors='',url='',note='',cn='',links=(),role=''):
    return dict(id=id,title=title,venue=venue,category=category,year=year,authors=authors,url=url,note=note,cn=cn,links=links,role=role)
def acl(id,title,venue,cat,authors,note='',cn='',role=''):
    return paper(id,title,venue,cat,2026,authors,ACL+id+'/',note,cn,[('PDF',ACL+id+'.pdf'),('BibTeX',ACL+id+'.bib')],role)
papers=[
paper('teacher-stress','Analysis of Psychological Stress of Vocational Teachers Based on the JD-R Model and Artificial Intelligence Intervention','The International Journal of Psychiatry in Medicine · 61(1_suppl), 129S–130S','supplement',2026,'Guiheng Hu, Zida Yang, Bingyan Yu','https://scholar.google.com/citations?view_op=view_citation&user=0XE_GW4AAAAJ&citation_for_view=0XE_GW4AAAAJ:IjCSPb-OGe4C'),
paper('mechedit','MechEdit-Agent: Auditable Mechanism-Editable Event Twins for Risk-Aware Compound-Flood Emergency Response','WSDM 2027 Findings','accepted',2027,note='How can the mechanisms in a compound-flood model be edited and audited when planning an emergency response?',cn='在复合洪灾应急规划中，如何修改事件模型的机制，并让这些修改可供审计？'),
paper('exact','EXACT-Bench: EX-ante Availability-aware Counterfactual Temporal Retrieval over Versioned Knowledge Snapshots','WSDM 2027 Findings','accepted',2027,note='What could a retrieval system have known at the time of a decision? This benchmark poses that question across versions of a knowledge source.',cn='在作出决策的那一刻，检索系统实际能知道什么？这项研究从知识的历史版本出发，评估面向特定时间的检索。'),
paper('copies','Copies Should Not Create Evidence: Conservation Laws for Web Retrieval under Representation Multiplicity','WSDM 2027 Findings','accepted',2027,note='If several pages repeat the same source, should they count as independent evidence? A study of duplication in web retrieval.',cn='多个网页重复同一来源时，能否把它们视为独立证据？这项工作研究网页检索中的重复表征。'),
acl('2026.aacl-short.30','SEAL-PR: Scientific Evidence-Audited and Locally Isolated Peer Review under Untrusted Manuscripts','IJCNLP–AACL 2026 · Short Papers','proceedings','Zida Yang, Guquan You, Weiqing Zeng, Yu Zheng'),
acl('2026.findings-aacl.136','Prompt Rewrites Are Semantic Actions: Testing Whether Language Models Obey Typed Operator Laws','Findings of ACL: IJCNLP–AACL 2026','proceedings','Zida Yang, Weiqing Zeng, Guquan You, Yu Zheng'),
acl('2026.emnlp-main.1205','EMER-Guard: Protocol-Grounded Verification for LLM Emergency Instructions','EMNLP 2026 · Main Conference','proceedings','Zida Yang, Guquan You, Yu Zheng','We built a 69,000-example benchmark to test emergency instructions against official guidance. The verifier is evaluated on both missed hazards and unnecessary refusals.','构建含 6.9 万个反事实样本的评测基准，依据应急规程核查大模型指令，分别衡量漏检危险建议和误拦安全建议的代价。'),
acl('2026.emnlp-main.1494','Beyond Static Grounding: Behavioral Contracts for Trustworthy Retrieval-Augmented Generation','EMNLP 2026 · Main Conference','proceedings','Weiqing Zeng, Zida Yang, Guquan You, Haoran Yang, Yu Zheng','We test the same question after removing, contradicting, reordering, or adding distracting evidence, and measure whether the answer changes as it should.','对同一问题分别删除证据、制造冲突、调换顺序或引入干扰，检验检索增强生成系统是否在该改变答案时改变、该坚持时坚持。','Co-first & corresponding author'),
acl('2026.emnlp-main.1270','Beyond Leaderboards: A Frozen-Rubric Contract for Position-Invariant Winning-Argument Detection','EMNLP 2026 · Main Conference','proceedings','Zida Yang, Weiqing Zeng, Guquan You, Jiexin Zheng','Tests whether an argument judge reaches the same conclusion when the speakers swap positions.','交换陈述顺序，检验论证评判模型能否保持判断一致。'),
acl('2026.groundlm-1.18','Lifecycle Faithfulness for Grounded Retrieval-Augmented Generation: Benchmarks, Evaluation, and the Vera-Life Controller','GroundLM 2026 · EMNLP Workshop','workshop','Zida Yang, Guquan You, Jiexin Zheng, Yijie Peng'),
acl('2026.groundlm-1.24','CoSched-Cert: Faithful Multi-Turn Scheduling Dialogue via Solver-Verified Certificates','GroundLM 2026 · EMNLP Workshop','workshop','Zida Yang, Minhao Zou, Yijie Peng'),
acl('2026.groundlm-1.77','When Targeted Grounded Gains Hide Complementary Abstraction Regression: DION-Bench and a Conjunctive Evaluation Protocol','GroundLM 2026 · EMNLP Workshop','workshop','Zida Yang, Guquan You, Jiexin Zheng, Yijie Peng'),
paper('evovla','EvoVLA: Self-Evolving Vision-Language-Action Model','ECCV 2026','proceedings',2026,'Zeting Liu, Zida Yang, Zeyu Zhang, Hao Tang','https://aigeeksgroup.github.io/EvoVLA/','Studies how a robot can tell actual progress from states that merely look like success in a multi-step task.','在多阶段任务中，机器人怎样分辨真正完成了一步与仅仅看上去完成了一步？',[('Paper','https://arxiv.org/abs/2511.16166'),('Code',GH+'AIGeeksGroup/EvoVLA'),('Dataset','https://huggingface.co/datasets/AIGeeksGroup/Discoverse-L')],'Co-first author'),
paper('mobile','MobileVLA-R1: Reinforcing Vision-Language-Action for Mobile Robots','ECCV 2026','proceedings',2026,'Ting Huang, Dongjian Li, Rui Yang, Zeyu Zhang, Zida Yang, Hao Tang','https://aigeeksgroup.github.io/MobileVLA-R1/',links=[('Paper','https://arxiv.org/abs/2511.17889'),('Code',GH+'AIGeeksGroup/MobileVLA-R1'),('Dataset','https://huggingface.co/datasets/AIGeeksGroup/MobileVLA-CoT')]),
paper('geometry','Geometry-consistent Video World Models: A Survey','SSRN · Preprint','preprint',2026,'Zida Yang, Yihao Lu, Liyang Wang, Zeyu Zhang, Ling Shao, Hao Tang','https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7420018',links=[('Reading list',GH+'AIGeeksGroup/Awesome-GC-VWM')]),
paper('indl-lineage','Labor as Critical Infrastructure: Worker-Verified Traceability for Human-Centric AI Supply Chains','INDL-9 · Conference Abstract','abstract',2026,'Zida Yang, Yuxuan Cao','https://indl-9.sciencesconf.org/736729'),
paper('indl-lbom','From Human-in-the-Loop to Workers-in-Governance: A Labour Bill of Materials for Human-Centric AI Supply Chains','INDL-9 · Conference Abstract','abstract',2026,'Zida Yang, Yuxuan Cao','https://indl-9.sciencesconf.org/736739'),
]
# The personal account's public repository directory. A fork is not evidence of authorship.
repos=[
('EvoVLA','Research fork','Vision–language–action research.','视觉语言动作模型合作研究。'),
('MobileVLA-R1','Research fork','Vision–language–action for mobile robots.','面向移动机器人的视觉语言动作模型。'),
('CohortCert','Repository','Project space for shared evidence and proof costs in cohort decisions.','面向群体决策的共享证据与证明成本研究仓库。'),
('Q-BRIDGE-ICDE2027','Repository','Project space for reusable policy certificates across observational and randomized logs.','面向观察与随机试验日志的可复用策略证书研究仓库。'),
('ShoppingBench','Fork','A fork of the ShoppingBench benchmark.','ShoppingBench 基准的复刻仓库。'),
('mingxin-brochure-2026','Project','A recruitment brochure built with TypeScript.','使用 TypeScript 实现的招聘宣传手册。'),
('my-novel','Project','A creative writing repository.','创意写作项目。'),
('claw-code','Fork','A fork of the upstream coding-agent project.','上游编程智能体项目的复刻仓库。'),
('ceshi','Project','A small Python test repository.','Python 测试仓库。'),
('test-repo','Project','A test repository.','测试仓库。'),
('yzd2002','Profile','GitHub profile and academic homepage link.','GitHub 个人资料与学术主页入口。'),
('yzd2002.github.io','Website','Source for this academic website.','本学术主页的源代码。'),
]
