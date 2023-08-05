from logging.handlers import QueueHandler
from pyenzymekinetics.calibrator.calibrationmodel import CalibrationModel, linear1, quadratic, poly3, poly_e, rational

from typing import Dict, Callable


from scipy.optimize import curve_fit
from numpy import ndarray, linspace, tile
import matplotlib.pyplot as plt


class StandardCurve():
    # TODO docstring
    def __init__(self,
                 concentration: ndarray,
                 absorption: ndarray,
                 concentration_unit: str,
                 substance_name: str):
        self.concentration = concentration
        self.absorption = absorption
        self.substance_name = substance_name
        self.concentration_unit = concentration_unit
        self.model_dict: Dict[str, CalibrationModel] = self.initialize_models()
        self.fit_models()
        self.aic_dict = self.evaluate_aic()

    def initialize_models(self) -> Dict[str, CalibrationModel]:
        linear_model = CalibrationModel(
            name="Linear",
            equation=linear1,
            parameters={"a": 0.0}
        )

        quadratic_model = CalibrationModel(
            name="Quadratic",
            equation=quadratic,
            parameters={"a": 0.0, "b": 0.0}
        )

        poly3_model = CalibrationModel(
            name="3rd polynominal",
            equation=poly3,
            parameters={"a": 0.0, "b": 0.0, "c": 0.0}
        )

        polye_model = CalibrationModel(
            name="Exponential",
            equation=poly_e,
            parameters={"a": 0.0, "b": 0.0}
        )

        rational_model = CalibrationModel(
            name="Rational",
            equation=rational,
            parameters={"a": 0.0, "b": 0.0}
        )

        models: Dict[str, CalibrationModel] = {
            linear_model.name: linear_model,
            quadratic_model.name: quadratic_model,
            poly3_model.name: poly3_model,
            polye_model.name: polye_model,
            rational_model.name: rational_model
        }

        return models

    def fit_models(self):
        for model in self.model_dict.values():

            # Check data shape, and adjust shape for multiple replicates
            if self.absorption.shape != self.concentration.shape and len(self.concentration.shape) == 1:
                abso_shape = self.absorption.shape
                self.concentration = tile(self.concentration,(abso_shape[0], 1))
                self.concentration = self.concentration.flatten()
                self.absorption = self.absorption.flatten()

            # Get parameter estimates
            result = curve_fit(
                f=model.equation, xdata=self.concentration, ydata=self.absorption)[0]
            model.parameters = dict(zip(model.parameters.keys(), result))

            # Initialize LmFit Parameter object
            model.lmfit_params = CalibrationModel.set_lmfit_parameters(
                model)

            # Fit data to models
            model.result = model.lmfit_model.fit(
                data=self.absorption, x=self.concentration, params=model.lmfit_params)

    def evaluate_aic(self):
        names = []
        aic = []
        for model in self.model_dict.values():
            names.append(model.name)
            aic.append(model.result.aic)

        result_dict = dict(zip(names, aic))
        result_dict = {k: v for k, v in sorted(
            result_dict.items(), key=lambda item: item[1], reverse=False)}

        self.model = self.model_dict[next(iter(result_dict))]
        return result_dict

    def visualize_fit(self, model_name: str = None):
        # TODO: add file directory for save
        if model_name is None:
            model = self.model
        else:
            model = self.model_dict[model_name]

        print(model)
        smooth_x = linspace(
            self.concentration[0], self.concentration[-1], len(self.concentration)*2)

        equation = model.equation
        params = model.result.params.valuesdict()

        plt.scatter(self.concentration, self.absorption)
        plt.plot(smooth_x, equation(smooth_x, **params))
        plt.ylabel("absorption")
        plt.xlabel(f"{self.substance_name} [{self.concentration_unit}]")
        plt.title(f"calibration curve of {self.substance_name}")
        plt.show()

        #plt.plot(smooth_x, self.models[model].equation(sm))
        # plt.show()


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from pyenzymekinetics.parameterestimator.helper.load_utitlity import calibration_conc, calibration_abso
    print("bubu")
    obj = StandardCurve(concentration=calibration_conc, absorption=calibration_abso,
                        concentration_unit="mM", substance_name= "pNPGP")
    obj.visualize_fit()
    print((obj.model))
