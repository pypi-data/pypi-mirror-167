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
        RGB0 = (0.1, 0.1, 0.1)
        RGB1 = (0.        , 0.31372549, 0.45098039)
        RGB2 = (0.0627451 , 0.49019608, 0.6745098 )
        RGB3 = (0.09411765, 0.60392157, 0.82745098)
        RGB4 = (0.11764706, 0.73333333, 0.84313725)
        RGB5 = (0.44313725, 0.78039216, 0.9254902 )
        RGB6 = (0.99, 0.99, 0.99 )
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
        #https://mycolor.space/gradient?ori=to+right+top&hex=%2385A938&hex2=%233C770E&sub=1
        #https://imagecolorpicker.com/en
        RGB1   = (0.30588235, 0.05490196, 0.05490196)   #RGB(78,14,14)          
        RGB2   = (0.39215686, 0.09803922, 0.07843137)   #RGB(100,25,20)
        RGB3   = (0.43921569, 0.18431373, 0.00392157)   #RGB(112,47,1)
        RGB4   = (0.50980392, 0.23529412, 0.05098039)   #RGB(130,60,13)
        RGB5   = (0.54901961, 0.2745098 , 0.05882353)   #RGB(140,70,15)
        RGB6   = (0.61960784, 0.30588235, 0.02745098)   #RGB(158,78,7)
        RGB7   = (0.70980392, 0.40784314, 0.0627451 )   #RGB(181,104,16) 
        RGB8   = (0.79607843, 0.49019608, 0.16470588)   #RGB(203, 125, 42)
        RGB9   = (0.85490196, 0.58823529, 0.04705882)   #RGB(218,150,12)
        RGB10  = (0.85882353, 0.63529412, 0.05490196)   #RGB(219,162,14)
        RGB11  = (0.88235294, 0.7254902 , 0.01568627)   #RGB(225,185,4)
        RGB12  = (0.87058824, 0.8       , 0.05098039)   #RGB(222,204,13)
        RGB13  = (0.89019608, 0.8745098 , 0.07058824)   #RGB(227,223,18)
        RGB14  = (0.92156863, 0.91764706, 0.09019608)   #RGB(235,234,23)
        RGB15  = (0.81176471, 0.85882353, 0.2745098 )   #RGB(207,219,70)
        RGB16  = (0.68627451, 0.77647059, 0.26666667)   #RGB(175,198,68)
        RGB17  = (0.56078431, 0.69803922, 0.25882353)   #RGB(143,178,66)
        RGB18  = (0.52156863, 0.6627451 , 0.21960784)   #RGB(133,169,56)
        RGB19  = (0.38039216, 0.56470588, 0.14117647)   #RGB(97, 144, 36)
        RGB20  = (0.23529412, 0.46666667, 0.05490196)   #RGB(60,119,14)
        RGB21  = (0.16078431, 0.36862745, 0.04313725)   #RGB(41,94,11)
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



from sklearn.preprocessing import MinMaxScaler, RobustScaler
from sklearn.model_selection import train_test_split
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import calinski_harabasz_score
from sklearn.naive_bayes import GaussianNB
from sklearn import cluster
import numpy as np


class water:
        #fix
        required_bands = {'mndi','Green','ndwi','Mir2','mbwi'}
        required_indices = {'ndwi','mbwi','mndwi'}
        bands_keys = ['mndwi','ndwi','Mir2']
        invalid_mask = None
        glint_processor = None
        # config = config
        data_as_columns = None
        clusters_labels = None
        clusters_params = None
        cluster_matrix = None
        water_cluster = None
        water_mask = None
        best_k = None
        _product_name = None
        # bands_keys = bands_keys
        cluster_matrix = None
        train_size = 0.2
        min_train_size = 500
        max_train_size = 10000
        linkage = 'average'
        clip_band = ['mndwi', 'Mir2', 'ndwi']
        clip_inf_value = [-0.1, None, -0.15]
        clip_sup_value = [None, 0.075, None]
        glint_mode = True
        glint_processor = None
        detect_water_cluster = 'maxmndwi'
        min_k = 2
        score_index = 'calinsk'
        #unfix
        max_k = 5
        classifier = 'naivebayes'
        clustering_method = 'agglomerative'
        
        def __init__(self,bands):
            self.bands = bands   
            
        def __str__(self):
            lst = list()
            for i in self.bands.keys():
                lst.append(i)
            lst = str(lst)
            return "bands : "+lst 
    
        def show(self):
            # oe.plotshow(oe.band_combination(self.bands['Red'],self.bands['Green'],self.bands['Blue'],5))
            print(self.bands)
            
        ############################################ DWImageClustering ############################################
        #check if the MNDWI index is necessary and if it exists
        @staticmethod
        def calc_normalized_difference(img1, img2, mask=None, compress_cte=0.02):
            # create a minimum array
            min_values = np.where(img1 < img2, img1, img2)

            # then create the to_add matrix (min values turned into positive + epsilon)
            min_values = np.where(min_values <= 0, -min_values + 0.001, 0) + compress_cte

            nd = ((img1 + min_values) - (img2 + min_values)) / ((img1 + min_values) + (img2 + min_values))

            nd[nd > 1] = 1
            nd[nd < -1] = -1

            # if result is infinite, result should be 1
            nd[np.isinf(nd)] = 1

            # nd_mask = np.isinf(nd) | np.isnan(nd) | mask
            nd_mask = np.isnan(nd) | (mask if mask is not None else False)

            nd = np.ma.array(nd, mask=nd_mask, fill_value=-9999)

            return nd.filled(), nd.mask

        @staticmethod
        #check if the MBWI index exist
        def calc_mbwi(bands, factor, mask):
            # changement for negative SRE values scene
            min_cte = np.min([np.min(bands['Green'][~mask]), np.min(bands['Red'][~mask]),
                                np.min(bands['Nir'][~mask]), np.min(bands['Mir'][~mask]), np.min(bands['Mir2'][~mask])])
            if min_cte <= 0:
                min_cte = -min_cte + 0.001
            else:
                min_cte = 0
            mbwi = factor * (bands['Green'] + min_cte) - (bands['Red'] + min_cte) - (bands['Nir'] + min_cte) \
                    - (bands['Mir'] + min_cte) - (bands['Mir2'] + min_cte)
            mbwi[~mask] = RobustScaler(copy=False).fit_transform(mbwi[~mask].reshape(-1, 1)).reshape(-1)
            mbwi[~mask] = MinMaxScaler(feature_range=(-1, 1), copy=False).fit_transform(mbwi[~mask].reshape(-1, 1)) \
                .reshape(-1)
            mask = np.isinf(mbwi) | np.isnan(mbwi) | mask
            mbwi = np.ma.array(mbwi, mask=mask, fill_value=-9999)
            return mbwi, mask

        @staticmethod
        #check if the list contains the required bands
        def listify(lst, uniques=[]):
            # pdb.set_trace()
            for item in lst:
                if isinstance(item, list):
                    uniques = listify(item, uniques)
                else:
                    uniques.append(item)
            return uniques.copy()
        ############################################ DWImageClustering ############################################
        ############################################ run_detect_water #############################################
        #Transform the rasters in a matrix where each band is a column
        @staticmethod
        def bands_to_columns(bands,invalid_mask):
            data = None
            for key in sorted(bands.keys()):
                band_array = bands[key]

                band_as_column = band_array[~invalid_mask].reshape(-1,1)

                if (key == 'Mir') or (key == 'Mir2') or (key == 'Nir') or (key == 'Nir2') or (key == 'Green'):
                    band_as_column = band_as_column * 4
                    band_as_column[band_as_column > 4] = 4

                data = band_as_column if data is None else np.concatenate([data, band_as_column], axis=1)
            return data

        # if algorithm is not kmeans,split data for a smaller ser (for performnce purposes)
        @staticmethod
        def get_train_test_split(data,train_size,min_train_size,max_train_size):
            dataset_size = data.shape[0]

            if (dataset_size * train_size) < min_train_size:
                train_size = min_train_size / dataset_size
                train_size = 1 if train_size > 1 else train_size

            elif (dataset_size * train_size) > max_train_size:
                train_size = max_train_size / dataset_size
            
            return train_test_split(data, train_size=train_size)
        
        #create data bunch only with the bands used for clustering
        @staticmethod
        def split_data_by_bands(bands,data, selected_keys):

            bands_index = []
            bands_keys = list(sorted(bands.keys()))

            for key in selected_keys:
                bands_index.append(bands_keys.index(key))
            return data[:, bands_index]
        
    
        def find_best_k(self,data):
            # print('min_k :',self.min_k)
            # print('max_k :',self.max_k)
            # print('score_index :',self.score_index)
            # print(data)

            if self.min_k == self.max_k:
                print('Same number for minimum and maximum clusters: k = {}'.format(self.min_k))
                best_k = self.min_k
                return best_k

            # if score_index == 'silhouette':
            #     print('Selection of best number of clusters using Silhouete Index:')
            # else:
            #     print('Selection of best number of clusters using Calinski-Harabasz Index:')

            # if self.score_index == 'silhouette':
            #     print('score_index --> Silhouete')
            # else:
            #     print('score_index --> Calinski_harabaz')

            computed_metrics = []
            for num_k in range(self.min_k, self.max_k + 1):
                # cluster_model = cluster.KMeans(n_clusters=num_k, init='k-means++')
                cluster_model = cluster.AgglomerativeClustering(n_clusters=num_k, linkage=self.linkage)

                labels = cluster_model.fit_predict(data)

                if self.score_index == 'silhouette':
                    computed_metrics.append(metrics.silhouette_score(data, labels))
                    # print('k = {} index : {}'.format(num_k, computed_metrics[num_k - self.min_k]))

                else:
                    computed_metrics.append(calinski_harabasz_score(data, labels))
                    # print('k = {} index : {}'.format(num_k, computed_metrics[num_k - self.min_k]))

            best_k = computed_metrics.index(max(computed_metrics)) + self.min_k
            # print("best_k :",best_k)

            return best_k
        
        #apply the clusterization algorithm and return labels and train dataset
        @staticmethod
        def apply_cluster(data,best_k):
            clustering_method = 'agglomerative'
            if clustering_method == 'kmeans':
                cluster_model = cluster.KMeans(n_clusters=best_k, init='k-means++')
            elif clustering_method == 'gauss_mixture':
                cluster_model = GMM(n_components=best_k, covariance_type='full')
            else:
                cluster_model = cluster.AgglomerativeClustering(n_clusters=best_k, linkage='average')

            cluster_model.fit(data)
            return cluster_model.labels_.astype('int8')
        
        #cals statistics for each cluster
        @staticmethod
        def calc_clusters_params(data, clusters_labels,best_k):
            clusters_params = []
            for label_i in range(best_k):
                # first slice the values in the indexed cluster
                cluster_i = data[clusters_labels == label_i, :]

                cluster_param = {'clusterid': label_i}
                cluster_param.update({'mean': np.mean(cluster_i, 0)})
                cluster_param.update({'variance': np.var(cluster_i, 0)})
                cluster_param.update({'stdev': np.std(cluster_i, 0)})
                cluster_param.update({'diffb2b1': cluster_param['mean'][1] - cluster_param['mean'][0]})
                cluster_param.update({'pixels': cluster_i.shape[0]})

                clusters_params.append(cluster_param)

            return clusters_params
        
        #detect the water cluster
        @staticmethod
        def detect_cluster(bands,clusters_params, param, logic, band1, band2=None):
            # get the bands available in the columns
            available_bands = sorted(bands.keys())

            param_list = []
            if band1:
                idx_band1 = available_bands.index(band1)
            if band2:
                idx_band2 = available_bands.index(band2)

            # todo: fix the fixed values
            for clt in clusters_params:
                if param == 'diff':
                    if not idx_band2:
                        raise OSError('Two bands needed for diff method')
                    param_list.append(clt['mean'][idx_band1] - clt['mean'][idx_band2])

                elif param == 'value':
                    if (clt['pixels'] > 5): # and (clt['mean'][available_bands.index('Mir2')] < 0.25*4):
                        param_list.append(clt['mean'][idx_band1])
                    else:
                        param_list.append(-1)

            if logic == 'max':
                idx_detected = param_list.index(max(param_list))
            else:
                idx_detected = param_list.index(min(param_list))

            return clusters_params[idx_detected]
        
        def identify_water_cluster(self,detect_water_cluster,bands):
            if detect_water_cluster == 'maxmndwi':
                if 'mndwi' not in bands.keys():
                    raise OSError('MNDWI band necessary for detecting water with maxmndwi option')
                water_cluster = self.detect_cluster(bands,self.clusters_params,'value', 'max', 'mndwi')

            # elif detect_water_cluster == 'maxmbwi':
            #     if 'mbwi' not in bands.keys():
            #         raise OSError('MBWI band necessary for detecting water with maxmbwi option')
            #     water_cluster = detect_cluster(bands,clusters_params,'value', 'max', 'mbwi')

            # elif detect_water_cluster == 'minmir2':
            #     if 'mndwi' not in bands.keys():
            #         raise OSError('Mir2 band necessary for detecting water with minmir2 option')
            #     water_cluster = detect_cluster(bands,clusters_params,'value', 'min', 'Mir2')

            # elif detect_water_cluster == 'maxndwi':
            #     if 'ndwi' not in bands.keys():
            #         raise OSError('NDWI band necessary for detecting water with minmir2 option')
            #     water_cluster = detect_cluster(bands,clusters_params,'value', 'max', 'ndwi')

            # elif detect_water_cluster == 'minnir':
            #     water_cluster = detect_cluster(bands,clusters_params,'value', 'min', 'Nir')

            # else:
            #     raise OSError('Method {} for detecting water cluster does not exist'.
            #                     format(self.config.detect_water_cluster))

            return water_cluster
        
        @staticmethod
        def apply_naive_bayes(data, clusters_labels, clusters_data):
            # train a NB classifier with the data and labels provided
            model = GaussianNB()

            # print('Applying clusters based --> naive bayes classifier')
            # print('Cross_val_score:{}'.format(cross_val_score(model, clusters_data, clusters_labels)))

            model.fit(clusters_data, clusters_labels)

            # return the new predicted labels for the whole dataset
            return model.predict(data)
        
        
        def supervised_classification(self,data, train_data, clusters_labels):
            if self.classifier == 'SVM':
                clusters_labels = apply_svm(data, clusters_labels, train_data)
            elif self.classifier == 'MLP':
                clusters_labels = apply_mlp(data, clusters_labels, train_data)
            else:
                clusters_labels = self.apply_naive_bayes(data, clusters_labels, train_data)

            return clusters_labels.astype('int8')
        
        # after obtain the final labels,clip bands with superios limit
        # after obtainting the final labels,clip bands with inferior limit
        #create an cluster array based on the cluster result (water will be value1)
        @staticmethod
        def create_matrice_cluster(indices_array,bands,clusters_labels,water_cluster,best_k):
            # create an empty matrix
            matrice_cluster = np.zeros_like(list(bands.values())[0]).astype('int8')

            # apply water pixels to value 1
            matrice_cluster[indices_array[0][clusters_labels == water_cluster['clusterid']],
                            indices_array[1][clusters_labels == water_cluster['clusterid']]] = 1

            # print('Assgnin 1 to cluster_id {}'.format(water_cluster['clusterid']))

            # loop through the remaining labels and apply value >= 3
            new_label = 2
            for label_i in range(best_k):

                if label_i != water_cluster['clusterid']:
                    matrice_cluster[indices_array[0][clusters_labels == label_i],
                                    indices_array[1][clusters_labels == label_i]] = new_label

                    new_label += 1
                else:
                    pass
                    # print('Skipping cluster_id {}'.format(label_i))

            return matrice_cluster
        ############################################ run_detect_water #############################################
        
        ################################################## main ###################################################
        def waterdetect(self):
            ## wd.DWImageClustering
            # get the first band as reference of size
            ref_band = list(self.bands.keys())[0]
            ref_shape = self.bands[ref_band].shape

            #check the invalid_mask
            invalid_mask = np.zeros(ref_shape,dtype=bool)
            
            #check if the MNDWI index is necessary and if it exists
            if 'mndwi' in self.required_indices and 'mndwi' not in self.bands:
                mndwi,mndwi_mask = self.calc_normalized_difference(self.bands['Green'],self.bands['Mir2'],invalid_mask)
                invalid_mask |= mndwi_mask
                self.bands.update({'mndwi':mndwi})

            #check if the NDWI index exist
            if 'ndwi' in self.required_bands and 'ndwi' not in self.bands.keys():
                ndwi,ndwi_mask = self.calc_normalized_difference(self.bands['Green'],self.bands['Nir'],invalid_mask)
                invalid_mask |= ndwi_mask
                self.bands.update({'ndwi':ndwi})

            #check if the MBWI index exist
            if 'mbwi' in self.required_bands and 'mbwi' not in self.bands.keys():
                mbwi,mbwi_mask = self.calc_mbwi(self.bands,3,invalid_mask)
                invalid_mask |= mbwi_mask

            #check if the list contains the required bands
            for band in self.listify(self.bands_keys):
                if band == 'otsu' or band == 'canny':
                    continue
                if band not in self.bands.keys():
                    raise OSError('Band {}, not available in the dictionary'.format(self.band))
                if type(self.bands[band]) is not np.ndarray:
                    raise OSError('Band {} is not a numpy array'.format(self.band))
                if ref_shape != self.bands[band].shape:
                    raise OSError('Bands {} and {} with different size in clustering core'.format(self.band, ref_band))
                else:
                    pass
                    # print("band : ",band+"In require bands list")

            ## run_detect_water
            # print('My.DataComponent : self.bands_keys[0] :',self.bands_keys[0])
            #if passed options,override the existing options
            if self.bands_keys[0] == 'otsu':
                cluster_matrix = self.apply_otsu_treshold()
            elif self.bands_keys[0] == 'canny':
                cluster_matrix = self.apply_canny_treshold()
            elif False:
                cluster_matrix = None

            #Transform the rasters in a matrix where each band is a column
            data_as_columns = self.bands_to_columns(self.bands,invalid_mask)

            # two line vectors indicating the indexes (line column) of valid pixels
            ind_data = np.where(~invalid_mask)   

            # if algorithm is not kmeans,split data for a smaller ser (for performnce purposes)
            if self.clustering_method == 'kmean':
                train_data_as_columns=data_as_columns
            else:
                train_data_as_columns,ts= self.get_train_test_split(data_as_columns,self.train_size,self.min_train_size,self.max_train_size)

            #split1
            split_train_data_as_columns = self.split_data_by_bands(self.bands,train_data_as_columns,self.bands_keys)
            #split2
            split_data_as_columns = self.split_data_by_bands(self.bands,data_as_columns,self.bands_keys)


            #find best_k
            best_k = self.find_best_k(split_train_data_as_columns)

            #apply the clusterization algorithm and return labels and train dataset
            train_clusters_labels = self.apply_cluster(split_train_data_as_columns,best_k)

            #cals statistics for each cluster
            self.clusters_params = self.calc_clusters_params(train_data_as_columns,train_clusters_labels,best_k)

            #detect the water cluster
            water_cluster = self.identify_water_cluster(self.detect_water_cluster,self.bands)

            if self.clustering_method != 'kmeans':
                clusters_labels = self.supervised_classification(split_data_as_columns,split_train_data_as_columns,train_clusters_labels)
            else:
                clusters_labels = train_clusters_labels
            # print('My.DataComponent : clusters_labels :',clusters_labels)
            # after obtain the final labels,clip bands with superios limit
            for band,value in zip(self.clip_band,self.clip_sup_value):
                if value is not None:
                    if self.glint_mode and self.glint_processor is not None:
                        print('0')
                    else:
                        comp_array = value
                    clusters_labels[(clusters_labels == water_cluster['clusterid']) & (self.bands[band][~invalid_mask]>comp_array)] = -1
            #after obtainting the final labels,clip bands with inferior limit
            for band,value in zip(self.clip_band,self.clip_inf_value):
                if value is not None:
                    if self.glint_mode and self.glint_processor is not None:
                        print('0')
                    else:
                        comp_array = value
                    clusters_labels[(clusters_labels == water_cluster['clusterid']) & (self.bands[band][~invalid_mask]<comp_array)] = -1
            
            #create an cluster array based on the cluster result (water will be value1)
            cluster_matrix = self.create_matrice_cluster(ind_data,self.bands,clusters_labels,water_cluster,best_k)
            water_mask = np.where(cluster_matrix == 1,1,np.where(invalid_mask == 1,255,0)).astype('int8')
            watermask0 = water_mask==0
            watermask1 = water_mask==1
            return watermask1