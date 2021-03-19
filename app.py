from flask import Flask, abort, jsonify, request
import saxonc
import os
app = Flask(__name__)

@app.route("/transform/", methods=["POST"])
def transform():
    data = request.data

    result = transform_xml(data)

    return result

def transform_xml(xml: bytes) -> str:
    with saxonc.PySaxonProcessor(license=False) as proc:
        base_dir = os.getcwd()
        xslt_path = os.path.join(base_dir, "test.xslt")

        xslt_proc = proc.new_xslt30_processor()

        node = proc.parse_xml(xml_text=xml.decode("utf-8"))

        result = xslt_proc.transform_to_string(stylesheet_file=xslt_path, xdm_node=node)
        
        return result