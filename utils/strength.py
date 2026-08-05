def resume_strength(score):

    if score >= 80:
        return "⭐⭐⭐⭐⭐ Excellent"

    elif score >= 60:
        return "⭐⭐⭐⭐☆ Good"

    elif score >= 40:
        return "⭐⭐⭐☆☆ Average"

    elif score >= 20:
        return "⭐⭐☆☆☆ Weak"

    else:
        return "⭐☆☆☆☆ Poor"