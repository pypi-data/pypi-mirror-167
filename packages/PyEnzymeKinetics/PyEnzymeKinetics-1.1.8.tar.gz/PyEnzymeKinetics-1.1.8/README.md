# PyEnzymeKinetics

Software-package for easy enzyme kinetic parameter estimation.
Supports EnzymeML format (not yet)
Allows comprehensive data analysis from experimental raw data to kinetic parameters

## Calibration

- linear and non-linear calibration for calculating concentrations from analytic signal (spectroscopy / HPLC)
- Selection of best fit model based on akaike-criterion

## Michaelis Menten kinetics

- Fitting of enzyme assay data Michaelis Menten equations for:
  - irreversible MM
  - enzyme inactivation
  - inhibition

### Dependencies

- standard stuff

### Installation

```
pip install PyEnzymeKinetics
```

## ⚙️ Example code

This example will demonstrate, how to analyze data from an enzyme kinetics experiment. Call an ```EnzymeKinetics``` object and provide provide data in the form of numpy arrays. Note that all data has to be provided in the same unit! 
- ```time``` has to be an one-dimentional array, resresenting the individual time points of measurements.
- ```initial_substrate``` concentrations need to be provided. Multiple measurement_series at different initial substrate concentrations can be provided.
- Eighter ```substrate``` or ```product``` concentrations need to be provided. The array can be two-dimentional in order to provide multiple measurement series e.g. for different initial substrate concentrations or varying inhibitor concentrations. Hence, an array for multiple concentrations should have the shape ```(len(init_substrates), len(measurements_series))```. Note measurement_series need to be in the same order as in ```initial_substrate```.
- Eighter on or multiple concentrations can be provided for ```enzyme```. For multiple (varying) concentrations, the array needs to be as long as the ```initial_substrate``` array.
- One or multiple ```inhibitor``` concentrations can be provided. For the estimation of the inhibitor constant *Ki* data with and without inhibitor need to be provided. Therefore, the array should look like: [0, 0, 0, 0.69, 0.69, 0.69], resembling 3 reactions without and 3 reactions with inhibitor present.

```python
from pyenzymekinetics import EnzymeKinetics

# Provide experimental data as numpy arrays
kinetics = EnzymeKinetics(
    time=time,
    init_substrate=init_substrate,
    substrate=substrate #or product = product,
    enzyme=enzyme,
    inhibitor=inhibitor # optional
)

# fit experimental data to kinetic models
kinetics.fit_models()
```

The fit-quality of the model is evaluated by comparing the Akaike (AIC) information criterion between all models. By calling ```EnzymeKinetics.result_dict``` an overview of all models with the respective AIC score is returned.

```EnzymeKinetics.visualize_fit()``` plots the experimental data and the kinetic model with the respective estimated parameters of the best model according to the AIC score. Additionaly, fit-statistics of the fitted kinetic model are printed.

Optionaly, alternative models can be assessed by providing the name of the respective model: ```EnzymeKinetics.visualize_fit("substrate inhibition")```

```python
# plot experimental data to kinetic models
kinetics.visualize_fit()

# plot the result of the substrate inhibition model
kinetics.visualize_fit("substrate inhibition")


## Authors

Contributors names and contact info

Max Haeussler
max.haeussler@t-online.de


## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

ex
