from pathlib import Path
from html import escape as e
R=Path(__file__).resolve().parents[1]
def pair(en,zh): return [en,zh]
D={
'name':pair('Han Lan','兰晗'),
'role':pair('Physics educator · Learning experience designer','物理教师 · 学习体验设计'),
'headline':pair('Designing for understanding.','为真正理解而设计。'),
'intro':pair('I teach international physics in Shanghai and build AI-assisted learning resources. My work starts with a classroom question: how can we tell whether a student understands, beyond getting the answer right?','我在上海教授国际课程物理，并借助 AI 开发学习资源。我的工作始于一个课堂问题：除了答对题目，我们如何知道学生是否真正理解？'),
'nav':pair(['Selected work','Experience','Inquiry','Contact'],['精选作品','经历','研究兴趣','联系']),
'metrics':pair([('34','physics simulations designed'),('50+','units of bilingual notes'),('4 centres','WorkBuddy guide adopted')],[('34','个已设计的物理模拟'),('50+','单元中英双语讲义'),('4 个中心','采用 WorkBuddy 指南')]),
'work_intro':pair('Three perspectives on the same problem: making thinking visible, supporting feedback, and helping teachers use AI with care.','从三个角度回应同一个问题：让思考可见、支持反馈，并帮助教师审慎地使用 AI。'),
'cases':[
{'id':'simulations','img':'simulations.jpg','title':pair('Making wave representations meaningful','让波的多种表征建立联系'),'tag':pair('01 / Interactive learning · Used in teaching','01 / 交互学习 · 已用于教学'),'summary':pair('Connecting particle motion with displacement–distance and displacement–time graphs.','把粒子运动与位移—距离、位移—时间图像联系起来。'),'blocks':[
('The learning problem','学习问题','Some students read a longitudinal-wave displacement graph as a picture of the medium. A correct-looking curve can conceal a misunderstanding of particle motion.','部分学生把纵波位移图像当成介质的形状。看似正确的曲线背后，可能仍然混淆了粒子的运动。'),
('My contribution','我的工作','I selected the concepts, checked the physics, and used AI-assisted coding to build browser simulations. The wave example places particle motion beside both graph types and allows a single particle to be followed frame by frame.','我选择概念、核验物理规律，并借助 AI 编程实现浏览器模拟。波动案例将粒子运动与两种图像并列呈现，可逐帧追踪单个粒子。'),
('Evidence and limits','证据与局限','I designed 34 simulations across mechanics, waves and electricity. They have been shared with roughly 100 teachers; this is estimated sharing reach, not verified active use. Classroom walkthroughs suggested clearer understanding, but transfer to unfamiliar problems has not been reliably measured.','我设计了力学、波动和电学等 34 个模拟，分享覆盖约 100 位教师；这是估计的分享范围，而非核实的活跃用户数。课堂讲解中观察到理解有所改善，但尚未可靠测量对陌生题目的迁移。'),
('Next evaluation','下一步验证','Compare explanations before and after the activity, then use an unfamiliar wave question without the simulation. Score explanations with a clear rubric and examine persistent misconceptions. This is a proposed study, not a completed result.','计划对比活动前后的解释，再用不提供模拟的陌生波动题检查迁移；按明确量规评分，并分析仍然存在的误解。这是拟开展的研究，而非已完成的结果。')], 'video':'simulations.mp4'},
{'id':'whitespace','img':'assets/ws-desk.jpg','title':pair('Whitespace: when should AI step back?','留白：AI 何时应当退场？'),'tag':pair('02 / Formative feedback · Prototype paused','02 / 形成性反馈 · 原型开发暂停'),'summary':pair('Independent attempts, rubric-based feedback and hints, followed by a new task.','先独立作答，再接受基于评分标准的反馈与提示，最后换题检验。'),'blocks':[
('The learning problem','学习问题','Fast answers can hide fragile understanding. I wanted a workflow that preserves the learner’s effort while making feedback manageable for a teacher.','快速获得答案可能掩盖脆弱的理解。我希望保留学生必要的思考，同时让教师能够处理反馈工作。'),
('My contribution','我的工作','I designed an AI marking and hinting prototype using official marking criteria. Independent attempts and transfer checks are separated from supported practice. The interface presents scoring evidence and flags disagreements for teacher review. Implementation used AI-assisted coding.','我设计了依照官方评分标准批改并提供提示的 AI 原型，将独立作答、换题验证与有辅助的练习分开。界面呈现评分依据，并将分歧交给教师复核；实现过程使用了 AI 辅助编程。'),
('What the initial test can tell us','初步测试能够说明什么','I tested seven language models on 16 student responses. Reference scores were checked with AI assistance, without a dependable human benchmark. Agreement in that exercise cannot establish marking accuracy or learning benefit. Further development is paused until evaluation is reliable.','我用 16 份学生作答测试了 7 个大模型。对照分数经 AI 辅助复核，缺少可靠的人工基准；因此一致率不能证明批改准确率或学习效果。在建立可靠评价方法之前，进一步开发已暂停。'),
('Next evaluation','下一步验证','Build a human-graded benchmark, resolve disagreements between raters, and evaluate feedback quality alongside scoring agreement. Test whether students can explain and solve a new problem without AI.','建立人工评分基准，处理评分者分歧，同时检查反馈质量与评分一致性；再验证学生能否在无 AI 支持时解释并解决新问题。')], 'extra':'assets/ws-probe.jpg'},
{'id':'teacher-tools','img':'assets/bilingual-en.jpg','title':pair('AI tools with a teacher’s quality checks','带着教师质量检查使用 AI'),'tag':pair('03 / Teacher development · Internal practice','03 / 教师发展 · 内部实践'),'summary':pair('Bilingual curriculum resources, explicit review criteria and practical training.','双语课程资源、明确的检查标准与实际培训。'),'blocks':[
('The practical problem','实践问题','AI can produce teaching materials quickly, but speed alone does not ensure coherent explanations, accurate physics or useful assessment tasks.','AI 可以快速生成教学材料，但速度本身不能保证解释连贯、物理准确或评价任务有效。'),
('My contribution','我的工作','Since January 2026, I have built 13 internal tools with AI assistance for curriculum work, producing notes across more than 50 units. I defined requirements, created a nine-dimension review checklist, and reviewed and corrected 11 batches of output.','自 2026 年 1 月起，我借助 AI 搭建了 13 个内部教研工具，产出覆盖 50 多个单元的讲义。我定义需求、制定九个维度的检查表，并审查和修订了 11 批产出。'),
('Sharing the practice','推广与培训','I wrote a Tencent WorkBuddy guide adopted by centres in Shanghai, Beijing, Wuxi and Chongqing, trained around 60 teachers and 30 education advisers, and ran two workshops on AI in teaching. These describe delivery and reach, not measured learning gains.','我撰写的腾讯 WorkBuddy 指南被上海、北京、无锡、重庆四个中心采用；培训约 60 位教师和 30 位教育顾问，并开展两次 AI 教学应用教研活动。这些数据说明交付与覆盖范围，不代表已测得学习增益。'),
('What I want to investigate','希望进一步研究的问题','Which review steps catch consequential errors, and which can be made less demanding? I want to connect teacher review effort with the quality of the learning tasks students actually receive.','哪些检查步骤能够发现关键错误，哪些步骤可以降低教师负担？我希望把教师复核投入与学生实际获得的学习任务质量联系起来。')]}],
'explorations':pair([
('Learning OS','Local prototype','A beginner programming learning flow connects a web lesson view with real files, execution and checks in VS Code. It distinguishes reading instructions from producing evidence of an independent attempt. Learning effectiveness remains untested.'),
('AI-supported PBL','Course package in development','An interactive marketing project takes learners through needs, generation, testing, revision and delivery. Existing checks concern software logic; classroom feasibility and individual transfer still need validation.'),
('Standard course workflow','Pilot paused','Piloted the first five stages of an eight-stage course development workflow for Edexcel IAL Unit 1. Further development is paused pending reliable evaluation of generated course content.')],[
('Learning OS','本地原型','把网页课程与 VS Code 中的真实文件、运行和检查连接起来，区分“读过讲解”和“产出独立尝试的证据”。学习效果尚未验证。'),
('AI 支持的 PBL','课程包开发中','互动营销任务围绕需求、生成、测试、迭代与交付展开。已有检查主要涉及软件逻辑，课堂可行性及个人迁移仍待验证。'),
('标准课程工作流','试点暂停','以 Edexcel IAL Unit 1 试跑八阶段课程开发流程的前五步。在建立可靠的生成内容评价方法之前，进一步开发已暂停。')]),
'experience':pair([
('2025.02 — present','International Physics Teacher · New Oriental, Shanghai','Teaching AP, Cambridge International and Pearson Edexcel physics, alongside competition teaching and IB course preparation. In May 2026, four of my six AP students scored 5 and two scored 4; these results do not isolate the effect of any single resource.'),
('2026.07 — present','Trainee Product Designer · concurrent role','Selected as one of six trainee product designers from 37 candidates. My focus is translating classroom problems into learning tools and examining the evidence needed to improve them.'),
('2023.07 — 2025.02','Testing Engineer · Shanghai Jianke Testing','Worked on testing, standards-based reporting and preparation for a testing laboratory. This strengthened my attention to explicit criteria and traceable judgements.'),
('2022.08 — 2023.07','Research Assistant · Tongji University','Worked on structural testing, data analysis and numerical modelling. This work led to four patent applications, two of which have since been granted.'),
('2018.09 — 2022.07','BEng, Civil Engineering · Tongji University','Engineering training is the foundation of my approach to modelling, measurement and checking assumptions.')],[
('2025.02 — 至今','国际物理教师 · 上海新东方','教授 AP、Cambridge International、Pearson Edexcel 物理及竞赛课程，并参与 IB 课程准备。2026 年 5 月的 6 位 AP 学生中，4 位获 5 分、2 位获 4 分；这不能单独归因于某项教学资源。'),
('2026.07 — 至今','见习产品设计师 · 兼任','从 37 位候选人中选出的 6 位见习产品设计师之一。关注如何把课堂问题转化为学习工具，以及需要什么证据来改进它们。'),
('2023.07 — 2025.02','检测工程师 · 上海建科检验','参与检测、依据标准撰写报告和实验室筹备。这段经历让我重视明确的判定标准与可追溯的依据。'),
('2022.08 — 2023.07','研究助理 · 同济大学','参与结构试验、数据分析和数值模拟。相关工作形成四项专利申请，其中两项已获授权。'),
('2018.09 — 2022.07','土木工程 · 工学学士 · 同济大学','工程训练构成了我建模、测量和检查假设的基础。')]),
'inquiry':pair('My next question is how teachers can review and calibrate AI-generated feedback efficiently without losing sight of student reasoning. I hope to study a human-in-the-loop formative assessment workflow for explanations in waves or electricity, using clear rubrics, human-graded responses and independent transfer tasks.','我下一步关注的问题是：教师如何高效复核、校准 AI 生成的反馈，同时看清学生的推理？我希望围绕波动或电学解释题，结合明确量规、人工评分作答和独立迁移任务，研究教师参与复核的形成性评价流程。'),
'reflection':pair('An AI-assisted review of transcripts from 217 of my lessons prompted me to reconsider how quickly I answered my own questions. I now plan key questions and give students longer to explain. I treat that analysis as a prompt for reflection, not a precise measure of teaching quality.','对自己 217 节课转录文本的 AI 辅助分析，促使我反思是否过早回答了自己的问题。我开始提前设计关键问题，并留出更长的解释时间。这项分析是反思线索，并非教学质量的精确测量。')}

def render(i):
 def t(k):return D[k][i]
 def p(s):return '<p>'+e(s)+'</p>'
 home='index.html' if i==0 else 'index.zh.html'
 other='index.zh.html' if i==0 else 'index.html'
 nav=''.join(f'<a href="#{id}">{label}</a>' for id,label in zip(['works','resume','inquiry','contact'],t('nav')))
 out=f'''<!doctype html><html lang="{'en' if i==0 else 'zh-CN'}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{t('name')} | {t('role')}</title><meta name="description" content="{e(t('intro'),quote=True)}"><meta name="theme-color" content="#151617"><link rel="icon" href="favicon.svg"><link rel="stylesheet" href="portfolio.css"><link rel="alternate" hreflang="en" href="index.html"><link rel="alternate" hreflang="zh-CN" href="index.zh.html"></head><body><a class="skip" href="#main">{'Skip to content' if i==0 else '跳至正文'}</a><header><a class="brand" href="{home}">HL<span>{t('name')}</span></a><nav aria-label="{'Main navigation' if i==0 else '主导航'}">{nav}</nav><div class="languages" aria-label="Language"><a href="index.html" lang="en" {'aria-current="page"' if i==0 else ''}>EN</a><a href="index.zh.html" lang="zh-CN" {'aria-current="page"' if i==1 else ''}>中文</a></div></header><main id="main"><section class="hero" id="about"><p class="eyebrow">{t('role')}</p><h1>{t('headline')}</h1><p class="lead">{t('intro')}</p><a class="button" href="#works">{'Explore selected work' if i==0 else '浏览精选作品'} <span>↗</span></a><div class="hero-note">SHANGHAI · {'TEACHING / DESIGN / REFLECTION' if i==0 else '教学 / 设计 / 反思'}</div></section><div class="metrics">'''
 out+=''.join(f'<div><strong>{a}</strong><span>{b}</span></div>' for a,b in t('metrics'))+'</div>'
 out+=f'<section id="works"><p class="eyebrow">01 / PORTFOLIO</p><h2>{t("nav")[0]}</h2>'+p(t('work_intro'))+'<div class="cards">'
 for c in D['cases']:
  out+=f'<a class="card" href="#{c["id"]}"><img src="{c["img"]}" alt="{e(c["title"][i])}" loading="lazy"><div><p class="tag">{c["tag"][i]}</p><h3>{c["title"][i]}</h3>{p(c["summary"][i])}<span class="read">{"Read case study" if i==0 else "阅读案例"} ↗</span></div></a>'
 out+='</div></section>'
 for c in D['cases']:
  out+=f'<section class="case" id="{c["id"]}"><p class="eyebrow">{c["tag"][i]}</p><h2>{c["title"][i]}</h2><div class="case-grid">'
  for a,b,en,zh in c['blocks']:out+=f'<div><h3>{a if i==0 else b}</h3>{p(en if i==0 else zh)}</div>'
  out+='</div>'
  if c.get('video'):out+=f'<figure><video controls preload="none" poster="simulations.jpg" aria-label="{"Physics simulation demonstration (original Chinese recording)" if i==0 else "物理交互模拟演示视频"}"><source src="{c["video"]}" type="video/mp4"></video><figcaption>{"Original demonstration video; interface labels are in Chinese. The English case study above explains the design and evidence limits." if i==0 else "原有演示视频；上文说明设计过程及证据边界。"}</figcaption></figure>'
  if c.get('extra'):out+=f'<details><summary>{"View prototype interface (Chinese)" if i==0 else "查看原型界面"}</summary><img class="evidence" src="{c["extra"]}" alt="{"Prototype screen showing independent work with AI assistance locked" if i==0 else "独立作答阶段锁定 AI 辅助的原型截图"}" loading="lazy"></details>'
  if c['id']=='teacher-tools':out+=f'<details><summary>{"View bilingual resource samples" if i==0 else "查看双语教学资源样例"}</summary><div class="samples"><img src="assets/bilingual-en.jpg" alt="English teaching notes sample" loading="lazy"><img src="assets/bilingual-cn.jpg" alt="中文教学讲义样例" loading="lazy"></div></details>'
  out+='</section>'
 out+=f'<section><p class="eyebrow">IN DEVELOPMENT</p><h2>{"Further explorations" if i==0 else "进一步探索"}</h2><div class="explorations">'
 for title,status,body in t('explorations'):out+=f'<div><span class="tag">{status}</span><h3>{title}</h3>{p(body)}</div>'
 out+='</div></section>'
 out+=f'<section id="resources"><p class="eyebrow">RESOURCE ARCHIVE</p><h2>{"Teaching resource collection" if i==0 else "教学资源合集"}</h2>'+p('The original Chinese archive contains a concept and misconception explorer, resource samples and project documentation. The case studies above provide the English reading route.' if i==0 else '原有中文资料页保留知识点与易错点浏览、教学资源样例及项目过程材料；上方双语案例提供统一的阅读主线。')+'<ul class="resource-links">'
 for url,en,zh in [('knowledge-map.html','Concept and misconception explorer (Chinese)','知识点与易错点库'),('materials.html','Notes, workbooks and video demonstrations (Chinese)','讲义、习题册与演示视频'),('standard-course.html','Course workflow pilot archive (Chinese; paused)','标准课程试点记录（已暂停）'),('whitespace.html','Whitespace prototype archive (Chinese; paused)','留白原型记录（已暂停）'),('lanhan-resume.pdf','Earlier public CV (Chinese, October 2026)','早期公开简历（中文，2026 年 10 月）')]:
  out+=f'<li><a href="{url}">{en if i==0 else zh} ↗</a></li>'
 out+='</ul></section>'
 out+=f'<section id="resume"><p class="eyebrow">02 / BACKGROUND</p><h2>{t("nav")[1]}</h2><div class="timeline">'
 for date,title,body in t('experience'):out+=f'<article><span class="date">{date}</span><div><h3>{title}</h3>{p(body)}</div></article>'
 out+='</div></section>'
 out+=f'<section id="inquiry"><p class="eyebrow">03 / QUESTIONS TO PURSUE</p><h2>{"From classroom impressions to dependable evidence" if i==0 else "从课堂印象走向可靠证据"}</h2><div class="case-grid"><div><h3>{"Reflecting on my teaching" if i==0 else "反思自己的教学"}</h3>{p(t("reflection"))}</div><div><h3>{"A direction for graduate study" if i==0 else "研究生阶段的探索方向"}</h3>{p(t("inquiry"))}</div></div></section>'
 out+=f'<section id="contact"><p class="eyebrow">04 / CONTACT</p><h2>{"Let’s talk about learning." if i==0 else "交流如何让学习发生。"}</h2><a class="email" href="mailto:lanhansmart@gmail.com">lanhansmart@gmail.com ↗</a><p><a href="https://github.com/Bright-han0516">GitHub ↗</a></p><p class="muted">{"This portfolio presents selected work and reflections. Student records and internal organisational materials are not published here. Original screenshots may contain Chinese text; both language editions provide the same case narratives." if i==0 else "本作品集展示精选工作与反思，不公开学生记录及机构内部材料。原始截图可能包含中文；中英文版本提供对应的完整案例说明。"}</p></section></main><footer>© 2026 {t("name")} · {"Updated 10 November 2026" if i==0 else "更新于 2026 年 11 月 10 日"}</footer><script>document.querySelectorAll(".languages a").forEach(a=>a.addEventListener("click",()=>{{a.hash=location.hash;}}));</script></body></html>'
 return out
for i,f in enumerate(['index.html','index.zh.html']):(R/f).write_text(render(i))
