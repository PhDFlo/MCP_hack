import gradio as gr
import os

def get_pdb(pdb_code="", filepath=""):
    if pdb_code is None or len(pdb_code) != 4:
        try:
            return filepath.name
        except AttributeError as e:
            return None
    else:
        os.system(f"wget -qnc https://files.rcsb.org/view/{pdb_code}.pdb")
        return f"{pdb_code}.pdb"
    
def get_cfi(cfi_code="", filepath=""):
    if cfi_code is None or len(cfi_code) != 4:
        try:
            return filepath.name
        except AttributeError as e:
            return None
    else:
        os.system(f"wget -qnc https://files.rcsb.org/view/{cfi_code}.cfi")
        return f"{cfi_code}.cfi"
    
def molecule(input_pdb):
    mol = read_mol(input_pdb)
    # setup HTML document
    x = ("""<!DOCTYPE html><html> [..] </html>""") # do not use ' in this input
    return f"""<iframe  [..] srcdoc='{x}'></iframe>"""

def update(inp, file):
    # in this simple example we just retrieve the pdb file using its identifier from the RCSB or display the uploaded file
    pdb_path = get_cfi(inp, file)
    return molecule(pdb_path) # this returns an iframe with our viewer
    
    
## Create a Gradio Blocks app
demo = gr.Blocks()

with demo:
    gr.Markdown("# CFI viewer using 3Dmol.js")
    with gr.Row():
        with gr.Group():
            inp = gr.Textbox(
                placeholder="CFI Code or upload file below", label="Input structure"
            )
            file = gr.File(file_count="single")
            btn = gr.Button("View structure")
        mol = gr.HTML()
    btn.click(fn=update, inputs=[inp, file], outputs=mol)
demo.launch()