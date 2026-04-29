# AI Agents

Collection of small example agent projects used for experiments and interviews.

## Overview

This workspace contains three simple Python agent examples:

- `customer_support_agent` - basic customer support agent prototype.
- `my_first_agent` - an introductory example agent (includes `new_agent.yaml`).
- `product_extractor` - extracts product information (current file: `agent.py`).

## Repository Structure

- `customer_support_agent/`
  - `agent.py`
- `my_first_agent/`
  - `agent.py`
  - `new_agent.yaml`
- `product_extractor/`
  - `agent.py`

## Requirements

- Python 3.8 or newer
- Any additional dependencies required by individual agents should be listed in a `requirements.txt` in the corresponding folder (none provided by default).

## Setup

Create and activate a virtual environment, then install dependencies if present:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

# Install dependencies if a requirements file exists
pip install -r requirements.txt
```

## Running an agent

You can run an agent module directly. From the workspace root, for example:

```bash
# Run the product_extractor agent
python -m product_extractor.agent

# Or run a specific script file
python product_extractor/agent.py
```

Replace `product_extractor` with `customer_support_agent` or `my_first_agent` to run those examples.

## Configuration

Some agents may include YAML or other config files (for example `my_first_agent/new_agent.yaml`). Edit those files to adjust agent behavior.

## Contributing

If you add dependencies, please add a `requirements.txt` to the relevant folder and update this README with any special run instructions.

## Notes

This is a small example workspace intended for experimentation. If you want, I can:

- Add a top-level `requirements.txt` capturing common dependencies.
- Add simple runner scripts to start each agent.

