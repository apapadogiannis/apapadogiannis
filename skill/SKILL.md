---
name: papadogiannis-finance-research
description: Open finance research by Agisilaos Papadogiannis, with replication packages and live tools. Use for questions such as: what return should the holders of Bitcoin, Ether, BNB, Solana or Tron require, and did Bitcoin deliver it; how has a covered-call fund (QYLD, XYLD, RYLD, JEPI, JEPQ and others) done against its index fund, and what does it pay out; how much of a valuation gap is the discount rate and how much the forecast. Also for what one of his papers says or reports on Bitcoin's required and expected return, the valuation of scarcity and of blockchain networks, covered-call funds, broad index investing and AI, discount rates and unpriced risk; for a number from one of them; for the latest figure of a live tool; or for which of them covers a topic. 9 of the 21 papers come with data and code; the others are papers only.
---

# Research by Agisilaos Papadogiannis

This one skill covers the whole account: the live tools and every paper. It tells you where the work is
and how to reach a number. It holds no figures: fetch them each time.

## Steps

1. Fetch the index: https://raw.githubusercontent.com/apapadogiannis/apapadogiannis/main/llms.txt
   It lists every tool, paper, replication package and paper record under four questions, with the address of
   each guide.
2. Open the guide of the repository the question is about (an `llms.txt`). It states the headline
   figures, which file holds what, how to read the figures and what they cannot answer.
3. For a number, use the file the guide names, usually `outputs/results.json` in a package.
   Quote it with its unit and date, and cite the paper as the guide says.
4. For a paper that has no package, the index gives its venue and its SSRN or published address. Say what
   the paper is and where it is; do not state a number from it unless you have read the paper itself.

## What is there

Live tools. Read the guide first: it has the reading rules and says which data file to fetch.

- Covered-Call Monitor: returns, overlays and flows from SEC filings
  Use for: Covered-call funds: returns, payouts, written calls and flows
  Guide: https://apapadogiannis.github.io/covered-call-monitor/llms.txt
  Same guide in the repository: https://raw.githubusercontent.com/apapadogiannis/covered-call-monitor/main/api/llms.txt
- Crypto Observatory: required returns, risks and survival
  Use for: The required return of Bitcoin, Ether, BNB, Solana and Tron, what each is made of, what changed since last month, and Bitcoin's record
  Guide: https://apapadogiannis.github.io/crypto-observatory/llms.txt
  Same guide in the repository: https://raw.githubusercontent.com/apapadogiannis/crypto-observatory/main/api/llms.txt
- Dual-Risk DCF Calculator: the discount rate and the forecast, separated
  Use for: Splitting a valuation gap into the discount rate and the forecast, from your own numbers
  Guide: https://apapadogiannis.github.io/dual-risk-calculator/llms.txt
  Same guide in the repository: https://raw.githubusercontent.com/apapadogiannis/dual-risk-calculator/main/api/llms.txt

Papers with a replication package, each with its guide:

- Economic Scarcity as Value: A Universal Framework for Blockchain and Beyond
  Guide: https://raw.githubusercontent.com/apapadogiannis/economic-scarcity-as-value/main/llms.txt
- The Architecture of Blockchain Value: Capabilities, Pillars, and Growth Dynamics
  Guide: https://raw.githubusercontent.com/apapadogiannis/architecture-of-blockchain-value/main/llms.txt
- Bitcoin Is Not Money: Why Fixed Supply Fails in a Modern Economy
  Guide: https://raw.githubusercontent.com/apapadogiannis/bitcoin-is-not-money/main/llms.txt
- Bitcoin's Required Return: Market Risk, Concentration and Mortality
  Guide: https://raw.githubusercontent.com/apapadogiannis/bitcoin-required-return/main/llms.txt
- Bitcoin's Expected Return: An Age Rule That Beats Current Practice
  Guide: https://raw.githubusercontent.com/apapadogiannis/bitcoin-age-rule/main/llms.txt
- Beyond Discount Rates: A Valuation Framework for Unpriced Systematic Risk
  Guide: https://raw.githubusercontent.com/apapadogiannis/beyond-discount-rates/main/llms.txt
- From Unified Discounting to Dual-Risk: A New Lens on DCF Valuation
  Guide: https://raw.githubusercontent.com/apapadogiannis/dual-risk-dcf/main/llms.txt
- Does AI break the case for broad index investing? Rent decay, private capital, and deflation
  Guide: https://raw.githubusercontent.com/apapadogiannis/ai-broad-index-investing/main/llms.txt
- High Yield, Capped Gains: Mechanics, Trade-Offs, and Practical Diagnostics for Covered-Call ETFs
  Guide: https://raw.githubusercontent.com/apapadogiannis/covered-call-etfs/main/llms.txt

Papers with a paper record (no computation; the definitions, model and tables as data):

- Scarcity in an age of AI abundance
  Guide: https://raw.githubusercontent.com/apapadogiannis/ai-abundance/main/llms.txt

The other 11 papers have no package. They are listed in the index with their addresses.

## Rules

- A tool and the paper behind it can give different figures for the same thing, because a tool is
  recomputed and a paper is a fixed record. Give the tool's figure with its date for a question about
  now, and the paper's for what the paper reports. Say which one you are giving.
- A replication package is a fixed record of one paper. For current figures use the live tool the
  guide points to.
- 10 of the 21 papers are peer-reviewed journal articles, published or accepted; the index marks each one.
  The others are working papers. Say which a paper is, and report a figure as that paper's result.
- For the calculator: if the tools of the MCP server `dual-risk` are available to you, use them and do
  not do the arithmetic yourself.
- The results are under CC BY 4.0, whose one condition is credit: cite the paper.
- A published article belongs to its publisher. The packages hold its numbers, not its text.

Page for people: https://github.com/apapadogiannis
