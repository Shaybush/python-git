from gcd import gcd

# numerator = 8
# denominator = 12
# returns 2, 3
def simplify_fraction(numerator, denominator):
  gcd_num = gcd(numerator, denominator)
  return numerator // gcd_num, denominator // gcd_num

print(simplify_fraction(12,24))