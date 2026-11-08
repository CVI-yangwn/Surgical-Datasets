<div align="center">

# 🩺 Surgical-Datasets

**手术视频与内镜公开数据集整理 · 附中文论文精读**

[![Papers](https://img.shields.io/badge/精读论文-71-4f5bd5)](https://cvi-yangwn.github.io/Surgical-Datasets/)
[![Datasets](https://img.shields.io/badge/数据集-71-8b5cf6)](#-数据集总览)
[![Reading](https://img.shields.io/badge/在线阅读-GitHub%20Pages-b84fa3)](https://cvi-yangwn.github.io/Surgical-Datasets/)

[📚 在线阅读全部精读](https://cvi-yangwn.github.io/Surgical-Datasets/) · [📊 数据集总览](#-数据集总览) · [🔍 精读是怎么做的](#-精读是怎么做的)

</div>

---

## 📚 论文精读

每篇精读都包含：背景与动机、核心观点速览、数据与实验、深入分析，以及**论文没有说明或前后对不上的地方**。点开分组查看。

<details open>
<summary><b>👁️ 眼科 Ophthalmic</b>（6 篇）</summary>

| 数据集 | 一句话 | 阅读 |
| :-- | :-- | :-- |
| **Cataract-1K** | 一个来自单一诊所的白内障手术视频数据集:1000 个视频,三类标注各自只覆盖其中一小部分 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/cataract-1k/) · [📝 笔记](docs/papers/cataract-1k/note.md) |
| **OphNet** | 一个由 YouTube 眼科手术视频搭起来的三级标注基准，规模是真的，几个数字却对不上 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/ophnet/) · [📝 笔记](docs/papers/ophnet/note.md) |
| **CaDIS** | 给白内障手术视频补上整场景像素级标注:4670 帧、36 类、三种类别粒度 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/cadis/) · [📝 笔记](docs/papers/cadis/note.md) |
| **Cataract-LMM** | 两家医院 3,000 个白内障手术视频，四层标注，第一次能在白内障数据上做站点留出评测 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/cataract-lmm/) · [📝 笔记](docs/papers/cataract-lmm/note.md) |
| **Cataract-101** | 一家医院、四名医生、101 台白内障手术的公开阶段标注视频 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/cataract-101/) · [📝 笔记](docs/papers/cataract-101/note.md) |
| **CATARACTS** | 白内障手术视频的器械使用标注挑战赛：50 个视频、21 种器械、14 支队伍 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/cataracts/) · [📝 笔记](docs/papers/cataracts/note.md) |

</details>

<details open>
<summary><b>🔬 内镜 Endoscopic</b>（8 篇）</summary>

| 数据集 | 一句话 | 阅读 |
| :-- | :-- | :-- |
| **Colon-Bench** | 用大模型漏斗加医生把关做出的 14 类结肠镜病灶视频基准 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/colon-bench/) · [📝 笔记](docs/papers/colon-bench/note.md) |
| **REAL-Colon-VQA（SurgViVQA）** | 结肠镜视频问答:从单帧换成 8 帧短片段,能否答对"内镜在前进还是后退 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/tg-surgvqa/) · [📝 笔记](docs/papers/tg-surgvqa/note.md) |
| **REAL-Colon** | 60 段全程未剪辑结肠镜视频与逐帧息肉框的公开数据集 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/real-colon/) · [📝 笔记](docs/papers/real-colon/note.md) |
| **EndoBench** | 用 6,832 道选择题量一量大模型离内镜医师有多远 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/endobench/) · [📝 笔记](docs/papers/endobench/note.md) |
| **Kvasir-SEG** | 给 1000 张结肠镜息肉图补上像素级掩码：Kvasir-SEG 数据集说明 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/kvasir-seg/) · [📝 笔记](docs/papers/kvasir-seg/note.md) |
| **PolypGen** | 六家医院的结肠镜息肉数据：PolypGen 能测出多少跨中心泛化差距 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/polypgen/) · [📝 笔记](docs/papers/polypgen/note.md) |
| **PitVis** | 首个公开的内镜垂体手术步骤与器械识别数据集及挑战赛 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/pitvis/) · [📝 笔记](docs/papers/pitvis/note.md) |
| **EndoSLAM** | 给胶囊内镜定位一个能打分的考场：离体猪器官上的位姿与三维真值数据集 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/endoslam/) · [📝 笔记](docs/papers/endoslam/note.md) |

</details>

<details open>
<summary><b>🩻 腹腔镜 Laparoscopic</b>（16 篇）</summary>

| 数据集 | 一句话 | 阅读 |
| :-- | :-- | :-- |
| **SLAM** | SLAM:34 台腹腔镜手术切出 4097 个短片段,标注七类基础动作 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/slam/) · [📝 笔记](docs/papers/slam/note.md) |
| **Cholec80（EndoNet）** | EndoNet 与 Cholec80：只看画面识别胆囊切除术的阶段和器械 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/cholec80/) · [📝 笔记](docs/papers/cholec80/note.md) |
| **CholecT50** | CholecT50 与 Rendezvous：让模型说出“哪件器械、在做什么、作用在哪” | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/cholect50/) · [📝 笔记](docs/papers/cholect50/note.md) |
| **CholecSeg8k** | 给胆囊切除术视频补一层像素级标注：CholecSeg8k 数据集说明 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/cholecseg8k/) · [📝 笔记](docs/papers/cholecseg8k/note.md) |
| **HeiChole** | HeiChole：三个中心的腹腔镜胆囊切除视频，检验手术工作流与技能识别到底解决了多少 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/heichole/) · [📝 笔记](docs/papers/heichole/note.md) |
| **AutoLaparo** | 在 21 台子宫切除术上叠了三层标注，任务设计有新意，多任务的价值却还没被验证 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/autolaparo/) · [📝 笔记](docs/papers/autolaparo/note.md) |
| **Endoscapes** | 一个面向胆囊切除术关键安全视野的分层标注数据集:201 个视频,CVS 标签多、框少、掩码更少 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/endoscapes/) · [📝 笔记](docs/papers/endoscapes/note.md) |
| **CholecTrack20** | 同一个器械框标三套身份：手术器械多视角跟踪数据集 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/cholectrack20/) · [📝 笔记](docs/papers/cholectrack20/note.md) |
| **CholecInstanceSeg** | 在 85 段胆囊切除术视频上补一层七类器械实例分割标注 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/cholecinstanceseg/) · [📝 笔记](docs/papers/cholecinstanceseg/note.md) |
| **ROBUST-MIS** | ROBUST-MIS 2019：在真实结直肠手术画面上，比较器械分割算法的最差情况与跨术式泛化 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/robust-mis/) · [📝 笔记](docs/papers/robust-mis/note.md) |
| **DSAD** | 32 台机器人直肠手术中 11 类腹部解剖结构的像素级分割：DSAD 数据集说明 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/dsad/) · [📝 笔记](docs/papers/dsad/note.md) |
| **D4D** | 形变腹腔软组织的 4D 重建数据集：内镜视频配上形变前后的结构光几何 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/d4d/) · [📝 笔记](docs/papers/d4d/note.md) |
| **MultiBypass140** | 两家医院、140 例胃旁路手术：换一家医院，手术流程识别模型还剩多少 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/multibypass140/) · [📝 笔记](docs/papers/multibypass140/note.md) |
| **GynSurg** | 一份把动作、副作用、器械和解剖标签放在一起的妇科腹腔镜数据集 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/gynsurg/) · [📝 笔记](docs/papers/gynsurg/note.md) |
| **ATLAS-120k** | ATLAS-120k：14 种术式的整场景手术解剖分割数据集与上下文分割模型 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/atlas-120k/) · [📝 笔记](docs/papers/atlas-120k/note.md) |
| **PhaKIR** | 同一批完整胆囊切除手术上同时标阶段、器械实例掩码和关键点:8 个视频、三家医院 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/phakir/) · [📝 笔记](docs/papers/phakir/note.md) |

</details>

<details open>
<summary><b>🤖 机器人手术 Robotic</b>（11 篇）</summary>

| 数据集 | 一句话 | 阅读 |
| :-- | :-- | :-- |
| **JIGSAWS** | 达芬奇机器人台架任务的运动学、立体视频与手势、技能标注：JIGSAWS 数据集说明 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/jigsaws/) · [📝 笔记](docs/papers/jigsaws/note.md) |
| **SurgPose** | 用紫外荧光漆给 da Vinci 器械关节自动打点的姿态估计数据集 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/surgpose/) · [📝 笔记](docs/papers/surgpose/note.md) |
| **VL-SurgPT** | 给手术跟踪点打上"被烟雾挡住""被器械挡住"的标签:在体点跟踪数据集与文本引导基线 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/vl-surgpt/) · [📝 笔记](docs/papers/vl-surgpt/note.md) |
| **EndoVis 2017** | 给机器人手术器械分割建一个可信的考场：EndoVis 2017 挑战赛总结 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/endovis2017/) · [📝 笔记](docs/papers/endovis2017/note.md) |
| **EndoVis 2018** | 从只分割器械到分割整个手术画面:EndoVis 2018 猪肾手术场景分割挑战 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/endovis2018/) · [📝 笔记](docs/papers/endovis2018/note.md) |
| **SCARED** | 用结构光给猪尸体内镜视频配上深度真值：SCARED 挑战赛报告 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/scared/) · [📝 笔记](docs/papers/scared/note.md) |
| **PSI-AVA** | 在同一批前列腺切除手术视频上同时标注阶段、步骤、器械和原子动作,并给出融合检测特征的基线 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/psi-ava/) · [📝 笔记](docs/papers/psi-ava/note.md) |
| **SAR-RARP50** | 前列腺根治术缝合视频上的动作识别与器械分割挑战赛：SAR-RARP50 数据集与 12 支队伍的结果 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/sar-rarp50/) · [📝 笔记](docs/papers/sar-rarp50/note.md) |
| **GraSP** | 在 13 台机器人前列腺根治术上同时标注阶段、步骤、器械实例分割和原子动作，并用统一基线检验各层能否互相帮助 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/grasp/) · [📝 笔记](docs/papers/grasp/note.md) |
| **SurgToolLoc / SurgVU** | 只给“装了哪些器械”的标签,能不能学会在手术画面里框出器械?四年挑战赛的答案 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/surgtoolloc/) · [📝 笔记](docs/papers/surgtoolloc/note.md) |
| **SurgVU** | 用达芬奇系统日志给上千小时猪模型培训录像打上噪声标签，再配一个人工框标注的验证集 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/surgvu/) · [📝 笔记](docs/papers/surgvu/note.md) |

</details>

<details open>
<summary><b>💬 多模态与问答 Multimodal</b>（13 篇）</summary>

| 数据集 | 一句话 | 阅读 |
| :-- | :-- | :-- |
| **Surgical-VQA** | 把手术标注改写成问答，用 Transformer 回答手术画面的问题 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/surgical-vqa/) · [📝 笔记](docs/papers/surgical-vqa/note.md) |
| **SurgMLLMBench** | 六个手术数据集合成一套问答加分割的训练集：一个模型能否通吃三个手术域 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/surgmllmbench/) · [📝 笔记](docs/papers/surgmllmbench/note.md) |
| **SurgVLM** | 把 23 个公开手术数据集改写成问答对话,微调 Qwen2.5-VL 并组建 6 项评测 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/surgvlm/) · [📝 笔记](docs/papers/surgvlm/note.md) |
| **SUREON** | 删掉“不看视频也能答对”的题之后，手术视觉推理还剩多难 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/sureon/) · [📝 笔记](docs/papers/sureon/note.md) |
| **SurgCoT** | 手术视频链式推理基准:把一道题拆成三级子问题,看大模型在哪一步掉链子 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/surgcot/) · [📝 笔记](docs/papers/surgcot/note.md) |
| **SurgVidLM（SVU-31K）** | 先看全片、再按时间码放大片段的手术视频大模型,附 3 万条 GPT-4 生成的视频问答 SVU-31K | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/surgvidlm/) · [📝 笔记](docs/papers/surgvidlm/note.md) |
| **MIS-VQA** | 把已有手术标注写成文字,让大模型照着出题的手术视觉问答数据集 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/mis-vqa/) · [📝 笔记](docs/papers/mis-vqa/note.md) |
| **SAP-Bench（已撤稿）** | 看一张术中画面,猜下一个手术动作:多模态大模型的胆囊切除下一动作预测基准 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/sap-bench/) · [📝 笔记](docs/papers/sap-bench/note.md) |
| **SurgLaVi** | 用大模型自动切分、过滤和改写手术讲解视频,做出 24 万对三层视频-字幕数据 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/surglavi/) · [📝 笔记](docs/papers/surglavi/note.md) |
| **SSG-VQA** | 用场景图自动出题的手术视觉问答数据集 SSG-VQA 及其参考模型 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/ssg-vqa/) · [📝 笔记](docs/papers/ssg-vqa/note.md) |
| **SurgBench** | 把 16 个手术视频来源统一切片,做成预训练集加 72 个标签的分类评测集 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/surgbench/) · [📝 笔记](docs/papers/surgbench/note.md) |
| **SurgAtlas** | 从 YouTube 收集 15,291 个开放与微创手术视频，自动生成四层文本标注，并首次给开放手术建立推理评测 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/surgatlas/) · [📝 笔记](docs/papers/surgatlas/note.md) |
| **LEMON（Surg-3M）** | 把 18K 个 YouTube 手术视频清洗成 938 小时的预训练库，再训练一个手术基础模型 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/lemon/) · [📝 笔记](docs/papers/lemon/note.md) |

</details>

<details open>
<summary><b>🏥 手术室 Operating room</b>（5 篇）</summary>

| 数据集 | 一句话 | 阅读 |
| :-- | :-- | :-- |
| **MVOR** | 真实介入手术室里的多视角彩色加深度人体姿态数据集 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/mvor/) · [📝 笔记](docs/papers/mvor/note.md) |
| **4D-OR** | 把手术室画成一张图：首个公开的 4D 手术室语义场景图数据集 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/4d-or/) · [📝 笔记](docs/papers/4d-or/note.md) |
| **MM-OR** | 不止看画面：首个支持多模态场景图生成的大规模手术室数据集 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/mm-or/) · [📝 笔记](docs/papers/mm-or/note.md) |
| **EgoSurgery-Phase** | 主刀头戴眼动相机拍下的开放手术阶段数据集，以及用注视引导掩码的视频预训练 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/egosurgery-phase/) · [📝 笔记](docs/papers/egosurgery-phase/note.md) |
| **EgoExOR** | 让手术室里的每个人戴上眼镜：自我视角加天花板视角的同步数据集与场景图基准 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/egoexor/) · [📝 笔记](docs/papers/egoexor/note.md) |

</details>

<details open>
<summary><b>🕒 尚未公开 Not yet</b>（12 篇）</summary>

| 数据集 | 一句话 | 阅读 |
| :-- | :-- | :-- |
| **MultiBypass-4C-T40** | MultiBypass-4C-T40：四中心胃旁路手术动作三元组数据集与跨中心基准 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/multibypass-4c-t40/) · [📝 笔记](docs/papers/multibypass-4c-t40/note.md) |
| **Colon-LQA（SurgLQA）** | 先问事件在哪、再在那里加密采样的结肠镜长视频问答方法，附一个拼接出的 Colon-LQA 评测集 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/long-horizon-vqa/) · [📝 笔记](docs/papers/long-horizon-vqa/note.md) |
| **SurgXBench** | 手术视觉语言模型可解释性基准:答对了,但看的是不是器械 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/surgxbench/) · [📝 笔记](docs/papers/surgxbench/note.md) |
| **SurgMotion-15M** | 在 3,658 小时多专科手术视频上做潜空间运动预测的视频基础模型 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/surgmotion/) · [📝 笔记](docs/papers/surgmotion/note.md) |
| **LD-RSVIS** | 支持无目标、单目标、多目标表达的大规模手术视频器械指代分割基准 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/ld-rsvis/) · [📝 笔记](docs/papers/ld-rsvis/note.md) |
| **SurgSkill-Bench** | 一份把手术视频、六维 OSATS 评分和专家评语放在一起的技能评估小基准 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/surgskill-bench/) · [📝 笔记](docs/papers/surgskill-bench/note.md) |
| **SVL（SurgVLP）** | 让模型看手术讲座学会手术：两路语音转写当监督的视觉-语言预训练 SurgVLP | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/svl/) · [📝 笔记](docs/papers/svl/note.md) |
| **Sankara-MSICS** | 第一个手法小切口白内障手术数据集,以及用手术阶段辅助器械分割的 ToolSeg | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/sankara-msics/) · [📝 笔记](docs/papers/sankara-msics/note.md) |
| **OphCLIP** | 用眼科手术视频教会模型看懂手术：数据集 OphVL 与检索增强预训练 OphCLIP | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/ophclip/) · [📝 笔记](docs/papers/ophclip/note.md) |
| **SurgPub-Video** | 用期刊论文附带的手术视频做视频问答数据:3,538 个视频、48,520 个问答、一个 3B 模型 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/surgpub-video/) · [📝 笔记](docs/papers/surgpub-video/note.md) |
| **NeuroABench** | 让多模态大模型认神经外科术中解剖:1079 道五选一题,最好的模型只有 40.87% | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/neuroabench/) · [📝 笔记](docs/papers/neuroabench/note.md) |
| **RoboSurg-VQA** | 让视觉语言模型替 EndoVis17/18 的 11,480 帧回答九个固定问题,再抽检 15% 帧把关 | [🌐 网页](https://cvi-yangwn.github.io/Surgical-Datasets/papers/robosurg-vqa/) · [📝 笔记](docs/papers/robosurg-vqa/note.md) |

</details>

> 页面上的分数是模型自评，不是外部评审；文中的数字都用脚本与论文原文逐一核对过。

---

## 📊 数据集总览

> 这里只收录能拿到数据的数据集（可直接下载，或按官方流程注册、申请后获取）。数据未公开的工作只出现在上面的论文精读里。年份是论文首版上传 arXiv 的年份；规模只填摘要里写明的数字，未写明的留空。

### 👁️ 眼科 Ophthalmic

| 数据集 | 年份 | 论文 | 数据 | 任务 | 规模 | 来源 | 精读 |
| :-- | :--: | :--: | :--: | :-- | :-- | :-- | :--: |
| Cataract-1K | 2023 | [arXiv](https://arxiv.org/abs/2312.06295) | [<img src="https://github.githubassets.com/favicons/favicon.svg" width="16">](https://github.com/Negin-Ghamsarian/Cataract-1K) | 阶段识别 / 分割 / 异常检测 | 1000 个视频 | 医院 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/cataract-1k/) |
| OphNet | 2024 | [arXiv](https://arxiv.org/abs/2406.07471) | [链接](https://forms.gle/GhJyQDPUrE74jLy87) | 阶段、器械、操作识别 | 2278 个视频 | YouTube | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/ophnet/) |
| CaDIS | 2019 | [arXiv](https://arxiv.org/abs/1906.11586) | [链接](https://cataracts-semantic-segmentation2020.grand-challenge.org/) | 白内障手术图像语义分割 |  |  | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/cadis/) |
| Cataract-LMM | 2025 | [arXiv](https://arxiv.org/abs/2510.16371) | [🤗](https://huggingface.co/datasets/mjahmadi/Cataract-LMM) | 阶段识别 / 实例分割 / 器械-组织交互跟踪 / 技能评估 | 3000 个视频 | 两家眼科医院 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/cataract-lmm/) |
| Cataract-101 | 2018 | [论文](https://doi.org/10.1145/3204949.3208137) | [链接](https://doi.org/10.5281/zenodo.1220951) | 白内障手术阶段识别（十阶段） | 101 个视频（14 小时） | 奥地利克拉根福医院 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/cataract-101/) |
| CATARACTS | 2019 | [论文](https://discovery.ucl.ac.uk/10068008/1/CATARACTS.pdf) | [链接](https://cataracts.grand-challenge.org) | 帧级器械使用识别（21 种器械） | 50 个视频 | 布雷斯特大学医院 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/cataracts/) |

### 🔬 内镜 Endoscopic

| 数据集 | 年份 | 论文 | 数据 | 任务 | 规模 | 来源 | 精读 |
| :-- | :--: | :--: | :--: | :-- | :-- | :-- | :--: |
| Colon-Bench | 2026 | [arXiv](https://arxiv.org/abs/2603.25645) | [🤗](https://huggingface.co/datasets/ajhamdi/colon-bench) | 结肠镜病灶检测 / 开放词汇分割 / 视频问答 | 528 个视频窗口（46 万帧，14 类病灶） | REAL-Colon 全程结肠镜录像 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/colon-bench/) |
| REAL-Colon-VQA（SurgViVQA） | 2025 | [arXiv](https://arxiv.org/abs/2511.03325) | [<img src="https://github.githubassets.com/favicons/favicon.svg" width="16">](https://github.com/madratak/SurgViVQA/tree/main/REAL-Colon-VQA_annotations) | 结肠镜短片段视频问答 | 5,200 条 8 帧片段问答 | REAL-Colon 6 段结肠镜录像 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/tg-surgvqa/) |
| REAL-Colon | 2024 | [arXiv](https://arxiv.org/abs/2403.02163) | [figshare](https://plus.figshare.com/articles/media/REAL-colon_dataset/22202866) | 结肠镜息肉逐帧检测 | 60 段全程视频（270 万帧） | 四国六中心临床研究录像 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/real-colon/) |
| EndoBench | 2025 | [arXiv](https://arxiv.org/abs/2505.23601) | [🤗](https://huggingface.co/datasets/Saint-lsy/EndoBench) | 多模态大模型视觉问答评测 |  |  | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/endobench/) |
| Kvasir-SEG | 2019 | [arXiv](https://arxiv.org/abs/1911.07069) | [链接](https://datasets.simula.no/kvasir-seg/) | 息肉分割 |  |  | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/kvasir-seg/) |
| PolypGen | 2021 | [arXiv](https://arxiv.org/abs/2106.04463) | [链接](https://doi.org/10.7303/syn26376615) | 息肉检测与分割（跨中心泛化） | 超过 300 名患者 | 六个中心 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/polypgen/) |
| PitVis | 2024 | [arXiv](https://arxiv.org/abs/2409.01184) | [链接](https://doi.org/10.5522/04/26531686) | 内镜垂体手术步骤 / 器械识别 | 25 个公开视频 + 8 个私有测试视频 | 英国国立神经病学与神经外科医院 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/pitvis/) |
| EndoSLAM | 2020 | [arXiv](https://arxiv.org/abs/2006.16670) | [<img src="https://github.githubassets.com/favicons/favicon.svg" width="16">](https://github.com/CapsuleEndoscope/EndoSLAM) | 内镜视觉里程计与深度估计 |  |  | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/endoslam/) |

### 🩻 腹腔镜 Laparoscopic

| 数据集 | 年份 | 论文 | 数据 | 任务 | 规模 | 来源 | 精读 |
| :-- | :--: | :--: | :--: | :-- | :-- | :-- | :--: |
| SLAM | 2025 | [论文](https://www.nature.com/articles/s41597-025-05093-7) | [figshare](https://figshare.com/articles/dataset/SLAM_-_Surgical_LAparoscopic_Motions/28104782/3) | 动作分类 | 4,097 个视频片段 | 瑞金医院卢湾分院 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/slam/) |
| Cholec80（EndoNet） | 2016 | [arXiv](https://arxiv.org/abs/1602.03012) | [链接](https://camma.unistra.fr/datasets/) | 阶段识别 / 器械识别 |  |  | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/cholec80/) |
| CholecT50 | 2021 | [arXiv](https://arxiv.org/abs/2109.03223) | [<img src="https://github.githubassets.com/favicons/favicon.svg" width="16">](https://github.com/CAMMA-public/cholect50) | 手术动作三元组识别 | 50 个视频 |  | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/cholect50/) |
| CholecSeg8k | 2020 | [arXiv](https://arxiv.org/abs/2012.12453) | [链接](https://www.kaggle.com/newslab/cholecseg8k) | 胆囊切除语义分割 | 8,080 帧（17 段视频） | Cholec80 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/cholecseg8k/) |
| HeiChole | 2021 | [arXiv](https://arxiv.org/abs/2109.14956) | [链接](https://www.synapse.org/#!Synapse:syn18824884) | 工作流与技能评估 | 33 个视频 | 三个中心 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/heichole/) |
| AutoLaparo | 2022 | [arXiv](https://arxiv.org/abs/2208.02049) | [<img src="https://github.githubassets.com/favicons/favicon.svg" width="16">](https://autolaparo.github.io) | 子宫切除多任务（工作流、运动预测、分割） |  |  | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/autolaparo/) |
| Endoscapes | 2023 | [arXiv](https://arxiv.org/abs/2312.12429) | [<img src="https://github.githubassets.com/favicons/favicon.svg" width="16">](https://github.com/CAMMA-public/Endoscapes) | 分割 / 检测 / 关键安全视野评估 | 201 个视频 |  | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/endoscapes/) |
| CholecTrack20 | 2023 | [arXiv](https://arxiv.org/abs/2312.07352) | [<img src="https://github.githubassets.com/favicons/favicon.svg" width="16">](https://github.com/camma-public/cholectrack20) | 多器械跟踪 | 20 个视频 |  | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/cholectrack20/) |
| CholecInstanceSeg | 2024 | [arXiv](https://arxiv.org/abs/2406.16039) | [链接](https://doi.org/10.7303/syn64891826.1) | 器械实例分割 | 41.9k 帧（85 台手术） | Cholec80 与 CholecT50 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/cholecinstanceseg/) |
| ROBUST-MIS | 2021 | [arXiv](https://arxiv.org/abs/2003.10299) | [链接](https://www.synapse.org/#!Synapse:syn18779624/wiki/592660) | 器械二值 / 多实例检测与分割 | 30 台手术（10,040 帧） | 海德堡大学医院 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/robust-mis/) |
| DSAD | 2023 | [论文](https://www.nature.com/articles/s41597-022-01719-2) | [figshare](https://doi.org/10.6084/m9.figshare.21702600) | 腹部解剖结构语义分割（11 类） | 13,195 张图像（32 台手术） | 德累斯顿大学医院机器人直肠手术 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/dsad/) |
| D4D | 2026 | [arXiv](https://arxiv.org/abs/2603.02985) | [链接](https://doi.org/10.25532/OPARA-1033) | 形变软组织 4D 重建 / 深度估计评测 | 98 段序列（30 万+ 帧） | 猪尸体开腹，达芬奇立体内镜 + 结构光 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/d4d/) |
| MultiBypass140 | 2024 | [arXiv](https://arxiv.org/abs/2312.11250) | [<img src="https://github.githubassets.com/favicons/favicon.svg" width="16">](https://github.com/CAMMA-public/MultiBypass140) | 胃旁路阶段与步骤识别（跨中心泛化） | 140 个视频 | 斯特拉斯堡与伯尔尼两家医院 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/multibypass140/) |
| GynSurg | 2025 | [arXiv](https://arxiv.org/abs/2506.11356) | [链接](https://ftp.itec.aau.at/datasets/GynSurge/) | 妇科动作识别 / 出血烟雾检测 / 语义分割 | 152 个动作视频 + 12,362 帧掩码 | 维也纳与多伦多两所医科大学 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/gynsurg/) |
| ATLAS-120k | 2026 | [arXiv](https://arxiv.org/abs/2606.22124) | [🤗](https://huggingface.co/datasets/TimJaspersTue/ATLAS-120k) | 整场景解剖结构视频分割（42 类） | 100 个视频（121,018 帧） | YouTube 公开视频，14 种术式 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/atlas-120k/) |
| PhaKIR | 2025 | [arXiv](https://arxiv.org/abs/2511.06549) | [链接](https://doi.org/10.5281/zenodo.15740619) | 阶段识别 / 器械关键点 / 器械实例分割 | 8 个视频（485,875 帧阶段标注） | 三家德国医院 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/phakir/) |

### 🤖 机器人手术 Robotic

| 数据集 | 年份 | 论文 | 数据 | 任务 | 规模 | 来源 | 精读 |
| :-- | :--: | :--: | :--: | :-- | :-- | :-- | :--: |
| JIGSAWS | 2014 | [论文](https://cirl.lcsr.jhu.edu/wp-content/uploads/dlm_uploads/2014/09/JIGSAWS.pdf) | [链接](https://cirl.lcsr.jhu.edu/research/hmm/datasets/jigsaws_release/) | 手势识别 / 技能评估 | 103 个试次（8 名医生） | 达芬奇台架任务 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/jigsaws/) |
| SurgPose | 2025 | [arXiv](https://arxiv.org/abs/2502.11534) | [链接](https://zenodo.org/records/15278516) | 器械关节关键点姿态估计与跟踪 | 约 12 万个器械实例（6 类） | 达芬奇 IS1200 + dVRK，离体组织 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/surgpose/) |
| VL-SurgPT | 2025 | [arXiv](https://arxiv.org/abs/2511.12026) | [🤗](https://huggingface.co/datasets/zhourulin88888/VL-SurgPT) | 组织点与器械点跟踪 + 点状态分类 | 908 个在体片段 | 深圳市人民医院达芬奇 Xi 胃肠手术 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/vl-surgpt/) |
| EndoVis 2017 | 2019 | [arXiv](https://arxiv.org/abs/1902.06426) | [链接](https://endovissub2017-roboticinstrumentsegmentation.grand-challenge.org) | 器械分割 |  | MICCAI 挑战赛 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/endovis2017/) |
| EndoVis 2018 | 2020 | [arXiv](https://arxiv.org/abs/2001.11190) | [链接](https://endovissub2018-roboticscenesegmentation.grand-challenge.org) | 手术场景分割 |  | MICCAI 挑战赛 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/endovis2018/) |
| SCARED | 2021 | [arXiv](https://arxiv.org/abs/2101.01133) | [链接](https://endovissub2019-scared.grand-challenge.org/) | 双目匹配与三维重建 |  | MICCAI 挑战赛 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/scared/) |
| PSI-AVA | 2022 | [arXiv](https://arxiv.org/abs/2212.04582) | [<img src="https://github.githubassets.com/favicons/favicon.svg" width="16">](https://github.com/BCV-Uniandes/TAPIR) | 阶段、步骤、器械与原子动作识别 |  | 前列腺根治术 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/psi-ava/) |
| SAR-RARP50 | 2023 | [arXiv](https://arxiv.org/abs/2401.00496) | [链接](https://rdr.ucl.ac.uk/projects/SARRARP50_Segmentation_of_surgical_instrumentation_and_Action_Recognition_on_Robot-Assisted_Radical_Prostatectomy_Challenge/191091) | 动作识别 / 器械分割 | 50 段缝合视频 | 前列腺根治术 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/sar-rarp50/) |
| GraSP | 2024 | [arXiv](https://arxiv.org/abs/2401.11174) | [<img src="https://github.githubassets.com/favicons/favicon.svg" width="16">](https://github.com/BCV-Uniandes/GraSP) | 整体场景理解（含分割） |  | 前列腺根治术 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/grasp/) |
| SurgToolLoc / SurgVU | 2023 | [arXiv](https://arxiv.org/abs/2305.07152) | [链接](https://console.cloud.google.com/storage/browser/isi-surgtoolloc-2022) | 器械定位 |  | MICCAI 挑战赛 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/surgtoolloc/) |
| SurgVU | 2025 | [arXiv](https://arxiv.org/abs/2501.09209) | [链接](https://storage.googleapis.com/isi-surgvu/surgvu24_videos_only.zip) | 器械识别与弱监督检测 / 步骤识别 / 视觉问答 | 840+ 小时（280 个片段） | 达芬奇培训录像（猪模型） | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/surgvu/) |

### 💬 多模态与问答 Multimodal

| 数据集 | 年份 | 论文 | 数据 | 任务 | 规模 | 来源 | 精读 |
| :-- | :--: | :--: | :--: | :-- | :-- | :-- | :--: |
| Surgical-VQA | 2022 | [arXiv](https://arxiv.org/abs/2206.11053) | [<img src="https://github.githubassets.com/favicons/favicon.svg" width="16">](https://github.com/lalithjets/Surgical_VQA) | 手术场景视觉问答 |  | EndoVis 2018 与 Cholec80 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/surgical-vqa/) |
| SurgMLLMBench | 2025 | [arXiv](https://arxiv.org/abs/2511.21339) | [🤗](https://huggingface.co/datasets/KIST-HARILAB/SurgMLLMBench) | 多模态大模型问答 / 器械分割 | 561,418 帧（112.8 小时） | 5 个公开数据集 + 新采集 MAVIS | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/surgmllmbench/) |
| SurgVLM | 2025 | [arXiv](https://arxiv.org/abs/2506.02555) | [🤗](https://huggingface.co/datasets/SurgSigma/SurgSigma-DB) | 手术视觉语言指令微调与多任务评测 | 181 万帧、779 万段对话（部分公开） | 23 个公开数据集改写 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/surgvlm/) |
| SUREON | 2026 | [arXiv](https://arxiv.org/abs/2603.06570) | [🤗](https://huggingface.co/datasets/aleperez24/sureon) | 手术视频推理问答 | 76,061 条训练问答 + 340 题基准 | YouTube 手术讲解视频 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/sureon/) |
| SurgCoT | 2026 | [arXiv](https://arxiv.org/abs/2604.20319) | [🤗](https://huggingface.co/datasets/wanggui/SurgCoT) | 链式时空推理问答 | 2,841 个视频（19,345 个主问题） | 公开平台、10 个开源数据集与临床档案 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/surgcot/) |
| SurgVidLM（SVU-31K） | 2025 | [arXiv](https://arxiv.org/abs/2506.17873) | [🤗](https://huggingface.co/datasets/gkw0010/SVU-31K) | 多粒度手术视频指令问答 | 1,882 个视频（约 3.1 万条问答） | YouTube 与 WebSurg 机器人手术讲解 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/surgvidlm/) |
| MIS-VQA | 2026 | [arXiv](https://arxiv.org/abs/2610.34210) | [🤗](https://huggingface.co/datasets/M-Hamdy/MIS-VQA) | 手术视觉问答 / 场景描述 / 复杂推理 | 84.9 万问答（3.3 万帧） | EndoVis18 与 CholecT50 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/mis-vqa/) |
| SAP-Bench（已撤稿） | 2025 | [arXiv](https://arxiv.org/abs/2506.07196v1) | [🤗](https://huggingface.co/datasets/SAPbench/SAPBench) | 下一手术动作预测（多模态大模型评测） | 1,152 帧（74 台手术） | CholecT50 与 HeiChole 重标 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/sap-bench/) |
| SurgLaVi | 2025 | [arXiv](https://arxiv.org/abs/2509.10555) | [🤗](https://huggingface.co/datasets/aleperez24/SurgLaVi) | 手术视频-文本预训练 | 24 万对片段-字幕（β 版 11.3 万对公开） | YouTube 讲解视频 + 机构档案 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/surglavi/) |
| SSG-VQA | 2024 | [arXiv](https://arxiv.org/abs/2312.10251) | [<img src="https://github.githubassets.com/favicons/favicon.svg" width="16">](https://github.com/CAMMA-public/SSG-VQA) | 基于场景图的手术视觉问答 | 96 万问答（2.5 万场景） | CholecT45 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/ssg-vqa/) |
| SurgBench | 2025 | [arXiv](https://arxiv.org/abs/2506.07603) | [🤗](https://huggingface.co/datasets/JianhuiWei/SurgBench_NIPS25) | 手术视频基础模型预训练与多任务评测 | 5300 万帧（22 种术式） | 16 个来源整合 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/surgbench/) |
| SurgAtlas | 2026 | [arXiv](https://arxiv.org/abs/2606.25905) | [🤗](https://huggingface.co/datasets/filbel/SurgAtlas) | 手术视频-语言预训练与推理问答 | 15,291 个视频（2,391 小时） | YouTube | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/surgatlas/) |
| LEMON（Surg-3M） | 2025 | [arXiv](https://arxiv.org/abs/2503.19740) | [<img src="https://github.githubassets.com/favicons/favicon.svg" width="16">](https://github.com/visurg-ai/LEMON) | 手术视频自监督预训练 / 术式分类 | 4K+ 视频（938 小时） | YouTube | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/lemon/) |

### 🏥 手术室 Operating room

| 数据集 | 年份 | 论文 | 数据 | 任务 | 规模 | 来源 | 精读 |
| :-- | :--: | :--: | :--: | :-- | :-- | :-- | :--: |
| MVOR | 2018 | [arXiv](https://arxiv.org/abs/1808.08180) | [<img src="https://github.githubassets.com/favicons/favicon.svg" width="16">](https://github.com/CAMMA-public/MVOR) | 手术室人员检测与 2D/3D 姿态估计 | 732 个多视角帧 | 斯特拉斯堡大学附属医院介入手术室 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/mvor/) |
| 4D-OR | 2022 | [arXiv](https://arxiv.org/abs/2203.11937) | [<img src="https://github.githubassets.com/favicons/favicon.svg" width="16">](https://github.com/egeozsoy/4D-OR) | 手术室语义场景图 / 3D 位姿 / 临床角色 | 10 台手术（6734 帧） | 模拟全膝关节置换 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/4d-or/) |
| MM-OR | 2025 | [arXiv](https://arxiv.org/abs/2503.02579) | [链接](https://forms.gle/kj47QXEcraQdGidg6) | 手术室多模态场景图 / 全景分割 / 动作预测 | 17 台完整录制（约 500GB） | 模拟机器人膝关节置换 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/mm-or/) |
| EgoSurgery-Phase | 2024 | [arXiv](https://arxiv.org/abs/2405.19644) | [<img src="https://github.githubassets.com/favicons/favicon.svg" width="16">](https://github.com/Fujiry0/EgoSurgery) | 开放手术阶段识别（头戴相机 + 注视） | 20 段视频（15 小时） | 庆应义塾大学医院 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/egosurgery-phase/) |
| EgoExOR | 2025 | [arXiv](https://arxiv.org/abs/2505.24287) | [<img src="https://github.githubassets.com/favicons/favicon.svg" width="16">](https://github.com/ardamamur/EgoExOR) | 手术室场景图生成（第一人称 + 外部视角） | 94 分钟（84,553 帧） | 模拟脊柱手术 | [✅](https://cvi-yangwn.github.io/Surgical-Datasets/papers/egoexor/) |

---

## 🔍 精读是怎么做的

精读由仓库内的 [DeepPaperNote](.claude/skills/deeppapernote) skill 生成（基于 [917Dhj/DeepPaperNote](https://github.com/917Dhj/DeepPaperNote) 修改），每篇走两轮：

1. **第 1 轮：原版精读**。取 PDF、按章节抽原文、逐张审图表，写出结构化笔记并通过引用与格式检查。
2. **第 2 轮：多轮追问与叙事修改**。先列出读者需要的知识点，再对着原文追问细节（答不上的写“论文未说明”），然后对每个核心结论找最强的另一种解释；最后按“背景 → 核心观点 → 实验 → 深入分析”重写，并核对每个数字。

两轮各自评分。第 1 轮在动笔修改之前记录，第 2 轮在改完之后记录，每轮都保存当时笔记和文稿的快照与哈希，见每篇的 `review/` 目录。

### 目录结构

```
docs/                          # GitHub Pages 站点
├── index.html                 # 首页：按类别分组的数据集与精读
└── papers/<数据集>/
    ├── index.html             # 图文解读网页
    ├── note.md                # Markdown 精读笔记
    ├── report.md              # 网页文稿
    ├── images/                # 论文图表裁剪
    └── review/                # 评分记录、各轮快照、多轮追问与数字核对
tools/
├── publish_paper.py           # 把一篇读完的论文发布到 docs/papers/<数据集>/
└── build_site.py              # 生成首页和本 README 的表格
.claude/skills/deeppapernote/  # 生成精读的 skill
```

### 自己读一篇

1. 在仓库根目录启动 Claude Code，说：

   ```
   读这篇论文并生成深度笔记：arXiv:xxxx.xxxxx，输出中文，保存到工作区，领域：手术数据集
   ```

   skill 的工作产物写在 `DeepPaperNote_output/`，这个目录不进版本库。

2. 在 `tools/build_site.py` 的 `CATALOG` 里补上这个数据集，然后发布并重建首页：

   ```
   python3 tools/publish_paper.py DeepPaperNote_output/手术数据集/<论文目录> --slug <数据集>
   python3 tools/build_site.py
   ```
