=UNIQUE(D2:D) - unique no of states
=COUNTIF(D$2:D,H2) - count of times state name is repeated
=SUMIF(D$2:D,H2,F$2:F) - sum of no. of orders from different states
=COUNTIFS(D:D,J2,F:F,"> 40") -the formula counts how many rows have a value in column D (states) that matches the value in cell J2(distinct states) and also have a value in column F(no of orders) that is greater than 40.
=LEFT(T2,2) -> select 2 characters from T2 from left side. eg "12" from "12-09-24"
=RIGHT(T2,2) -> select 2 characters from T2 from right side. eg "24" from "12-09-24"
=MID(T2,4,2) -> starting from 4th character select 2 characters from T2 (i.e 4,5th char). eg "09" from "12-09-24"
### Useful Menubar items
Format -> Conditional formatting (select and highlight the cells based on conditon eg, values >= 200 highlight in red.)

Data -> Data validation (add predefined values to cell)