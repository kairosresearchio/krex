# Development environment setup

## Installation

1. Download uv [Official Documentation](https://docs.astral.sh/uv/getting-started/installation/)
2. Create a virtual environment:
   ```sh
   uv venv
   ```
3. Activate the virtual environment:
   - **Windows**:
     ```sh
     .venv\Scripts\activate
     ```
   - **Mac/Linux**:
     ```sh
     source .venv/bin/activate
     ```
4. Install dependencies:
   ```sh
   uv sync
   ```
5. Run the project:
   ```sh
   uv run ooo.py
   ```

6. Run pre commit checks on all files:
   ```sh
   pre-commit run --all-files
   ```
