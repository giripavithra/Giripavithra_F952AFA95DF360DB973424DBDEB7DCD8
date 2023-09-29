def linearSearchProduct(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices


products = ["chair", "table", "bed","door", "table", "bench", "sofa"]
target = "table"
target2 = 'melon'
result = linearSearchProduct(products, target)
print(result)