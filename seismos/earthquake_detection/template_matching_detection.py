# %%
import logging
from eqcorrscan.core.match_filter import match_filter
import glob
import os
import sys
from eqcorrscan.core.match_filter import Tribe
from eqcorrscan.utils.pre_processing import shortproc
import obspy

# Directory containing hourly files
directory = '/Volumes/kwintsheul/02_data_converted/hourlyfiles/2019/'

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('log_file.txt')  # Specify the log file path
    ]
)

# Configuration parameters
freqmin = 4
freqmax = 25
templ_len = 1
prepick = 0
num_cores = 4
threshold = 10.0
min_trig = 4
trig_int = 6.0

st_template = obspy.read(
    os.path.join("/Volumes/kwintsheul/04_earthquake_catalog/events/",
                 "20190714T0848/20190714T0848hour_file.mseed"))

samp_rate = st_template[0].stats.sampling_rate
stations = [tr.stats.station for tr in st_template]
tribe = Tribe().construct(
    method='from_meta_file',
    lowcut=freqmin,
    highcut=freqmax,
    samp_rate=samp_rate,
    length=templ_len,
    prepick=prepick,
    swin='all',
    plot=False,
    parallel=False,
    meta_file='2019_07_14T0848.xml',
    st=st_template,
    filt_order=3,
    name="Kwintsheul"
)
# Loop over days and hours
for julday in range(306, 312):
    if julday == 295:
        startat = 6
    else:
        startat = 0 
    for hour in range(startat, 24):
        hourly_file = os.path.join(
            directory, "*", str(julday), f"*_{julday}_{hour:02d}*.mseed")

        # Skip if no files match the pattern
        if len(glob.glob(hourly_file)) == 0:
            continue

        logging.info(f"Processing Julian day: {julday}, hour: {hour}")

        # Load seismic data
        try:
            st_complete = obspy.read(hourly_file)
            st = obspy.Stream()

            # Filter seismic data and select relevant stations
            for tr in st_complete:
                if tr.stats.station in stations:
                    st.append(tr)
            if len(st) == 0:
                continue

            # Pre-process seismic data
            st = shortproc(
                st=st,
                lowcut=freqmin,
                highcut=freqmax,
                filt_order=3,
                samp_rate=samp_rate
            )
            logging.info(f"Seismic data pre-processing complete")

            # Perform template matching detection
            detections = match_filter(
                template_names=['2019_07_14t08_48_31'],
                template_list=[tribe[0].st],
                st=st,
                threshold=threshold,
                threshold_type='MAD',
                min_trig=min_trig,
                trig_int=trig_int,
                cores=4
            )
            logging.info(
                f"Template matching detection complete. Found {len(detections)} detections")

            # Save detections to a file
            for detection in detections:
                detection.write(f"detections_julday{julday}.csv", append=True)
            logging.info("Detections saved to file")

        except Exception as e:
            logging.error(f"An error occurred during processing: {str(e)}")

logging.info("Processing complete")

# %%
# import obspy
# st = obspy.read("/Volumes/kwintsheul/02_data_converted/hourlyfiles/2019/0*/174/*_174_08*.mseed")

# # %%
# st = obspy.read("/Users/localadmin/Dropbox/GitHub/seismos/seismos/earthquake_detection/2019-06-23T0802.mseed")
# time = obspy.UTCDateTime("2019-06-23T08:02:08.068000Z")
# st = st.trim(starttime=time-2, endtime=time+5)
# # st.write("/Users/localadmin/Dropbox/GitHub/seismos/seismos/earthquake_detection/2019-06-23T0802.mseed", format="MSEED")
# st.plot()

# # %%
# # open with pyrocko snuffle
# import pyrocko
