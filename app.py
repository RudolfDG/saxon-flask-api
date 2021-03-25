from flask import Flask, abort, jsonify, request
import saxonc
import os
app = Flask(__name__)

cache = {
    "processor": saxonc.PySaxonProcessor(license=False)
}

@app.route("/transform/", methods=["POST"])
def transform():
    data = request.data

    result = transform_xml(data)

    return result

def transform_xml(xml: bytes) -> str:
    processor = cache["processor"]

    base_dir = os.getcwd()
    xslt_path = os.path.join(base_dir, "test.xslt")

    xslt_proc = processor.new_xslt30_processor()

    node = processor.parse_xml(xml_text=xml.decode("utf-8"))

    result = xslt_proc.transform_to_string(stylesheet_file=xslt_path, xdm_node=node)
    
    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0")