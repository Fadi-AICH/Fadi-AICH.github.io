---
layout: post
title: "CyberGuard MLOps — IoT Intrusion Detection Platform"
date: 2026-05-07
permalink: /projects/cyberguard-mlops/
categories: [Projects, Cybersecurity, MLOps]
tags: [CICIoT2023, DVC, MLflow, FastAPI, Prometheus, Grafana, Airflow, Streamlit]
external_image: https://raw.githubusercontent.com/Fadi-AICH/cyberguard-mlops/main/screenshots/11_grafana_soc_dashboard.png
hide_banner: true
case_study: true
toc: true
excerpt: "End-to-end cybersecurity MLOps platform for CICIoT2023 intrusion detection with reproducible pipelines, model tracking, API serving, monitoring, orchestration and an analyst workbench."
---

<div class="case-kicker">Cybersecurity · Machine Learning · MLOps · SOC Analytics</div>
<p class="case-lead"><strong>CyberGuard MLOps</strong> is an end-to-end IoT intrusion-detection project built to go beyond a notebook that trains a model once. The system covers data ingestion and validation, reproducible training, experiment tracking, model registration, API serving, production-style monitoring, orchestration, drift analysis and an analyst-facing SOC workflow.</p>

<div class="case-summary">
  <div><b>0.941 F1</b><span>selected Gradient Boosting model</span></div>
  <div><b>CICIoT2023</b><span>reproducible public-dataset sample</span></div>
  <div><b>7 services</b><span>API, MLflow, Prometheus, Grafana, Airflow, SOC UI, replay</span></div>
  <div><b>CI + tests</b><span>formatting, linting, typing, tests and Docker builds</span></div>
</div>

<div class="case-flow"><span>CICIoT2023</span><i>→</i><span>Validation</span><i>→</i><span>DVC</span><i>→</i><span>Training + MLflow</span><i>→</i><span>FastAPI</span><i>→</i><span>Prometheus / Grafana</span><i>→</i><span>Streamlit analyst UI</span></div>

<div class="case-note"><strong>Project goal:</strong> treat an intrusion-detection model as a maintainable system. Reproducibility, model evidence, monitoring and analyst usability are first-class parts of the design rather than afterthoughts.</div>

## 1. Architecture

The architecture connects the machine-learning lifecycle to the operational security lifecycle. Data is ingested and validated, the training pipeline is reproducible with DVC, experiments are tracked with MLflow, the selected model is served through FastAPI, and production-style signals are exposed to Prometheus and Grafana. Airflow orchestrates the workflow while Streamlit gives the analyst a separate interface for triage and evidence review.

<figure class="case-evidence"><img src="https://raw.githubusercontent.com/Fadi-AICH/cyberguard-mlops/main/screenshots/architecture.jpeg" alt="CyberGuard MLOps architecture"><figcaption><strong>System architecture.</strong> The project links the ML lifecycle—data, training and registry—to API serving, monitoring, orchestration and analyst-facing security operations.</figcaption></figure>

## 2. Data ingestion and validation

The project uses a reproducible sample from the public **CICIoT2023** IoT intrusion-detection dataset rather than claiming results on the complete benchmark. The ingestion stage creates the local dataset used by the rest of the pipeline, then validation checks confirm that the expected schema and basic data assumptions hold before training.

Data-quality work includes schema validation and Great Expectations artifacts. This is important because a model pipeline should fail visibly when the data contract changes instead of silently training on malformed input.

<figure class="case-evidence"><img src="https://raw.githubusercontent.com/Fadi-AICH/cyberguard-mlops/main/screenshots/02_ciciot2023_ingestion_validation.png" alt="CICIoT2023 ingestion and validation"><figcaption><strong>Dataset ingestion and validation.</strong> The pipeline verifies the data before model training so later metrics can be traced to a known input state.</figcaption></figure>

## 3. Reproducibility with DVC

DVC is used to make the sequence of data preparation, validation, training and reporting reproducible. Instead of manually running unrelated scripts, the project exposes a dependency graph and versioned metrics that can be regenerated with `dvc repro`.

This provides three useful properties:

- changes in data or code can trigger the appropriate downstream stages;
- model results are tied to the versioned pipeline state;
- another run can reproduce the same sequence instead of relying on a one-off notebook session.

<figure class="case-evidence"><img src="https://raw.githubusercontent.com/Fadi-AICH/cyberguard-mlops/main/screenshots/04_dvc_pipeline_ciciot2023.png" alt="DVC pipeline"><figcaption><strong>DVC pipeline evidence.</strong> Training is part of an explicit reproducible workflow rather than a standalone command with no dependency tracking.</figcaption></figure>

## 4. Model training and comparison

Three classical supervised models were compared on the project sample: Logistic Regression, Random Forest and Gradient Boosting. The final model was selected by F1-score.

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.835 | 1.000 | 0.804 | 0.892 | 0.938 |
| Random Forest | 0.891 | 0.982 | 0.887 | 0.932 | 0.961 |
| **Gradient Boosting** | **0.903** | **0.962** | **0.921** | **0.941** | **0.956** |

Gradient Boosting was selected because its F1 of **0.941** provided the best balance on the project sample. I keep the wording deliberately narrow: these are project-sample results, not a claim that the model establishes a new CICIoT2023 benchmark.

<figure class="case-evidence"><img src="https://raw.githubusercontent.com/Fadi-AICH/cyberguard-mlops/main/screenshots/03_training_metrics_ciciot2023.png" alt="CyberGuard training metrics"><figcaption><strong>Training metrics.</strong> Several models are evaluated before the selected model is promoted into the serving workflow.</figcaption></figure>

## 5. Experiment tracking and model registry

MLflow records experiments, metrics and model artifacts. That gives a direct audit trail between a training run and the model that is eventually served.

The registry layer matters because the API should not depend on an unexplained `.pkl` file copied into a folder. A registered model carries experiment context and makes the relationship between training and serving easier to inspect.

<div class="case-grid">
<figure class="case-evidence"><img src="https://raw.githubusercontent.com/Fadi-AICH/cyberguard-mlops/main/screenshots/06_mlflow_registry_ciciot2023.png" alt="MLflow registry"><figcaption>MLflow model registry.</figcaption></figure>
<figure class="case-evidence"><img src="https://raw.githubusercontent.com/Fadi-AICH/cyberguard-mlops/main/screenshots/22_mlflow_run_details_metrics_artifacts.png" alt="MLflow run details"><figcaption>Run-level metrics and artifacts used as model evidence.</figcaption></figure>
</div>

## 6. Serving with FastAPI

The selected model is exposed through a FastAPI service. The API separates inference from the training code and provides a documented interface that other services can call.

The serving layer also exports Prometheus metrics so inference is observable instead of becoming a black box. That allows the monitoring layer to track API and prediction behavior while the model is exercised by replayed traffic.

<div class="case-grid">
<figure class="case-evidence"><img src="https://raw.githubusercontent.com/Fadi-AICH/cyberguard-mlops/main/screenshots/07_fastapi_docs_ciciot2023.png" alt="FastAPI documentation"><figcaption>FastAPI Swagger documentation for the inference service.</figcaption></figure>
<figure class="case-evidence"><img src="https://raw.githubusercontent.com/Fadi-AICH/cyberguard-mlops/main/screenshots/08_prediction_response.png" alt="Prediction response"><figcaption>Example model-inference response generated by the API.</figcaption></figure>
</div>

## 7. Containerized platform

Docker Compose brings the project components together as one local platform. The stack includes MLflow, the FastAPI model service, Prometheus, Grafana, Airflow, the Streamlit SOC UI and a traffic-replay service.

This makes the project closer to a real system integration exercise: services have separate responsibilities and communicate through explicit interfaces rather than everything running inside one Python process.

<figure class="case-evidence"><img src="https://raw.githubusercontent.com/Fadi-AICH/cyberguard-mlops/main/screenshots/09_docker_services-desktop.png" alt="CyberGuard Docker services"><figcaption><strong>Containerized service stack.</strong> Each part of the MLOps/SOC workflow runs as a separate service under Docker Compose.</figcaption></figure>

## 8. Prometheus and Grafana monitoring

Prometheus collects metrics from the serving layer. Grafana turns those metrics and security-enrichment signals into a SOC-style dashboard with operational and analyst-oriented views.

The dashboard includes signals such as attack ratio, latency, source-country enrichment, severity and server-flow views. These contextual fields are used for monitoring and triage; the project explicitly does **not** use country, source IP, destination server or severity as model-training features.

<div class="case-grid">
<figure class="case-evidence"><img src="https://raw.githubusercontent.com/Fadi-AICH/cyberguard-mlops/main/screenshots/10_prometheus_targets.png" alt="Prometheus targets"><figcaption>Prometheus confirms the monitored targets are reachable.</figcaption></figure>
<figure class="case-evidence"><img src="https://raw.githubusercontent.com/Fadi-AICH/cyberguard-mlops/main/screenshots/11_grafana_soc_dashboard.png" alt="Grafana SOC dashboard"><figcaption>Grafana SOC command-center view populated by replayed inference traffic.</figcaption></figure>
</div>

A `traffic-replay` service periodically sends CICIoT2023 rows to the API. This gives the monitoring layer continuous activity during demonstrations instead of showing a static dashboard with manually fabricated values.

## 9. Drift and security reporting

The project produces an Evidently drift report to inspect changes in the data presented to the system. Drift monitoring is important in security ML because the input distribution can evolve even when the application code remains unchanged.

It also produces a SOC-oriented threat report so model output can be translated into information that is easier for an analyst to review.

<div class="case-grid">
<figure class="case-evidence"><img src="https://raw.githubusercontent.com/Fadi-AICH/cyberguard-mlops/main/screenshots/12_evidently_drift_html.png" alt="Evidently drift report"><figcaption>Evidently drift analysis for model-input monitoring.</figcaption></figure>
<figure class="case-evidence"><img src="https://raw.githubusercontent.com/Fadi-AICH/cyberguard-mlops/main/screenshots/13_soc_threat_report_html.png" alt="SOC threat report"><figcaption>SOC-oriented report generated from the project outputs.</figcaption></figure>
</div>

## 10. Airflow orchestration

Airflow orchestrates the multi-stage workflow. This separates scheduling and dependency management from the individual Python components and makes the pipeline state visible through a DAG rather than hidden in a long shell script.

<div class="case-grid">
<figure class="case-evidence"><img src="https://raw.githubusercontent.com/Fadi-AICH/cyberguard-mlops/main/screenshots/21_airflow_dag_graph_view.png" alt="Airflow DAG graph"><figcaption>Airflow graph view showing the workflow dependency structure.</figcaption></figure>
<figure class="case-evidence"><img src="https://raw.githubusercontent.com/Fadi-AICH/cyberguard-mlops/main/screenshots/14_airflow_dag_success.png" alt="Airflow DAG success"><figcaption>Successful orchestrated workflow run.</figcaption></figure>
</div>

## 11. SOC analyst workbench

The Streamlit application is deliberately separate from Grafana. Grafana is useful for monitoring and operational dashboards; Streamlit is used as an analyst workbench for triage, live scoring, model evidence and incident-note export.

<figure class="case-evidence"><img src="https://raw.githubusercontent.com/Fadi-AICH/cyberguard-mlops/main/screenshots/16_streamlit_soc_analyst_ui.png" alt="Streamlit SOC analyst UI"><figcaption><strong>SOC analyst interface.</strong> The analyst gets a workflow-oriented view rather than only raw model predictions.</figcaption></figure>

<div class="case-grid">
<figure class="case-evidence"><img src="https://raw.githubusercontent.com/Fadi-AICH/cyberguard-mlops/main/screenshots/17_streamlit_live_scoring_case_export.png" alt="Live scoring and case export"><figcaption>Live scoring and incident/case export workflow.</figcaption></figure>
<figure class="case-evidence"><img src="https://raw.githubusercontent.com/Fadi-AICH/cyberguard-mlops/main/screenshots/19_streamlit_ModelEvidence.png" alt="Model evidence"><figcaption>Model-evidence view that exposes the reasoning artifacts around a prediction.</figcaption></figure>
</div>

## 12. Code quality and CI/CD

The repository includes automated checks rather than relying on manual testing before a commit. The documented quality pipeline covers:

- `pytest` for tests;
- Black formatting checks;
- isort import ordering;
- Ruff linting;
- mypy type checking;
- Docker build validation through GitHub Actions.

<figure class="case-evidence"><img src="https://raw.githubusercontent.com/Fadi-AICH/cyberguard-mlops/main/screenshots/15_github_repo_actions.png" alt="GitHub Actions"><figcaption><strong>CI evidence.</strong> Automated checks help keep the ML and serving code reproducible as the project evolves.</figcaption></figure>

## 13. What this project demonstrates

CyberGuard brings several engineering disciplines together:

- reproducible data and model workflows;
- data-quality checks;
- supervised model comparison;
- experiment tracking and model registry;
- API-based model serving;
- metrics and dashboard monitoring;
- drift reporting;
- containerized multi-service deployment;
- workflow orchestration;
- analyst-facing security tooling;
- automated code-quality checks.

## 14. Limitations

<div class="case-warning"><strong>Scope boundary:</strong> the repository uses a reproducible CICIoT2023 sample for an educational MLOps demonstration, not the full benchmark dataset. The model metrics therefore describe this project sample and should not be presented as general production performance.</div>

A production version would need a much larger and continuously refreshed dataset, production feature contracts, authentication and authorization around services, managed secrets, stronger model-governance controls, persistent infrastructure, longer-term drift baselines and a defined analyst feedback loop.

<div class="case-actions"><a href="https://github.com/Fadi-AICH/cyberguard-mlops" target="_blank">GitHub repository ↗</a><a href="{{ '/projects/' | relative_url }}">All projects</a></div>
