Original Paper
==============

:Original publication:  "A Simplified Biophysical Cell Model For Gastric Slow Wave
Entrainment Simulation
" 35th Annual International Conference of the IEEE EMBS.

Imtiaz_2002
===========

:Imtiaz et al-2002:  "A Theoretical Model of Slow Wave Regulation Using Voltage-Dependent
Synthesis of Inositol 1,4,5-Trisphosphate" Biophysical Journal Volume 83 October 2002 1877–1890.
:DOI: https://doi.org/10.1016/S0006-3495(02)73952-0


Model status
=============

The current CellML model implementation runs in OpenCOR_.
The CellML model parameters and equations must be updated regarding each specific model variation to reproduce the related simulations.
The main results that reproduced by CellML implementation: Cell model simulations Fig. 3.
The Entrainment model includes partial differential equations, we were not able to implement partial differential equations in CellML.
Using the default parameters and equations provided in the paper except for the modification listed in the sections :ref:`Model Issues`.

Model Summary
==============
Slow waves are rhythmic electrical depolarizations that
initiate and control the mechanical activity of many smooth
muscles. The mechanism responsible for generating slow waves involves IP3-induced calcium release and calcium-induced calcium release from IP3-operated intracellular calcium stores. The resultant calcium increases in the subplasmalemmal space then activate calcium-sensitive inward currents across the plasmalemma that result in slow-wave
depolarizations which are according to the work has done by :ref:`Imtiaz_2002`

To develop a more computationally efficient model of ICC slow wave activity, the biophysical basis of the ion gated conductance included in the model (see :ref:`Original Paper`).

Model Equations
===============
The model is implemented using a Hodgkin-Huxley type formulation. The cell membrane lipid bilayer is represented as a capacitance (Cm),
and the ion channels in the membrane are represented as conductance. The change in the transmembrane potential (Vm) over time depends on
is the sum of the individual ion currents through each class of ion channel in the cell current:

:math:` \frac{dVm}{dt} = - \frac{I_{tot}}{C_{m}}`.


Model Issues
===================
1. There is an issue of unit consistency.

- In Eq. 14 , :math:`u` has a unit of :math:`\mu M /ms`, while  :math:`u` is the Hill coefficient and does not carry any unit.
- On the right-hand side of Eq.14, the term :math:`\beta` that indicates the external stimuli has a unit of :math:`1/ms ` while on the other side of Eq.14, the term :math:`dP /dt` which indicates IP3 concentration in the cytosol with the unit :math:`mM/ms`, please see Eq. 14 in below: :math:`dP /dt = \beta - \epsilon *  P  - V_{m4}(P) + P (V)`

- All the maximum conductances are carrying the unit of mS, while it should be nS.
- The Algebraic definition :math:`P(V)` was modified to the original formulation in Imtiaz_2002.

==============     ==========================================================          ======================================================
                   Imtiaz_2002                                                         Du_2013
--------------    -----------------------------------------------------------         -------------------------------------------------------
:math:`P(V)`      :math:`P_{MV}(1-\frac{V_{m}^{r}}{k_{\nu}^{r}+V_{m}^{r}})`           :math:`P_{MV}(\frac{V_{m}^{r}}{k_{\nu}^{r}+V_{m}^{r}})`
==============    ===========================================================         =======================================================

2. Applying the default parameters and equations, the model moves into a stable non-periodic steady-state. Please see the table below in the case of model parameters modifications:

================     ==========================    ============================
Parameters           Du_2013                       Modified Du_2013
================     ==========================    ============================
:math:`V_{1}`        :math:`0.2266 ~ms^{-1}`       :math:`0.0002266~ ms^{-1}`
:math:`V_{M3}`       :math:`0.044 ~mM. ms^{-1}`    :math:`0.44~ mM. ms^{-1}`
:math:`P_{MV}`       :math:`0.32 ~ mM. ms^{-1}`    :math:`0.032~ mM. ms^{-1}`
:math:`\epsilon`     :math:`0.02021~ ms^{-1}`      :math:` 0.00015~ ms^{-1}`
:math:`n`            :math:`2`                     :math:`1.8`
:math:`u`            :math:`0.05`                  :math:`4`
================     ==========================    ============================

Model Validations
===================
Using the default parameters provided in the paper we were not able to reproduce reported results.
Applying the default parameters in the  plus in some cases modified parameters (see :ref:`Model Issues`), we were able to reproduce Figure 1 from :ref:`Model Issues` with a slight difference:
In the top, one can see the time-series membrane voltage, in the bottom the stimulus injected current.
As a :math:`10 ~\mu A` stimulus current was applied, the phase of the simulated slow wave was advanced.


.. image:: Doc/Figure_1.png
    :width: 70%
    :align: center
    :alt: State_variable_derivatives.

Model Simulation
================
To run the simulations,
execute 'New_IP3_Du_2013.py' in the Python console in OpenCOR_. This can be done
with the following commands at the prompt in the OpenCOR_ Python console:

 In [1]: cd path/to/folder_this_file_is_in

 In [2]: run New_IP3_Du_2013.py

Also see the 'IP3_Du_2013.py', which is based on the defaul equations and parameters in the :ref:`Original Paper`.
