def finding_lcm(a, b):
    # lcm formula : (a * b) / gcd(a, b)
    original_a, original_b = a, b
    while b != 0:
        a, b = b, a % b
        gcd = a
    return (original_a * original_b) // gcd
print(finding_lcm(12,15))
"""
	1. The Mathematical Relationship: There is a mathematical rule that states: $LCM(a, b) = \frac{|a \times b|}{GCD(a, b)}$.
	2. Finding GCD: We repeat the Euclidean algorithm from the previous problem to find the GCD. We must save the original values of a and b first, because the while loop destroys them.
	3. Applying the Formula: We multiply the original numbers and divide by the GCD. We use // (floor division) to ensure the result is returned as an integer, not a float.
"""