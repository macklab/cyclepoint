
################## CYCLEPOINT CALCULATION ##################

# Original / unadjusted:

df$cyclepoint <- df$cycleDay / df$cycleLength


# Adjusted for lesser variance in luteal phase length:

adjustedCyclePoint <- function(cycleDay, cycleLength) {
  if (is.na(cycleDay) || is.na(cycleLength)){
    return ()
  }
  follicular_length <- cycleLength - 14
  if (cycleDay <= follicular_length){ # if in follicular phase
    return (cycleDay/follicular_length*0.5)
  } else { #  if in luteal phase
    luteal_day <- cycleDay - follicular_length
    luteal_point <- luteal_day / 14
    return (0.5 + luteal_point * 0.5)
  }
}

df$adjustedCyclePoint <- mapply(adjustedCyclePoint, df$cycleday, df$cyclelength)