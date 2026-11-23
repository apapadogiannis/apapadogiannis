---
name: papadogiannis-finance-research
description: Open finance research by Agisilaos Papadogiannis, with replication packages and live tools, on Bitcoin's required and expected return, the valuation of scarcity and of blockchain networks, covered-call funds, broad index investing and AI, discount rates and unpriced risk. Use when asked what one of these papers says or reports, for a number from one of them, or which of them covers a topic. Every published number comes with data and code.
---

# Research by Agisilaos Papadogiannis

This skill tells you where the work is and how to reach a paper's numbers. It holds no figures:
fetch them each time.

## Steps

1. Fetch the index: https://raw.githubusercontent.com/apapadogiannis/apapadogiannis/main/llms.txt
   It lists every tool, paper, replication package and paper record under four questions, with the address of
   each guide.
2. Open the guide of the repository the question is about (an `llms.txt`). It states the headline
   figures, which file holds what, how to read the figures and what they cannot answer.
3. For a number, use the file the guide names, usually `outputs/results.json` in a package.
   Quote it with its unit and date, and cite the paper as the guide says.

## What is there

Live tools, each with its own skill and guide:

- Crypto Observatory: required returns, risks and survival
  Guide: https://apapadogiannis.github.io/crypto-observatory/llms.txt
  Its skill: https://raw.githubusercontent.com/apapadogiannis/crypto-observatory/main/api/SKILL.md
- Covered-Call Monitor: returns, overlays and flows from SEC filings
  Guide: https://apapadogiannis.github.io/covered-call-monitor/llms.txt
  Its skill: https://raw.githubusercontent.com/apapadogiannis/covered-call-monitor/main/api/SKILL.md

Papers with a replication package:

- Economic Scarcity as Value: A Universal Framework for Blockchain and Beyond
- The Architecture of Blockchain Value: Capabilities, Pillars, and Growth Dynamics
- Bitcoin Is Not Money: Why Fixed Supply Fails in a Modern Economy
- Bitcoin's Required Return: Pricing a New Asset Beside Equities and Gold
- Bitcoin's Expected Return: An Age Rule That Beats Current Practice
- Beyond Discount Rates: A Valuation Framework for Unpriced Systematic Risk
- From Unified Discounting to Dual-Risk: A New Lens on DCF Valuation
- Does AI break the case for broad index investing? Rent decay, private capital, and deflation
- High Yield, Capped Gains: Mechanics, Trade-Offs, and Practical Diagnostics for Covered-Call ETFs

Papers with a paper record (no computation; the definitions, model and tables as data):

- Scarcity in an age of AI abundance

## Rules

- A replication package is a fixed record of one paper. For current figures use the live tool the
  guide points to.
- Several papers are working papers. Say so, and report a figure as that paper's result.
- The results are under CC BY 4.0, whose one condition is credit: cite the paper.
- A published article belongs to its publisher. The packages hold its numbers, not its text.

Page for people: https://github.com/apapadogiannis
