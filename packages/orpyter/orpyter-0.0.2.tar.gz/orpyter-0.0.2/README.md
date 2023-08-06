<!-- markdownlint-disable MD033 MD041 -->
<h1 align="center">
    Orpyter
</h1>

<p align="center">
    <strong>Yet another tool to turn your Python functions into microservices with web API, interactive GUI, and more.</strong>
</p>

<p align="center">
    <a href="https://pypi.org/project/orpyter/" title="PyPi Version"><img src="https://img.shields.io/pypi/v/orpyter?color=green&style=flat"></a>
    <a href="https://pypi.org/project/orpyter/" title="Python Version"><img src="https://img.shields.io/badge/Python-3.6%2B-blue&style=flat"></a>
    <a href="https://github.com/weanalyze/orpyter/blob/main/LICENSE" title="Project License"><img src="https://img.shields.io/badge/License-MIT-green.svg"></a>
    <a href="https://github.com/weanalyze/orpyter/actions?query=workflow%3Abuild-pipeline" title="Build status"><img src="https://img.shields.io/github/workflow/status/weanalyze/orpyter/build-pipeline?style=flat"></a>
</p>

<p align="center">
  <a href="#getting-started">Getting Started</a> •
  <a href="#license">License</a> •
  <a href="https://github.com/weanalyze/orpyter/releases">Changelog</a>
</p>

Instantly turn your Python functions into production-ready microservices. Deploy and access your services via HTTP API or interactive UI. Seamlessly export your services into portable, shareable, and executable files or Docker images. orpyter builds on open standards - OpenAPI,  JSON Schema, and Python type hints - and is powered by FastAPI, Streamlit, and Pydantic. It cuts out all the pain for productizing and sharing your Python code - or anything you can wrap into a single Python function.

<sup>Pre-alpha Version: Not feature-complete and only suggested for experimental usage.</sup>

<img align="center" style="width: 80%" src="https://github.com/weanalyze/orpyter/blob/main/docs/images/orpyter-header.png?raw=true"/>

---

## Highlights

- 🪄&nbsp; Turn functions into production-ready services within seconds.
- 🔌&nbsp; Auto-generated HTTP API based on FastAPI.
- 🌅&nbsp; Auto-generated Web UI based on Streamlit.
- 📦&nbsp; Save and share as self-contained executable file or Docker image.
- 🧩&nbsp; Reuse pre-defined components & combine with existing Opyrators.
- 📈&nbsp; Instantly deploy and scale for production usage.

## Getting Started

### Installation

> _Requirements: Python 3.6+._

```bash
pip install orpyter
```

### Usage

1. A simple orpyter-compatible function could look like this:

    ```python
    from pydantic import BaseModel

    class Input(BaseModel):
        message: str

    class Output(BaseModel):
        message: str

    def hello_world(input: Input) -> Output:
        """Returns the `message` of the input data."""
        return Output(message=input.message)
    ```

    _💡 An orpyter-compatible function is required to have an `input` parameter and return value based on [Pydantic models](https://pydantic-docs.helpmanual.io/). The input and output models are specified via [type hints](https://docs.python.org/3/library/typing.html)._

2. Copy this code to a file, e.g. `my_orpyter.py`
3. Run the UI server from command-line:

    ```bash
    orpyter launch-ui my_orpyter:hello_world
    ```

    _In the output, there's a line that shows where your web app is being served, on your local machine._

    <img style="width: 100%" src="https://github.com/weanalyze/orpyter/blob/main/docs/images/orpyter-hello-world-ui.png?raw=true"/>

4. Run the HTTP API server from command-line:

    ```bash
    orpyter launch-api my_orpyter:hello_world
    ```
    _In the output, there's a line that shows where your web service is being served, on your local machine._

    <img style="width: 100%" src="https://github.com/weanalyze/orpyter/blob/main/docs/images/orpyter-hello-world-api.png?raw=true"/>

5. Find out more usage information in the [Features](#features) section or get inspired by our [examples](#examples).

## License

MIT License.

This project is originated from [Opyrator](https://github.com/ml-tooling/opyrator), by updating outdated dependencies and fixing minor issues.
