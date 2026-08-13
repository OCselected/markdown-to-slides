## Slide 1 · 开源许可：软件自由和知识财产法
- 「开源之道」·适兕 2022-04-26     51CTO 书友会直播
- 「开源之道」· 致力于开源相关思想、知识和价值的探究！

---

## Slide 2 · 议程
- 关于我
- 为什么要读这本书？
- 本书的作者和序言作者介绍
- 内容特色及讲解
- 互动交流
---

## Slide 3 · 关于我
- 「发现开源三部曲」作者
- 「开源之道」主创
- 开源布道师
- 参与和服务多家开源组织
---

## Slide 4 · 声明：我不是律师
- 本次分享内容，不可作为任何法律依据！
- 有关任何商业模式、诉讼等法律问题，请咨询您的律师！

---

## Slide 5 · 为什么要读这本书？
- 十四五规划中“完善开源知识产权和法律体系，” 指的是什么？
- 作者是谁？写序言的又是谁？
- 什么软件自由？和车厘子自由有啥区别？
- 什么是知识财产？软件怎么就成了知识财产？
- 法律背景下，何以成为开源？原则是什么？
- 为何会有开源许可？
- 开源许可该如何分类？
- 兼容性如何？
- 逃避诉讼是不是一定就是占了便宜？开发者应该持一个什么样的价值观？
---

## Slide 6 · 对于个人来讲，之所以阅读本书
- 正在创作《开源之史》
- 知识财产、软件、开源许可的困惑
- 梳理脉络
---

## Slide 7 · 本书的推荐出处
- 振华-开源之道 的豆瓣书单
- 理解开源许可
- 对已有的中文原创解读作品并不满意～
- 王东芳翻译的 GPL 合规值得推荐
- 木兰许可，只有文本，没有解读
---

## Slide 8 · 作者 Lawrence rosen 其人
- 律师，计算机专家
- Rosenlaw & Einschlag, 律师事务所合伙人
- 在各类开源基金会担任过重要职务
- — OSI 总法律顾问兼秘书
- — Apache 软件基金会 董事 2011～2012
- —  参与过 python基金会和Linux基金会前身FSG
- 撰写许可作品：Academic Free License 和Open Software License
---

## Slide 9 · 推荐序言作者
- 劳伦斯·莱斯格(Lawrence Lessig)
- 斯坦福大学法学院教授
- 几乎参与了所有重大论争：美国在线一时代华纳合并案、Napster音乐版权大虞、微软反垄断案、俄罗斯黑客事件、DVD破解案
- 竞选过总统

---

## Slide 10 · ——摘抄自 foreword by Lawrence Lessig

This book builds a framework within which the family of free and open source licenses can be understood. And in a rare talent for a lawyer, rosen succeeds in making these points about the law meaningful and understandable to anyone at all.

- ——摘抄自 foreword by Lawrence Lessig

---

## Slide 11 · 标题解析之前提：software freedom
- 积极自由
- 消极自由
- 积极共有
- 消极共有

---

## Slide 12 · 前言
- 本书不是写给律师的
- 献给开源共同体的亲力亲为者，解惑
- 写给客户
- 为开源的许可正名

---

## Slide 13 · 自由和开源
- Freedom 一词的解释，自由软件的四条准则
- 欲解软件许可，先解自由之意。
- Software freedom is the goal; open source is the means to that goal.
- 开源定义十条
---

## Slide 14 · 开源定义OSD的历史
- Bruce Perens 1997 撰写《 Debian 自由软件向导》
- 1999 修改以匹配开源
- 2002增加到十条
- 理解协议的关键指引或原则

---

## Slide 15 · ——- 作者解读 OSD
- 1.Licensees are free to use open source softwarefor any purpose whatsoever.
- ——- 作者解读 OSD

---

## Slide 16 · ——- 作者解读 OSD

2.Licensees are free to make copies of open sourcesoftware and to distribute them without paymentof royalties to a licensor.

- ——- 作者解读 OSD

---

## Slide 17 · ——- 作者解读 OSD

3.Licensees are free to create derivative worksof open source software and to distribute them withoutpayment of royalties to a licensor.

- ——- 作者解读 OSD

---

## Slide 18 · ——- 作者解读 OSD
- 4.Licensees are free to access and use the sourcecode of open source software.
- ——- 作者解读 OSD

---

## Slide 19 · ——- 作者解读 OSD
- 5.Licensees are free to combineopen source and other software.
- ——- 作者解读 OSD

---

## Slide 20 · 知识财产权
- 软件是财产？怎么识别？
- 何为知识财产？软件之前的左脑与右脑差异
- 软件的特殊性：两个左脑：we create both copyrightable expressions and patentable ideas
- 打工人没有著作权，而是归雇佣其公司所有。
- 集体（collective）和衍生作品

---

## Slide 21 · 知识财产权（续）
- Joint Works：Open source prides itself on being a cooperative development

process. Communities of engineers work together over the Internet to write software. In this way, they may create collective works. But they may also, without realizing the difference, create an entirely different kind of work: The result of collaborative development may become a joint work rather than a collective work.

Each contribution to a collective work is owned by its author, and that author has the exclusive right to decide how that contribution is to be licensed. A contribution to a joint work is owned by all of its authors jointly.

---

## Slide 22 · 知识财产权（续二）
- 著作权和专利的有效期（知识财产特有）
- 进入公有领域（Public domain）就是全人类可免费/自由获得基于任何目的使用
- 莎士比亚、莫扎特、牛顿、论语……
- 商标：和许可无关，不兼容！和 开源原则#3 衍生作品有冲突
- 题外话：SQLite 项目，Open-Source, not Open-Contribution

---

## Slide 23 · 知识财产法（续三）
- 无法保护到的：
- 著作权只能保护具体的表达，无法做到保护想法/观念
- 申请专利是一件昂贵、费时的操作

---

## Slide 24 · 软件的分发（利益攸关）

There may be no time, place, or manner limitations on distribution in an open source license—but this does not mean that there may be no conditions on distribution at all.

It is not always easy to distinguish between a contributor and a distributor of open source software, because people aggregate software into larger systems at each step of the development and distribution process. A distributor becomes a contributor to the next higher level of the food chain, just as fish in the ocean become food for larger fish.

关于Contributor Agreement 签署：There is one important caveat: Even a perpetual license can be revoked.

---

## Slide 25 · 许可的归类

License 释义（法律与文学）不是 1：驾照/营业执照；而是 2: In this book, the term License is used to describe the legal way a copyright and patent owner grants permission to others to use his intellectual property.

- 开源许可、专有许可和商业许可的区别～

The main difference between a bare license and a contract is in the way the relationship between licensor and licensee is formed./

- 学术、互惠、标准、内容 四大类型～

---

## Slide 26 · ——- 后记

Paradigms evolve over time. The software world is not what it was in 1989 when the GPL and BSD licenses were first indeed, …… that is the very foundational concept of the open source paradigm, which requires that people be free to learn from their predecessors and to create “derivative works.

- ——- 后记

---
