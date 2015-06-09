# -*- coding: utf-8 -*-
"""
Created on Mon Jun 08 11:26:38 2015

@author: Jwink

Defines useful/wordy functions for the Data_Concat_and_Preproc.py file

"""

####################### Functions to help preprocessing #######################


# drop useless columns in tsv data
def drop_cols(dat):
        dat.drop(['ExportDate','StudioVersionRec','StudioProjectName',
              'StudioTestName','RecordingName','RecordingDate',
              'RecordingDuration','FixationFilter','MediaName','MediaWidth',
              'MediaHeight','SegmentName','SegmentStart','SegmentEnd',
              'SegmentDuration','SceneName','SceneSegmentStart',
              'SceneSegmentEnd','SceneSegmentDuration','LocalTimeStamp',
              'EyeTrackerTimestamp','MouseEventIndex','MouseEvent',
              'MouseEventX (ADCSpx)','MouseEventY (ADCSpx)',
              'MouseEventX (MCSpx)','MouseEventY (MCSpx)','ExternalEventIndex',
              'ExternalEvent','ExternalEventValue','EventMarkerValue',
              'FixationPointX (MCSpx)','FixationPointY (MCSpx)',
              'GazePointX (MCSpx)','GazePointY (MCSpx)',
              'GazePointLeftX (ADCSmm)','GazePointLeftY (ADCSmm)',
              'GazePointRightX (ADCSmm)','GazePointRightY (ADCSmm)',
              'StrictAverageGazePointX (ADCSmm)',
              'StrictAverageGazePointY (ADCSmm)','EyePosLeftX (ADCSmm)',
              'EyePosLeftY (ADCSmm)','EyePosLeftZ (ADCSmm)',
              'EyePosRightX (ADCSmm)','EyePosRightY (ADCSmm)',
              'EyePosRightZ (ADCSmm)','CamLeftX','CamLeftY','CamRightX',
              'CamRightY','IRMarkerCount','IRMarkerID','PupilGlassesRight'], 
              axis=1, inplace=True)
        return dat

        
# sync times in behavioral and eye tracking data files
def sync_t(t_beh, beh_dat, eye_dat):
    # get eye tracker timestamp when 'B' was pressed
    t_eye = eye_dat.RecordingTimestamp[eye_dat.loc[eye_dat.KeyPressEvent == 'B'].index.tolist()[0]]    
    # subtract sync time from ET time stamps
    eye_dat.RecordingTimestamp = eye_dat.RecordingTimestamp - t_eye 
    # subtract experiment start timestamp from other matlab timestamps
    beh_dat.Fix_Onset = (beh_dat.Fix_Onset - t_beh) * 1000
    beh_dat.Trial_Onset = (beh_dat.Trial_Onset - t_beh) * 1000
    # turn RT into milliseconds
    beh_dat.Response_Time = beh_dat.Response_Time * 1000
    beh_dat.Fix_Time = beh_dat.Fix_Time * 1000
    # return data frames
    return (beh_dat, eye_dat)
    
    
# trim excess data points from eye tracking data    
def trim(beh_dat, eye_dat):
    # drop rows before time sync
    eye_dat.drop(eye_dat.index[eye_dat.RecordingTimestamp < 0], inplace=True)
    frames = []
    # loop for extracting relevant data based on trial times
    for row in range(beh_dat.shape[0]):
        # get start timestamp
        start_idx = int(beh_dat.Trial_Onset[row])
        # get end timestamp
        end_idx = int(beh_dat.Trial_Onset[row] + beh_dat.Response_Time[row])
        # select et data in between start and end timestamps of trial        
        tmp_eye = eye_dat.loc[eye_dat['RecordingTimestamp'].isin(range(start_idx,end_idx))]
        # append Px information to this chunk of data        
        px_series = pd.Series(beh_dat.Px[row],name='Px').repeat(tmp_eye.shape[0])
        px_series.index = tmp_eye.index
        tmp_eye = concat([tmp_eye, px_series], axis=1)
        # append trial information to this chunk of data        
        trial_series = pd.Series(beh_dat.Trial[row],name='Trial').repeat(tmp_eye.shape[0])
        trial_series.index = tmp_eye.index
        tmp_eye = concat([tmp_eye, trial_series], axis=1)
        # append phase information to this chunk of data
        phase_series = pd.Series(beh_dat.Phase[row],name='Phase').repeat(tmp_eye.shape[0])
        phase_series.index = tmp_eye.index
        tmp_eye = concat([tmp_eye, phase_series], axis=1)
        # add selected data to frames holder
        frames.append(tmp_eye)
    
    # sew it all together
    eye_dat = pd.concat(frames)    
    
    return eye_dat








            