
import gradio as gr
from shutil import copyfile


## Modify to match format username-spacename
## Only works for hosted spaces on Huggingface, for local spaces or spaces hosted on Colab you need to use the gradio.live url with share=True as described in the last two lines
public_link = "https://simonduerr-molstar-gradio.hf.space"


import gradio as gr
import os

def get_pdb(upload_choice="PDB Code", pdb_code="", filepath=""):
    urls = {
        "PDB Code": {"base":"https://files.rcsb.org/view/", "suffix":".pdb"}, 
        "AlphaFold DB": {"base":"https://alphafold.ebi.ac.uk/files/AF-", "suffix": "-F1-model_v4.pdb"}, 
        "ESM Atlas": {"base": "https://api.esmatlas.com/fetchPredictedStructure/", "suffix":".pdb"}
    }
    if upload_choice=="local file":
        try:
            #move file to home folder to have it accessible from the web
            copyfile(filepath.name, os.path.join(os.getcwd(), os.path.basename(filepath.name)))
            return os.path.join(os.getcwd(), os.path.basename(filepath.name))  
        except AttributeError as e:
            return None
    else:
        os.system(f"wget -qnc {urls[upload_choice]['base']}{pdb_code}{urls[upload_choice]['suffix']}")
        return f"{pdb_code}{urls[upload_choice]['suffix']}"


def read_mol(molpath):
    with open(molpath, "r") as fp:
        lines = fp.readlines()
    mol = ""
    for l in lines:
        mol += l
    return mol


def molecule(input_pdb, public_link):

    print(input_pdb)
    print(public_link+'/file='+os.path.basename(input_pdb))
    link = public_link+"/file="+os.path.basename(input_pdb)
    x ="""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">
    <title>PDBe Molstar - Helper functions</title>
    <!-- Molstar CSS & JS -->
    <link rel="stylesheet" type="text/css" href="https://www.ebi.ac.uk/pdbe/pdb-component-library/css/pdbe-molstar-light-3.1.0.css">
    <script type="text/javascript" src="https://www.ebi.ac.uk/pdbe/pdb-component-library/js/pdbe-molstar-plugin-3.1.0.js"></script>
    <style>
      * {
          margin: 0;
          padding: 0;
          box-sizing: border-box;
      }
      .msp-plugin ::-webkit-scrollbar-thumb {
          background-color: #474748 !important;
      }
      .viewerSection {
        margin: 120px 0 0 0px;
      }
      #myViewer{
        float:left;
        width:100%;
        height: 600px;
        position:relative;
      }
    </style>
  </head>
  <body>
    <div class="viewerSection">
      <!-- Molstar container -->
      <div id="myViewer"></div>
      
    </div>
    <script>
      //Create plugin instance
      var viewerInstance = new PDBeMolstarPlugin();
  
      //Set options (Checkout available options list in the documentation)
      var options = {
        customData: {
          url: \""""+link+"""\",
          format: "pdb"
        },
        alphafoldView: true,
        bgColor: {r:255, g:255, b:255},
        //hideCanvasControls: ["selection", "animation", "controlToggle", "controlInfo"]
      }
      
      //Get element from HTML/Template to place the viewer 
      var viewerContainer = document.getElementById("myViewer");
  
      //Call render method to display the 3D view
      viewerInstance.render(viewerContainer, options);
      
    </script>
  </body>
</html>"""
    
    return f"""<iframe style="width: 100%; height: 720px" name="result" allow="midi; geolocation; microphone; camera; 
    display-capture; encrypted-media;" sandbox="allow-modals allow-forms 
    allow-scripts allow-same-origin allow-popups 
    allow-top-navigation-by-user-activation allow-downloads" allowfullscreen="" 
    allowpaymentrequest="" frameborder="0" srcdoc='{x}'></iframe>"""


def update(upload_choice, inp, file, public_link):
    pdb_path = get_pdb(upload_choice, inp, file)
    return molecule(pdb_path, public_link)

def toggle_upload_input(choice):
    if choice != "local file":
        return gr.update(visible=True, placeholder=choice), gr.update(visible=False, value=None)
    elif choice == "local file":
        return gr.update(visible=False), gr.update(visible=True, value=None)

        

demo = gr.Blocks()

with demo:
    gr.Markdown("# PDB viewer using Mol*")
    gr.Markdown("""If using please cite 
    > David Sehnal, Sebastian Bittrich, Mandar Deshpande, Radka Svobodová, Karel Berka, Václav Bazgier, Sameer Velankar, Stephen K Burley, Jaroslav Koča, Alexander S Rose: Mol* Viewer: modern web app for 3D visualization and analysis of large biomolecular structures, Nucleic Acids Research, 2021; 10.1093/nar/gkab31.""")
    public_link = gr.State(value=public_link)
    with gr.Row():
        with gr.Group():
            upload_choice = gr.Radio(["PDB Code", "AlphaFold DB", "ESM Atlas","local file"], label="File source", value='PDB Code')
            inp = gr.Textbox(
                placeholder="PDB Code", label="Input structure"
            )
            file = gr.File(file_count="single", visible=False)
            upload_choice.change(fn=toggle_upload_input,
                                    inputs=[upload_choice],
                                    outputs=[inp, file],
                                    queue=False)

            
            btn = gr.Button("View structure")
    gr.Examples([["PDB Code", "2CBA"],["AlphaFold DB", "A0A1U8FD60"], ["ESM Atlas", "MGYP001531319262"]], [upload_choice,inp])
    mol = gr.HTML()
    btn.click(fn=update, inputs=[upload_choice, inp, file, public_link], outputs=mol)
_, _, pl = demo.launch()  # use public link with share=True locally and uncomment below
#public_link = pl
