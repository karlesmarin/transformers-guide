# Transformers Guide · Cómo Atienden los Transformers / How Transformers Attend

> Una guía de campo y referencia · A field guide & reference
> De los tokens al contexto largo — cada fórmula verificada, medida y construida desde cero.
> From tokens to long context — every formula verified, measured and built from scratch.

**🌐 Live:** https://karlesmarin.github.io/transformers-guide/

---

## Español

Guía de campo y **referencia completa** sobre transformers: de los tokens al contexto largo,
en **8 partes / 40 capítulos + apéndices**. Doble público por capas: la **superficie** la
entiende cualquiera (prosa llana + analogía + ejemplo); la **profundidad** es una joya para el
técnico (fórmulas término a término, datos reales, pruebas formales en Lean, el atlas de
modelos y la app interactiva).

Lo que la hace única (la espina **atención-sobre-distancia**): la ley de decaimiento
`A(d) ∝ d^−γ`, el atlas de γ en decenas de modelos, la estructura de fases (Hagedorn), la
lente termodinámica, y el *audit* honesto "verificado vs folclore vs numerología".

- 📖 **Leer en español:** [`es/`](es/index.html)
- 🧪 **App interactiva (compañera):** [tafagent](https://karlesmarin.github.io/tafagent/)

## English

A field guide and **complete reference** on transformers: from tokens to long context, across
**8 parts / 40 chapters + appendices**. Dual audience by layers: the **surface** is readable by
anyone (plain prose + analogy + example); the **depth** is a gem for the practitioner
(term-by-term formulas, real data, formal Lean proofs, the model atlas, and the interactive app).

What makes it unique (the **attention-over-distance** spine): the decay law `A(d) ∝ d^−γ`, the
γ atlas across dozens of models, the phase structure (Hagedorn), the thermodynamic lens, and an
honest "verified vs folklore vs numerology" audit.

- 📖 **Read in English:** [`en/`](en/index.html)
- 🧪 **Interactive companion app:** [tafagent](https://karlesmarin.github.io/tafagent/)

---

## Interactive & animated visualizations (new — 2026-06)

The topic is intensely visual, so key chapters now embed **interactive, self-contained diagrams** — pure CSS/JS plus a locally **vendored three.js** (no external CDN: they work offline and under the GitHub Pages sub-path). Everything is **bilingual** (Spanish by default, English when the page language is English) and respects `prefers-reduced-motion`:

- **Live architecture explorer** (Ch. 1) — a token rising through the residual stream; each stage opens its real mini-component (embedding vector, mini causal attention map, FFN expand→compress, logit bars); play/pause, layer slider, click a stage to jump to its chapter.
- **RoPE in 3D** (Ch. 8) — the "tunnel of clocks": frequency bands spinning at different rates (aliasing made visible), drag to orbit; plus a 2D view showing the relative angle = relative position.
- **The γ atlas — interactive + 3D** (Ch. 16) — compare real models on one γ axis (and in 3D: γ × θ × R²), colored by phase, hover to identify each model; text vs random-token toggle.
- **Live formula plots** — γ_Padé(θ,T), `A(d)=d⁻ᵞ` (linear/log-log), softmax temperature, `1/√d_k` — move a slider and watch the formula respond, computed live from the real math.
- **Concept schemas** — Q/K/V as a soft dictionary lookup (real worked example), LayerNorm step by step, KV-cache compressibility (`Σ d⁻ᵞ`), the causal mask (−∞ → softmax), attention "who-attends-to-whom" arcs, and animated step timelines across many chapters.

## What's in this repo

This is the **published static site** (GitHub Pages). It is **generated** from a
[Quarto](https://quarto.org) book project (the `.qmd` sources live separately) — do not edit the
HTML here by hand.

| Path | What it is |
|------|------------|
| `index.html` | Language entry — auto-redirects by browser language (Spanish → ES, **everyone else → English** by default); `?choose` forces the picker |
| `es/` | The book in Spanish (lead version), rendered HTML |
| `en/` | The book in English (mirror), rendered HTML |
| `icon.png` | Favicon / logo |
| `.nojekyll` | Tells GitHub Pages to serve the files as-is |

## Author & links

- **Author:** Carles Marín
- **Companion app:** [tafagent](https://karlesmarin.github.io/tafagent/) — browser-only LLM diagnostics
- **Paper:** *Predicting How Transformers Attend* — [Zenodo](https://zenodo.org/records/20314038)
