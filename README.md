# Session10-Advanced-Task6

# Q1 Answer:-

              turns   rating_diff
count  20058.000000  20058.000000
mean      60.465999    173.091435
std       33.570585    179.214854
min        1.000000      0.000000
25%       37.000000     45.000000
50%       55.000000    115.000000
75%       79.000000    241.000000
max      349.000000   1605.000000

# -------------------------------------------

# Q2 Answer:-

Skewness:
Turns: 0.897 : -1.611
Rating_Diff: 1.949 : -0.901

# Q3 Answer:-

correlation_matrix round 3=> : 
turns  white_rating  black_rating  rating_diff  time_control
turns         1.000         0.130         0.160       -0.127        -0.059
white_rating  0.130         1.000         0.634        0.073        -0.070
black_rating  0.160         0.634         1.000        0.025        -0.077
rating_diff  -0.127         0.073         0.025        1.000         0.054
time_control -0.059        -0.070        -0.077        0.054         1.000

# Q4 Answer:-

contingency_table:

winner_group  Advanced  Beginner  Draw  Expert  Intermediate
white_group                                                 
Advanced          6119        32   346     821           496
Beginner           227       835    65      45           422
Expert             336         2   317    4184            41
Intermediate       950       149   222     246          4203
