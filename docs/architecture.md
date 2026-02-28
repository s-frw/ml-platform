ML Platform Architecture
1. Overview

This repository defines a GitOps ML platform deployed on Kubernetes.
All infrastructure and ML components are declaratively managed and continuously reconciled from Git.

The platform follows the App-of-Apps GitOps model using Argo CD to synchronize cluster state from this repository.

Core Capabilities

GitOps infrastructure management

ML experiment tracking

Artifact storage

GPU-aware training workloads

Full observability stack

Declarative environment configuration

2. High level architecture
Git Repository
      │
      ▼
ArgoCD (App-of-Apps)
      │
      ▼
Kubernetes Cluster
      │
      ├── MLflow ───────────────► PostgreSQL (metadata backend)
      │        │
      │        └───────────────► MinIO (artifact storage)
      │
      ├── Training Jobs (CPU/GPU)
      │
      ├── Observability Stack
      │       ├── Prometheus
      │       └── Grafana
      │
      └── Networking (Cilium CNI)

3. GitOps Model

The platform uses:

Argo CD App-of-Apps pattern (applications/root-app.yaml)

Kustomize overlays.

Declarative environment structure:

Changes are pushed to Git.

ArgoCD detects repository updates.

Desired state is reconciled.

Kubernetes resources are applied automatically.


4. Core Components

4.1 MLflow

Experiment tracking is handled by MLflow.

Deployment path:

platform/ml/mlflow/

Configuration:

Backend store: PostgreSQL

Artifact store: MinIO


4.2 Artifact Storage (MinIO)

Artifacts are stored in MinIO.

Location:

platform/ml/minio/


4.3 Metadata Backend (PostgreSQL)

Experiment metadata is stored in PostgreSQL.

Location:

platform/data/postgres/


4.4 Training Workloads

Training jobs are defined in:

ml/training/job.yaml

Containers are built via:

ml/training/Dockerfile


4.5 GPU Enablement

GPU scheduling is enabled through:

NVIDIA device plugin

Node labeling (clusters/base/node-labels.yaml)

Hybrid CPU/GPU execution model.


4.6 Observability Stack

Monitoring stack includes:

Prometheus

Grafana

Location:

platform/observability/


4.7 Networking

Cluster networking is powered by Cilium.

Location:

platform/networking/


5. Environment Structure

Cluster configuration is organized under:

clusters/

Designed for future expansion:

base/

dev/

prod/


