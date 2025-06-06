import streamlit as st
import molviewspec as mvs
import os

st.header("Mol* Custom Component")

pdb_id = st.text_input("file name", value="6vjj.cif")

with open(os.path.join("./cif_files",pdb_id)) as f:
    cif_data = f.read()

builder = mvs.create_builder()

#structure = builder.download(url=f'https://files.wwpdb.org/download/{pdb_id}.cif').parse(format='mmcif').model_structure()
structure = builder.download(url='local.cif').parse(format='mmcif').model_structure()

structure.component(selector="polymer").representation().color(custom=dict(molstar_use_default_coloring=True))

structure.component(selector="ligand").representation().color(color="blue")

#print(builder.get_state())

#builder.molstar_streamlit()
builder.molstar_gradio(data={'local.cif': cif_data}, width=500, height=400)