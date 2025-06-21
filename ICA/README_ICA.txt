README: ICA Data and Documentation
==================================

This folder contains all files necessary for Independent Component Analysis (ICA) processing across participants.
For each participant, three '.csv' files and one '.joblib' file are included:

File Descriptions
-----------------

1. Bad Electrodes (sub-{subject}_bad_elec.csv)
   This file lists the electrodes identified as malfunctioning or unreliable for a given participant. 
   To ensure proper ICA decomposition, these channels should be removed prior to ICA fitting on this dataset. 
   Each electrode is accompanied by a brief justification for removal.

2. Rejected Components – Eye Artefacts (sub-{subject}_deleted_eye_components.csv)
   This file contains the ICA components that were rejected because they are likely to be eye artefacts. 
   Removing these components helps to eliminate eye-related noise from the EEG signal. 
   Each rejected component includes a reasoning for its removal.

3. Retained Components – Other Artefacts (sub-{subject}_retained_noise_components.csv)
   This file documents components that are suspected to represent other forms of noise such as muscle activity or environmental artefacts. 
   These components were not removed in the current preprocessing pipeline, but have been flagged for potential future exclusion. 
   Reasons for flagging are also included per component.

4. ICA Solution ({subject}_ICA_.joblib)
   This is the '.joblib' file containing the fitted ICA solution for each participant. 
   These files can be loaded using 'joblib.load()' for reuse or further inspection.

5. Visualizations of the bad electrodes.
   This file contains visualizations of the EEG electrodes that were marked as artifactual. A more detailed justification for the rejection of each electrode can be found in the Bad Electrodes file. Electrodes that were flagged during the experiment are not always clearly artifactual in the signal. However, to maintain consistency across participants and sessions, these were removed to be sure. In cases where electrodes exhibited odd oscillatory behaviour, a shorter time window was selected in the plots to better highlight the abnormal patterns. In other cases, a longer time window was chosen to highlight artifacts that were evident over a broader timescale.

Notes
-----

- All '.csv' files contain both the artifactual electrodes or components and brief explanations for each decision.
- The current preprocessing pipeline removes only eye-related components. 

