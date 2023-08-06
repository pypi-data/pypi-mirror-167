earth_params = {
'0':{'shape':'spherical','radius':6367470.0},
'1':{'shape':'spherical','radius':None},
'2':{'shape':'oblateSpheriod','major_axis':6378160.0,'minor_axis':6356775.0,'flattening':1.0/297.0},
'3':{'shape':'oblateSpheriod','major_axis':None,'minor_axis':None,'flattening':None},
'4':{'shape':'oblateSpheriod','major_axis':6378137.0,'minor_axis':6356752.314,'flattening':1.0/298.257222101},
'5':{'shape':'oblateSpheriod','major_axis':6378137.0,'minor_axis':6356752.3142,'flattening':1.0/298.257223563},
'6':{'shape':'spherical','radius':6371229.0},
'7':{'shape':'oblateSpheriod','major_axis':None,'minor_axis':None,'flattening':None},
'8':{'shape':'spherical','radius':6371200.0},
}
for i in range(9,256):
    earth_params[str(i)] = {'shape':'unknown','radius':None}
