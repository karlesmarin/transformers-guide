# Transformers Guide · Cómo Atienden los Transformers / How Transformers Attend

> Una guía de campo y referencia · A field guide & reference
> De los tokens al contexto largo — cada fórmula verificada, medida y construida desde cero.
> From tokens to long context — every formula verified, measured and built from scratch.

**🌐 Live:** https://karlesmarin.github.io/transformers-guide/

---

## Español

Guía de campo y **referencia completa** sobre transformers: de los tokens al contexto largo,
en **8 partes / 41 capítulos + apéndices**. Doble público por capas: la **superficie** la
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
**8 parts / 41 chapters + appendices**. Dual audience by layers: the **surface** is readable by
anyone (plain prose + analogy + example); the **depth** is a gem for the practitioner
(term-by-term formulas, real data, formal Lean proofs, the model atlas, and the interactive app).

What makes it unique (the **attention-over-distance** spine): the decay law `A(d) ∝ d^−γ`, the
γ atlas across dozens of models, the phase structure (Hagedorn), the thermodynamic lens, and an
honest "verified vs folklore vs numerology" audit.

- 📖 **Read in English:** [`en/`](en/index.html)
- 🧪 **Interactive companion app:** [tafagent](https://karlesmarin.github.io/tafagent/)

---

## 🪜 New — 2026-07-11 · One-click into the Depth map (Part III)

**Depth-map deep-links** — Ch. 08 (RoPE) and Ch. 42 (the whiteboard) now open tafagent's new
**🪜 Depth map** demo (Part III, `?demo=depth`): the two geometric axes (distance γ ⟂ depth
L_crit), the three RoPE scales and the δ band-position lead — config-only, no inference, honest
that L_crit is not the commitment knee. · **Enlaces directos** al nuevo modo *Mapa de
profundidad* de tafagent desde los cap. 08 y 42.

## 🧊 New — 2026-07-10 · Part III lands + a campaign of analogies & 3D widgets

**Part III integrated** into *The global workspace* chapter (ES+EN): the J-lens advantage band
is reframed —honestly— as a property of the **transport operator** (not a store of content), the
residual computation is split into **three observables** (transport → writing → commitment, with
an *exact* direct-logit-attribution identity), and the γ↔band link is corrected to
*inconclusive* (the live lead is the **trained displacement** δ = γ_obs − γ_geom). · **Part III
integrada** en el capítulo del *espacio de trabajo global* (ES+EN), con la corrección honesta
γ→δ y dos widgets 3D nuevos.

**A whole campaign of clarity** across the physics / γ / systems chapters (14, 16, 17, 20, 21,
22, 23, 24): a plain-language **analogy** for each hard idea and **9 brand-new bespoke 3D
widgets** (Three.js) — each a *distinct* visual metaphor, all with play/pause + sliders and a
text fallback. · **Una campaña de claridad**: una analogía por cada idea difícil + 9 widgets 3D
nuevos, cada uno con su metáfora:

- 🌡️ **Attention as a gas** (Ch. 22) — γ is the cold: slide it and watch the distribution freeze
  or evaporate; the bars shudder ∝ heat capacity C_V near the critical point.
- ⛰️ **The χ mountain** (Ch. 21) — transition vs crossover: raise N and watch the divergence
  spike round into a finite bump.
- 🐜🕊️ **Ant vs albatross** (Ch. 23) — a Brownian walk beside a Lévy flight, driven by γ.
- 🧩 **The circuit under the plateau** (Ch. 24) — grokking's inter-layer coordination (CKA)
  re-weaving before the test jump; a weight-decay slider that can stall it.
- 📏 **The resolution waterfall** (Ch. 14) — RoPE pairs aliasing one by one; sweep distance for
  n_active, raise θ to stretch the three scales.
- 🗄️ **The KV-cache growing** (Ch. 20) — O(n) memory, and what compression keeps (sink + D_f).
- 🚰 **The drain and the slope** (Ch. 17) — γ ⊥ sink: move θ and the tail reshapes while the
  sink pillar doesn't budge.
- 🔭 **Two workspace widgets** (Ch. 42) — the Jacobian's "echo of the future" (transport vs
  writing, anticorrelated), and the "three clocks" tunnel (decode < write < commit).

**Formula audit** of all 49 sections: everything checks out; one glossary imprecision fixed
(Lévy *index* α = γ−1 vs fractional *order* s = (γ−1)/2). · **Repaso completo de fórmulas.**

## 🎮 Interactive & animated visualizations (new — 2026-06)

The topic is intensely visual, so key chapters now embed **interactive, self-contained diagrams** — pure CSS/JS plus a locally **vendored three.js** (no external CDN: they work offline and under the GitHub Pages sub-path). Everything is **bilingual** (Spanish by default, English when the page language is English) and respects `prefers-reduced-motion`:

- **Live architecture explorer** (Ch. 1) — a token rising through the residual stream; each stage opens its real mini-component (embedding vector, mini causal attention map, FFN expand→compress, logit bars); play/pause, layer slider, click a stage to jump to its chapter.
- **RoPE in 3D** (Ch. 8) — the "tunnel of clocks": frequency bands spinning at different rates (aliasing made visible), drag to orbit; plus a 2D view showing the relative angle = relative position.
- **The γ atlas — interactive + 3D** (Ch. 16) — compare real models on one γ axis (and in 3D: γ × θ × R²), colored by phase, hover to identify each model; text vs random-token toggle.
- **Live formula plots** — γ_Padé(θ,T), `A(d)=d⁻ᵞ` (linear/log-log), softmax temperature, `1/√d_k` — move a slider and watch the formula respond, computed live from the real math.
- **Concept schemas** — Q/K/V as a soft dictionary lookup (real worked example), LayerNorm step by step, KV-cache compressibility (`Σ d⁻ᵞ`), the causal mask (−∞ → softmax), attention "who-attends-to-whom" arcs, and animated step timelines across many chapters.

## ✨ Updated — July 2026 · Actualizado — julio 2026

**New chapter (2026-07-07) — *The global workspace: reading the model's whiteboard* / *El
espacio de trabajo global: leer la pizarra del modelo*** (closes Part VII, ES+EN): the
Anthropic global-workspace result (Jacobian lens, the readable "whiteboard" inside the
residual stream, ignition, the automatic/deliberate double dissociation), told as the
payoff of the "shared whiteboard" analogy from Ch. 3 — with **4 new interactive widgets**
(whiteboard-in-action with a J-lens/logit-lens toggle, erase-the-whiteboard, ignition
slider, intro flow) and the L_crit formula term by term, with its real validation status
and a pre-registered measurement in progress. · **Nuevo capítulo** con 4 widgets
interactivos y honestidad explícita (predicciones congeladas antes de medir).

A major content + freshness pass (both languages) · Gran tanda de contenido y actualización (ambos idiomas):

- **New chapter — *Evaluation: measuring without fooling yourself*** (Part VII, now 41 chapters): perplexity & bits-per-byte, capability benchmarks (MMLU/GPQA/HumanEval/SWE-bench/GSM8K/RULER), data **contamination** & **Goodhart's law**, the **LLM-as-judge** and its biases, and statistical rigor. · **Nuevo capítulo de *Evaluación*.**
- **Brought up to date to mid-2026:** **MoE** as the frontier default (+ an open *gpt-oss* X-ray), **FP4** quantization (MXFP4/NVFP4), **DeepSeek Sparse Attention**, **reasoning models & test-time compute** (RLVR), **circuit tracing / attribution graphs**, **benchmark saturation** (ARC-AGI-2, Humanity's Last Exam, FrontierMath), **GGUF & KV-cache quantization**, the inference **engine zoo** (vLLM/SGLang/llama.cpp/Ollama), **MCP/A2A**, SigLIP, Matryoshka, GraphRAG, EAGLE/Medusa, diffusion LLMs. *Every claim verified against primary sources; version-number rumors excluded.*
- **New interactive graphics:** a **Mixture-of-Experts router** and a **benchmark-contamination "mirage"** widget, plus **7 new animated flow diagrams** (training loop, encoder→decoder, classification, LoRA, FlashAttention, quantization, prefill→decode).
- **Honesty pass:** rigor/consistency fixes verified against the data (γ atlas, Lévy vs fractional integration, model counts, R² floor).

## 📦 What's in this repo

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

## 👤 Author & links

- **Author:** Carles Marín
- **Companion app:** [tafagent](https://karlesmarin.github.io/tafagent/) — browser-only LLM diagnostics
- **Paper:** *Predicting How Transformers Attend* — [Zenodo](https://zenodo.org/records/20314038)
