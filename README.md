# Jackknife - Simulated PoC (Tabletop Exercise Artifact)

**This repository contains no real exploit code.** Everything here is a
labeled, non-functional simulation built for a Trifident Advisory Services
tabletop exercise (TTX) run with Zebra Technologies in November 2026.

## 这是什么

这是一个名为 `jackknife_poc.py` 的 Python 脚本，其样式设计成类似概念验证漏洞利用程序，用于在练习中作为讨论素材。

它的目的是在引导式演示过程中以类似漏洞利用程序的形式呈现，仅此而已。

- 漏洞名称“Jackknife”和 ID `CVE-2026-XXXXX` 是

**虚构的**。它们不对应于任何真实的 CVE 编号。

- 脚本输出中引用的“库”是一个占位符名称，

并非实际的软件包。

- 此代码库中没有任何混淆处理。每一行都是

纯文本的、带有注释的 Python 代码，您可以在一分钟内从头到尾阅读完毕。

## 这不是什么

- 不是一个可用的漏洞利用程序。它没有实现、演示或启用

任何真实的攻击技术。

- 不具备网络功能。它不会打开任何套接字，不会发出任何请求，也不会

联系任何主机。

- 这不是通用安全工具。请勿将其改装成通用安全工具。

## 脚本实际功能

运行脚本后，会输出一段简短且清晰的描述（例如“步骤 1 - 模拟

侦察”等），说明真实的攻击链在每个阶段的假设操作，供演练参与者阅读和讨论。脚本不进行任何文件

I/O 操作（除了向标准输出打印信息之外），不调用子进程，不进行网络调用，不执行

动态代码，也不执行任何编码或隐藏的有效载荷。

每个步骤还会输出一行模拟的“工具对话”信息，

其格式模仿真实入侵工具的捕获输出，

以增强演练的真实性。

每行信息之后都会立即显示其英文翻译，

因此，
本仓库中的任何内容都不会以未翻译的形式呈现，

也不会让参与者凭空想象。此处使用中文文本仅为练习样式

并不代表、归因或暗示任何真实个人、组织或国家参与其中



python3 jackknife_poc.py --i-understand-this-is-fake

```

特意需要使用 `--i-understand-this-is-fake` 标志，

提醒运行此程序的用户这只是练习材料。


## Why it's public

This repo exists to support a live tabletop exercise where participants
may be asked to look at "found" artifacts, including something that
resembles a PoC. It is public, readable, and inert so that nothing about
it needs to be taken on faith: open the script and read it.

## License / use

Provided as-is for tabletop exercise purposes. Do not represent this as,
or repurpose this into, a real security tool.
