ReadMe for dataset accompanying article PONE-D-15-10019: Modeling and mapping the probability of occurrence of invasive wild pigs across the contiguous United States. McClure, M.L., Burdett, C.L., Farnsworth, M.L., Lutman, M.W., Theobald, D.M., Riggs, P.D., Grear, D.A., Miller, R.S.
 2015-05-14
This readme file describes the data file accompanying the above publication.  For any further queries please contact meredith@csp-inc.org.  
“wildpig_sdm_data.csv”
This is the final dataset used to derive the wild pig distribution model for the contiguous United States presented in the accompanying publication, along with predictive model output values.  Table rows represent values for each HUC10 level watershed in the contiguous United States.  Table column values are described in detail below.  For additional information regarding aggregation of wild pig presence to HUC10 watersheds, derivation of covariates, model fitting, model selection, and model validation procedures, please see the Methods section of the accompanying publication.
Please note that spatial information (HUC10 identification codes) has been stripped from the dataset.  Spatial data for wild pig presence was provided by a third party, and the authors are not at liberty to provide this information due to a history of hunters using the data to locate wild pig populations then bait, trap, and relocate them for hunting purposes, which interfered with ongoing control and eradication efforts.  Spatial data are available by request through the Southeastern Cooperative Wildlife Disease Study (SCWDS) National Feral Swine Mapping System (http://swine.vet.uga.edu/nfsms/).  The system administrator, Joe Corn, can be contact at feralpig@uga.edu.
Column Values
1)  “Presence”
Indicator variable for wild pig presence.  1 indicates recorded presence, 0 indicates that pigs were not reported present (but cannot be considered absent).
2)  “zAvgAb35”
Standardized mean number of days above 35 degrees Celsius across weather stations within 250 km (up to 10 closest stations), adjusted for average adiabatic lapse rate and averaged across 30 years of observations (or all years in a 30 year period for which data were available).  Estimated from National Oceanic and Atmospheric Administration (NOAA) weather station data.
3) “zAvgBeln4”
Standardized mean number of days below 35 degrees Celsius across weather stations within 250 km (up to 10 closest stations), adjusted for average adiabatic lapse rate and averaged across 30 years of observations (or all years in a 30 year period for which data were available). Estimated from National Oceanic and Atmospheric Administration (NOAA) weather station data.
4) “zSnowDep”
Standardized 10 year mean snow depth on April 1 (the estimated date of annual maximum accumulation), estimated from the Snow Data Assimilation System (SNODAS).
5) “zdH2O”
Standardized mean distance to nearest perennial (>3 cubic feet/second) stream or water body perimeter, estimated from National Hydrography Dataset Plus (NHDPlus).
6) “zPercForest”
Standardized percent watershed area with deciduous, evergreen, or mixed forest cover, estimated from the 2006 National Land Cover Dataset (NLCD).
7) “zForage”
Standardized percent watershed area classified as hard mast-producing or crop cover, estimated from the GAP land cover dataset and the National Agricultural Statistics Service (NASS) 2012 CropScape dataset.
8) “zHeterog”
Standardized mean number of key habitat elements (water, forest cover, and forage) available within a radius defined by the average wild pig sounder group home range size (see Table S1). Estimated using the National Hydrography Dataset Plus (NHDPlus), GAP land cover dataset, and National Agricultural Statistics Service (NASS) 2012 CropScape dataset.
9) “PrOcc”
Relative probability of wild pig occurrence derived using a logistic discrimination function to relate wild pig presence (1) to physiological and ecological covariates (2-8).  Please see the accompanying publication for full methodological details.
