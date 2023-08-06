def nice_p_string(p_val):

    if p_val > 0.0095:
        p_str = f"{p_val:.2f}"
    elif p_val > 0.00095:
        p_str = f"{p_val:.3f}"
    elif p_val > 0.000095:
        p_str = f"{p_val:.4f}"
    else:
        p_str = f"{p_val:.2e}"
    return p_str
