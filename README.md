# RAG_Project

This project implements a Retrieval-Augmented Generation (RAG) system designed to assist with code generation and software development tasks. The system takes user requests and extracts relevant information from various sources such as PDFs, GitHub repositories, and project source files. This extracted data provides context to large language models (LLMs), enabling them to generate code, build websites, or complete other software-related tasks with increased accuracy and relevance.

By integrating RAG, this project helps enhance the LLM's capabilities by retrieving precise information required to fulfill complex development requests.

## Requirements

- Python 3.11 or later

#### Install Python using MiniConda

1) Download and install MiniConda from [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install)
2) Create a new environment using the following command:
```bash
$ conda create -n rag_project python=3.11
```
3) Activate the environment:
```bash
$ conda activate rag_project
```

## Installation

### Install the required packages

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```

Set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value.

## Run the FastAPI server

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```