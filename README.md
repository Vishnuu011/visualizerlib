<p align="center">
  <img src="https://github.com/Vishnuu011/visualizerlib/raw/main/assets/logo.png" width="300" alt="VisualizerLib Logo"/>
</p>


# VisualizerLib

**VisualizerLib** is a lightweight, scikit-learn–like preprocessing and visualization library built from scratch for educational and rapid prototyping purposes. It provides custom pipeline utilities, encoders, imputers, scalers, and plotting tools with AI agent integration for automated data insights.

---

## ✨ Features

- 🧱 **Custom Transformers**: Includes implementations like `VlibSimpleImputer`, `VlibStandardScaler`, `VlibMinMaxScaler`, `VlibOneHotEncoder`, `VlibOrdinalEncoder`, `VlibLabelEncoder`, `VlibFunctionalTransformer`, `remove_outliers_IQR`, and more.
- 🔁 **Chained Pipelines**: Use the `|` operator to chain preprocessing steps in a clean, readable way, or use the standard `VlibPipeline`.
- 🧩 **VlibColumnTransformer**: Apply transformers to specific subsets of columns.
- 🧠 **VlibLabelEncoder**: Auto-detects usage context and returns either `numpy` arrays or `pandas` DataFrames.
- 📊 **Integrated Plotting**: Generate common categorical and numerical plots easily.
- 🤖 **Agent Insights**: Let an AI agent (Groq API only) suggest relevant plots and data exploration insights.

---

## 🛠️ Installation

> ⚠️ This package is under active development. Please install manually for now.

```bash
git clone https://github.com/Vishnuu011/visualizerlib
cd visualizerlib
pip install -e .

pip install visualizerlib
