# Data Project Python


## Analytics on UN Population


### Aim 

To convert raw open data, country and year wise population estimates in this case, into charts that tell some kind of story.


### Preparation

#### raw data

To get the raw Data in .csv file click [here.](https://datahub.io/core/population-growth-estimates-and-projections/r/population-estimates.csv)

#### Terms

* Over the years span is considered from year _**2004**_ to year _**2014**._
  
* List of ASEAN Countries
  * Brunei
  * Combodia
  *  Indonesia
  *  Laos
  *  Malaysia
  *  Myanmar
  *  Philippines
  *  Singapore
  *  Thailand
  *  Vietnam
  


* List of SAARC Countries
  *  Afghanistan
  *  Bangladesh
  *  Bhutan
  *  India
  *  Maldives
  *  Nepal
  *  Pakistan
  *  Sri Lanka



### Tasks

1. **India population over years - Bar Plot**
   
   _Make a Bar Plot of 'population of India' vs. years._
   ```shell
   $ pyhton3 india_bchart.py
   ```

2. **For the year 2014. Bar Chart of population of ASEAN countries**
  
   _Plot a Bar Chat of the population of these countries. Only use data for the year 2014._
    ```shell
    $ python3 asean_bchart.py
    ```

3. **Over the years, TOTAL population of SAARC countries**
  
   _In this case for each year you have to calculate the sum of the population of all SAARC countries. Then plot a BAR CHART of Total SAARC population vs. year._
   ```shell
   $ python3 saarc_bchart.py
   ```

4. **Grouped Bar Chart - ASEAN population vs. years**
   
   _You have to plot population of ASEAN countries as groups over the years._
   ```shell
   $ python3 asean_gbchart.py
   ```