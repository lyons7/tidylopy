# Grabbing same data as tidylo example 
# https://github.com/juliasilge/tidylo/blob/main/vignettes/tidy_log_odds.Rmd
library(dplyr)
library(janeaustenr)
library(tidytext)
library(stringr)
library(tidylo)


tidy_bigrams <- austen_books() %>%
  unnest_tokens(bigram, text, token="ngrams", n = 2, to_lower = FALSE) %>%
  filter(!str_detect(bigram, "[A-Z]"))

bigram_counts <- tidy_bigrams %>%
  count(book, bigram, sort = TRUE)

bigram_log_odds <- bigram_counts %>%
  bind_log_odds(book, bigram, n) %>%
  arrange(-log_odds_weighted)  # Sorting them for convenience (separate step in original R example)


# Going to save both bigram_counts and bind_log_odds so as to compare
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
setwd('..') # Moves up one

# Save
write.csv(bigram_counts, 'example_data/bigram_counts_r.csv')
write.csv(bigram_log_odds, 'example_data/bigram_log_odds_r.csv')


