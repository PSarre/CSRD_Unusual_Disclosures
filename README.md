# CSRD Unusual Disclosures Pipeline

**PhD Research**: LLM extraction of CSRD IROs → industry baselines → unusual disclosure strategy detection vs keyword baselines.

## Repository structure

This project builds a CSRD-specific pipeline by adapting ideas and some utilities
from the EulerESG / ESG demo codebase.

- `csrd_pipeline/` – CSRD-specific research pipeline  
  - `01_esrs_iro_extraction/`: ESRS AR 16 ontology and IRO extraction scripts  
  - `config/`: ESRS / IRO schemas and configuration files

- `euleresg_legacy/` – EulerESG demo and supporting code kept for reference  
  (`ESG-demo-main`, `backend`, `logs`, `outputs`, `scripts`, `uploads`, `data`, etc.)

In the paper, EulerESG is cited for the general architecture (metadata module,
report preprocessing, LLM extraction). The CSRD-specific schema, prompts, and
analysis (unusual disclosures vs industry baselines) are original to this project.

