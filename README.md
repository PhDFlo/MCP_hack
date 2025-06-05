# MCP_hack

This project is a collection of tools and experiments for molecular structure prediction and visualization using various AI and computational methods.

## Project Structure

The project consists of four main components:

### 1. Chai1 Test (`chai1_test/`)
A Python module for molecular structure prediction using the Chai model. This component:
- Processes molecular structure data
- Performs predictions using pre-trained models
- Generates CIF files for structural visualization
- Uses configuration files for model parameters and inference settings

### 2. Modal Test (`modal_test/`)
A test implementation using Modal.com for cloud computation:
- Provides serverless computation capabilities
- Includes utility functions for numerical operations
- Demonstrates Modal.com integration patterns

### 3. Molecular Visualization Notebooks (`notebooks_molviewspec/`)
Jupyter notebooks for molecular structure visualization:
- Contains example notebooks for structure visualization
- Includes sample data (1CBS protein structure)
- Demonstrates various visualization techniques and annotations
- Uses common molecular structure file formats (CIF, BCIF)

### 4. Streamlit Interface (`streamlit_test/`)
A web interface built with Streamlit for:
- Interactive molecular structure visualization
- File upload and processing
- Results visualization and analysis

## Setup and Installation

Each component has its own `pyproject.toml` file for dependency management. To set up any component:

1. Navigate to the component directory
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   ```
3. Install dependencies:
   ```bash
   pip install -e .
   ```

## Usage

Please refer to the README files in each component directory for specific usage instructions and examples.

## File Structure
```
.
├── chai1_test/          # Molecular structure prediction
├── modal_test/          # Cloud computation integration
├── notebooks_molviewspec/ # Visualization notebooks
└── streamlit_test/      # Web interface
```

## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository.

## License

[Your chosen license]
