# CM5241 Group Project — 2D NMR 结构解析

NUS CM5241 Modern Analytical Techniques 小组项目，Topic 9：**Structural Elucidation of Unknown Organic Compounds Using 2D NMR Spectroscopy**。

## 分工

全组 5 人，展示 12–15 分钟，分成两部分：

| 部分 | 人数 | 内容 |
|---|---|---|
| Part 2 原理 | 2 | 2D NMR 的历史、原理、实验种类和用途 |
| Part 3 实例 | 3 | 找只有用 2D NMR 才能解决的真实例子：COSY / HSQC / HMQC 解平面结构，NOESY 解空间结构 |

## 关键日期（Week 12）

- **周二 23:59**：在 Canvas > Assignments 交 .pptx，每组 1 份
- **周三 14:00–18:00**：在 LT28 展示
- 选视频形式的话，周五 23:59 前上传到 Panopto，并嵌入 Canvas
- Week 13 周五 23:59 前：在 TEAMMATES 做自评和互评

完整要求和出处见 [requirements.md](requirements.md)。两条最容易出错：数据必须真实、可追溯，也就是每张图、每个数字都要标来源；用了 AI 要在最后声明。

## 仓库内容

| 位置 | 内容 |
|---|---|
| [requirements.md](requirements.md) | 课程对小组项目的要求（摘自 Lecture 1 slides） |
| [part2-principles/outline.md](part2-principles/outline.md) | Part 2 的逐页大纲（Slide 1–7） |
| [refered-doc/index.md](refered-doc/index.md) | **文献目录**：35 条已核实的文献，标了每条适合用在哪一页 |
| [refered-doc/paper/](refered-doc/paper/) | 开放获取的论文 PDF，文件名和目录里的 id 一致 |
| [refered-doc/references.bib](refered-doc/references.bib) | BibTeX，可以导入 Zotero 或 EndNote |

## 加一条文献

`index.md` 和 `references.bib` 都是自动生成的，**不要直接改**。加文献的步骤：

1. 在 [refered-doc/references.json](refered-doc/references.json) 里加一条，照着已有条目的格式写。DOI 要先在 [Crossref](https://search.crossref.org/) 上核对；还没核对的，`verified_via` 填 `"UNVERIFIED"`。
2. 运行下面的命令。它会先检查格式，再重新生成目录和 BibTeX：

   ```bash
   python3 refered-doc/script/build_index.py
   ```

3. 看到 `OK: N refs` 后再 commit。

目录里标 ⚠️ 的文献还没核实，不要放到 slide 上。

## 讨论

有问题或想法，请到 [Discussions](https://github.com/dzylol/CM5241-NMR-group-project/discussions) 发帖。
