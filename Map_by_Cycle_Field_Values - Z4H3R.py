field_name = '"your_field_name"' # - Name of the field you want to cycle.
field_index =  # - Index of the field you want to cycle. You find it in: Layer properties -> Fields
layoutName = "your_layout_name" # - Name of the Print Layout you want to use.
png_path = '/Users/your_user/your_folder/' # - Path where you want to save the .png files.
png_name_template = "your_file_name{}.png" # - Name of the .png file. Put "{}" where you want the field_value in the file name.
project = QgsProject.instance()
layer = iface.activeLayer()
values_list = layer.uniqueValues(field_index)
manager = project.layoutManager()
layout = manager.layoutByName(layoutName)
exporter = QgsLayoutExporter(layout)
for field_value in values_list:
    subset_str = "'" + str(field_value)+"'"+'LIKE '+ field_name
    layer.setSubsetString(subset_str)
    pngName = png_name_template.format(field_value) 
    dest_file = str(png_path + pngName)
    label_name = layout.itemById("field_value")
    label_name.setText(field_value)
    exporter.exportToImage(dest_file, QgsLayoutExporter.ImageExportSettings())
    layer.setSubsetString('')
print("done")