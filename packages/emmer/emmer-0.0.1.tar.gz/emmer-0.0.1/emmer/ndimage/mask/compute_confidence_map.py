
def compute_confidence_map(emmap, apix, window_size,fdr=0.01, lowPassFilter_resolution=None,remove_temp_files=True, return_fdr_value=False):
    '''
    Compute a confidence map from a EM map
    
    Parameters
    ----------
    emmap   : numpy.ndimage
        emmap data 
    apix : float
        Pixel size of the EM map
    window_size : int
        Window size for the confidence map
    apix : float
        Pixel size of the EM map
    fdr : float, optional
        False discovery rate. The default is 0.01.
    lowPassFilter_resolution : float, optional
        Low pass filter resolution. The default is None.
    remove_temp_files : bool, optional
        Remove temporary files. The default is True.
    
    Returns
    -------
    confidence_map : ndarray
        Confidence map
    fdr_threshold : float
        FDR threshold
    '''
    import numpy as np
    from emmer.include.confidenceMapUtil.confidenceMapMain import calculateConfidenceMap
    import os, shutil, time
    
    current_cwd = os.getcwd()
    timestamp =  str(time.time())
    temp_dir = current_cwd + '/fdr_output_temp_'+timestamp
    os.mkdir(temp_dir)
    os.chdir(temp_dir)
    confidenceMap,locFiltMap,locScaleMap,binMap,maskedMap = calculateConfidenceMap(
        em_map=emmap,apix=apix,noiseBox=None,testProc=None,ecdf=None,
        lowPassFilter_resolution=lowPassFilter_resolution,method=None, 
        window_size=window_size,windowSizeLocScale=None, locResMap=None,
        meanMap=None,varMap=None,fdr=fdr,modelMap=None,stepSize=None,mpi=None)
    
    fdr_threshold = np.min(maskedMap[np.nonzero(maskedMap)])
    
    os.chdir(current_cwd)
    if remove_temp_files:
        print("Clearing temporary files")
        shutil.rmtree(temp_dir)
    
    if return_fdr_value:
        return confidenceMap, fdr_threshold
    else:
        return confidenceMap