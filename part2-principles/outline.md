# Part 2 — 2D NMR 的历史、原理、种类与用途（2 人）

**目标时长约 6 min**（全组 12–15 min，Part 3 实例组 3 人约占 7–8 min）
**听众没有 NMR 基础**（CM5241 课程没讲 NMR），所以第 1 页要先补 1D NMR 的最低限度知识。
**引用要求**："authentic, traceable data" → 每张图或谱都要标注来源；下面的文献在定稿前要逐条核对 DOI。

---

## Slide 1 — 为什么 1D NMR 不够（衔接 Part 3 的场景）
- 1D ¹H NMR 能给出三类信息：化学位移 δ（化学环境）、积分（H 的数目）、耦合裂分 J（相邻的 H）
- 分子变大以后：信号会**重叠**，¹H 的谱宽只有约 10 ppm，所以无法判断"哪个 H 和哪个 H 相连"或"哪个 H 连在哪个 C 上"
- 核心思路：把信号铺展到**第二个频率维度**上，交叉峰（cross peak）直接表示两个核之间存在相关
- 图：同一化合物的 1D ¹H 谱（重叠严重）和 2D 谱的对比

## Slide 2 — 历史时间线
| 年份 | 事件 | 文献 |
|---|---|---|
| 1971 | Jean Jeener 在 Ampère Summer School（南斯拉夫 Basko Polje）提出二维实验的设想 | 会议报告，未正式发表 |
| 1976 | Aue, Bartholdi & Ernst 给出 2D NMR 的完整理论，COSY 由此诞生 | *J. Chem. Phys.* 1976, 64, 2229 |
| 1979 | NOESY 提出 | Jeener, Meier, Bachmann & Ernst, *J. Chem. Phys.* 1979, 71, 4546 |
| 1980 | HSQC 原型（Bodenhausen–Ruben） | *Chem. Phys. Lett.* 1980, 69, 185 |
| 1983 | HMQC（反式检测，用 ¹H 检测 ¹³C） | Bax, Griffey & Hawkins, *J. Magn. Reson.* 1983, 55, 301 |
| 1986 | HMBC | Bax & Summers, *J. Am. Chem. Soc.* 1986, 108, 2093 |
| 1991 | Richard Ernst 获 Nobel 化学奖（FT NMR 与 2D NMR） | nobelprize.org |
| 2002 | Kurt Wüthrich 获 Nobel 化学奖（用 NMR 测定生物大分子的三维结构） | nobelprize.org |

## Slide 3 — 通用原理：四段式脉冲序列
```
Preparation ── Evolution (t1) ── Mixing ── Detection (t2)
```
- **Preparation**：用脉冲激发自旋
- **Evolution t1**：让 t1 按步长递增，每个 t1 采一条 FID；自旋在 t1 期间按频率 ν₁ 演化，这个频率信息被"编码"进信号的幅度或相位
- **Mixing**：磁化在核之间转移，转移的途径决定了谱的类型：J 耦合（通过化学键）或偶极/NOE（通过空间）
- **Detection t2**：采集 FID，得到频率 ν₂
- 对 t1 和 t2 两个时间维度做 2D Fourier transform，得到 S(ν₁, ν₂)
- 读谱方法：**对角峰**就是 1D 谱本身；**交叉峰 (ν_A, ν_B)** 表示 A 和 B 之间发生了磁化转移

## Slide 4 — 种类总览（分类图，全段最重要的一页）
| 实验 | 相关核 | 转移途径 | 回答的问题 |
|---|---|---|---|
| **COSY** | ¹H–¹H | ²J/³J 耦合（通过 2–3 根键） | 哪些 H 是相邻的 → H–C–C–H 片段 |
| **TOCSY** | ¹H–¹H | 沿整个耦合网络接力 | 哪些 H 属于同一个自旋体系，例如一个糖环或一个氨基酸残基 |
| **HSQC / HMQC** | ¹H–¹³C | ¹J_CH（约 125–160 Hz） | 每个 H 直接连在哪个 C 上 |
| **HMBC** | ¹H–¹³C | ²J/³J_CH（约 2–15 Hz） | 跨 2–3 根键的连接，能越过季碳和杂原子把片段拼起来 |
| **NOESY / ROESY** | ¹H–¹H | 偶极弛豫（NOE ∝ r⁻⁶，约 < 5 Å） | 空间上相近的 H → 相对构型、构象 |

- 大类划分：**through-bond**（COSY/TOCSY/HSQC/HMBC）→ 平面结构（constitution）；**through-space**（NOESY/ROESY）→ 立体结构（与 Part 3 的两个例子一一对应）

## Slide 5 — HSQC vs HMQC（为什么两个都讲）
- 两者给出的信息相同：¹J_CH 一键相关
- HMQC：多量子相干，序列短，对脉冲误差不敏感；但 F1 维会带有 ¹H–¹H 耦合，峰形较宽
- HSQC：单量子相干，F1 分辨率更高，可以做 multiplicity-edited 版本（CH/CH₃ 与 CH₂ 的峰相位相反）→ 现在通常首选 HSQC
- 两者都用 ¹H 检测 ¹³C（inverse detection），灵敏度远高于直接检测 ¹³C

## Slide 6 — NOESY / ROESY 补充
- NOE 强度 ∝ r⁻⁶，所以只有距离小于约 5 Å 的 H 对才能看到交叉峰
- 中等分子量的分子（约 1000–2000 Da，取决于场强和黏度）NOE 可能接近 0 → 改用 ROESY
- 用途：顺式/反式、环上取代基的 axial/equatorial、相对构型

## Slide 7 — 解析流程（交给 Part 3）
```
MS → 分子式 & 不饱和度
1D ¹H / ¹³C (+DEPT) → 官能团、C 和 H 的类型
HSQC → C–H 一一配对
COSY (+TOCSY) → H–H 自旋体系片段
HMBC → 跨季碳和杂原子拼接片段 → 平面结构
NOESY/ROESY → 相对构型 → 立体结构
```
- 这一页对应课程强调的分析流程（Lecture 1 slide 29–31：sample → detection/identification → data analysis → report）
- 结尾一句话过渡："下面看两个只有 2D NMR 才能解决的真实例子"

---

## 分工与时间
<!-- TODO(human): 决定两位成员如何分配 Slide 1–7，以及每页的时间（合计约 6 min） -->
待定,我需要与他讨论

## 参考书（图可以引用这两本，都可追溯）
- T. D. W. Claridge, *High-Resolution NMR Techniques in Organic Chemistry*, 3rd ed., Elsevier, 2016
- R. M. Silverstein, F. X. Webster, D. J. Kiemle, *Spectrometric Identification of Organic Compounds*, 8th ed., Wiley
- 谱图可以从 SDBS（AIST）、BMRB 或 nmrshiftdb2 获取，图注里标明出处
