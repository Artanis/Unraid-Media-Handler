from pprint import pprint
from itertools import groupby

# adapted from https://stackoverflow.com/a/19293966/152313
def interleaved(*iterables):
  # sort lists by length
  iterables = sorted(iterables, key=len)
  length = sum([len(l) for l in iterables])

  grp = \
  list(
    list(l[len(l)]*i//length for l in iterables)
    for i in range(length))

  # a, b = iterables
  #
  # grp = list(
  #   (a[len(a)*i//len_ab], b[len(b)*i//len_ab])
  #   for i in range(len_ab))

  print(grp)

  groups = groupby(grp, key=lambda x:x[0])

  interleave = [j[i] for k,g in groups for i,j in enumerate(g)]

  return interleave


def main():
  a = ["A"+str(n) for n in range(1, 13)]
  b = ["B"+str(n) for n in range(1, 23)]
  pprint(interleaved(a, b))


if __name__ == "__main__":
  print("SRC")
  a = range(8)
  b = list("abc")
  len_ab = len(a) + len(b)

  grp = list((a[len(a)*i//len_ab], b[len(b)*i//len_ab]) for i in range(len_ab))
  print(grp)
  groups = groupby(grp, key=lambda x:x[0])
  print([j[i] for k,g in groups for i,j in enumerate(g)])

  print("\nMAIN")
  main()
