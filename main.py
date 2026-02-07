import sympy as sp

sp.init_printing(use_unicode=True, num_columns=300, wrap_line=False)


points = []


first_point = str(input("\n\nProvide the first point (in \"x\u1D62 y\u1D62\" format):\n "))
first_coords = [sp.Rational(x) for x in first_point.split()]
points.append(first_coords)


while True:
    next_point = str(input("Provide the next point (in \"x\u1D62 y\u1D62\" format). Enter \"s\" to stop:\n "))
    if (next_point == "s"):
        break
    
    next_coords = [sp.Rational(x) for x in next_point.split()]
    points.append(next_coords)
    

nodes = [p[0] for p in points]
scalars = [p[1] for p in points]

    
    
def build_lagrange_term(x_val, i, all_nodes):
    x = sp.symbols('x')
    num = 1
    den = 1
    
    for j in range(len(all_nodes)):
        if i == j:
            continue
        num *= (x - all_nodes[j])
        den *= (all_nodes[i] - all_nodes[j])
    
    return num / den
        
    


def print_polynomial(nodes, scalars):
    
    final_poly = 0
    
    for i in range(len(nodes)):
        L_i = build_lagrange_term(nodes[i], i, nodes)
        term = scalars[i] * L_i
        final_poly += term
    
        
    print("\n\nFull Expression (Unsimplified):\n")
    sp.pprint(final_poly)
    print("\n\nSimplified Expression:\n")
    sp.pprint(sp.simplify(final_poly))
    print("\n\nCombined Polynomial:\n")
    sp.pprint(sp.together(sp.simplify(final_poly)))
    
print_polynomial(nodes, scalars)


