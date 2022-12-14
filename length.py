fn = 'C:/Users/Rysunek22.shp'

layer= iface.addVectorLayer(fn, '', 'ogr')
pv = layer.dataProvider()
pv.addAttributes([QgsField('len_test_m', QVariant.Double)])

layer.updateFields()

expression1 = QgsExpression('round($length,3)')


context= QgsExpressionContext()
context.appendScopes(\
QgsExpressionContextUtils.globalProjectLayerScopes(layer))

with edit(layer):
    for f in layer.getFeatures():
        context.setFeature(f)
        f['len_test_m'] = expression1.evaluate(context)
        layer.updateFeature(f)
