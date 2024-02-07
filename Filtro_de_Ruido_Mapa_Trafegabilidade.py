from osgeo import gdal
import rasterio
import numpy as np

#Ler Mapa de Trafegabilidade
endereco = r'C:\Users\Desktop\Mapa_Trafegabilidade_Final\Mapa_Trafegabilidade_out_nov_dez_jan.tif'
img = gdal.Open(endereco,gdal.GA_ReadOnly)

#Transforma imagem .tif em array do numpy (forma matricial)
img_array = img.ReadAsArray()

#filtro de ruídos
filtrado=0
for j in range(1,img.RasterXSize-1):
    for i in range(1,img.RasterYSize-1):
        if img_array[i-1][j-1]==img_array[i-1][j]==img_array[i-1][j+1]==img_array[i][j-1]==img_array[i][j+1]==img_array[i+1][j-1]==img_array[i+1][j]==img_array[i+1][j+1]:
            if img_array[i][j]<img_array[i-1][j-1]:
                img_array[i][j]=img_array[i-1][j-1]
                filtrado=filtrado+1

#Resultado
print("Filtragem concluída! \nTotal de pixels filtrados no Mapa:",filtrado)

#Salva arquivo filtrado em um novo arquivo .tif
imagem=rasterio.open(endereco)
out_meta = imagem.meta.copy()
out_tif=r"C:\Users\Desktop\Mapa_Trafegabilidade_Final\Mapa_Trafegabilidade_out_nov_dez_jan_filtrado.tif"

with rasterio.open(out_tif,"w",**out_meta) as dest:
    dest.write(img_array, 1)
dest.close()

