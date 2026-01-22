# GPU Accelerated Kubernetes Machine Learning Platform
Machine Learning platform with NVIDIA 3050. 

## Hardware
Control Plane: 
  - 
GPU worker node:
  - 8 CPUs i3-10105F @ 3.70 GHz
  - NVIDIA GeForce 3050 8GB VRAM
  - RAM 24 Gb

## Core Platform
 - Ubuntu Server 22.04 LTS
 - Kubeadm
 - Containerd
 - Cilium (eBPF CNI)

## GPU & ML
 - NVIDIA GPU Operator
 - vLLM

## MLOps
 - Argo Workflows
 - MLFlow
 - MinIO

## GitOps & Observability
 - ArgoCD
 - Prometheus & Grafana
