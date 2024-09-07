=UNIQUE(D2:D) - unique no of states
=COUNTIF(D$2:D,H2) - count of times state name is repeated
=SUMIF(D$2:D,H2,F$2:F) - sum of no. of orders from different states

###
Format -> Conditional formatting (select and highlight the cells based on conditon eg, values >= 200 highlight in red.)