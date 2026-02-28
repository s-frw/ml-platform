ML Platform Architecture

1. Overview

This repository defines a GitOps-driven ML platform deployed on Kubernetes.
All infrastructure and ML components are declaratively managed and continuously reconciled from Git.

The platform follows the App-of-Apps GitOps model using Argo CD to synchronize cluster state from this repository.

Core Capabilities

GitOps-based infrastructure management

ML experiment tracking and model lifecycle management

Artifact storage with S3-compatible backend

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

Kustomize overlays

Declarative environment structure

Operational flow:

Changes are pushed to Git.

ArgoCD detects repository updates.

Desired state is compared with the live cluster state.

Drift is reconciled automatically.

Kubernetes resources are applied to converge the cluster to the declared state.


4. Core Components

4.1 MLflow

Experiment tracking and model lifecycle management is handled by MLflow.

Deployment path:

platform/ml/mlflow/

Configuration:

Backend store: PostgreSQL

Artifact store: MinIO


4.2 Artifact Storage (MinIO)

Artifacts are stored in MinIO, providing S3-compatible object storage.

Location:

platform/ml/minio/


4.3 Metadata Backend (PostgreSQL)

Experiment metadata and model registry information are stored in PostgreSQL.

Location:

platform/data/postgres/


4.4 Training Workloads

Training jobs are defined in:

ml/training/job.yaml

Containers are built via:

ml/training/Dockerfile

Workloads support CPU and GPU execution depending on node scheduling and available resources.


4.5 GPU Enablement

GPU scheduling is enabled through:

NVIDIA device plugin

Node labeling (clusters/base/node-labels.yaml)

This enables explicit GPU resource requests and hybrid CPU/GPU execution.


4.6 Observability Stack

Monitoring stack includes:

Prometheus (metrics collection)

Grafana (visualization and dashboards)

Location:

platform/observability/


4.7 Networking

Cluster networking is powered by Cilium CNI.

Location:

platform/networking/


5. Environment Structure

Cluster configuration is organized under:

clusters/

Designed for future expansion into multiple environments:

base/

dev/

prod/
