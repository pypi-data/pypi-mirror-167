import numpy
import xarray
import matplotlib.pyplot as plt
from osgeo import gdal
from matplotlib import colors

class objearth():
    def __init__(self):
        pass
    @staticmethod
    def montage(img1,img2):
        """
        montage with 2 image image1,image2
        :param img1: image 1 numpy array
        :param img2: image 2 numpy array
        """
        plt.figure(figsize=(15,15))
        plt.subplot(121),plt.imshow(img1, cmap = 'gray')
        plt.title('Image 1'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(img2, cmap = 'viridis')
        plt.title('Image 2'), plt.xticks([]), plt.yticks([])
        plt.show()
    @staticmethod
    def falsecolor(Dataset1,Dataset2,Dataset3,bright=10):
        """
        color combination with xarray data
        :param Dataset1: band 1
        :param Dataset1: band 2
        :param Dataset3: band 3
        """
        BAND1    = xarray.where(Dataset1==-9999,numpy.nan,Dataset1)
        band1    = BAND1.to_numpy()/10000*bright
        BAND2    = xarray.where(Dataset2==-9999,numpy.nan,Dataset2)
        band2    = BAND2.to_numpy()/10000*bright
        BAND3    = xarray.where(Dataset3==-9999,numpy.nan,Dataset3)
        band3    = BAND3.to_numpy()/10000*bright
        product  = numpy.stack([band1,band2,band3],axis=2)
        return product
    @staticmethod
    def truecolor(Dataset,bright=10):
        RED    = xarray.where(Dataset.red==-9999,numpy.nan,Dataset.red)
        red    = RED.to_numpy()/10000*bright
        BLUE   = xarray.where(Dataset.blue==-9999,numpy.nan,Dataset.blue)
        blue   = BLUE.to_numpy()/10000*bright
        GREEN  = xarray.where(Dataset.green==-9999,numpy.nan,Dataset.green)
        green  = GREEN.to_numpy()/10000*bright
        rgb    = numpy.stack([red,green,blue],axis=2)
        return rgb
    def clearcloud(self,Dataset0,Dataset1):
        self.Dataset0 = Dataset0
        self.Dataset1 = Dataset1
        pixel0 = self.Dataset0.pixel_qa
        mask1 = xarray.where(pixel0==352,1,0)    
        mask2 = xarray.where(pixel0==480,1,0)
        mask3 = xarray.where(pixel0==944,1,0)
        sum = mask1+mask2+mask3
        mask0 = xarray.where(sum.data>0,1,0)
        blue        = xarray.where(mask0,self.Dataset1.blue,self.Dataset0.blue)
        green       = xarray.where(mask0,self.Dataset1.green,self.Dataset0.green)
        red         = xarray.where(mask0,self.Dataset1.red,self.Dataset0.red)
        nir         = xarray.where(mask0,self.Dataset1.nir,self.Dataset0.nir)
        pixel_qa    = xarray.where(mask0,self.Dataset1.pixel_qa,self.Dataset0.pixel_qa)
        # Create DataArray
        return xarray.merge([blue,green,red,nir,pixel_qa])
    @staticmethod
    def plotshow(DataArray,lst=True):
        DataArray = DataArray
        lst = lst
        if type(DataArray) == xarray.core.dataarray.DataArray:
            if lst==True:
                ymax = 0 ; ymin = DataArray.shape[0]
                xmin = 0 ; xmax = DataArray.shape[1] 
            else:
                ymax = lst[0] ; ymin = lst[1]
                xmin = lst[2] ; xmax = lst[3]
            lon  =  DataArray.longitude.to_numpy()[xmin:xmax]
            lon0 =  lon[0] ; lon1 =  lon[-1]
            lat  =  DataArray.latitude.to_numpy()[ymax:ymin]
            lat0 = -lat[-1] ; lat1 = -lat[0]
            def longitude(lon):
                return [lon0,lon1]
            def latitude(lat):
                return [lat0,lat1]
            def axis(x=0):
                return x
            fig,ax = plt.subplots(constrained_layout=True)
            fig.set_size_inches(7,7)
            ax.set_xlabel('x axis size')
            ax.set_ylabel('y axis size')
            ax.imshow(DataArray[ymax:ymin,xmin:xmax],extent=[xmin,xmax,ymin,ymax])
            secax_x = ax.secondary_xaxis('top',functions=(longitude,axis))
            secax_x.set_xlabel('longitude')
            secax_x = ax.secondary_xaxis('top',functions=(longitude,axis))
            secax_x.set_xlabel('longitude')
            secax_y = ax.secondary_yaxis('right',functions=(latitude,axis))
            secax_y.set_ylabel('latitute')
            plt.grid(color='w', linestyle='-', linewidth=0.15)
            plt.show()
        elif type(DataArray) == numpy.ndarray:
            if lst==True:
                ymax = 0 ; ymin = DataArray.shape[0]
                xmin = 0 ; xmax = DataArray.shape[1]
            else:
                ymax = lst[0] ; ymin = lst[1]
                xmin = lst[2] ; xmax = lst[3]
            plt.figure(figsize=(8,8))
            plt.imshow(DataArray[ymax:ymin,xmin:xmax],extent=[xmin,xmax,ymin,ymax])
            plt.xlabel("x axis size")
            plt.ylabel("y axis size")
            plt.grid(color='w', linestyle='-', linewidth=0.15)
            plt.show()

        else:
            print("Nonetype :",type(DataArray))
    def percentcloud(self,Dataset):
        self.Dataset = Dataset
        FashCloud = [352,480,944]
        dstest    = self.Dataset.pixel_qa
        dsnew     = xarray.where(dstest == FashCloud[0],numpy.nan,dstest)
        dsnew     = xarray.where(dsnew  == FashCloud[1],numpy.nan,dsnew)
        dsnew     = xarray.where(dsnew  == FashCloud[2],numpy.nan,dsnew)
        Cpixel    = (numpy.isnan(dsnew.to_numpy())).sum()
        Allpixel  = int(self.Dataset.pixel_qa.count())
        Cloudpercent = (Cpixel/Allpixel)*100
        print("Percent Cloud : %.4f"%Cloudpercent,"%")
    def NDVI(self,DataArray):
        """Normalized Difference vegetation Index"""
        self.DataArray = DataArray
        red = xarray.where(self.DataArray.red==-9999,numpy.nan,self.DataArray.red)
        nir = xarray.where(self.DataArray.nir==-9999,numpy.nan,self.DataArray.nir)
        ndvi1 = (nir-red)/(nir+red).to_numpy()
        ndvi3 = numpy.clip(ndvi1,-1,1)
        im_ratio = ndvi3.shape[1]/ndvi3.shape[0]
        plt.figure(figsize=(8,8))
        plt.xticks([]), plt.yticks([])
        plt.imshow(ndvi3,cmap='viridis')
        plt.clim(-1,1)
        plt.colorbar(orientation="vertical",fraction=0.0378*im_ratio)
        plt.show()
        return ndvi3
    def NDMI(self,DataArray):
        """Normalized Difference Moisture Index"""
        self.DataArray = DataArray
        swir = xarray.where(self.DataArray.swir1==-9999,numpy.nan,self.DataArray.swir1)
        nir = xarray.where(self.DataArray.nir==-9999,numpy.nan,self.DataArray.nir)
        ndmi1 = (nir-swir)/(nir+swir).to_numpy()
        ndmi3 = numpy.clip(ndmi1,-1,1)
        im_ratio = ndmi3.shape[1]/ndmi3.shape[0]
        plt.figure(figsize=(8,8))
        plt.xticks([]), plt.yticks([])
        plt.imshow(ndmi3,cmap='viridis')
        plt.clim(-1,1)
        plt.colorbar(orientation="vertical",fraction=0.0378*im_ratio)
        plt.show()
        return ndmi3
    def BSI(self,DataArray):
        """Bare Soil Index"""
        self.DataArray = DataArray
        green = xarray.where(self.DataArray.green==-9999,numpy.nan,self.DataArray.green)
        nir = xarray.where(self.DataArray.nir==-9999,numpy.nan,self.DataArray.nir)
        bsi1 = (nir+green)/(green-nir).to_numpy()
        bsi3 = numpy.clip(bsi1,-1,1)
        im_ratio = bsi3.shape[1]/bsi3.shape[0]
        plt.figure(figsize=(8,8))
        plt.xticks([]), plt.yticks([])
        plt.imshow(bsi3,cmap='viridis')
        plt.clim(-1,1)
        plt.colorbar(orientation="vertical",fraction=0.0378*im_ratio)
        plt.show()
        return bsi3
    def EVI(self,DataArray):
        """Enhanced Vegetation Index"""
        self.DataArray = DataArray
        red = xarray.where(self.DataArray.red==-9999,numpy.nan,self.DataArray.red)
        blue = xarray.where(self.DataArray.blue==-9999,numpy.nan,self.DataArray.blue)
        nir = xarray.where(self.DataArray.nir==-9999,numpy.nan,self.DataArray.nir)
        evi1 = (nir-red)/(nir+6*red-7.5*blue+1).to_numpy()
        evi3 = numpy.clip(evi1,-1,1)
        im_ratio = evi3.shape[1]/evi3.shape[0]
        plt.figure(figsize=(8,8))
        plt.xticks([]), plt.yticks([])
        plt.imshow(evi3,cmap='viridis')
        plt.clim(-1,1)
        plt.colorbar(orientation="vertical",fraction=0.0378*im_ratio)
        plt.show()
        return evi3
    def NDWI(self,DataArray):
        """Normalized Difference Water Index"""
        self.DataArray = DataArray
        swir = xarray.where(self.DataArray.swir1==-9999,numpy.nan,self.DataArray.swir1)
        nir = xarray.where(self.DataArray.nir==-9999,numpy.nan,self.DataArray.nir)
        ndwi1 = (nir-swir)/(nir+swir).to_numpy()
        ndwi3 = numpy.clip(ndwi1,-1,1)
        im_ratio = ndwi3.shape[1]/ndwi3.shape[0]
        plt.figure(figsize=(8,8))
        plt.xticks([]), plt.yticks([])
        plt.imshow(ndwi3,cmap='viridis')
        plt.clim(-1,1)
        plt.colorbar(orientation="vertical",fraction=0.0378*im_ratio)
        plt.show()
        return ndwi3
    def NMDI(self,DataArray):
        """Normalized Multi-Band Drought Index"""
        self.DataArray = DataArray
        swir1 = xarray.where(self.DataArray.swir1==-9999,numpy.nan,self.DataArray.swir1)
        swir2 = xarray.where(self.DataArray.swir2==-9999,numpy.nan,self.DataArray.swir2)
        nir   = xarray.where(self.DataArray.nir==-9999,numpy.nan,self.DataArray.nir)
        nmdi1 = (nir-(swir1-swir2))/(nir-(swir1+swir2)).to_numpy()
        nmdi3 = numpy.clip(nmdi1,-1,1)
        im_ratio = nmdi3.shape[1]/nmdi3.shape[0]
        plt.figure(figsize=(8,8))
        plt.xticks([]), plt.yticks([])
        plt.imshow(nmdi3,cmap='viridis')
        plt.clim(-1,1)
        plt.colorbar(orientation="vertical",fraction=0.0378*im_ratio)
        plt.show()
        return nmdi3
    def NDDI(self,DataArray):
        """Normalized Difference Drought Index"""
        self.DataArray = DataArray
        red = xarray.where(self.DataArray.red==-9999,numpy.nan,self.DataArray.red)
        nir = xarray.where(self.DataArray.nir==-9999,numpy.nan,self.DataArray.nir)
        swir = xarray.where(self.DataArray.swir1==-9999,numpy.nan,self.DataArray.swir1)
        ndvi = (nir-red)/(nir+red)
        ndwi = (nir-swir)/(nir+swir)       
        nddi1 = (ndvi-ndwi)/(ndvi+ndwi).to_numpy() 
        nddi3 = numpy.clip(nddi1,-1,1)
        im_ratio = nddi3.shape[1]/nddi3.shape[0]
        plt.figure(figsize=(8,8))
        plt.xticks([]), plt.yticks([])
        plt.imshow(nddi3,cmap='viridis')
        plt.clim(-1,1)
        plt.colorbar(orientation="vertical",fraction=0.0378*im_ratio)
        plt.show()
        return nddi3
    def genimg(size=[2,2],range=[-1,1],nan=0,inf=0):
        data = numpy.random.uniform(range[0],range[1],[size[0],size[1]])
        index_nan = numpy.random.choice(data.size,nan,replace=1)
        data.ravel()[index_nan] = numpy.nan
        index_inf = numpy.random.choice(data.size,inf,replace=1)
        data.ravel()[index_inf] = numpy.inf
        return data

    @staticmethod
    def band_combination(RED,GREEN,BLUE,bright=10):
        red    = RED/10000   *bright
        green  = GREEN/10000 *bright
        blue   = BLUE/10000  *bright
        return numpy.stack([red,green,blue],axis=2)

    @staticmethod
    def bandopen(target):
        return gdal.Open(target).ReadAsArray()
    
    @staticmethod
    def genguasian(size1,size2):
        x, y = numpy.meshgrid(numpy.linspace(-1,1,size1), numpy.linspace(-1,1,size2))
        d = numpy.sqrt(x*x+y*y)
        sigma, mu = 0.5, 1.0
        g = numpy.exp(-( (d-mu)**2 / ( 2.0 * sigma**2 ) ) )
        return g
    
    @staticmethod
    def bluesea():
        RGB6 = (0.1, 0.1, 0.1)
        RGB5 = (0.        , 0.31372549, 0.45098039)
        RGB4 = (0.0627451 , 0.49019608, 0.6745098 )
        RGB3 = (0.09411765, 0.60392157, 0.82745098)
        RGB2 = (0.11764706, 0.73333333, 0.84313725)
        RGB1 = (0.44313725, 0.78039216, 0.9254902 )
        RGB0 = (0.99, 0.99, 0.99 )
        cdict = {
        'red':  ((1  / 6 * 0, RGB0[0]  ,RGB0[0]),
                (1  / 6 * 1, RGB1[0]  ,RGB1[0]),
                (1  / 6 * 2, RGB2[0]  ,RGB2[0]),
                (1  / 6 * 3, RGB3[0]  ,RGB3[0]),
                (1  / 6 * 4, RGB4[0]  ,RGB4[0]),
                (1  / 6 * 5, RGB5[0]  ,RGB5[0]),
                (1  / 6 * 6, RGB6[0]  ,RGB6[0])
                ),

        'green':((1  / 6 * 0, RGB0[1]    , RGB0[1]),
                (1  / 6 * 1, RGB1[1]    , RGB1[1]),
                (1  / 6 * 2, RGB2[1]    , RGB2[1]),
                (1  / 6 * 3, RGB3[1]    , RGB3[1]),
                (1  / 6 * 4, RGB4[1]    , RGB4[1]),
                (1  / 6 * 5, RGB5[1]    , RGB5[1]),
                (1  / 6 * 6, RGB6[1]    , RGB6[1])
                ),

        'blue': ((1  / 6 * 0, RGB0[2]    , RGB0[2]),
                (1  / 6 * 1, RGB1[2]    , RGB1[2]),
                (1  / 6 * 2, RGB2[2]    , RGB2[2]),
                (1  / 6 * 3, RGB3[2]    , RGB3[2]),
                (1  / 6 * 4, RGB4[2]    , RGB4[2]),
                (1  / 6 * 5, RGB5[2]    , RGB5[2]),
                (1  / 6 * 6, RGB6[2]    , RGB6[2])
                ),
        }
        nc = colors.LinearSegmentedColormap('bluesea',segmentdata=cdict)
        return nc    
    
    @staticmethod
    def leafwood():
        RGB1  = (0.30588235, 0.05490196, 0.05490196)
        RGB2  = (0.39215686, 0.09803922, 0.07843137)
        RGB3  = (0.43921569, 0.18431373, 0.00392157)
        RGB4  = (0.54901961, 0.2745098 , 0.05882353)
        RGB5  = (0.61960784, 0.30588235, 0.02745098)
        RGB6  = (0.70980392, 0.40784314, 0.0627451)
        RGB7  = (0.85098039, 0.51764706, 0.04705882)
        RGB8  = (0.8627451 , 0.49019608, 0.05490196)
        RGB9  = (0.85882353, 0.63529412, 0.05490196)
        RGB10 = (0.91764706, 0.69019608, 0.01568627)
        RGB11 = (0.87058824, 0.8       , 0.05098039)
        RGB12 = (0.89019608, 0.8745098 , 0.07058824)
        RGB13 = (0.92156863, 0.91764706, 0.09019608)
        RGB14 = (0.81176471, 0.85882353, 0.2745098 )
        RGB15 = (0.56862745, 0.68627451, 0.21960784)
        RGB16 = (0.56078431, 0.69803922, 0.25882353)
        RGB17 = (0.52156863, 0.6627451 , 0.21960784)
        RGB18 = (0.35686275, 0.49803922, 0.11764706)
        RGB19 = (0.23529412, 0.46666667, 0.05490196)
        RGB20 = (0.16078431, 0.36862745, 0.04313725)
        RGB21 = (0.09411765, 0.35294118, 0.01176471)
        cdict = {
            'red':  ((1  / 20 * 0,  (RGB1[0])  ,(RGB1[0])),
                    (1  / 20 * 1,  (RGB2[0])  ,(RGB2[0])),
                    (1  / 20 * 2,  (RGB3[0])  ,(RGB3[0])),
                    (1  / 20 * 3,  (RGB4[0])  ,(RGB4[0])),
                    (1  / 20 * 4,  (RGB5[0])  ,(RGB5[0])),
                    (1  / 20 * 5,  (RGB6[0])  ,(RGB6[0])),
                    (1  / 20 * 6,  (RGB7[0])  ,(RGB7[0])),
                    (1  / 20 * 7,  (RGB8[0])  ,(RGB8[0])),
                    (1  / 20 * 8,  (RGB9[0])  ,(RGB9[0])),
                    (1  / 20 * 9,  (RGB10[0])  ,(RGB10[0])),
                    (1  / 20 * 10, (RGB11[0])  ,(RGB11[0])),
                    (1  / 20 * 11, (RGB12[0])  ,(RGB12[0])),
                    (1  / 20 * 12, (RGB13[0])  ,(RGB13[0])),
                    (1  / 20 * 13, (RGB14[0])  ,(RGB14[0])),
                    (1  / 20 * 14, (RGB15[0])  ,(RGB15[0])),
                    (1  / 20 * 15, (RGB16[0])  ,(RGB16[0])),
                    (1  / 20 * 16, (RGB17[0])  ,(RGB17[0])),
                    (1  / 20 * 17, (RGB18[0])  ,(RGB18[0])),
                    (1  / 20 * 18, (RGB19[0])  ,(RGB19[0])),
                    (1  / 20 * 19, (RGB20[0])  ,(RGB20[0])),
                    (1  / 20 * 20, (RGB21[0])  ,(RGB21[0]))),

            'green':((1  / 20 * 0,  (RGB1[1])  ,(RGB1[1])),
                    (1  / 20 * 1,  (RGB2[1])  ,(RGB2[1])),
                    (1  / 20 * 2,  (RGB3[1])  ,(RGB3[1])),
                    (1  / 20 * 3,  (RGB4[1])  ,(RGB4[1])),
                    (1  / 20 * 4,  (RGB5[1])  ,(RGB5[1])),
                    (1  / 20 * 5,  (RGB6[1])  ,(RGB6[1])),
                    (1  / 20 * 6,  (RGB7[1])  ,(RGB7[1])),
                    (1  / 20 * 7,  (RGB8[1])  ,(RGB8[1])),
                    (1  / 20 * 8,  (RGB9[1])  ,(RGB9[1])),
                    (1  / 20 * 9,  (RGB10[1])  ,(RGB10[1])),
                    (1  / 20 * 10, (RGB11[1])  ,(RGB11[1])),
                    (1  / 20 * 11, (RGB12[1])  ,(RGB12[1])),
                    (1  / 20 * 12, (RGB13[1])  ,(RGB13[1])),
                    (1  / 20 * 13, (RGB14[1])  ,(RGB14[1])),
                    (1  / 20 * 14, (RGB15[1])  ,(RGB15[1])),
                    (1  / 20 * 15, (RGB16[1])  ,(RGB16[1])),
                    (1  / 20 * 16, (RGB17[1])  ,(RGB17[1])),
                    (1  / 20 * 17, (RGB18[1])  ,(RGB18[1])),
                    (1  / 20 * 18, (RGB19[1])  ,(RGB19[1])),
                    (1  / 20 * 19, (RGB20[1])  ,(RGB20[1])),
                    (1  / 20 * 20, (RGB21[1])  ,(RGB21[1]))),

            'blue': ((1  / 20 * 0,  (RGB1[2])  ,(RGB1[2])),
                    (1  / 20 * 1,  (RGB2[2])  ,(RGB2[2])),
                    (1  / 20 * 2,  (RGB3[2])  ,(RGB3[2])),
                    (1  / 20 * 3,  (RGB4[2])  ,(RGB4[2])),
                    (1  / 20 * 4,  (RGB5[2])  ,(RGB5[2])),
                    (1  / 20 * 5,  (RGB6[2])  ,(RGB6[2])),
                    (1  / 20 * 6,  (RGB7[2])  ,(RGB7[2])),
                    (1  / 20 * 7,  (RGB8[2])  ,(RGB8[2])),
                    (1  / 20 * 8,  (RGB9[2])  ,(RGB9[2])),
                    (1  / 20 * 9,  (RGB10[2])  ,(RGB10[2])),
                    (1  / 20 * 10, (RGB11[2])  ,(RGB11[2])),
                    (1  / 20 * 11, (RGB12[2])  ,(RGB12[2])),
                    (1  / 20 * 12, (RGB13[2])  ,(RGB13[2])),
                    (1  / 20 * 13, (RGB14[2])  ,(RGB14[2])),
                    (1  / 20 * 14, (RGB15[2])  ,(RGB15[2])),
                    (1  / 20 * 15, (RGB16[2])  ,(RGB16[2])),
                    (1  / 20 * 16, (RGB17[2])  ,(RGB17[2])),
                    (1  / 20 * 17, (RGB18[2])  ,(RGB18[2])),
                    (1  / 20 * 18, (RGB19[2])  ,(RGB19[2])),
                    (1  / 20 * 19, (RGB20[2])  ,(RGB20[2])),
                    (1  / 20 * 20, (RGB21[2])  ,(RGB21[2])),
            )
        }
        nc4 = colors.LinearSegmentedColormap('leafwood',segmentdata=cdict)
        return nc4
