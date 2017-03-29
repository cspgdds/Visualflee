# Visualflee

## Overview

Flee, an agent model based simulation tool, developed by Groen (2016) at Brunel University London. It uses data from [United Nations High Commission for Refugees](http://data2.unhcr.org/en/situations) (UNHCR) about camps and data from the [Armed Conflicat Location & Event Data Project](http://data2.unhcr.org/en/situations) (ACLED) to model the migration of refugees within a conflict zone. This project aims to automate the data acquisition that are used as the inputs to Flee and visualise the outputs of Flee. Currently Flee is closed source but it will be soon be made available (after the first journal paper publication) under a BSD 3-clause licence.

Initially, this will be of benefit as a reasearch project but, if accurate, it could be of help for governmental and non-govermental organisations to manage refugees escaping conflict zones. The project can be divided into three major components:

* data acquisition
* refugee movement simulation
* visualisation of the results

Currently these aspects are decoupled but the ultimate aim is to produce a tightly coupled applcation of the type that would allow the migration of refugees to be modelled in real time:

![Design of the interface](images/visualflee_plan.png)

## Data acquisition

The migration application uses data from two main sources:

* UNHCR data about camps.
* ACLED information about conflict location and times.

As a result of this project an R package [runchr](https://github.com/AndySouth/runhcr) is being 
developed to extract data from the UN. It was thought to create a new separate repository for this
as it was envisaged that such a framework might be of use to a more general audience than just for
this project. 

For the ACLED data the use of their [API](http://www.acleddata.com/wp-content/uploads/2017/03/API-User-Guide_March-2017.pdf) was investigated. A query was developed that returns the data required which could still do with a 
little bit more filtering.

## Simulation of refugee movements
   Acquired data from 3 different publicly available sources provide an input for running agent-based simulation. It uses FLEE code for predicting refugee movements and produces output numbers of population for cities and camps over simulation period. 


## Visualisation
