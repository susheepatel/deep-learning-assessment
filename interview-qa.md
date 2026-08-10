# Technical Q&A — AIML & Web Development

Based on the skill set in the profile (Python, Machine Learning, TensorFlow/PyTorch, React.js, and LegalTech/AI applications), here are 5 common interview-style questions with detailed answers and explanations.

---

## Q1. What is the difference between TensorFlow and PyTorch, and when would you choose one over the other?

**Answer:**
TensorFlow uses a mostly static computation graph (with eager execution added later), while PyTorch uses a dynamic computation graph built on the fly during execution.

**Explanation:**
- **PyTorch** is generally preferred for research and rapid prototyping because its dynamic graph makes debugging easier (you can use standard Python debuggers) and model architecture can change at runtime.
- **TensorFlow** (especially with TensorFlow Serving, TFLite, and TF Extended) has stronger tooling for production deployment, mobile/edge inference (relevant for TinyML work), and scaling across distributed systems.
- In practice, many teams prototype in PyTorch and convert to ONNX or TensorFlow formats for deployment, or use TensorFlow directly if the target is edge devices.

---

## Q2. How would you evaluate a machine learning model beyond just accuracy?

**Answer:**
Use metrics appropriate to the problem type: precision, recall, F1-score, and ROC-AUC for classification; RMSE/MAE for regression; and confusion matrices to understand error types.

**Explanation:**
Accuracy alone is misleading on imbalanced datasets (e.g., a health-tech model predicting a rare condition could get 95% accuracy by always predicting "no condition"). Precision/recall trade-offs matter especially in health-tech (false negatives can be costly) and legal-tech (false positives in document flagging waste reviewer time). Cross-validation and holdout test sets also guard against overfitting.

---

## Q3. In a React.js application, what's the difference between state and props, and why does it matter for performance?

**Answer:**
`props` are read-only data passed from parent to child components; `state` is data owned and managed within a component that can change over time and triggers re-renders when updated.

**Explanation:**
Misusing state (e.g., storing derived data in state instead of computing it from props) causes unnecessary re-renders and bugs where UI gets out of sync. For performance, tools like `React.memo`, `useMemo`, and `useCallback` prevent components from re-rendering when their props/state haven't meaningfully changed — important in data-heavy apps like a legal document review interface with many list items.

---

## Q4. How would you design an AI system (like a legal research assistant) to reduce hallucination when summarizing documents?

**Answer:**
Use retrieval-augmented generation (RAG): retrieve relevant source passages from a verified document store, then constrain the model to generate answers grounded in that retrieved text, with citations back to the source.

**Explanation:**
Pure generative summarization without grounding risks the model inventing facts or misquoting legal text — a serious problem in LegalTech where accuracy is critical. Techniques to reduce this include: chunking documents with embeddings for semantic search, prompting the model to quote/cite retrieved passages, adding a verification/consistency-check step, and flagging low-confidence outputs for human review rather than presenting everything as certain.

---

## Q5. What is TinyML, and what are the main constraints when deploying ML models to edge devices?

**Answer:**
TinyML is the practice of running machine learning models on low-power, resource-constrained hardware (microcontrollers, IoT sensors) rather than servers or GPUs.

**Explanation:**
The main constraints are: limited memory (often kilobytes, not gigabytes), limited compute (no GPU, minimal CPU), and power budget (often battery-powered). This requires model compression techniques — quantization (reducing weight precision from float32 to int8), pruning (removing unnecessary weights/neurons), and knowledge distillation (training a smaller model to mimic a larger one). Frameworks like TensorFlow Lite for Microcontrollers are built specifically for this constrained deployment target.

---
