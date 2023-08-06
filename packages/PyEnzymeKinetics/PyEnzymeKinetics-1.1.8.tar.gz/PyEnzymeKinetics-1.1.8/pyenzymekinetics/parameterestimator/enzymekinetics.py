from lib2to3.pygram import python_grammar_no_print_statement
from pyenzymekinetics.utility.initial_parameters import get_initial_vmax, get_initial_Km
from pyenzymekinetics.parameterestimator.models import KineticModel, kcatKm_inactivation, irreversible_model, irreversible_enzyme_inactication_model, competitive_inhibition_model, kcatKm, competitive_inhibition_enzyme_inactivation_model, uncompetitive_inhibition_model, uncompetitive_inhibition_enzyme_inactivation_model, partially_competitive_inhibition_model, noncompetitive_inhibition_model, substrate_inhibition_model, product_inhibition_model, substrate_inhibition_enzyme_inactivation_model

from pyenzyme import EnzymeMLDocument

from matplotlib.cm import get_cmap
from typing import Dict
from matplotlib import pyplot as plt
from numpy import ndarray, array, zeros, max, tile
import numpy as np
from scipy.integrate import odeint
from lmfit import minimize, report_fit


class EnzymeKinetics():

    def __init__(self,
                 time: ndarray,
                 enzyme: ndarray,
                 substrate: ndarray = None,
                 product: ndarray = None,
                 init_substrate: ndarray or float = None,
                 inhibitor: ndarray = None,
                 substrate_name: str = None,
                 product_name: str = None,
                 unit: str = None,
                 time_unit: str = None,
                 ):
        self.time = time
        self.enzyme = enzyme
        self.substrate = substrate
        self.product = product
        self.init_substrate = init_substrate
        self.inhibitor = inhibitor
        self.product_name = product_name
        self.substrate_name = substrate_name
        self.time_unit = time_unit
        self.unit = unit

        self._initialize_data()


    def _initialize_data(self) -> None:  
        self._check_is_substrate()
        self._check_multiple_concentrations()

        if self.substrate is None:
            self.substrate = self.calculate_substrate()

        if self.product is None:
            self.product = self.calculate_product()

        self._check_enzyme()
        self._check_inhibitor()

        self._w0 = self._get_w0()
        self.result_dict: dict = None

        self.models: Dict[str, KineticModel] = self.initialize_models()


    def _check_is_substrate(self) -> bool:
        if self.substrate is not None:
            _is_substrate = True
        else:
            _is_substrate = False

        self._is_substrate = _is_substrate

    def _check_multiple_concentrations(self) -> bool:
        """Checks if data contains one or multiple concentration array based on the shape of the array"""

        result = None

        if self.substrate is not None and len(self.substrate.shape) == 2 or self.product is not None and len(self.product.shape) == 2:
            result = True
        else:
            result = False

        self._multiple_concentrations = result

    def _check_enzyme(self):
        """Make enzyme concentration array same length as init substrate array"""
        if len(self.enzyme) == 1:
            self.enzyme = tile(self.enzyme, len(self.init_substrate))
        elif len(self.enzyme) == len(self.init_substrate):
            pass
        else:
            raise Exception(
                "Inconsistent array Lengths. Enzyme array length should be one or equivalent to init_Substrate array length."
            )

    def _check_inhibitor(self):
        print(self.inhibitor)
        """Make inhibitor array same length as init substrate array"""
        #if self.inhibitor == None:
         #   self.inhibitor = np.array([0])

        if len(self.inhibitor) == 1:
            self.inhibitor = tile(self.inhibitor, len(self.init_substrate))
        elif len(self.inhibitor) == len(self.init_substrate):
            pass
        else:
            raise Exception(
                "Inconsistent array Lengths. Enzyme array length should be one or equivalent to init_Substrate array length."
            )

    def calculate_substrate(self) -> ndarray:
        """If substrate data is not provided substrate data is calculated, assuming conservation of mass"""

        if self.substrate is None and self.product is not None:
            substrate = zeros(self.product.shape)
            if not self._multiple_concentrations:
                substrate = array(
                    [self.init_substrate - product for product in self.product])
            else:
                for i, row in enumerate(self.product):
                    substrate[i] = [self.init_substrate[i] -
                                    product for product in row]
                    # TODO: catch error if no init_substrate is provided

            return substrate

        else:
            raise Exception(
                "Data must be provided eighter for substrate or product")

    def calculate_product(self) -> ndarray:

        if self.product is None and self.substrate is not None:
            product = zeros(self.substrate.shape)
            if not self._multiple_concentrations:
                product = array(
                    [self.init_substrate - substrate for substrate in self.substrate])
            else:
                for i, row in enumerate(self.substrate):
                    product[i] = [self.init_substrate[i] -
                                    substrate for substrate in row]
                    # TODO: catch error if no init_substrate is provided

            return product

    def _get_w0(self):
        return (self.init_substrate, self.enzyme)

    def _get_kcat(self) -> float:

        v_max = get_initial_vmax(self.substrate, self.time)

        if self.enzyme.size > 1:
            try:
                return max(v_max / self.enzyme)
            except:
                raise Exception(
                    f"Substrate ({len(self.substrate)}) and enzyme ({len(self.enzyme)}) need to have the same length")

        else:
            return get_initial_vmax(self.substrate, self.time) / self.enzyme


    def initialize_models(self) -> Dict[str, KineticModel]:
        irreversible_MM = KineticModel(
            name="irreversible Michaelis Menten",
            params=(""),
            w0={"cS": self.init_substrate, "cE": self.enzyme,
                "cP": self.product, "cI": self.inhibitor},            kcat_initial=self._get_kcat(),
            Km_initial=get_initial_Km(self.substrate, self.time),
            model=irreversible_model
        )

        irrev_MM_enz_inact = KineticModel(
            name="irreversible Michaelis Menten with enzyme inactivation",
            params=["K_ie"],
            w0={"cS": self.init_substrate, "cE": self.enzyme,
                "cP": self.product, "cI": self.inhibitor},
            kcat_initial=self._get_kcat(),
            Km_initial=get_initial_Km(self.substrate, self.time),
            model=irreversible_enzyme_inactication_model
        )
        kcat_km = KineticModel(
            name="kcat/Km",
            params=["kcat/Km"],
            w0={"cS": self.init_substrate, "cE": self.enzyme,
                "cP": self.product, "cI": self.inhibitor},
            kcat_initial=self._get_kcat(),
            Km_initial=get_initial_Km(self.substrate, self.time),
            model=kcatKm
        )

        kcat_km_enz_inactivation = KineticModel(
            name="kcat/Km with enzyme inactivation",
            params=["kcat/Km", "K_ie"],
            w0={"cS": self.init_substrate, "cE": self.enzyme,
                "cP": self.product, "cI": self.inhibitor},
            kcat_initial=self._get_kcat(),
            Km_initial=get_initial_Km(self.substrate, self.time),
            model=kcatKm_inactivation
        )

        substrate_inhibition = KineticModel(
            name="substrate inhibition",
            params=["K_iu"],
            w0={"cS": self.init_substrate, "cE": self.enzyme,
                "cP": self.product, "cI": self.inhibitor},
            kcat_initial=self._get_kcat(),
            Km_initial=get_initial_Km(self.substrate, self.time),
            model=substrate_inhibition_model
        )

        substrate_inhibition_enz_inactivation = KineticModel(
            name="substrate inhibition with enzyme inactivation",
            params=["K_iu", "K_ie"],
            w0={"cS": self.init_substrate, "cE": self.enzyme,
                "cP": self.product, "cI": self.inhibitor},
            kcat_initial=self._get_kcat(),
            Km_initial=get_initial_Km(self.substrate, self.time),
            model=substrate_inhibition_enzyme_inactivation_model
        )
        

        product_inhibition = KineticModel(
            name="product inhibition",
            params=["K_ic"],
            w0={"cS": self.init_substrate, "cE": self.enzyme,
                "cP": self.product, "cI": self.inhibitor},
            kcat_initial=self._get_kcat(),
            Km_initial=get_initial_Km(self.substrate, self.time),
            model=product_inhibition_model
        )

        competitive_inhibition = KineticModel(
            name="competitive inhibition",
            params=["K_ic"],
            w0={"cS": self.init_substrate, "cE": self.enzyme,
                "cP": self.product, "cI": self.inhibitor},
            kcat_initial=self._get_kcat(),
            Km_initial=get_initial_Km(self.substrate, self.time),
            model=competitive_inhibition_model
        )

        competitive_inhibition_enzyme_inactivation = KineticModel(
            name="competitive inhibition with enzyme inactivation",
            params=["K_ic", "K_ie"],
            w0={"cS": self.init_substrate, "cE": self.enzyme,
                "cP": self.product, "cI": self.inhibitor},
            kcat_initial=self._get_kcat(),
            Km_initial=get_initial_Km(self.substrate, self.time),
            model = competitive_inhibition_enzyme_inactivation_model
        )

        uncompetitive_inhibition = KineticModel(
            name="uncompetitive inhibition",
            params=["K_iu"],
            w0={"cS": self.init_substrate, "cE": self.enzyme,
                "cP": self.product, "cI": self.inhibitor},
            kcat_initial=self._get_kcat(),
            Km_initial=get_initial_Km(self.substrate, self.time),
            model=uncompetitive_inhibition_model
        )

        uncompetitive_inhibition_enzyme_inactivation = KineticModel(
            name="uncompetitive inhibition with enzyme inactivation",
            params=["K_iu", "K_ie"],
            w0={"cS": self.init_substrate, "cE": self.enzyme,
                "cP": self.product, "cI": self.inhibitor},
            kcat_initial=self._get_kcat(),
            Km_initial=get_initial_Km(self.substrate, self.time),
            model=uncompetitive_inhibition_enzyme_inactivation_model
        )

        partially_competitive_inhibition = KineticModel(
            name="partially competitive inhibition",
            params=["K_iu", "K_ic"],
            w0={"cS": self.init_substrate, "cE": self.enzyme,
                "cP": self.product, "cI": self.inhibitor},
            kcat_initial=self._get_kcat(),
            Km_initial=get_initial_Km(self.substrate, self.time),
            model=partially_competitive_inhibition_model
        )

        noncompetitive_inhibition = KineticModel(
            name="non-competitive inhibition",
            params=["K_iu", "K_ic"],
            w0={"cS": self.init_substrate, "cE": self.enzyme,
                "cP": self.product, "cI": self.inhibitor},
            kcat_initial=self._get_kcat(),
            Km_initial=get_initial_Km(self.substrate, self.time),
            model=noncompetitive_inhibition_model
        )

        """
        irrev_MM_subabs = KineticModel(
            name="irreversible Michaelis Menten with absorbing substrate",
            params=("a"),
            w0={"cS": self.init_substrate, "cE": self.enzyme, "cP": self.product, "cS0": self.init_substrate},
            kcat_initial=self._get_kcat(),
            Km_initial=get_initial_Km(self.substrate, self.time),
            model=subabs_menten_irreversible
        )
        """
        kinetic_model_dict: Dict[str, KineticModel] = {
            irreversible_MM.name: irreversible_MM,
            irrev_MM_enz_inact.name: irrev_MM_enz_inact,
            kcat_km.name: kcat_km,
            kcat_km_enz_inactivation.name: kcat_km_enz_inactivation,
            substrate_inhibition.name: substrate_inhibition,
            product_inhibition.name: product_inhibition,
            competitive_inhibition.name: competitive_inhibition,
            competitive_inhibition_enzyme_inactivation.name: competitive_inhibition_enzyme_inactivation,
            uncompetitive_inhibition.name: uncompetitive_inhibition,
            uncompetitive_inhibition_enzyme_inactivation.name: uncompetitive_inhibition_enzyme_inactivation,
            uncompetitive_inhibition_enzyme_inactivation.name: uncompetitive_inhibition_enzyme_inactivation,
            noncompetitive_inhibition.name: noncompetitive_inhibition,
            substrate_inhibition_enz_inactivation.name: substrate_inhibition_enz_inactivation
            #irrev_MM_subabs.name: irrev_MM_subabs
        }

        return kinetic_model_dict

    def evaluate_aic(self):
        names = []
        aic = []
        for model in self.models.values():
            names.append(model.name)
            aic.append(model.result.aic)

        result_dict = dict(zip(names, aic))
        result_dict = {k: v for k, v in sorted(
            result_dict.items(), key=lambda item: item[1], reverse=False)}
        return result_dict


    def fit_models(self):
        for kineticmodel in self.models.values():

            def g(t, w0, params):
                '''
                Solution to the ODE w'(t)=f(t,w,p) with initial condition w(0)= w0 (= [S0])
                '''
                w = odeint(kineticmodel.model, w0, t, args=(params,))
                return w

            def residual(params, t, data):

                # get dimensions of data (here we fit against 4 measurments => ndata = 4)
                ndata, nt = data.shape
                resid = 0.0 * data[:]  # initialize the residual vector

                for i in range(ndata):

                # compute residual per data set
                    if len(kineticmodel.w0) == 4:
                        cS, cE, cP, cI = kineticmodel.w0.values()
                        w0 = (cS[i], cE[i], 0, cI[i])
                            
                    #if kineticmodel.name == "irreversible Michaelis Menten with absorbing substrate":
                     #   cS, cE, cP, cS0 = kineticmodel.w0.values()
                      #      # TODO: fix initia product concentration
                       # w0 = (cS[i], cE[i], cP[i,0], cS0[i])

                    model = g(t, w0, params)  # solve the ODE with sfb.

                    # get modeled product
                    model = model[:, 0]

                    # compute distance to measured data
                    resid[i, :] = data[i, :]-model

                return resid.flatten()

            print(kineticmodel.name)
            kineticmodel.result = minimize(residual, kineticmodel.parameters, args=(
                self.time, self.substrate), method='leastsq', nan_policy='omit')

        self.result_dict = self.evaluate_aic()


    def visualize_fit(self, model_name: str = None, path: str = None, title:str = None, visualize_species: str = None, **plt_kwargs):

        # Visualization modes
        plot_modes = {
            "S": [self.substrate,0, self.substrate_name], # Substrate
            "P": [self.product, 2, self.product_name], # Product
        }
        print("mashallah")

        if visualize_species is None:
            if self._is_substrate:
                experimental_data, reactant, name = plot_modes["S"]
            else:
                experimental_data, reactant, name = plot_modes["P"]
        else:
            experimental_data, reactant, name = plot_modes[visualize_species]


        # TODO: add file directory for save
        best_model = next(iter(self.result_dict))
        if model_name is None:
            model_name = best_model

        model = self.models[model_name]
        report_fit(model.result)

        def g(t, w0, params):

            '''
            Solution to the ODE w'(t)=f(t,w,p) with initial condition w(0)= w0 (= [S0])
            '''

            w = odeint(model.model, w0, t, args=(params,))
            return w

        unique_a = np.unique(self.inhibitor)
        markers = ["o", "x", "D", "X", "d"]
        marker_mapping = dict(zip(unique_a, markers[:len(unique_a)]))
        marker_vector = [marker_mapping[item] for item in self.inhibitor]

        unique_concs = np.unique(self.init_substrate)
        cmap = get_cmap("tab20").colors
        color_mapping = dict(zip(unique_concs, cmap[:len(unique_concs)]))
        color_vector = [color_mapping[item] for item in self.init_substrate]

        for i, data in enumerate(experimental_data):

            cS, cE, cP, cI = model.w0.values()
            w0 = (cS[i], cE[i], 0, cI[i])

            # Plot data
            ax = plt.scatter(x=self.time, y=data, label=self.init_substrate[i], marker=marker_vector[i], color=color_vector[i], **plt_kwargs)

            data_fitted = g(t=self.time, w0=w0, params=model.result.params)

            # Plot model
            ay = plt.plot(self.time, data_fitted[:,reactant], color = color_vector[i])

        if title is None:
            plt.title(model.name)
        else:
            plt.title(title)

        plt.ylabel(f"{name} [{self.unit}]")
        plt.xlabel(f"time [{self.time_unit}]")

        # Legend
        handles, labels = plt.gca().get_legend_handles_labels()

        new_handles, new_labels = [[],[]]
        for handle, label in zip(handles, labels):
            if len(new_labels) == 0:
                new_labels.append(label)
                new_handles.append(handle)
            else:
                if label == new_labels[-1]:
                    pass
                else:
                    new_labels.append(label)
                    new_handles.append(handle)

        plt.legend(title = "initial substrate [mM]", handles=new_handles, labels=new_labels)
        if path != None:
            plt.savefig(path, format="svg")
        plt.show()


    @classmethod
    def from_EnzymeML(
        cls, 
        enzymemldoc: EnzymeMLDocument, 
        substrate_id: str ="s0", 
        product_id: str = "s1",
        protein_id: str = "p0",
        inhibitor_id: str = None
        ) -> "EnzymeKinetics":

        """
        Initializes EnzymeKinetics class isntance from a EnzymeMLDocument.

        Args:
            str: substrate_id, product_id, protein_id as defined in the EnzymeMLDocument
            str (optional): inhibitor_id as defined in the EnzymeMLDocument.

        Returns:
            EnymeKinetics: Initialized EnzymeKinetics object
        """


        substrate_data = np.array([])
        product_data = np.array([])
        protein_data = np.array([])
        init_substrate_data = np.array([])
        inhibitor_data = np.array([])

        n_measurements = len(list(enzymemldoc.measurement_dict.keys()))

        for measurement in enzymemldoc.measurement_dict.values():

            substrate = measurement.getReactant(substrate_id)
            product = measurement.getReactant(product_id)
            protein = measurement.getReactant(protein_id)
            if inhibitor_id != None:
                inhibitor = measurement.getReactant(inhibitor_id)

            if len(substrate.replicates) > len(product.replicates):
                measured_species = substrate_id
            else:
                measured_species = product_id

            n_replicates = len(measurement.getReactant(measured_species).replicates)

            init_substrate_data = np.append(init_substrate_data, np.repeat(substrate.init_conc, n_replicates))

            if measured_species == substrate_id:
                for replicate in substrate.replicates:
                    substrate_data = np.append(substrate_data, replicate.data)
                product_data = None

            if measured_species == product_id:
                for replicate in product.replicates:
                    product_data = np.append(product_data, replicate.data)
                substrate_data = None

            protein_data = np.append(protein_data, np.repeat(protein.init_conc, n_replicates))

            time = np.array(measurement.getReactant(measured_species).replicates[0].time)

            if inhibitor_id != None:
                inhibitor_data = np.append(inhibitor_data, inhibitor.init_conc)
            else:
                inhibitor_data = np.array([0])

        if isinstance(substrate_data, np.ndarray):
            substrate_data = substrate_data.reshape((n_measurements*n_replicates,len(time)))
        if isinstance(product_data, np.ndarray):
            product_data = substrate_data.reshape((n_measurements*n_replicates,len(time)))

        substrate_name = enzymemldoc.getReactant(substrate_id).name
        product_name = enzymemldoc.getReactant(product_id).name
        time_unit = measurement.getReactant(measured_species).replicates[0].time_unit
        unit = measurement.getReactant(measured_species).replicates[0].data_unit

        instance = cls(
            time=time,
            enzyme=protein_data,
            substrate=substrate_data,
            product=product_data,
            init_substrate=init_substrate_data,
            inhibitor=inhibitor_data,
            substrate_name=substrate_name,
            product_name=product_name,
            time_unit=time_unit,
            unit=unit
        )
        return instance



if __name__ == "__main__":

    import matplotlib.pyplot as plt
    #from pyenzymekinetics.parameterestimator.helper.load_utitlity import *
    from pyenzymekinetics.calibrator.standardcurve import StandardCurve
    from pyenzymekinetics.calibrator.utility import to_concentration
    import numpy as np

    import pyenzyme as pe

    enzmldoc = pe.EnzymeMLDocument.fromFile("/Users/maxhaussler/Dropbox/master_thesis/data/marwa/round4/DocTest.omex")
    mm = EnzymeKinetics.from_EnzymeML(enzmldoc)
    mm.fit_models()
    mm.visualize_fit(visualize_species="P", s=12)