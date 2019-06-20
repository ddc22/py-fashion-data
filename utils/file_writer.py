
xml_header = """
<Batch>"""
xml_footer = """
</Batch>"""


def write_config(file_name, xml_array):
    xml_dump = "\n".join(xml_array)
    tf = open("configs/" + file_name, "w")
    tf.truncate()
    tf.close()
    text_file = open("configs/" + file_name, "a")

    text_file.write(xml_header)
    text_file.write(xml_dump)
    text_file.write(xml_footer)
    text_file.close()
