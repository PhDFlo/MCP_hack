import gradio as gr
import molviewspec as mvs
from gradio_molecule3d import Molecule3D
import os

def plot_molecule(pdb_id: str):
    """Plot a molecular structure from a CIF file using MolViewSpec.

    Args:
        pdb_id (str): The name of the CIF file to load. If the .cif extension is missing,
                      it will be automatically added. The file should be present in the
                      ./cif_files directory.

    Raises:
        FileNotFoundError: If the specified CIF file does not exist in the cif_files directory.

    Returns:
        molviewspec.Structure: A molecular structure visualization with default coloring for
                             polymer components and blue coloring for ligands.
    """
    if not pdb_id.endswith('.cif'):
        pdb_id += '.cif'
    if not os.path.exists(os.path.join("./cif_files", pdb_id)):
        raise FileNotFoundError(f"File {pdb_id} does not exist in the cif_files directory.")


    with open(os.path.join("./cif_files",pdb_id)) as f:
        cif_data = f.read()

    builder = mvs.create_builder()

    structure = builder.download(url='local.cif').parse(format='mmcif').model_structure()
    structure.component(selector="polymer").representation().color(custom=dict(molstar_use_default_coloring=True))
    structure.component(selector="ligand").representation().color(color="blue")


    builder.get_molstar_html(cif_data)
    #builder.molstar_streamlit(data={'local.cif': cif_data}, width=500, height=400)

#pdb_id = st.text_input("file name", value="6vjj.cif")

# Create a standard Gradio interface
demo = gr.Interface(
    fn=plot_molecule,
    inputs=gr.Text(label="CIF File Name (without .cif extension)", placeholder="Enter CIF file name"),
    outputs=gr.HTML(label="Molecular Structure Visualization"),
    title="Mol* Custom Component",
    description="Enter a CIF file name (without .cif extension) to visualize the molecular structure.",
)

# Launch both the Gradio web interface and the MCP server
if __name__ == "__main__":
    demo.launch(mcp_server=True)