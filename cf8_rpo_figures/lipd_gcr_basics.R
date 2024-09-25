# Manuscript title: Postglacial carbon cycling history of a northeastern Baffin
# Island lake catchment inferred from ramped pyrolysis oxidation and radiocarbon
# dating

# Manuscript authors: Kurt R. Lindberg, Elizabeth K. Thomas, Brad E. Rosenheim,
# Gifford H. Miller, Julio Sepulveda, Devon F. Firesinger, Gregory A. de Wet,
# Benjamin V. Gaglioti

# DOI: pending

## Basic commands for working with LiPD files, Bacon, and GeoChronR

# Author: Kurt R. Lindberg
# Last edited: 09/25/2024

# Install necessary packages if not available in the R environment
install.packages("lipdR")
install.packages("geoChronR")
install.packages("ggplot2")
install.packages("magrittr")

# Add necessary packages to R environment
library(lipdR)
library(geoChronR)
library(ggplot2)
library(magrittr)

setwd("~/Documents/PACEMAP/CH1 Lake CF8 Holocene RPO Chronology/figures/Manuscript Figures/figure_codedata")

# Open LiPD file using GUI
d <- readLipd()

# Run Bacon.R to generate age-depth model ensemble based on chronology tables
d <- runBacon(d)

# Add age ensemble to each paleoData table
# Repeat this line for each paleoData table you want to map the age model to
d <- mapAgeEnsembleToPaleoData(d)

# Save age model and ensemble to LiPD file
writeLipd(d)

# Select age ensemble from a specific paleoData table
d_ae <- selectData(d)
ae <- d_ae$values
age_med <- apply(ae, 1, median)

# Export entire age ensemble to a csv file
write.csv(ae)

# Remove mapped age ensemble from a selected paleoData table

# If you have multiple data tables in your LiPD file, change the number in
# measurementTable[[#]] to remove the age ensembe and age median from each one
d$paleoData[[1]]$measurementTable[[1]]$ageEnsemble <- NULL
d$paleoData[[1]]$measurementTable[[1]]$ageMedian <- NULL
