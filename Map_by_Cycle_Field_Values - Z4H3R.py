import os
field_name = 'your_field_name' # - Name of the field you want to cycle.
layoutName = "your_print_layout_name" # - Name of the Print Layout you want to use.
png_path = r'your_path' # - Path where you want to save the .png files.
png_name_template = "your_file_name - {}.png" # - Name of the .png file. Use "{}" where you want the field_value inserted in the file name.
label_name = layout.itemById("your_print_layout_ID") # - ID of the label in Print Layout you want to show the unique value beeing mapped. You must first set it in the Layout you want to use.
project = QgsProject.instance()
layer = iface.activeLayer()
field_index = layer.fields().indexFromName(field_name)
values_list = layer.uniqueValues(field_index)
manager = project.layoutManager()
layout = manager.layoutByName(layoutName)
exporter = QgsLayoutExporter(layout)
for field_value in values_list:
    subset_str = "'" + str(field_value)+"'"+'LIKE '+ '"' + field_name + '"'
    layer.setSubsetString(subset_str)
    pngName = png_name_template.format(field_value)
    dest_file = os.path.join(png_path, pngName)
    label_name.setText(field_value)
    exporter.exportToImage(dest_file, QgsLayoutExporter.ImageExportSettings())
    layer.setSubsetString('')
print("DONE")
