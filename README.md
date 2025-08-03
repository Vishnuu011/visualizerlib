# VisualizerLib

VisualizerLib is a lightweight, scikit-learn–like preprocessing and visualization library built from scratch for educational and rapid prototyping purposes. It provides custom pipeline utilities, encoders, imputers, scalers, and plotting tools with AI agent integration for automated data insights.

---

## ✨ Features

- 🧱 **Custom Transformers**: Implement your own `VlibSimpleImputer`, `VlibStandardScaler`, `VlibMinMaxScaler`, `VlibOneHotEncoder`, `VlibOrdinalEncoder`, `VlibLabelEncoder`, `VlibFunctionalTransformer`, `remove_outliers_IQR`etc.
- 🔁 **Chained Pipelines**: Use `|` operator to chain preprocessing steps in a clean, readable way and normal **VlibPipeline**.
- 🧩 **VlibColumnTransformer**: Apply transformers to subsets of columns.
- 🧠 **VlibLabelEncoder**: Auto-detects usage context (returns `numpy` or `pandas`).
- 📊 **Integrated Plotting**: Generate common categorical/numerical plots.
- 🤖 **Agent Insights**: Let the AI suggest useful plots and data understanding steps Agent soppurt only (Groq API).

---

## 🛠️ Installation

> ⚠️ This package is in development. Clone manually for now.

```bash
git clone https://github.com/Vishnuu011/visualizerlib
cd visualizerlib
pip install -e .
pip install visualizerlib
