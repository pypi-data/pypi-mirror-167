def calculate_reward(
    Yield,
    Irr_amount,
    N_amount,
    P_amount,
    K_amount,
    Costs_dict,
    Discount_factors_dict,
):
    """
    calculate reward, on each step
    """
    Irr_disc_factor = Discount_factors_dict["Irrigation"]
    N_disc_factor = Discount_factors_dict["N"]
    P_disc_factor = Discount_factors_dict["P"]
    K_disc_factor = Discount_factors_dict["K"]

    reward = Yield * Costs_dict["Selling"] - (
        Irr_disc_factor * Irr_amount * Costs_dict["Irrigation"]
        + N_disc_factor * N_amount * Costs_dict["N"]
        + P_disc_factor * P_amount * Costs_dict["P"]
        + K_disc_factor * K_amount * Costs_dict["K"]
    )

    return reward
