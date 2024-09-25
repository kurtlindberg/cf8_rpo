## Lake CF8 MixSIAR - OC Endmember Contributions
# Example script in Supplemental Table 2
# Endmembers: Contemporaneous aquatic biomass
#             Postglacial (<12.5 ka) soil
#             MIS 5 soil

# Postglacial carbon cycling history of a northeastern Baffin Island lake catchment inferred from ramped pyrolysis oxidation and radiocarbon dating

# Manuscript authors: Kurt R. Lindberg, Elizabeth K. Thomas, Brad E. Rosenheim, Gifford H. Miller, Julio Sepulveda, Devon R. Firesinger,
# Gregory A. de Wet, Benjamin V. Gaglioti

# DOI: pending

# Author: Kurt R. Lindberg
# Last edited: 09/25/2024

# Based on example code from Douglas et al. (2022) Supplemental File 2
# DOI: https://doi.org/10.1016/j.chemgeo.2022.120887


# Add necessary packages to R library
# Use 'install.packages("package")' to install missing packages
library(ggplot2)
library(MASS)
library(RColorBrewer)
library(reshape)
library(reshape2)
library(lattice)
library(MCMCpack)
library(ggmcmc)
library(coda)
library(loo)
library(bayesplot)
library(splancs)
library(dplyr)
library(devtools)
library(OpenMx)

# The following packages require JAGS (Just Another Gibbs Sampler) to be installed
# Files and installation instructions: https://sourceforge.net/projects/mcmc-jags/
library(rjags)
library(R2jags)
library(MixSIAR)

# Set working directory
setwd("~/cf8_rpo/cf8_rpo_mixsiar")

### EXAMPLE SCRIPT FROM SUPPLEMETNAL TABLE 2 ###

# Test MixSIAR using a single CF8 RPO depth + CO2 split
# Set to CF817-03 depth 1 (5-6.5 cm), CO2 split 1 (lowest temperature)

## Import model input csv files

# Load csv file of mixture data
mix <- load_mix_data(filename = "mix/mix_depth_1_split_1.csv",
                     iso_names = c("d13C", "FM"),
                     factors = NULL,
                     fac_random = NULL,
                     fac_nested = NULL,
                     cont_effects = NULL)

# Load csv file of endmember (source) data
source <- load_source_data(filename = "source/source_depth_1_split_1.csv",
                           source_factors = NULL,
                           conc_dep = FALSE,
                           data_type = "means",
                           mix)

# Load csv file of discrimination factors for each endmember (all set to 0)
discr <- load_discr_data(filename = "discr/discr_depth_1_split_1.csv",
                         mix)

# Plot endmember statistics on tracer axes
plot_data(filename = "isospace_plot_depth1_split_1",
          plot_save_pdf = TRUE,
          plot_save_png = FALSE,
          mix,
          source,
          discr)

# Plot prior structure
plot_prior(alpha.prior = 1,
           source,
           plot_save_pdf = TRUE,
           plot_save_png = FALSE,
           filename = "prior_plot_depth_1_split_1")

# Start up MixSIAR
model_filename = "MixSIAR_model_depth_1_split_1.txt"
resid_err <- FALSE
process_err <- TRUE
write_JAGS_model(model_filename, resid_err, process_err, mix, source)
jags.1 <- run_model(run = "extreme", mix, source, discr, model_filename)

# Save MixSIAR outputs
output_options <- list(summary_save = TRUE,
                      summary_name = "summary_statistics_depth_1_split_1",
                      sup_post = FALSE,
                      plot_post_save_pdf = TRUE,
                      plot_post_name = "postderior_density_depth_1_split_1",
                      sup_pairs = FALSE,
                      plot_pairs_save_pdf = TRUE,
                      plot_pairs_name = "pairs_plot_depth_1_split_1",
                      sup_xy = TRUE,
                      plot_xy_save_pdf = FALSE,
                      plot_xy_name = "xy_plot_depth_1_split_1",
                      gelman = TRUE,
                      heidel = FALSE,
                      geweke = TRUE,
                      diag_save = TRUE,
                      diag_name = "diagnostics_depth_1_split_1",
                      indiv_effect = FALSE,
                      plot_post_save_png = FALSE,
                      plot_pairs_save_png = FALSE,
                      plot_xy_save_png = FALSE,
                      diag_save_ggmcmc = FALSE)

output_JAGS(jags.1, mix, source, output_options)


### RUN ALL CO2 SPLITS IN A SINGLE DEPTH ###

# Run MixSIAR using a single sediment depth with all CO2 splits
# Set to CF817-03 depth 1 (5-6.5 cm)
# NOTE: CF817-03 depths 3 (45-46.5 cm) and 6 (95-96.5 cm) only have CO2 splits 1-4

for (split in 1:5) {

  ## Import model input csv files

  # Load csv file of mixture data
  mix <- load_mix_data(filename = paste0("input/mix_depth_1_split_",split,".csv"),
                      iso_names = c("d13C", "FM"),
                      factors = NULL,
                      fac_random = NULL,
                      fac_nested = NULL,
                      cont_effects = NULL)

  # Load csv file of endmember (source) data
  source <- load_source_data(filename = paste0("input/source_depth_1_split_",split,".csv"),
                            source_factors = NULL,
                            conc_dep = FALSE,
                            data_type = "means",
                            mix)

  # Load csv file of discrimination factors for each endmember (all set to 0)
  discr <- load_discr_data(filename = paste0("input/discr_depth_1_split_",split,".csv"),
                          mix)

  # Plot endmember statistics on tracer axes
  plot_data(filename = paste0("prior_plots/isospace_depth_1_split_",split,"_plot"),
            plot_save_pdf = TRUE,
            plot_save_png = FALSE,
            mix,
            source,
            discr)

  # Plot prior structure
  plot_prior(alpha.prior = 1,
            source,
            plot_save_pdf = TRUE,
            plot_save_png = FALSE,
            filename = paste0("prior_plots/prior_depth_1_split_",split,"_plot"))

  # Start up MixSIAR
  model_filename = paste0("MixSIAR_model_depth_1_split_",split,".txt")
  resid_err <- FALSE
  process_err <- TRUE
  write_JAGS_model(model_filename, resid_err, process_err, mix, source)
  jags.1 <- run_model(run = "extreme", mix, source, discr, model_filename)

  # Save MixSIAR outputs
  output_options <- list(summary_save = TRUE,
                        summary_name = paste0("summary_diagnostics/summary_depth_1_split_",split,"_statistics"),
                        sup_post = FALSE,
                        plot_post_save_pdf = TRUE,
                        plot_post_name = paste0("output_plots/postderior_depth_1_split_",split,"_density"),
                        sup_pairs = FALSE,
                        plot_pairs_save_pdf = TRUE,
                        plot_pairs_name = paste0("output_plots/pairs_depth_1_split_",split,"_plot"),
                        sup_xy = TRUE,
                        plot_xy_save_pdf = TRUE,
                        plot_xy_name = paste0("output_plots/xy_depth_1_split_",split,"_plot"),
                        gelman = TRUE,
                        heidel = FALSE,
                        geweke = TRUE,
                        diag_save = TRUE,
                        diag_name = paste0("summary_diagnostics/diagnostics_depth_1_split_",split,"_output"),
                        indiv_effect = FALSE,
                        plot_post_save_png = FALSE,
                        plot_pairs_save_png = FALSE,
                        plot_xy_save_png = FALSE,
                        diag_save_ggmcmc = FALSE)

  output_JAGS(jags.1, mix, source, output_options)
}


## RUN ALL CO2 SPLITS FOR ALL DEPTHS ###
for (depth in 1:8) {
  for (split in 1:5) {

    # Conditions added to account for some CO2 splits not having d13C measurements
    if (depth == 3 & split == 5) {

      print("MixSIAR run skipped: no mixture d13C measurement")

    } else if (depth == 6 & split == 5) {

      print("MixSIAR run skipped: no mixture d13C measurement")

    } else {

    ## Import model input csv files

    # Load csv file of mixture data
    mix <- load_mix_data(filename = paste0("input/mix_depth_",depth,"_split_",split,".csv"),
                        iso_names = c("d13C", "FM"),
                        factors = NULL,
                        fac_random = NULL,
                        fac_nested = NULL,
                        cont_effects = NULL)

    # Load csv file of endmember (source) data
    source <- load_source_data(filename = paste0("input/source_depth_",depth,"_split_",split,".csv"),
                              source_factors = NULL,
                              conc_dep = FALSE,
                              data_type = "means",
                              mix)

    # Load csv file of discrimination factors for each endmember (all set to 0)
    discr <- load_discr_data(filename = paste0("input/discr_depth_",depth,"_split_",split,".csv"),
                            mix)

    # Plot endmember statistics on tracer axes
    plot_data(filename = paste0("prior_plots/isospace_depth_",depth,"_split_",split,"_plot"),
              plot_save_pdf = FALSE,
              plot_save_png = FALSE,
              mix,
              source,
              discr)

    # Plot prior structure
    plot_prior(alpha.prior = 1,
              source,
              plot_save_pdf = FALSE,
              plot_save_png = FALSE,
              filename = paste0("prior_plots/prior_depth_",depth,"_split_",split,"_plot"))

    # Start up MixSIAR
    model_filename = paste0("MixSIAR_model_depth_",depth,"_split_",split,".txt")
    resid_err <- FALSE
    process_err <- TRUE
    write_JAGS_model(model_filename, resid_err, process_err, mix, source)
    jags.1 <- run_model(run = "extreme", mix, source, discr, model_filename)

    # Save MixSIAR outputs
    output_options <- list(summary_save = TRUE,
                          summary_name = paste0("summary_diagnostics/summary_depth_",depth,"_split_",split,"_statistics"),
                          sup_post = FALSE,
                          plot_post_save_pdf = FALSE,
                          plot_post_name = paste0("output_plots/postderior_depth_",depth,"_split_",split,"_density"),
                          sup_pairs = FALSE,
                          plot_pairs_save_pdf = FALSE,
                          plot_pairs_name = paste0("output_plots/pairs_depth_",depth,"_split_",split,"_plot"),
                          sup_xy = TRUE,
                          plot_xy_save_pdf = FALSE,
                          plot_xy_name = paste0("output_plots/xy_depth_",depth,"_split_",split,"_plot"),
                          gelman = TRUE,
                          heidel = FALSE,
                          geweke = TRUE,
                          diag_save = TRUE,
                          diag_name = paste0("summary_diagnostics/diagnostics_depth_",depth,"_split_",split,"_output"),
                          indiv_effect = FALSE,
                          plot_post_save_png = FALSE,
                          plot_pairs_save_png = FALSE,
                          plot_xy_save_png = FALSE,
                          diag_save_ggmcmc = FALSE)

    output_JAGS(jags.1, mix, source, output_options)
    }
  }
}
