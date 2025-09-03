"""
MIT License

Copyright (c) 2022 PolarRS

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import re
from datetime import datetime

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import spectral
from os.path import join,basename,normpath



class HSCam:
    """ HSCam
        Container for HS camera data from SpecimIQ instrument.

    ...

    Attributes
    ----------
    datacube : 3D-Array (512,512,204)
        entire raw reflectance (not calibrated)

    wr_spectrum : 1D-Array (204)
        reflectance of white reference for each wavelength

    wl : 1D-Array (204)
        wavelengths list

    RGB : default RGB bands numbers (3)



    Methods
    -------
    get_img_at_wl(wl, calibtrated=True)
        returns image at certain wavelength specified by wl
        if calibrated is True, then it is divided by white reference at that wavelength
        otherwise it is directly returned
    
    quicklook(save=False)
        displays (if save==False) or saves (if save is a string) a RGB quicklook of the image
    
    get_raw_spectrum_for_point(y,x,r=3)
        returns the raw spectrum at all all wavelength at position y,x 
        where r sets tha radius for an average value (to reduce noise)
        
    set_wr_spectrum(y, x, r=3):
        sets the spectrum for the white reference at position y,x
        where r is the radius for averaging (noise reduction)

    get_cal_spectrum_for_point(self, y, x, r=3):
        return self.get_raw_spectrum_for_point(y, x, r=r)/self.wr_spectrum

    def plot_spec_and_loc(self, locs, r=3):
        create an overview plot (like quicklook) together with 
        spectrum of individual points. The locs variable 
        is a list of [x,y] positions like [[x1,y1],[x2,y2], ...] and the 
        r variable defines the radius for the averaging

    """
    _loaded_data = None
    _wr_spectrum = None

    def __init__(self, folder, wr_loc=None,from_raw=True):

        self.datapath = folder
        self.basename = folder.split("/")[-1]
        self._metadata = open(folder+"/metadata/" + self.basename+".xml").read()

        self.datetime, self.lat, self.lon, self.integration_time ,self.wrmode= self.__get_metadata()

        if from_raw:
            bname=basename(normpath(folder))+".hdr"
            rawdat_f=join(folder,"capture",bname)
            dark_f=join(folder,"capture","DARKREF_"+bname)  
            white_f=join(folder,"capture","WHITEREF_"+bname)    

            if self.wrmode=="Custom":
                #in Custom mode the WR can be from a different 
                # integration time and has a different dark reference
                whitedark_f=join(folder,"capture","WHITEDARKREF_"+bname)
            elif self.wrmode=="Simultaneous":
                #in Simultaneous mode the same dark reference is used
                # as in the raw image
                whitedark_f=join(folder,"capture","DARKREF_"+bname)
            
            #darref and rawdat have same integration time tint
            darkref=spectral.open_image(dark_f)
            rawdat=spectral.open_image(rawdat_f)
            whiteref=spectral.open_image(white_f)
            whitedarkref=spectral.open_image(whitedark_f)
            
            self.dbands = tuple(map(int, rawdat.metadata["default bands"]))
            self.wl = np.array(rawdat.bands.centers)
            
            darkref=darkref.asarray()

            #original white reference may be at different integration time
            #formula on page 9 applied
            traw=float(rawdat.metadata["tint"])
            twr=float(whiteref.metadata["tint"])
            self._loaded_data=(rawdat[:,:,:]-darkref[:,:,:])/(whiteref[:,:,:]-whitedarkref[:,:,:])*twr/traw
            self._loaded_data=self._loaded_data[::-1,:,:]

        else:

            datafile = folder+"/results/REFLECTANCE_"+self.basename+".hdr"

            simg = spectral.open_image(datafile)
            self.wl = np.array(simg.bands.centers)
            self.dbands = tuple(map(int, simg.metadata["default bands"]))
            self._loaded_data=simg.asarray()[::-1,:,:]

        if wr_loc is not None:
            self.set_wr_spectrum(wr_loc[0], wr_loc[1], r=3)

    def get_img_at_wl(self, wl, calibrated=True):
        assert (wl > np.min(self.wl)) & (wl < np.max(self.wl))
        ind = np.argmin(abs(self.wl-wl))
        if calibrated:
            return self._loaded_data[:,:,ind]/self._wr_spectrum[ind]
        else:
            return self._loaded_data[:,:,ind]

    def __get_metadata(self):
        datestr = re.findall('"datetime".+?>(.*?)<', self._metadata)[0]
        lat = float(re.findall('"latitude".+?>(.*?)<', self._metadata)[0])
        lon = float(re.findall('"longitude".+?>(.*?)<', self._metadata)[0])
        wrmode=re.findall('"WR_mode".+?>(.*?)<', self._metadata)[0]
        itime = float(re.findall(
            '"integration_time".+?>(.*?)<', self._metadata)[0])
        return datetime.strptime(datestr, "%d %b %Y %H:%M:%S +0000"), lat, lon, itime,wrmode

    @property
    def datacube(self):
        return self._loaded_data

    @property
    def wr_spectrum(self):
        if self._wr_spectrum is None:
            raise AttributeError(
                "no white reference set, use method set_wr_spectrum")
        else:
            return self._wr_spectrum

    def quicklook(self, save=False):
        data = self.datacube[:,:,self.dbands].transpose(
            (1, 0, 2))/self.integration_time
        vmin, vmax = np.percentile(data, (.1, 99.9))

        n = matplotlib.colors.Normalize(vmin, vmax, clip=True)
        if save:
            plt.imsave(save, n(data))
        else:
            plt.imshow(n(data))
            return plt.gca()

    def get_raw_spectrum_for_point(self, y, x, r=3):
        if r == 1:
            return self.datacube[x, y, :]
        rh = r//2
        return self.datacube[x-rh:x+rh, y-rh:y+rh, :].mean(axis=(0, 1))

    def set_wr_spectrum(self, y, x, r=3):
        self._wr_spectrum = self.get_raw_spectrum_for_point(y, x, r=r)

    def get_cal_spectrum_for_point(self, y, x, r=3):
        return self.get_raw_spectrum_for_point(y, x, r=r)/self.wr_spectrum

    def plot_spec_and_loc(self, locs, r=3):
        fig, axs = plt.subplots(ncols=2, figsize=[10, 3])
        plt.sca(axs[0])
        self.quicklook()
        for loc in locs:
            axs[0].plot([loc[1]], [loc[0]], "o")
            axs[1].plot(self.wl, self.get_cal_spectrum_for_point(
                loc[0], loc[1], r=r)) #x and y switched
        return fig

