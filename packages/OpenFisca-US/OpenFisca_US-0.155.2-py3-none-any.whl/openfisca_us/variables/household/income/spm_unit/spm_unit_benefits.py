from openfisca_us.model_api import *


class spm_unit_benefits(Variable):
    value_type = float
    entity = SPMUnit
    label = "Benefits"
    definition_period = YEAR
    unit = USD

    formula = sum_of_variables(
        [
            "social_security",
            "ssi",
            "ca_cvrp",  # California Clean Vehicle Rebate Project.
            "snap",
            "wic",
            "free_school_meals",
            "reduced_price_school_meals",
            "lifeline",
            "acp",
            "ebb",
            "spm_unit_capped_housing_subsidy",
            "tanf",
            "high_efficiency_electric_home_rebate",
            "residential_efficiency_electrification_rebate",
            # Contributed.
            "basic_income",
        ]
    )
