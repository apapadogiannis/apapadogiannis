## Agisilaos Papadogiannis

Engineer by training (PhD, MBA). My first research career was in wireless communications, with IEEE publications that have drawn about 2,000 citations. I now do independent research in finance, published in peer-reviewed journals.

My work asks three questions about assets: what they are worth (valuation), what return they must earn (pricing), and what their holders actually keep (capture). I treat research as engineering: every empirical result comes with open data and code, written in Python and re-run automatically on GitHub.

<p align="center">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="assets/research-map-dark.svg">
<source media="(prefers-color-scheme: light)" srcset="assets/research-map-light.svg">
<img src="assets/research-map-light.svg" width="820" alt="Two overlapping circles. Valuation: what an asset is worth. Pricing: what return it must earn. Their overlap is the dual-risk framework, in which expected cash flows shift the required return and the required return sets the value. Both lead to a band below: capture, what the holder actually keeps.">
</picture>
</p>

### Featured replication packages

One per question. Each holds the data and code behind a paper, with one script that regenerates every table and figure.

<table>
<tr>
<td width="50%" valign="top">
<p><img src="assets/hband-valuation.svg" width="100%" alt=""></p>
<a href="https://github.com/apapadogiannis/economic-scarcity-as-value"><img src="assets/economic-scarcity.png" alt="Implied desirability of Bitcoin, Ethereum and Bittensor, with sensitivity ranges"></a>
<p><img src="assets/tag-valuation.svg" height="22" alt="Valuation"></p>
<p><b><a href="https://github.com/apapadogiannis/economic-scarcity-as-value">Economic Scarcity as Value: A Universal Framework for Blockchain and Beyond</a></b></p>
<p>Network value written as desirability times scarcity times adoption, applied to Bitcoin, Ethereum and Bittensor. Bitcoin and Ethereum come out within about 25% of each other; Bittensor's valuation rests mainly on expectations.</p>
<p><a href="https://github.com/apapadogiannis/economic-scarcity-as-value/actions/workflows/replicate.yml"><img src="https://github.com/apapadogiannis/economic-scarcity-as-value/actions/workflows/replicate.yml/badge.svg" alt="replication"></a> <a href="https://doi.org/10.5281/zenodo.24051776"><img src="https://img.shields.io/badge/Zenodo-10.5281%2Fzenodo.24051776-007ec6" alt="Zenodo"></a> <a href="https://ssrn.com/abstract=5384204"><img src="https://img.shields.io/badge/SSRN-5384204-1f4e79" alt="SSRN"></a></p>
</td>
<td width="50%" valign="top">
<p><img src="assets/hband-pricing.svg" width="100%" alt=""></p>
<a href="https://github.com/apapadogiannis/bitcoin-required-return"><img src="assets/required-return.png" alt="Bitcoin&#x27;s required return since 2012, split into risk-free rate, market risk, concentration risk and mortality risk"></a>
<p><img src="assets/tag-pricing.svg" height="22" alt="Pricing"></p>
<p><b><a href="https://github.com/apapadogiannis/bitcoin-required-return">Bitcoin's Required Return: Pricing a New Asset Beside Equities and Gold</a></b></p>
<p>The MCM equation: the return Bitcoin's holders should require is the risk-free rate plus market, concentration and mortality risk. For 2026 that is about 18% a year (90% range 15–22%). Built on a census of 1,815 cryptoassets with 520 deaths; an audit script re-checks every number in the paper.</p>
<p><a href="https://github.com/apapadogiannis/bitcoin-required-return/actions/workflows/replicate.yml"><img src="https://github.com/apapadogiannis/bitcoin-required-return/actions/workflows/replicate.yml/badge.svg" alt="replication"></a> <a href="https://doi.org/10.5281/zenodo.24003938"><img src="https://img.shields.io/badge/Zenodo-10.5281%2Fzenodo.24003938-007ec6" alt="Zenodo"></a> <a href="https://ssrn.com/abstract=7705239"><img src="https://img.shields.io/badge/SSRN-7705239-1f4e79" alt="SSRN"></a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><img src="assets/hband-dual-risk.svg" width="100%" alt=""></p>
<a href="https://github.com/apapadogiannis/beyond-discount-rates"><img src="assets/beyond-discount-rates.png" alt="Realized gain of capital over three-year horizons for SPY, QQQ and IWM, by starting month, 2000 to 2020"></a>
<p><img src="assets/tag-dual-risk.svg" height="22" alt="Dual-risk framework"></p>
<p><b><a href="https://github.com/apapadogiannis/beyond-discount-rates">Beyond Discount Rates: A Valuation Framework for Unpriced Systematic Risk</a></b></p>
<p>Forthcoming in <i>The Journal of Investing</i>. Discounted cash flow valuation with two return components: a cost of capital for priced risk and a gain of capital that arises when expected cash flows are misestimated. For SPY, QQQ and IWM from 2000 to 2023 the gain is large and persistent: over one year it exceeds 20 percentage points in 22% of months for SPY and 43% for QQQ. Code and data only; the article text is copyright PMR.</p>
<p><a href="https://github.com/apapadogiannis/beyond-discount-rates/actions/workflows/replicate.yml"><img src="https://github.com/apapadogiannis/beyond-discount-rates/actions/workflows/replicate.yml/badge.svg" alt="replication"></a> <a href="https://doi.org/10.5281/zenodo.24243060"><img src="https://img.shields.io/badge/Zenodo-10.5281%2Fzenodo.24243060-007ec6" alt="Zenodo"></a> <a href="https://ssrn.com/abstract=5180040"><img src="https://img.shields.io/badge/SSRN-5180040-1f4e79" alt="SSRN"></a></p>
</td>
<td width="50%" valign="top">
<p><img src="assets/hband-capture.svg" width="100%" alt=""></p>
<a href="https://github.com/apapadogiannis/ai-broad-index-investing"><img src="assets/ai-broad-index.png" alt="Annual returns since the release of ChatGPT: capitalization-weighted indices against the equal-weighted S&amp;P 500 and three AI-themed funds"></a>
<p><img src="assets/tag-capture.svg" height="22" alt="Capture"></p>
<p><b><a href="https://github.com/apapadogiannis/ai-broad-index-investing">Does AI break the case for broad index investing? Rent decay, private capital, and deflation</a></b></p>
<p>Forthcoming in <i>The Journal of Beta Investment Strategies</i>. Since the release of ChatGPT the S&amp;P 500 returned 19% a year against 11% for its equal-weighted version, and two of three AI-themed funds trailed it: a capitalization-weighted index follows rents as AI moves them, without a forecast. Code and data only; the article text is copyright PMR.</p>
<p><a href="https://github.com/apapadogiannis/ai-broad-index-investing/actions/workflows/replicate.yml"><img src="https://github.com/apapadogiannis/ai-broad-index-investing/actions/workflows/replicate.yml/badge.svg" alt="replication"></a> <a href="https://doi.org/10.5281/zenodo.24240516"><img src="https://img.shields.io/badge/Zenodo-10.5281%2Fzenodo.24240516-007ec6" alt="Zenodo"></a> <a href="https://ssrn.com/abstract=6058896"><img src="https://img.shields.io/badge/SSRN-6058896-1f4e79" alt="SSRN"></a></p>
</td>
</tr>
</table>

### All papers by question

Click a line to open its list. Where a paper has a replication package, the green badge is live: GitHub re-runs the full pipeline on a clean machine at every change and once a month, and the badge turns red if a single table differs from the published one.

<details>
<summary><img src="assets/dot-valuation.svg" width="12" height="12" alt=""> <b>Valuation</b>: what an asset is worth (8 papers, 1 with a replication package)</summary>
<ul>
<li><b>Economic Scarcity as Value: A Universal Framework for Blockchain and Beyond</b>. <a href="https://ssrn.com/abstract=5384204">SSRN</a> · <a href="https://github.com/apapadogiannis/economic-scarcity-as-value">Replication package</a> <a href="https://github.com/apapadogiannis/economic-scarcity-as-value/actions/workflows/replicate.yml"><img src="https://github.com/apapadogiannis/economic-scarcity-as-value/actions/workflows/replicate.yml/badge.svg" alt="replication"></a></li>
<li><b>Valuing Scarcity: A General Framework for Bitcoin, Gold, and Traditional Assets</b>. Financial Economics Letters, 2026. <a href="https://ssrn.com/abstract=5289457">SSRN</a> · <a href="https://doi.org/10.58567/fel05020001">Published version</a></li>
<li><b>The Architecture of Blockchain Value: Capabilities, Pillars, and Growth Dynamics</b>. Frontiers in Blockchain, 2026. <a href="https://ssrn.com/abstract=6196338">SSRN</a> · <a href="https://www.frontiersin.org/journals/blockchain/articles/10.3389/fbloc.2026.1747512/full">Published version</a></li>
<li><b>Scarcity in an Age of AI Abundance</b>. <a href="https://ssrn.com/abstract=5924462">SSRN</a></li>
<li><b>What Moves the Price of Gold: An Economic-Scarcity Lens on Policy, the Dollar, and the Debasement Trade</b>. <a href="https://ssrn.com/abstract=5619373">SSRN</a></li>
<li><b>The Productivity Myth: Why Scarcity Drives All Value</b>. <a href="https://ssrn.com/abstract=5367197">SSRN</a></li>
<li><b>Bitcoin Is Not Money: Why Fixed Supply Fails in a Modern Economy</b>. <a href="https://ssrn.com/abstract=5435197">SSRN</a></li>
<li><b>How to Classify any Asset: Ontology, Anchor, Rail, Composability</b>. <a href="https://ssrn.com/abstract=5635610">SSRN</a></li>
</ul>
</details>

<details>
<summary><img src="assets/dot-pricing.svg" width="12" height="12" alt=""> <b>Pricing</b>: what return it must earn (5 papers, 2 with a replication package)</summary>
<ul>
<li><b>Bitcoin's Required Return: Pricing a New Asset Beside Equities and Gold</b>. <a href="https://ssrn.com/abstract=7705239">SSRN</a> · <a href="https://github.com/apapadogiannis/bitcoin-required-return">Replication package</a> <a href="https://github.com/apapadogiannis/bitcoin-required-return/actions/workflows/replicate.yml"><img src="https://github.com/apapadogiannis/bitcoin-required-return/actions/workflows/replicate.yml/badge.svg" alt="replication"></a></li>
<li><b>Bitcoin's Expected Return: An Age Rule That Beats Current Practice</b>. <a href="https://ssrn.com/abstract=7705438">SSRN</a> · <a href="https://github.com/apapadogiannis/bitcoin-age-rule">Replication package</a> <a href="https://github.com/apapadogiannis/bitcoin-age-rule/actions/workflows/replicate.yml"><img src="https://github.com/apapadogiannis/bitcoin-age-rule/actions/workflows/replicate.yml/badge.svg" alt="replication"></a></li>
<li><b>On the Physics of Expected Asset Returns</b>. <a href="https://ssrn.com/abstract=6586879">SSRN</a></li>
<li><b>Scarcity-Aligned Discounting in Asset Valuation</b>. <a href="https://ssrn.com/abstract=5368003">SSRN</a></li>
<li><b>The Bitcoin Hurdle Fallacy: Why Risk Misalignment Distorts Valuation</b>. <a href="https://ssrn.com/abstract=5368091">SSRN</a></li>
</ul>
</details>

<details>
<summary><img src="assets/dot-dual-risk.svg" width="12" height="12" alt=""> <b>Dual-risk framework</b>: where valuation and pricing meet (5 papers, 1 with a replication package)</summary>
<ul>
<li><b>Beyond Discount Rates: A Valuation Framework for Unpriced Systematic Risk</b>. The Journal of Investing, forthcoming 2027. <a href="https://ssrn.com/abstract=5180040">SSRN</a> · <a href="https://github.com/apapadogiannis/beyond-discount-rates">Replication package</a> <a href="https://github.com/apapadogiannis/beyond-discount-rates/actions/workflows/replicate.yml"><img src="https://github.com/apapadogiannis/beyond-discount-rates/actions/workflows/replicate.yml/badge.svg" alt="replication"></a></li>
<li><b>A Dual-Risk Theory of Valuation: Bridging Discounting and Expectational Distortion</b>. Discover Analytics, 2026. <a href="https://ssrn.com/abstract=5226017">SSRN</a> · <a href="https://doi.org/10.1007/s44257-026-00062-9">Published version</a></li>
<li><b>From Unified Discounting to Dual-Risk: A New Lens on DCF Valuation</b>. Finance Research Open, 2026. <a href="https://ssrn.com/abstract=6127866">SSRN</a> · <a href="https://doi.org/10.1016/j.finr.2026.100096">Published version</a></li>
<li><b>Rethinking Capital Budgeting: Embedding Ex-Ante Alpha in the Cost of Capital</b>.</li>
<li><b>Unifying DCF Valuation Across Traditional and Cryptoassets</b>. <a href="https://ssrn.com/abstract=5363661">SSRN</a></li>
</ul>
</details>

<details>
<summary><img src="assets/dot-capture.svg" width="12" height="12" alt=""> <b>Capture</b>: what the holder actually keeps (3 papers, 2 with a replication package)</summary>
<ul>
<li><b>Does AI break the case for broad index investing? Rent decay, private capital, and deflation</b>. The Journal of Beta Investment Strategies, forthcoming 2027. <a href="https://ssrn.com/abstract=6058896">SSRN</a> · <a href="https://github.com/apapadogiannis/ai-broad-index-investing">Replication package</a> <a href="https://github.com/apapadogiannis/ai-broad-index-investing/actions/workflows/replicate.yml"><img src="https://github.com/apapadogiannis/ai-broad-index-investing/actions/workflows/replicate.yml/badge.svg" alt="replication"></a></li>
<li><b>High Yield, Capped Gains: Mechanics, Trade-Offs, and Practical Diagnostics for Covered-Call ETFs</b>. The Journal of Beta Investment Strategies, 2026. <a href="https://ssrn.com/abstract=5370897">SSRN</a> · <a href="https://doi.org/10.3905/jbis.2026.001">Published version</a> · <a href="https://github.com/apapadogiannis/covered-call-etfs">Replication package</a> <a href="https://github.com/apapadogiannis/covered-call-etfs/actions/workflows/replicate.yml"><img src="https://github.com/apapadogiannis/covered-call-etfs/actions/workflows/replicate.yml/badge.svg" alt="replication"></a></li>
<li><b>Crypto Treasury Companies: Financing Dynamics, Accretion Conditions, and Systemic Risk</b>. <a href="https://ssrn.com/abstract=5487486">SSRN</a></li>
</ul>
</details>

### Elsewhere

<a href="https://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=7457522"><img src="https://img.shields.io/badge/SSRN-154881?style=for-the-badge&logo=ssrn&logoColor=white" alt="SSRN"></a>
<a href="https://scholar.google.com/citations?user=RihXr08AAAAJ"><img src="https://img.shields.io/badge/Google%20Scholar-4285F4?style=for-the-badge&logo=googlescholar&logoColor=white" alt="Google Scholar"></a>
<a href="https://orcid.org/0009-0002-7753-7052"><img src="https://img.shields.io/badge/ORCID-A6CE39?style=for-the-badge&logo=orcid&logoColor=white" alt="ORCID"></a>
<a href="https://scarcitythinker.substack.com"><img src="https://img.shields.io/badge/Substack-FF6719?style=for-the-badge&logo=substack&logoColor=white" alt="Scarcity Thinker on Substack"></a>

Contact: apapadogiannis@gmail.com
