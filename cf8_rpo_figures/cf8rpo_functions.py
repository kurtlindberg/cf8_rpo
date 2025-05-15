# Postglacial carbon cycling history of a northeastern Baffin Island lake catchment inferred from ramped pyrolysis oxidation and radiocarbon dating

## Manuscript authors: Kurt R. Lindberg, Elizabeth K. Thomas, Brad E. Rosenheim, Gifford H. Miller, Julio Sepulveda, Devon R. Firesinger,
## Gregory A. de Wet, Benjamin V. Gaglioti

## DOI: pending

## Code Author: Kurt R. Lindberg

### Supporting functions for cf8_rpo_figures Python scripts ###


## See cf8_rpo_conda_env.ymlimport pandas as pd
import numpy as np
import pyleoclim as pyleo
from pylipd.lipd import LiPD

## Create age ensemble mapping function for associated LiPD files
def mapAgeEnsembleToPaleoData(ensembleValues, paleoValues, ensembleDepth, paleoDepth,
                             value_name = None,value_unit = None,time_name = None,time_unit = None):
    """ Map the depth for the ensemble age values to the paleo values

    Parameters
    ----------

    ensembleValues : array
        A matrix of possible age models. Realizations
        should be stored in columns

    paleoValues : 1D array
        A vector containing the paleo data values. The vector
        should have the same length as depthPaleo

    ensembleDepth : 1D array
        A vector of depth. The vector should have the same
        length as the number of rows in the ensembleValues

    paleoDepth : 1D array
        A vector corresponding to the depth at which there
        are paleodata information

    value_name : str
        Paleo data value name

    value_unit : str
        Paleo data value unit

    time_name : str
        Time name

    time_unit : str
        Time unit

    Returns
    -------

    ensemble : pyleoclim.EnsembleSeries
        A matrix of age ensemble on the PaleoData scale

    """

    #Make sure that numpy arrays were given and try to coerce them into vectors if possible
    ensembleDepth=np.squeeze(np.array(ensembleDepth))
    paleoValues = np.squeeze(np.array(paleoValues))
    paleoDepth = np.squeeze(np.array(paleoDepth))

    #Check that arrays are vectors for np.interp
    if paleoValues.ndim > 1:
        raise ValueError('ensembleValues has more than one dimension, please pass it as a 1D array')
    if ensembleDepth.ndim > 1:
        raise ValueError('ensembleDepth has more than one dimension, please pass it as a 1D array')
    if paleoDepth.ndim > 1:
        raise ValueError('paleoDepth has more than one dimension, please pass it as a 1D array')

    if len(ensembleDepth)!=np.shape(ensembleValues)[0]:
        raise ValueError("Ensemble depth and age need to have the same length")

    if len(paleoValues) != len(paleoDepth):
        raise ValueError("Paleo depth and age need to have the same length")

    #Interpolate
    ensembleValuesToPaleo = np.zeros((len(paleoDepth),np.shape(ensembleValues)[1])) #placeholder

    for i in np.arange(0,np.shape(ensembleValues)[1]):
        ensembleValuesToPaleo[:,i]=np.interp(paleoDepth,ensembleDepth,ensembleValues[:,i])

    series_list = []

    for s in ensembleValuesToPaleo.T:
        series_tmp = pyleo.Series(time=s, value=paleoValues,
                       verbose=False,
                       clean_ts=False,
                       value_name=value_name,
                       value_unit=value_unit,
                       time_name=time_name,
                       time_unit=time_unit)
        series_list.append(series_tmp)

    ensemble = pyleo.EnsembleSeries(series_list=series_list)

    return ensemble


## Define function for importing LiPD data

# filename = name of LiPD file
# paleoData_variableName = column name of variable being imported
# depth_name = column name of depth variable (for using depths in multiple paleoData tables)
# val_unit = unit of the variable being imported
# ens_num = index of paleo data table containing the imported variable

def getlipd(filename,
            paleoData_variableName,
            depth_name,
            val_unit,
            ens_num=0):

    D = LiPD()
    D.load(filename)

    ensemble_df = D.get_ensemble_tables()
    pd.set_option('display.max_columns', None)
    # print(ensemble_df)

    timeseries, df = D.get_timeseries(D.get_all_dataset_names(), to_dataframe=True)
    # print(df)
    # print(df.columns)
    df['paleoData_variableName'].unique()

    df_row = df.loc[df['paleoData_variableName']==paleoData_variableName]
    paleoDepth = np.array(*df_row[depth_name])
    paleoAgeMedian = np.array(*df_row['ageMedian'])
    paleoValues = np.array(*df_row['paleoData_values'])
    # paleo_depth_units = df_row['depthUnits']
    value_name = paleoData_variableName
    value_unit = val_unit
    ensembleDepth = ensemble_df.iloc[ens_num]['ensembleDepthValues']
    ensembleValues = ensemble_df.iloc[ens_num]['ensembleVariableValues']
    ensemble_depth_units = ensemble_df.iloc[ens_num]['ensembleDepthUnits']
    time_name = 'Time'
    time_unit = f'{ensemble_df.iloc[ens_num]["ensembleVariableName"]} {ensemble_df.iloc[ens_num]["ensembleVariableUnits"]}'
    # print(type(ensembleValues))
    # print(ensembleValues)
    # print(ensembleDepth)
    # print(paleoValues)
    # print(f'Num rows in ensembleValues: {ensembleValues.shape[0]}, Length of ensembleDepth: {len(ensembleDepth)}')

    ensemble = mapAgeEnsembleToPaleoData(
        ensembleValues=ensembleValues,
        paleoValues=paleoValues,
        ensembleDepth=ensembleDepth,
        paleoDepth=paleoDepth,
        value_name=value_name,
        value_unit=value_unit,
        time_name=time_name,
        time_unit=time_unit
    )

    age_axis = pd.DataFrame({'depth':paleoDepth, 'ageMedian':paleoAgeMedian, 'paleoData_values':paleoValues})

    return ensemble, age_axis


## Convert fraction modern values to uncalibrated 14C yrs
def fm_to14c(fm):
    fm_arr = np.array(fm)
    to14c = -8033*np.log(fm_arr)

    return to14c


## Convert fraction modern values to delta 14C
def fm_todel14c(fm, yc):
    lam = 1/8267
    fm_arr = np.array(fm)
    todel14c = ((fm_arr * math.exp(lam*(1950-yc))) -1) * 1000

    return todel14c


## Convert delta 14C to uncalibrated 14C yrs
def del14c_to14c(del14c, yc):
    lam = 1/8267
    del14c_arr = np.array(del14c)
    tofm = ((del14c/1000)+1)/(math.exp(lam*(1950-yc)))
    to14c = fm_to14c(tofm)

    return to14c
