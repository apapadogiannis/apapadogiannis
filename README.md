## Agisilaos Papadogiannis

<sub><a href="https://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=7457522">SSRN</a> · <a href="https://scholar.google.com/citations?user=RihXr08AAAAJ">Google Scholar</a> · <a href="https://orcid.org/0009-0002-7753-7052">ORCID</a> · <a href="https://scarcitythinker.substack.com">Substack</a> · <a href="mailto:apapadogiannis@gmail.com">Email</a></sub>

**Live answers to three investor questions, recomputed on a schedule from public filings and market data.** Each figure is dated, checked automatically before it is published, and backed by a paper you can read and code you can run.

| The question | Latest answer | As of | Research behind it |
|---|---|---|---|
| [What does the yield of a covered-call fund cost?](https://apapadogiannis.github.io/covered-call-monitor/) | 87 funds followed from their SEC filings. Where a fund has an index fund on the same market, it returned 5.5 points less at the median | 12 months to June 2026, rebuilt quarterly | [Peer-reviewed](https://doi.org/10.3905/jbis.2026.001), The Journal of Beta Investment Strategies, 2026 |
| [What return should a Bitcoin holder require?](https://apapadogiannis.github.io/crypto-observatory/) | 18.8% a year, a hurdle rate, not a forecast | October 2026, recomputed monthly | [Working paper](https://ssrn.com/abstract=7705239) |
| [How much of a valuation gap is the forecast, and how much the discount rate?](https://apapadogiannis.github.io/dual-risk-calculator/) | Computed from your own numbers | Any time | [Peer-reviewed](https://doi.org/10.1016/j.finr.2026.100096), Finance Research Open, 2026 |

<sub>Free, no account. Every figure is also a data file your AI assistant can read. Methods: 21 papers, ten of them peer-reviewed.</sub>


### The tools

<table>
<tr>
<td width="33%" valign="top">
<a href="https://apapadogiannis.github.io/covered-call-monitor/"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/covered-call-monitor-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/covered-call-monitor-light.svg"><img src="assets/covered-call-monitor-light.svg" width="100%" alt="Total return over 3 years of 5 large covered-call funds, each beside the index fund on the same market"></picture></a>
<h4>Covered-Call Monitor</h4>
<p>What does the yield of a covered-call fund cost against its index fund?</p>
<p><sub>Covered-call funds followed, each from its SEC filings</sub></p>
<h3>87 funds</h3>
<p><sub>18 of them can be set beside an index fund on the same market. Over the 12 months to June 2026, all 18 returned less than it, by 5.5 percentage points at the median, distributions reinvested. Rebuilt every quarter.</sub></p>
<p><b><a href="https://apapadogiannis.github.io/covered-call-monitor/">Open the tool</a></b></p>
<p><img src="https://github.com/apapadogiannis/covered-call-monitor/actions/workflows/check.yml/badge.svg" alt="automated check"></p>
</td>
<td width="33%" valign="top">
<a href="https://apapadogiannis.github.io/crypto-observatory/"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/crypto-observatory-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/crypto-observatory-light.svg"><img src="assets/crypto-observatory-light.svg" width="100%" alt="The required return of Bitcoin, Ether, BNB, Solana and Tron, each as a bar made of the risk-free rate, market risk, concentration risk and mortality risk, with three equity series and gold below for scale"></picture></a>
<h4>Crypto Observatory</h4>
<p>What return should a cryptoasset's holders require?</p>
<p><sub>Bitcoin's required return, October 2026</sub></p>
<h3>18.8% a year</h3>
<p><sub>The midpoint of a range from 11.7% to 25.9% across the model's inputs. The paper's 18.1% is the median over the same inputs. Recomputed every month.</sub></p>
<p><b><a href="https://apapadogiannis.github.io/crypto-observatory/">Open the tool</a></b></p>
<p><img src="https://github.com/apapadogiannis/crypto-observatory/actions/workflows/check.yml/badge.svg" alt="automated check"></p>
</td>
<td width="33%" valign="top">
<a href="https://apapadogiannis.github.io/dual-risk-calculator/"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/dual-risk-calculator-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/dual-risk-calculator-light.svg"><img src="assets/dual-risk-calculator-light.svg" width="100%" alt="Two bars: the value of a benchmark forecast and of a forecast 10% lower, both discounted at the same benchmark rate, with the valuation ratio K, the gain of capital and the effective rate"></picture></a>
<h4>Dual-Risk DCF Calculator</h4>
<p>How much of a valuation gap is the forecast, and how much the discount rate?</p>
<p><sub>Example: a forecast 10% too low, valued at 8% over 5 years</sub></p>
<h3>11% gap in value</h3>
<p><sub>The value on the benchmark forecast is 1.11 times the value on the lower one: that ratio is K. One discount rate would have to fall to 4.1% to hide the gap. Enter your own forecasts or prices.</sub></p>
<p><b><a href="https://apapadogiannis.github.io/dual-risk-calculator/">Open the tool</a></b></p>
<p><img src="https://github.com/apapadogiannis/dual-risk-calculator/actions/workflows/check.yml/badge.svg" alt="automated check"></p>
</td>
</tr>
</table>

All three on one page, with what each one shows: **[apapadogiannis.github.io](https://apapadogiannis.github.io/)**

### The research behind them

21 papers, 10 of them peer-reviewed: published or accepted by a journal after review by its referees. 9 come with a replication package, the data and code to recompute every number. Together they follow value through four questions: where it comes from, what return it must earn, what it is worth once both are known, and what its holder actually keeps.

The peer-reviewed articles are in Financial Economics Letters, Frontiers in Blockchain, Asian Review of Political Economy, Asian Economics Letters, The Journal of Investing, Discover Analytics, Finance Research Open, Economics Bulletin and The Journal of Beta Investment Strategies.

<p align="center">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="assets/map-dark.svg">
<source media="(prefers-color-scheme: light)" srcset="assets/map-light.svg">
<img src="assets/map-light.svg" width="720" alt="Two overlapping circles. Value creation: where value comes from, through cash flows, scarcity, desirability and adoption. Returns: required and expected, what an asset must earn and is expected to earn. Their overlap is valuation, the dual-risk framework: a valuation carries two risks, in what the asset delivers and in the return it must earn. An arrow leads to a band below: value capture, what the holder actually keeps.">
</picture>
</p>

Click a line to open its list. A green badge means the package's stored results were reproduced at the last automated run.

<details>
<summary><img src="assets/q-creation-dot.svg" width="12" height="12" alt=""> <b>Value creation</b>: where value comes from (8 papers, 3 with a replication package, 1 with a paper record)</summary>
<ul>
<li><b>Economic Scarcity as Value: A Universal Framework for Blockchain and Beyond</b>. Working paper. <a href="https://ssrn.com/abstract=5384204">SSRN</a> · <a href="https://github.com/apapadogiannis/economic-scarcity-as-value">Replication package</a> <a href="https://github.com/apapadogiannis/economic-scarcity-as-value/actions/workflows/replicate.yml"><img src="https://github.com/apapadogiannis/economic-scarcity-as-value/actions/workflows/replicate.yml/badge.svg" alt="replication"></a><br><sub>Writes the value of a network as desirability times scarcity times adoption and applies it to Bitcoin, Ethereum and Bittensor; scarcity is scored from protocol features, and desirability is what remains, as implied volatility is recovered from an option price.</sub></li>
<li><b>The Architecture of Blockchain Value: Capabilities, Pillars, and Growth Dynamics</b>. <b>Peer-reviewed:</b> Frontiers in Blockchain, 2026. <a href="https://ssrn.com/abstract=5401302">SSRN</a> · <a href="https://www.frontiersin.org/journals/blockchain/articles/10.3389/fbloc.2026.1747512/full">Published version</a> · <a href="https://github.com/apapadogiannis/architecture-of-blockchain-value">Replication package</a> <a href="https://github.com/apapadogiannis/architecture-of-blockchain-value/actions/workflows/replicate.yml"><img src="https://github.com/apapadogiannis/architecture-of-blockchain-value/actions/workflows/replicate.yml/badge.svg" alt="replication"></a> · <a href="https://apapadogiannis.github.io/architecture-of-blockchain-value/">Interactive demo</a><br><sub>A theory of what a blockchain can deliver, its capabilities, and of how five architectural pillars decide which capabilities are feasible. It estimates nothing and uses no dataset.</sub></li>
<li><b>Bitcoin Is Not Money: Why Fixed Supply Fails in a Modern Economy</b>. <b>Peer-reviewed:</b> Asian Economics Letters, forthcoming. <a href="https://ssrn.com/abstract=5435197">SSRN</a> · <a href="https://github.com/apapadogiannis/bitcoin-is-not-money">Replication package</a> <a href="https://github.com/apapadogiannis/bitcoin-is-not-money/actions/workflows/replicate.yml"><img src="https://github.com/apapadogiannis/bitcoin-is-not-money/actions/workflows/replicate.yml/badge.svg" alt="replication"></a><br><sub>With a fixed money stock and stable velocity, output growth implies deflation at the same rate, so a money with a fixed supply could not serve a growing economy.</sub></li>
<li><b>Scarcity in an age of AI abundance</b>. <b>Peer-reviewed:</b> Asian Review of Political Economy, forthcoming 2027. <a href="https://ssrn.com/abstract=5924462">SSRN</a> · <a href="https://github.com/apapadogiannis/ai-abundance">Paper record</a> <a href="https://github.com/apapadogiannis/ai-abundance/actions/workflows/check.yml"><img src="https://github.com/apapadogiannis/ai-abundance/actions/workflows/check.yml/badge.svg" alt="check"></a><br><sub>AI can make many goods cheap to produce without making an essential standard of living broadly affordable, because scarcity and its rents move to five layers: physical resources, infrastructure, capabilities, institutions and jurisdictions.</sub></li>
<li><b>Valuing Scarcity: A General Framework for Bitcoin, Gold, and Traditional Assets</b>. <b>Peer-reviewed:</b> Financial Economics Letters, 2026. <a href="https://ssrn.com/abstract=5289457">SSRN</a> · <a href="https://doi.org/10.58567/fel05020001">Published version</a></li>
<li><b>What Moves the Price of Gold: An Economic-Scarcity Lens on Policy, the Dollar, and the Debasement Trade</b>. Working paper. <a href="https://ssrn.com/abstract=5619373">SSRN</a></li>
<li><b>The Productivity Myth: Why Scarcity Drives All Value</b>. Working paper. <a href="https://ssrn.com/abstract=5367197">SSRN</a></li>
<li><b>How to Classify any Asset: Ontology, Anchor, Rail, Composability</b>. Working paper. <a href="https://ssrn.com/abstract=5635610">SSRN</a></li>
</ul>
</details>

<details>
<summary><img src="assets/q-returns-dot.svg" width="12" height="12" alt=""> <b>Returns</b>: required and expected (5 papers, 2 with a replication package)</summary>
<ul>
<li><b>Bitcoin's Required Return: Market Risk, Concentration and Mortality</b>. Working paper. <a href="https://ssrn.com/abstract=7705239">SSRN</a> · <a href="https://github.com/apapadogiannis/bitcoin-required-return">Replication package</a> <a href="https://github.com/apapadogiannis/bitcoin-required-return/actions/workflows/replicate.yml"><img src="https://github.com/apapadogiannis/bitcoin-required-return/actions/workflows/replicate.yml/badge.svg" alt="replication"></a> · <a href="https://apapadogiannis.github.io/crypto-observatory/">Live tool</a><br><sub>Asks what return Bitcoin's holders should require for the market, concentration and mortality risk they carry (the MCM equation), tests the answer against delivered returns, and takes a census of cryptoasset deaths.</sub></li>
<li><b>Bitcoin's Expected Return: An Age Rule That Beats Current Practice</b>. Working paper. <a href="https://ssrn.com/abstract=7705438">SSRN</a> · <a href="https://github.com/apapadogiannis/bitcoin-age-rule">Replication package</a> <a href="https://github.com/apapadogiannis/bitcoin-age-rule/actions/workflows/replicate.yml"><img src="https://github.com/apapadogiannis/bitcoin-age-rule/actions/workflows/replicate.yml/badge.svg" alt="replication"></a><br><sub>Tests the ways practitioners set Bitcoin's long-run expected return against the returns that followed since 2012; fixed rates and trailing averages fail, and an age rule, the power-law exponent divided by Bitcoin's age, comes closest.</sub></li>
<li><b>On the Physics of Expected Asset Returns</b>. Working paper. <a href="https://ssrn.com/abstract=6586879">SSRN</a></li>
<li><b>Scarcity-Aligned Discounting in Asset Valuation</b>. Working paper. <a href="https://ssrn.com/abstract=5368003">SSRN</a></li>
<li><b>The Bitcoin Hurdle Fallacy: Why Risk Misalignment Distorts Valuation</b>. Working paper. <a href="https://ssrn.com/abstract=5368091">SSRN</a></li>
</ul>
</details>

<details>
<summary><img src="assets/q-valuation-dot.svg" width="12" height="12" alt=""> <b>Valuation</b>: the dual-risk framework (5 papers, 2 with a replication package)</summary>
<ul>
<li><b>Beyond Discount Rates: A Valuation Framework for Unpriced Systematic Risk</b>. <b>Peer-reviewed:</b> The Journal of Investing, forthcoming 2027. <a href="https://ssrn.com/abstract=5180040">SSRN</a> · <a href="https://github.com/apapadogiannis/beyond-discount-rates">Replication package</a> <a href="https://github.com/apapadogiannis/beyond-discount-rates/actions/workflows/replicate.yml"><img src="https://github.com/apapadogiannis/beyond-discount-rates/actions/workflows/replicate.yml/badge.svg" alt="replication"></a><br><sub>Splits an asset's expected return into a cost of capital and a gain of capital, the part that comes from misjudged future cash flows, and measures both for three US equity index funds, 2000 to 2023.</sub></li>
<li><b>From Unified Discounting to Dual-Risk: A New Lens on DCF Valuation</b>. <b>Peer-reviewed:</b> Finance Research Open, 2026. <a href="https://ssrn.com/abstract=5252774">SSRN</a> · <a href="https://doi.org/10.1016/j.finr.2026.100096">Published version</a> · <a href="https://github.com/apapadogiannis/dual-risk-dcf">Replication package</a> <a href="https://github.com/apapadogiannis/dual-risk-dcf/actions/workflows/replicate.yml"><img src="https://github.com/apapadogiannis/dual-risk-dcf/actions/workflows/replicate.yml/badge.svg" alt="replication"></a> · <a href="https://apapadogiannis.github.io/dual-risk-calculator/">Calculator</a><br><sub>Separates a benchmark cost of capital, set outside the asset, from a valuation ratio K, fair value over valuation, and illustrates both on Bitcoin, US equities and gold.</sub></li>
<li><b>A Dual-Risk Theory of Valuation: Separating Market-Based Discounting from Expectational Distortion</b>. <b>Peer-reviewed:</b> Discover Analytics, 2026. <a href="https://ssrn.com/abstract=5226017">SSRN</a> · <a href="https://doi.org/10.1007/s44257-026-00062-9">Published version</a></li>
<li><b>Rethinking Capital Budgeting: Embedding Ex-Ante Alpha in the Cost of Capital</b>. <b>Peer-reviewed:</b> Economics Bulletin, 2026. <a href="https://ideas.repec.org/a/ebl/ecbull/eb-25-00176.html">Published version</a><br><sub>An effective cost of capital that adjusts the benchmark rate for the systematic part of the bias in cash-flow forecasts, so that valuation and the decision to accept a project are kept apart.</sub></li>
<li><b>Unifying DCF Valuation Across Traditional and Cryptoassets</b>. Working paper. <a href="https://ssrn.com/abstract=5363661">SSRN</a></li>
</ul>
</details>

<details>
<summary><img src="assets/q-capture-dot.svg" width="12" height="12" alt=""> <b>Value capture</b>: what the holder actually keeps (3 papers, 2 with a replication package)</summary>
<ul>
<li><b>Does AI break the case for broad index investing? Rent decay, private capital, and deflation</b>. <b>Peer-reviewed:</b> The Journal of Beta Investment Strategies, forthcoming 2027. <a href="https://ssrn.com/abstract=6058896">SSRN</a> · <a href="https://github.com/apapadogiannis/ai-broad-index-investing">Replication package</a> <a href="https://github.com/apapadogiannis/ai-broad-index-investing/actions/workflows/replicate.yml"><img src="https://github.com/apapadogiannis/ai-broad-index-investing/actions/workflows/replicate.yml/badge.svg" alt="replication"></a><br><sub>Asks whether AI weakens the case for holding a broad capitalization-weighted index, and concludes that it does not: such an index follows the rents as AI moves them.</sub></li>
<li><b>High Yield, Capped Gains: Mechanics, Trade-Offs, and Practical Diagnostics for Covered-Call ETFs</b>. <b>Peer-reviewed:</b> The Journal of Beta Investment Strategies, 2026. <a href="https://ssrn.com/abstract=5370897">SSRN</a> · <a href="https://doi.org/10.3905/jbis.2026.001">Published version</a> · <a href="https://github.com/apapadogiannis/covered-call-etfs">Replication package</a> <a href="https://github.com/apapadogiannis/covered-call-etfs/actions/workflows/replicate.yml"><img src="https://github.com/apapadogiannis/covered-call-etfs/actions/workflows/replicate.yml/badge.svg" alt="replication"></a> · <a href="https://apapadogiannis.github.io/covered-call-monitor/">Live tool</a><br><sub>Explains how covered-call funds turn upside into distributions, what that costs in rising markets, and what to look at in a fund.</sub></li>
<li><b>Crypto Treasury Companies: Financing Dynamics, Accretion Conditions, and Systemic Risk</b>. Working paper. <a href="https://ssrn.com/abstract=5487486">SSRN</a></li>
</ul>
</details>

<details>
<summary><b>Four papers to start with</b>: one per question, each with its data and code</summary>

<table>
<tr>
<td width="25%" valign="top">
<p><img src="assets/q-creation-band.svg" width="100%" alt=""></p>
<img src="assets/economic-scarcity.png" alt="Implied desirability of Bitcoin, Ethereum and Bittensor, with sensitivity ranges">
<p><img src="assets/q-creation-tag.svg" height="22" alt="Value creation"></p>
<p><b><a href="https://github.com/apapadogiannis/economic-scarcity-as-value">Economic Scarcity as Value: A Universal Framework for Blockchain and Beyond</a></b></p>
<p>Network value written as desirability times scarcity times adoption, for Bitcoin, Ethereum and Bittensor.</p>
<p><sub>Working paper</sub></p>
<p><img src="https://github.com/apapadogiannis/economic-scarcity-as-value/actions/workflows/replicate.yml/badge.svg" alt="replication check"></p>
</td>
<td width="25%" valign="top">
<p><img src="assets/q-returns-band.svg" width="100%" alt=""></p>
<img src="assets/required-return.png" alt="Bitcoin&#x27;s required return since 2012, split into risk-free rate, market risk, concentration risk and mortality risk">
<p><img src="assets/q-returns-tag.svg" height="22" alt="Returns"></p>
<p><b><a href="https://github.com/apapadogiannis/bitcoin-required-return">Bitcoin's Required Return: Market Risk, Concentration and Mortality</a></b></p>
<p>The MCM equation prices market, concentration and mortality risk: about 18% a year for 2026 at the median. The live tool above shows the midpoint of its band.</p>
<p><sub>Working paper</sub></p>
<p><img src="https://github.com/apapadogiannis/bitcoin-required-return/actions/workflows/replicate.yml/badge.svg" alt="replication check"></p>
</td>
<td width="25%" valign="top">
<p><img src="assets/q-valuation-band.svg" width="100%" alt=""></p>
<img src="assets/beyond-discount-rates.png" alt="Realized gain of capital over three-year horizons for SPY, QQQ and IWM, by starting month, 2000 to 2020">
<p><img src="assets/q-valuation-tag.svg" height="22" alt="Valuation"></p>
<p><b><a href="https://github.com/apapadogiannis/beyond-discount-rates">Beyond Discount Rates: A Valuation Framework for Unpriced Systematic Risk</a></b></p>
<p>A cost of capital for priced risk, plus a gain of capital when expected cash flows are misestimated.</p>
<p><sub>Peer-reviewed: The Journal of Investing, forthcoming 2027</sub></p>
<p><img src="https://github.com/apapadogiannis/beyond-discount-rates/actions/workflows/replicate.yml/badge.svg" alt="replication check"></p>
</td>
<td width="25%" valign="top">
<p><img src="assets/q-capture-band.svg" width="100%" alt=""></p>
<img src="assets/ai-broad-index.png" alt="Annual returns since the release of ChatGPT: capitalization-weighted indices against the equal-weighted S&amp;P 500 and three AI-themed funds">
<p><img src="assets/q-capture-tag.svg" height="22" alt="Value capture"></p>
<p><b><a href="https://github.com/apapadogiannis/ai-broad-index-investing">Does AI break the case for broad index investing? Rent decay, private capital, and deflation</a></b></p>
<p>Since ChatGPT the S&amp;P 500 returned 19% a year against 11% equal-weighted: a capitalization-weighted index follows rents as AI moves them.</p>
<p><sub>Peer-reviewed: The Journal of Beta Investment Strategies, forthcoming 2027</sub></p>
<p><img src="https://github.com/apapadogiannis/ai-broad-index-investing/actions/workflows/replicate.yml/badge.svg" alt="replication check"></p>
</td>
</tr>
</table>

</details>

### For your AI assistant

Add one short instruction file, a skill, to an AI assistant such as Claude, and it answers from the latest figures here, with the date and the source, instead of from memory. Free, no account or key.

**One skill reads every figure and every paper here:** <a href="https://github.com/apapadogiannis/apapadogiannis/blob/main/skill/SKILL.md"><code>papadogiannis-finance-research</code></a>. It is one file, and it holds no figures, so it does not go out of date.

<details>
<summary>What it answers, and how to add it</summary>

<table>
<tr><th>What it answers</th><th>A question to try</th></tr>
<tr><td>Covered-call funds: returns, payouts, written calls and flows</td><td>“How did JEPI do against its index fund over three years?”</td></tr>
<tr><td>The required return of Bitcoin, Ether, BNB, Solana and Tron, what each is made of, and Bitcoin's record</td><td>“What return should the holders of Bitcoin and of Ether require now, and what is each made of?”</td></tr>
<tr><td>Splitting a valuation gap into the discount rate and the forecast, from your own numbers</td><td>“My forecast is 90 a year for five years and the benchmark is 100. At 8%, what is K and the effective rate?”</td></tr>
<tr><td>A number or a finding from any of the papers</td><td>“What does the age-rule paper report for Bitcoin's expected return?”</td></tr>
</table>

In Claude Code, one file in one folder:

```
mkdir -p ~/.claude/skills/papadogiannis-finance-research
curl -o ~/.claude/skills/papadogiannis-finance-research/SKILL.md https://raw.githubusercontent.com/apapadogiannis/apapadogiannis/main/skill/SKILL.md
```

In another assistant, add the same file wherever it takes instructions or skills, or give it the address of [llms.txt](llms.txt). It replaces the separate skills the tools used to publish. The Bitcoin and Ether price inputs come from Coin Metrics community data, which are for non-commercial use, as the Observatory's guide states.

**The calculator is also an MCP server.** A skill tells an assistant where to read figures. An MCP server gives it a tool to call: the assistant sends your numbers and gets the result computed, not estimated. It runs on your own machine, and the install line is in [its repository](https://github.com/apapadogiannis/dual-risk-calculator#use-it-from-your-own-ai-agent).

</details>

<sub>AI agents and programs: start at [llms.txt](llms.txt), the index of every tool, paper and data file, with the tools' latest figures and one sentence on what each paper finds.</sub>

### About

Engineer by training (PhD, MBA). My first research career was in wireless communications, with IEEE publications that have drawn about 2,000 citations. The finance research is independent and unfunded. Corrections and questions are welcome, by email or as an issue on the repository concerned.

---

<sub>This research was conducted independently and without funding, review, or endorsement. The views expressed are solely those of the author and do not represent any institutional position. This page, the tools and the papers are for informational and academic purposes only and do not constitute financial, investment, tax, or legal advice, nor a recommendation to buy or sell any financial instrument. All data used are from publicly available sources.</sub>
