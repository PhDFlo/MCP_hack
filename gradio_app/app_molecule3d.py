import gradio as gr
from gradio_molecule3d import Molecule3D
import gemmi

# prediction routine
def convert_cif_to_pdb(cif_name):
    print(cif_name.split('.cif')[0])
    pdb_name = cif_name.split('.cif')[0] + '.pdb'
    st = gemmi.read_structure(cif_name)
    st.write_minimal_pdb(pdb_name)
    return pdb_name

reps = [{"model": 0,"style": "cartoon","color": "whiteCarbon"}]

with gr.Blocks() as demo:
    inp = gr.Textbox(placeholder="Molecule file path", label="Input CIF file")
    btn = gr.Button("Run")
    out = Molecule3D(label="Molecule3D", reps=reps)
    btn.click(fn=convert_cif_to_pdb, inputs=[inp], outputs=[out])

demo.launch(ssr_mode=False)