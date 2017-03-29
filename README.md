# Visualflee

## Overview

Flee, an agent model based simulation tool, developed by Groen (2016) at Brunel University London. It uses data from [United Nations High Commission for Refugees](http://data2.unhcr.org/en/situations) (UNHCR) about camps and data from the [Armed Conflicat Location & Event Data Project](http://data2.unhcr.org/en/situations) (ACLED) to model the migration of refugees within a conflict zone. This project aims to automate the data acquisition that are used as the inputs to Flee and visualise the outputs of Flee. Currently Flee is closed source but it will be soon be made available (after the first journal paper publication) under a BSD 3-clause licence.

Initially, this will be of benefit as a reasearch project but, if accurate, it could be of help for governmental and non-govermental organisations to manage refugees escaping conflict zones. The project can be divided into three major components:

* data acquisition
* refugee simulation
* visualisation of the results

Currently these aspects are decoupled but the ultimate aim is to produce a tightly coupled applcation of the type that would allow the migration of refugees to be modelled in real time:

![Design of the interface](images/visualflee_plan.png)

## Data acquisition

## Simulation of refugee movements
   Acquired data from 3 different publicly available sources provide an input for running agent-based simulation. It uses FLEE code for predicting refugee movements and produces output numbers of population for cities and camps over simulation period. 

## Visualisation
