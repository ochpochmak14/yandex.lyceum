def solve(*coefficients):
    roots = []
    num_coeffs = len(coefficients)

    if num_coeffs == 1:
        if coefficients[0] == 0:
            roots.append("all")

    if num_coeffs == 2:
        linear_coeff, constant = coefficients
        roots.append(-constant / linear_coeff)
        print(*roots)

    if num_coeffs == 3:
        quadratic_coeff, linear_coeff, constant = coefficients
        discriminant = linear_coeff**2 - 4 * quadratic_coeff * constant

        if discriminant == 0:
            roots.append(-linear_coeff / (2 * quadratic_coeff))
        elif discriminant > 0:
            root1 = (-linear_coeff + discriminant**0.5) / (2 * quadratic_coeff)
            root2 = (-linear_coeff - discriminant**0.5) / (2 * quadratic_coeff)
            roots.append(root1)
            roots.append(root2)

    print(*roots)


coefficients_list = [int(value) for value in input().split()]

if len(coefficients_list) == 1:
    solve(coefficients_list[0])
if len(coefficients_list) == 2:
    solve(coefficients_list[0], coefficients_list[1])
if len(coefficients_list) == 3:
    solve(coefficients_list[0], coefficients_list[1], coefficients_list[2])
