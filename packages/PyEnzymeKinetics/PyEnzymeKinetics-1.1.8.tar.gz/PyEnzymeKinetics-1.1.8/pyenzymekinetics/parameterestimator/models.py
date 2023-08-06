from lmfit import Parameters
from typing import Any, Dict, List, Callable, Tuple
from pyenzymekinetics.utility.initial_parameters import get_v, get_initial_Km, get_initial_vmax
from numpy import max, ndarray

model_params_dict: Dict[str, List[str]] = {
    "irrev MM": ["kcat", "Km"],
    "irrev MM with enzyme inactivation": ["kcat", "Km", "ki"]
}


class KineticModel():
    def __init__(self,
                 name: str,
                 model: Callable,
                 params: list,
                 kcat_initial: float,
                 Km_initial: float,
                 w0: Dict[str, ndarray]
                 ) -> None:

        self.name = name
        self.model = model
        self.params = params

        self.w0 = w0
        self.kcat_initial = kcat_initial
        self.Km_initial = Km_initial
        self.parameters = self.set_params(params)
        self.w0 = w0
        self.result = None

    def set_params(self, params:list) -> Parameters:

        parameters = Parameters()
        if "kcat/Km" not in params:
            parameters.add('k_cat', value=self.kcat_initial,
                        min=self.kcat_initial/100, max=self.kcat_initial*100)
            parameters.add('Km', value=self.Km_initial, min=self.Km_initial/100,
                        max=max(self.Km_initial)*1000)

        if "K_ie" in params:
            parameters.add("K_ie", value=0.01, min=0.0001, max=0.9999)

        if "K_iu" in params:
            parameters.add("K_iu", value=0.1, min=0.0001, max=1000)

        if "K_ic" in params:
            parameters.add("K_ic", value=0.1, min=0.0001, max=1000)

        if "kcat/Km" in params:
            parameters.add("kcat_Km", value=1, min=0.001, max=1000)

        return parameters


def irreversible_model(w0: tuple, t, params):
    cS, cE, cP, cI = w0

    k_cat = params['k_cat'].value
    Km = params['Km'].value

    dc_S = -k_cat * cE * (cS) / (Km+cS)
    dc_E = 0
    dc_P = -dc_S
    dc_I = 0

    return (dc_S, dc_E, dc_P, dc_I)


def irreversible_enzyme_inactication_model(w0: tuple, t, params) -> tuple:
    cS, cE, cP, cI = w0

    k_cat = params['k_cat'].value
    Km = params['Km'].value
    K_ie = params["K_ie"].value

    dc_S = -k_cat * cE * (cS) / (Km+cS)
    dc_E = -K_ie * cE
    dc_P = -dc_S
    dc_I = 0

    return (dc_S, dc_E, dc_P, dc_I)

###################
# Inhibition Models
###################

def substrate_inhibition_model(w0: tuple, t, params) -> tuple:
    cS, cE, cP, cI = w0

    k_cat = params['k_cat'].value
    Km = params['Km'].value
    K_iu = params["K_iu"].value

    dc_S = -k_cat * cE * (cS) / (Km + ((1+(cS/K_iu))*cS))
    dc_E = 0
    dc_P = -dc_S
    dc_I = 0

    return (dc_S, dc_E, dc_P, dc_I)

def substrate_inhibition_enzyme_inactivation_model(w0: tuple, t, params) -> tuple:
    cS, cE, cP, cI = w0

    k_cat = params['k_cat'].value
    Km = params['Km'].value
    K_iu = params["K_iu"].value
    K_ie = params["K_ie"].value


    dc_S = -k_cat * cE * (cS) / (Km + ((1+(cS/K_iu))*cS))
    dc_E = -K_ie * cE
    dc_P = -dc_S
    dc_I = 0

    return (dc_S, dc_E, dc_P, dc_I)

def product_inhibition_model(w0: tuple, t, params) -> tuple:
    cS, cE, cP, cI = w0

    k_cat = params['k_cat'].value
    Km = params['Km'].value
    K_ic = params["K_ic"].value

    dc_S = -k_cat * cE * (cS) / (Km * (1+(cP/K_ic)) + cS)
    dc_E = 0
    dc_P = -dc_S
    dc_I = 0

    return (dc_S, dc_E, dc_P, dc_I)

def competitive_inhibition_model(w0: tuple, t, params) -> tuple:
    cS, cE, cP, cI = w0

    k_cat = params['k_cat'].value
    Km = params['Km'].value
    K_ic = params["K_ic"].value

    dc_S = -k_cat * cE * (cS) / (Km*(1+(cI / K_ic))+cS)
    dc_E = 0
    dc_P = -dc_S
    dc_I = 0

    return (dc_S, dc_E, dc_P, dc_I)


def competitive_inhibition_enzyme_inactivation_model(w0: tuple, t, params) -> tuple:
    cS, cE, cP, cI = w0

    k_cat = params['k_cat'].value
    Km = params['Km'].value
    K_ic = params["K_ic"].value
    K_ie = params["K_ie"].value

    dc_S = -k_cat * cE * (cS) / (Km*(1+(cI / K_ic))+cS)
    dc_E = -K_ie * cE
    dc_P = -dc_S
    dc_I = 0

    return (dc_S, dc_E, dc_P, dc_I)

def uncompetitive_inhibition_model(w0: tuple, t, params) -> tuple:
    cS, cE, cP, cI = w0

    k_cat = params['k_cat'].value
    Km = params['Km'].value
    K_iu = params["K_iu"].value

    dc_S = -k_cat * cE * (cS) / (cS*(1+(cI / K_iu))+Km)
    dc_E = 0
    dc_P = -dc_S
    dc_I = 0

    return (dc_S, dc_E, dc_P, dc_I)

def uncompetitive_inhibition_enzyme_inactivation_model(w0: tuple, t, params) -> tuple:
    cS, cE, cP, cI = w0

    k_cat = params['k_cat'].value
    Km = params['Km'].value
    K_iu = params["K_iu"].value
    K_ie = params["K_ie"].value

    dc_S = -k_cat * cE * (cS) / (cS*(1+(cI / K_iu))+Km)
    dc_E = -K_ie * cE
    dc_P = -dc_S
    dc_I = 0

    return (dc_S, dc_E, dc_P, dc_I)

def noncompetitive_inhibition_model(w0: tuple, t, params) -> tuple:
    cS, cE, cP, cI = w0

    k_cat = params['k_cat'].value
    Km = params['Km'].value
    K_iu = params["K_iu"].value
    K_ic = params["K_ic"].value

    dc_S = -k_cat * cE * (cS) / (Km * (1+(cI/K_ic)) + (1+(cI/K_iu)) * cS)
    dc_E = 0
    dc_P = -dc_S
    dc_I = 0

    return (dc_S, dc_E, dc_P, dc_I)

def partially_competitive_inhibition_model(w0: tuple, t, params) -> tuple:
    cS, cE, cP, cI = w0

    k_cat = params['k_cat'].value
    Km = params['Km'].value
    K_iu = params["K_iu"].value
    K_ic = params["K_ic"].value

    dc_S = -k_cat * cE * (cS) / (Km * (1+(cI/K_ic)) / (1+(cI/K_iu)) + cS)
    dc_E = 0
    dc_P = -dc_S
    dc_I = 0

    return (dc_S, dc_E, dc_P, dc_I)


#def subabs_menten_irreversible(w, t, params):
#    '''
#    Differential equations
#    Arguments:
#        w: vector of state variables, here only one: w = [S]
#        t: time
#        params: parameters
#    '''
#    cS, cE, cP, cS0 = w
#    
#    K_m = params['Km'].value
#    k_cat = params["k_cat"].value
#    a = params["a"].value
#    
#    dc_S = (-k_cat*cE*(cS-a*cS0))/(K_m+(cS-a*cS0)/(1-a))
#    dc_E = 0
#    dc_P = -dc_S
#    dc_S0 = 0
#    
#    return (dc_S, dc_E, dc_P, dc_S0)


def kcatKm(w0: tuple, t, params) -> tuple:
    cS, cE, cP, cI = w0

    kcat_Km = params['kcat_Km'].value

    dc_S = -kcat_Km * cE * (cS)
    dc_E = 0
    dc_P = -dc_S
    dc_I = 0

    return (dc_S, dc_E, dc_P, dc_I)

def kcatKm_inactivation(w0: tuple, t, params) -> tuple:
    cS, cE, cP, cI = w0

    kcat_Km = params['kcat_Km'].value
    K_ie = params["K_ie"].value


    dc_S = -kcat_Km * cE * (cS)
    dc_E = -K_ie*cE
    dc_P = -dc_S
    dc_I = 0

    return (dc_S, dc_E, dc_P, dc_I)


if __name__ == "__main__":
    pass