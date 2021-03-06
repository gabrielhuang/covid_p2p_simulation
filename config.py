
# NOISE IN SIM PARAMETERS
LOCATION_TECH = 'gps' # &location-tech

# CITY PARAMETERS
OPENING_HOUR = 9 # @param
CLOSING_HOUR = 18 # @param

# INDIVIDUAL DIFFERENCES PARAMETERS
WORK_FROM_HOME = False
P_HAS_APP = 0.5 # &has_app
P_CAREFUL_PERSON = 0.3 # &carefullness

# DISEASE PARAMETERS
AVG_INCUBATION_DAYS = 5 # &avg-incubation-days
SCALE_INCUBATION_DAYS = 1
AVG_RECOVERY_DAYS = 14
SCALE_RECOVERY_DAYS = 4
INFECTION_RADIUS = 200 # cms
INFECTION_DURATION = 2 # minutes

ASYMPTOMATIC_INFECTION_RATIO = 0.1 # &prob_infectious

# aerosol    copper      cardboard       steel       plastic
MAX_DAYS_CONTAMINATION = [0.125, 1/3, 1, 2, 3] # &envrionmental contamination

NUM_DAYS_SICK = 10 # @param
BASELINE_P_ASYMPTOMATIC = 50 # &p-asymptomatic
P_TEST = 0.5
P_FALSE_NEGATIVE = 0.1 #&false-negative # 0  1   2    3   4    5   6    7    8
INFECTIOUSNESS_CURVE = [0.05, 0.1, 0.2, 0.3, 0.25, 0.2, 0.15, 0.1, 0.05]
P_COLD = 0.1 # &p-cold
P_FLU = 0.05 # &p-flu

TEST_DAYS = 2 #

# SIMULATION PARAMETERS
TICK_MINUTE = 2  # @param increment
SIMULATION_DAYS = 30  # @param
SYMPTOM_DAYS = 5  # @param

# LIFESTYLE PARAMETERS
## SHOP
AVG_SHOP_TIME_MINUTES = 30 # @param
SCALE_SHOP_TIME_MINUTES = 15
AVG_SCALE_SHOP_TIME_MINUTES =  10
SCALE_SCALE_SHOP_TIME_MINUTES = 5
NUM_WEEKLY_GROCERY_RUNS = 2 # @param

AVG_MAX_NUM_SHOP_PER_WEEK = 5
SCALE_MAX_NUM_SHOP_PER_WEEK = 1

AVG_NUM_SHOPPING_DAYS = 3
SCALE_NUM_SHOPPING_DAYS = 1
AVG_NUM_SHOPPING_HOURS = 3
SCALE_NUM_SHOPPING_HOURS = 1

## WORK
AVG_WORKING_MINUTES = 8 * 60
SCALE_WORKING_MINUTES = 1 * 60
AVG_SCALE_WORKING_MINUTES = 2 * 60
SCALE_SCALE_WORKING_MINUTES = 1 * 60

## EXERCISE
AVG_EXERCISE_MINUTES = 60
SCALE_EXERCISE_MINUTES = 15
AVG_SCALE_EXERCISE_MINUTES = 15
SCALE_SCALE_EXERCISE_MINUTES = 5

AVG_MAX_NUM_EXERCISE_PER_WEEK = 5
SCALE_MAX_NUM_EXERCISE_PER_WEEK = 2

AVG_NUM_EXERCISE_DAYS = 3
SCALE_NUM_EXERCISE_DAYS = 1
AVG_NUM_EXERCISE_HOURS = 3
SCALE_NUM_EXERCISE_HOURS = 1

## MISC
AVG_MISC_MINUTES = 60
SCALE_MISC_MINUTES = 15
AVG_SCALE_MISC_MINUTES = 15
SCALE_SCALE_MISC_MINUTES = 5

# DISTANCE_ENCOUNTER PARAMETERS
MIN_DIST_ENCOUNTER = 20
MAX_DIST_ENCOUNTER = 50
