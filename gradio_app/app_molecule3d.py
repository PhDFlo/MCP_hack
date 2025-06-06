import gradio as gr
from gradio_molecule3d import Molecule3D

# prediction routine
def predict(x):
    return x

reps = [{"model": 0,"style": "cartoon","color": "whiteCarbon"}]

Molecule3D(label="Molecule3D", reps=reps)

with gr.Blocks() as demo:
    inp = gr.Textbox(placeholder="Molecule name")#Molecule3D(label="Molecule3D", reps=reps)
    btn = gr.Button("Run")
    out = Molecule3D(label="Molecule3D", reps=reps)
    btn.click(fn=predict, inputs=[inp], outputs=[out])

demo.launch(ssr_mode=False)